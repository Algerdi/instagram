"""
Let's interact with the users.
User listing
    For testing purposes
Allows for user creation (registration)
Creating user (by registrating)
Getting info on a specific user by ID
Updating user's info by specific ID
Deleting user by specific ID
Login/logout functionality
"""
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import NewUser


class UserFixtures:
    def setup_user_list(self):
        self.users = [
            {
                "email": "a@a.com",
                "user_name": "test1",
                "name": "test1",
                "password": "123",
                "phone_number": "+375293111122",
                "gender": "M",
            },
            {
                "email": "b@b.com",
                "user_name": "test2",
                "name": "test2",
                "password": "123",
                "phone_number": "+375293111123",
                "gender": "M",
            },
        ]
        for user in self.users:
            NewUser.objects.create_user(**user)

    def setup_user(self):
        self.user = {
            "email": "test@test.com",
            "user_name": "test_user",
            "name": "test",
            "password": "qwerty",
            "phone_number": "+375293115332",
            "gender": "M",
            "bio": "just a user for testing purposes",
            "website": "https://www.instagram.com/zelenskiy_official/",
        }


class UserModelTests(TestCase, UserFixtures):
    def test_new_superuser(self):
        """
        Check if we can create superuser
        And checking is it correctly saved to DB
        """
        super_user = NewUser.objects.create_superuser(
            "testsuperuser@super.com", "testsuperuser", "name", "qwerty")
        self.assertEqual(super_user.email, "testsuperuser@super.com")
        self.assertEqual(super_user.user_name, "testsuperuser")
        self.assertEqual(super_user.name, "name")
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), "testsuperuser")

        with self.assertRaises(ValueError):
            NewUser.objects.create_superuser(
                email="testuser@super.com", user_name="username1",
                name="first_name", password="password", is_superuser=False)

        with self.assertRaises(ValueError):
            NewUser.objects.create_superuser(
                email="testuser@super.com", user_name="username1",
                name="first_name", password="password", is_staff=False)

        with self.assertRaises(ValueError):
            NewUser.objects.create_superuser(
                email="", user_name="username1", name="first_name",
                password="password", is_superuser=True)

    def test_new_user(self):
        """
        Check if we can create user
        And checking is it correctly saved to DB
        """
        user = NewUser.objects.create_user(
            "testuser@user.com", "testuser", "firstname", "qwerty")
        self.assertEqual(user.email, "testuser@user.com")
        self.assertEqual(user.user_name, "testuser")
        self.assertEqual(user.name, "firstname")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

        with self.assertRaises(ValueError):
            NewUser.objects.create_user(
                email="", user_name="a",
                name="first_name",
                password="password"
            )


class UserAPITests(APITestCase, UserFixtures):
    def test_list_users(self):
        """
        Send a request to get a user list
        Expect to recieve the same user list as in the DB
        """
        self.setup_user_list()
        url = reverse("list_users")
        response = self.client.get(url)
        users = response.json()

        # Check if users have IDs
        self.assertTrue(all(user["id"] for user in users))

        # Check if users from DB have the same data as users from request
        for user_from_DB, user_from_request in zip(self.users, users):
            self.assertEqual(user_from_DB["email"],
                             user_from_request["email"])
            self.assertEqual(user_from_DB["user_name"],
                             user_from_request["user_name"])
            self.assertEqual(user_from_DB["name"],
                             user_from_request["name"])
            self.assertEqual(user_from_DB["phone_number"],
                             user_from_request["phone_number"])
            self.assertEqual(user_from_DB["gender"],
                             user_from_request["gender"])

        # Check is status is correct
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_register_user(self):
        """
        Register a new user
        Expecting that it returns as next fields:
        id, email, user_name, gender,
        name, avatar, phone_number, website,
        start_date, bio, password
        """
        self.setup_user()
        url = reverse("register")
        response = self.client.post(url, self.user, format="json")
        new_user = response.json()

        # Check if the user created correctly
        self.assertEqual(self.user["email"], new_user["email"])
        self.assertEqual(self.user["user_name"], new_user["user_name"])
        self.assertEqual(self.user["name"], new_user["name"])
        self.assertEqual(self.user["phone_number"], new_user["phone_number"])
        self.assertEqual(self.user["bio"], new_user["bio"])
        self.assertEqual(self.user["website"], new_user["website"])
        self.assertEqual(self.user["gender"], new_user["gender"])

        # Check if the registered user have necessary fields
        self.assertTrue(new_user["avatar"])
        self.assertTrue(new_user["start_date"])
        self.assertTrue(new_user["id"])

        # Check is status is correct
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getting_user_by_ID(self):
        """
        Get info on user by its ID
        """
        self.setup_user_list()
        url = reverse("get_user", kwargs={"pk": 2})
        response = self.client.get(url)
        user = response.json()

        # User have id
        self.assertTrue(user.pop("id"))

        # Check is it a right user
        self.assertEqual(self.users[0]["email"], user["email"])
        self.assertEqual(self.users[0]["user_name"], user["user_name"])

    def test_updating_user(self):
        """
        Update user by its ID
        """
        self.setup_user()
        # Registrate user
        url = reverse("register")
        response = self.client.post(url, self.user, format="json")
        new_user = response.json()
        # Change some user's field
        updated_name = "new name"
        self.user["name"] = updated_name
        # Updating our user
        url = reverse("get_user", kwargs={"pk": 7})
        response = self.client.put(url, self.user, format="json")
        updated_user = response.json()

        # Check if name was changed
        self.assertNotEqual(new_user["name"], updated_user["name"])
        self.assertEqual(updated_name, updated_user["name"])

    def test_deleting_user(self):
        """
        Delete user by its ID
        """
        self.setup_user()
        # Registrate user
        url = reverse("register")
        response = self.client.post(url, self.user, format="json")
        # Deleting user
        url = reverse("get_user", kwargs={"pk": 1})
        response = self.client.delete(url)

        # Check if status is correct
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_login(self):
        """
        Given an existing user account
        Expect to receive JWT token on a successful login
        """
        self.setup_user()
        # Register user
        url = reverse("register")
        response = self.client.post(url, self.user, format="json")
        url = reverse("token_obtain_pair")
        response = self.client.post(url, {
            "email": self.user["email"],
            "password": self.user["password"],
        })
        self.assertEqual({"access", "refresh"}, response.json().keys())

    def test_user_logout(self):
        """
        Giving an existing refresh token
        Expeect to blacklist it
        """
        self.setup_user()
        # Register user
        url = reverse("register")
        response = self.client.post(url, self.user, format="json")
        # Login user
        url = reverse("token_obtain_pair")
        response = self.client.post(url, {
            "email": self.user["email"],
            "password": self.user["password"],
        })
        refresh_token = response.json()["refresh"]
        url = reverse("blacklist")
        response = self.client.post(url, {
            "refresh": refresh_token
        })

        # Check if status correct
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)

        # Check if token is blacklisted
        url = reverse("token_refresh")
        response = self.client.post(url, {
            "refresh": refresh_token
        })
        self.assertEqual(
            "Token is blacklisted",
            response.json()["detail"]
        )
