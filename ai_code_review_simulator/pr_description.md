# Pull Request: Add User Authentication and Role Management

## Summary
Implements a user authentication system with role-based access control (RBAC). Adds endpoints for user registration, login, and secure resource access based on permissions.

## Changes
- Created AuthenticationManager class in auth.py
- Implemented JWT-like token generation and validation mechanisms
- Added role verification helpers for Admin and User types
- Written comprehensive unit tests for validation paths

## Context
~130 LOC. Related issue: #101.
