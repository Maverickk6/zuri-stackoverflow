from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserManagerTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='user@email.com', password='foo')
        self.assertEqual(user.email, 'user@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(TypeError):
            User.objects.create_user()

        with self.assertRaises(TypeError):
            User.objects.create_user(email='')

        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='foo')

  

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='superuser@email.com', password='foo')  
        self.assertEqual(admin_user.email, 'superuser@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)   
        self.assertTrue(admin_user.is_superuser)


