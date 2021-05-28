from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    
    def test_create_user_with_email_succesfull(self):
        """Function for checking that usemodel with email is successfully created"""
        email = 'vrushik0312@gmail.com'
        password = 'Testpass123'

        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email , email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Function for testing normalied email i.e lower case"""

        email = 'vrushik@GMAIL.COM'
        user = get_user_model().objects.create_user(email,'test123')

        self.assertEqual(user.email , email.lower())


    def test_new_user_invalid_email(self):
        """Function for testing invalid email"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test1231')

    def test_creat_new_superuser(self):
        """Function for testing new superuser and check value of isstaff and is suoeruser"""

        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            '12312ff'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)