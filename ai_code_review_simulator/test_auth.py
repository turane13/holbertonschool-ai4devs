import unittest
import time
from auth import AuthenticationManager

class TestAuthenticationManager(unittest.TestCase):
    def setUp(self):
        self.manager = AuthenticationManager()
        self.manager.register_user("admin_user", "AdminPass123", "Admin")
        self.manager.register_user("regular_user", "UserPass123", "User")

    def test_registration_success(self):
        res = self.manager.register_user("new_user", "Pass456", "User")
        self.assertTrue(res["success"])

    def test_duplicate_registration(self):
        res = self.manager.register_user("admin_user", "DifferentPass", "User")
        self.assertFalse(res["success"])

    def test_login_success(self):
        res = self.manager.login_user("regular_user", "UserPass123")
        self.assertTrue(res["success"])
        self.assertIsNotNone(res["token"])

    def test_login_failure(self):
        res = self.manager.login_user("regular_user", "WrongPass")
        self.assertFalse(res["success"])
        self.assertNone(res["token"])

    def test_access_control_granted(self):
        login_res = self.manager.login_user("admin_user", "AdminPass123")
        token = login_res["token"]
        access_res = self.manager.verify_access(token, "User")
        self.assertTrue(access_res["allowed"])

    def test_access_control_denied(self):
        login_res = self.manager.login_user("regular_user", "UserPass123")
        token = login_res["token"]
        access_res = self.manager.verify_access(token, "Admin")
        self.assertFalse(access_res["allowed"])

if __name__ == "__main__":
    unittest.main()
