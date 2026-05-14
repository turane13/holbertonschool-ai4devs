import hashlib
import secrets
import time

class AuthenticationManager:
    def __init__(self):
        self.users = {}
        self.active_tokens = {}
        self.token_expiry_seconds = 3600

    def _hash_password(self, password, salt):
        combined = password + salt
        return hashlib.sha256(combined.encode()).hexdigest()

    def register_user(self, username, password, role="User"):
        if not username or not password:
            return {"success": False, "message": "Missing credentials"}
        
        if username in self.users:
            return {"success": False, "message": "User already exists"}
            
        if role not in ["Admin", "User", "Guest"]:
            return {"success": False, "message": "Invalid role specified"}

        salt = secrets.token_hex(16)
        hashed_password = self._hash_password(password, salt)
        
        self.users[username] = {
            "password": hashed_password,
            "salt": salt,
            "role": role,
            "created_at": time.time()
        }
        return {"success": True, "message": "User registered successfully"}

    def login_user(self, username, password):
        if username not in self.users:
            return {"success": False, "token": None}

        user_data = self.users[username]
        input_hash = self._hash_password(password, user_data["salt"])

        if input_hash == user_data["password"]:
            token = secrets.token_urlsafe(32)
            expiry = time.time() + self.token_expiry_seconds
            self.active_tokens[token] = {
                "username": username,
                "role": user_data["role"],
                "expires_at": expiry
            }
            return {"success": True, "token": token}
            
        return {"success": False, "token": None}

    def verify_access(self, token, required_role):
        if token not in self.active_tokens:
            return {"allowed": False, "reason": "Invalid token"}

        token_data = self.active_tokens[token]
        
        if time.time() > token_data["expires_at"]:
            del self.active_tokens[token]
            return {"allowed": False, "reason": "Token expired"}

        user_role = token_data["role"]
        
        role_hierarchy = {"Admin": 3, "User": 2, "Guest": 1}
        
        if role_hierarchy.get(user_role, 0) >= role_hierarchy.get(required_role, 0):
            return {"allowed": True, "reason": "Access granted"}
            
        return {"allowed": False, "reason": "Insufficient permissions"}

    def logout_user(self, token):
        if token in self.active_tokens:
            del self.active_tokens[token]
            return True
        return False
