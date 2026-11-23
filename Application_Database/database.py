
import sqlite3
import hashlib
import os
from pathlib import Path


class UserDatabase:

    def __init__(self):

        # Store database inside Application_Database/data
        base_directory = Path(__file__).resolve().parent
        data_directory = base_directory / "data"

        data_directory.mkdir(parents=True, exist_ok=True)

        self.database_path = data_directory / "users.db"

        self.create_table()

    # ==========================================
    # DATABASE CONNECTION
    # ==========================================

    def connect(self):
        return sqlite3.connect(self.database_path)

    # ==========================================
    # CREATE USERS TABLE
    # ==========================================

    def create_table(self):

        connection = self.connect()
        cursor = connection.cursor()

        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    salt TEXT NOT NULL
                )
            """)

            connection.commit()

        finally:
            connection.close()

    # ==========================================
    # PASSWORD HASHING
    # ==========================================

    def hash_password(self, password, salt=None):

        if salt is None:
            salt = os.urandom(16).hex()

        password_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            bytes.fromhex(salt),
            310000
        ).hex()

        return password_hash, salt

    # ==========================================
    # REGISTER USER
    # ==========================================

    def register_user(self, username, email, password):

        connection = self.connect()
        cursor = connection.cursor()

        try:

            password_hash, salt = self.hash_password(password)

            cursor.execute("""
                INSERT INTO users
                (username, email, password_hash, salt)
                VALUES (?, ?, ?, ?)
            """, (username, email, password_hash, salt))

            connection.commit()

            return True, "Account successfully created!"

        except sqlite3.IntegrityError:

            return False, "Username or email already exists."

        finally:
            connection.close()

    # ==========================================
    # LOGIN USER
    # ==========================================

    def login_user(self, username, password):

        connection = self.connect()
        cursor = connection.cursor()

        try:

            cursor.execute("""
                SELECT password_hash, salt
                FROM users
                WHERE username = ?
            """, (username,))

            user = cursor.fetchone()

            # Check if account exists
            if user is None:
                return False, "Account not found. Please sign up first."

            stored_hash, salt = user

            # Verify entered password
            entered_hash, _ = self.hash_password(
                password,
                salt
            )

            if entered_hash == stored_hash:
                return True, "Login successful!"

            return False, "Incorrect password."

        finally:
            connection.close()
