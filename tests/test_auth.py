"""Tests for ForensicLens Investigator Authentication & User Management."""

import unittest
from forensiclens.dashboard.app import create_app


class AuthTests(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.client = self.app.test_client()

    def test_login_page_renders(self) -> None:
        resp = self.client.get('/login')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"FORENSICLENS", resp.data)
        self.assertIn(b"Investigator Sign In", resp.data)

    def test_signup_page_renders(self) -> None:
        resp = self.client.get('/signup')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"Admin", resp.data)

    def test_default_investigator_login(self) -> None:
        resp = self.client.post('/api/auth/login', json={
            "identifier": "investigator@cbi.gov.in",
            "password": "Investigator@2026",
        })
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data.get("status"), "success")
        self.assertEqual(data.get("user", {}).get("badge_id"), "IND-26150")

    def test_login_by_badge_id(self) -> None:
        resp = self.client.post('/api/auth/login', json={
            "identifier": "IND-26150",
            "password": "Investigator@2026",
        })
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data.get("status"), "success")
        self.assertIn("Insp. A. K. Sharma", data.get("user", {}).get("name"))

    def test_invalid_password_rejected(self) -> None:
        resp = self.client.post('/api/auth/login', json={
            "identifier": "investigator@cbi.gov.in",
            "password": "WrongPassword123",
        })
        self.assertEqual(resp.status_code, 401)
        data = resp.get_json()
        self.assertEqual(data.get("status"), "error")

    def test_signup_new_investigator(self) -> None:
        import uuid
        unique_email = f"officer_{uuid.uuid4().hex[:6]}@police.gov.in"
        unique_badge = f"BADGE-{uuid.uuid4().hex[:4].upper()}"

        resp = self.client.post('/api/auth/signup', json={
            "name": "Special Officer Kapoor",
            "email": unique_email,
            "badge_id": unique_badge,
            "password": "SecretPassphrase2026!",
            "agency": "State Anti-Terror Squad",
            "clearance": "Level 3 - Lead Forensic Examiner",
        })
        self.assertEqual(resp.status_code, 201)
        data = resp.get_json()
        self.assertEqual(data.get("status"), "success")
        self.assertEqual(data.get("user", {}).get("email"), unique_email)

        # Verify new user can now log in
        login_resp = self.client.post('/api/auth/login', json={
            "identifier": unique_badge,
            "password": "SecretPassphrase2026!",
        })
        self.assertEqual(login_resp.status_code, 200)

    def test_duplicate_signup_rejected(self) -> None:
        resp = self.client.post('/api/auth/signup', json={
            "name": "Duplicate Sharma",
            "email": "investigator@cbi.gov.in",
            "badge_id": "NEW-BADGE-999",
            "password": "AnyPassword123",
        })
        self.assertEqual(resp.status_code, 400)
        data = resp.get_json()
        self.assertIn("already exists", data.get("error", ""))

    def test_auth_me_and_logout(self) -> None:
        # First log in
        self.client.post('/api/auth/login', json={
            "identifier": "investigator@cbi.gov.in",
            "password": "Investigator@2026",
        })

        # Check me
        me_resp = self.client.get('/api/auth/me')
        self.assertEqual(me_resp.status_code, 200)
        self.assertTrue(me_resp.get_json().get("authenticated"))

        # Logout
        logout_resp = self.client.post('/api/auth/logout')
        self.assertEqual(logout_resp.status_code, 200)

        # Check me again
        me_after = self.client.get('/api/auth/me')
        self.assertFalse(me_after.get_json().get("authenticated"))

    def test_user_investigator_login(self) -> None:
        resp = self.client.post('/api/auth/login', json={
            "identifier": "user@forensiclens.gov.in",
            "password": "User@2026",
        })
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data.get("status"), "success")
        user = data.get("user", {})
        self.assertEqual(user.get("badge_id"), "CAM-26150")
        self.assertEqual(user.get("role"), "user_investigator")
        self.assertIn("P. Patel", user.get("name", ""))

    def test_user_investigator_badge_login(self) -> None:
        resp = self.client.post('/api/auth/login', json={
            "identifier": "CAM-26150",
            "password": "User@2026",
        })
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data.get("status"), "success")
        self.assertEqual(data.get("user", {}).get("role"), "user_investigator")

    def test_investigator_role_in_login(self) -> None:
        resp = self.client.post('/api/auth/login', json={
            "identifier": "investigator@cbi.gov.in",
            "password": "Investigator@2026",
        })
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data.get("user", {}).get("role"), "investigator")

    def test_user_login_pages_render(self) -> None:
        for path in ['/login?role=user', '/login/user', '/user-login']:
            resp = self.client.get(path)
            self.assertEqual(resp.status_code, 200)
            self.assertIn(b"User Investigator", resp.data)
            self.assertIn(b"Live Camera Surveillance", resp.data)

    def test_signup_user_investigator(self) -> None:
        import uuid
        unique_email = f"surv_{uuid.uuid4().hex[:6]}@surveillance.gov.in"
        unique_badge = f"CAM-{uuid.uuid4().hex[:4].upper()}"

        resp = self.client.post('/api/auth/signup', json={
            "name": "Operator Vikram",
            "email": unique_email,
            "badge_id": unique_badge,
            "password": "UserPass2026!",
            "agency": "Metro CCTV Monitoring Cell",
            "clearance": "Field Surveillance Operator",
            "role": "user_investigator",
        })
        self.assertEqual(resp.status_code, 201)
        data = resp.get_json()
        self.assertEqual(data.get("status"), "success")
        self.assertEqual(data.get("user", {}).get("role"), "user_investigator")

        # Verify login
        login_resp = self.client.post('/api/auth/login', json={
            "identifier": unique_badge,
            "password": "UserPass2026!",
        })
        self.assertEqual(login_resp.status_code, 200)
        self.assertEqual(login_resp.get_json().get("user", {}).get("role"), "user_investigator")


    def test_signup_user_investigator_minimal_fields(self) -> None:
        """User signup with only full name, email, and password."""
        import uuid
        unique_email = f"operator_{uuid.uuid4().hex[:6]}@surveillance.gov.in"
        resp = self.client.post('/api/auth/signup', json={
            "name": "Operator Sneha Rao",
            "email": unique_email,
            "password": "SnehaPassword2026!",
            "role": "user_investigator",
        })
        self.assertEqual(resp.status_code, 201)
        data = resp.get_json()
        self.assertEqual(data.get("status"), "success")
        self.assertEqual(data.get("user", {}).get("role"), "user_investigator")
        self.assertTrue(data.get("user", {}).get("badge_id", "").startswith("CAM-"))

        # Verify login with email
        login_resp = self.client.post('/api/auth/login', json={
            "identifier": unique_email,
            "password": "SnehaPassword2026!",
        })
        self.assertEqual(login_resp.status_code, 200)
        self.assertEqual(login_resp.get_json().get("user", {}).get("role"), "user_investigator")

    def test_login_page_has_admin_field_and_no_signup_buttons(self) -> None:
        """Verify signup buttons are removed and admin field is present."""
        resp = self.client.get('/login')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"btn-mode-admin", resp.data)
        self.assertIn(b"btn-mode-user-login", resp.data)
        self.assertIn(b"btn-mode-investigator-login", resp.data)
        self.assertNotIn(b"btn-mode-user-signup", resp.data)
        self.assertNotIn(b"btn-mode-investigator-signup", resp.data)

    def test_admin_accounts_list(self) -> None:
        """Test listing currently provisioned accounts."""
        resp = self.client.get('/api/auth/admin/accounts')
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data.get("status"), "success")
        self.assertIn("user", data)
        self.assertIn("investigator", data)
        self.assertIn("@", data["user"]["email"])
        self.assertIn("@", data["investigator"]["email"])

    def test_admin_provision_user_account(self) -> None:
        """Only the admin can give the email and password, and only that works."""
        import uuid
        new_user_email = f"custom_user_{uuid.uuid4().hex[:6]}@police.gov.in"
        new_user_pass = "SecureUserPass@999"

        # Provision through admin endpoint
        prov_resp = self.client.post('/api/auth/admin/provision', json={
            "role": "user_investigator",
            "email": new_user_email,
            "password": new_user_pass,
            "admin_key": "Admin@2026",
        })
        self.assertEqual(prov_resp.status_code, 200)
        prov_data = prov_resp.get_json()
        self.assertEqual(prov_data.get("status"), "success")
        self.assertEqual(prov_data.get("user", {}).get("email"), new_user_email)

        # Verify only this new email and password works to sign in
        login_resp = self.client.post('/api/auth/login', json={
            "identifier": new_user_email,
            "password": new_user_pass,
        })
        self.assertEqual(login_resp.status_code, 200)
        self.assertEqual(login_resp.get_json().get("user", {}).get("role"), "user_investigator")

        # Wrong password must fail
        wrong_pass_resp = self.client.post('/api/auth/login', json={
            "identifier": new_user_email,
            "password": "WrongPassword!",
        })
        self.assertEqual(wrong_pass_resp.status_code, 401)

    def test_admin_provision_investigator_account(self) -> None:
        """Admin provisions investigator credentials."""
        import uuid
        new_inv_email = f"custom_inv_{uuid.uuid4().hex[:6]}@cbi.gov.in"
        new_inv_pass = "SecureInvPass@888"

        prov_resp = self.client.post('/api/auth/admin/provision', json={
            "role": "investigator",
            "email": new_inv_email,
            "password": new_inv_pass,
            "admin_key": "Admin@2026",
        })
        self.assertEqual(prov_resp.status_code, 200)

        # Login with newly provisioned investigator credentials
        login_resp = self.client.post('/api/auth/login', json={
            "identifier": new_inv_email,
            "password": new_inv_pass,
        })
        self.assertEqual(login_resp.status_code, 200)
        self.assertEqual(login_resp.get_json().get("user", {}).get("role"), "investigator")

    def test_admin_provision_unauthorized_key(self) -> None:
        """Admin provisioning fails when master key is invalid."""
        resp = self.client.post('/api/auth/admin/provision', json={
            "role": "investigator",
            "email": "hacker@test.com",
            "password": "hackedpassword",
            "admin_key": "WrongMasterKey",
        })
        self.assertEqual(resp.status_code, 400)
        self.assertIn("Invalid Admin Master Key", resp.get_json().get("error", ""))


if __name__ == "__main__":
    unittest.main()
