from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthTests(TestCase):
    def test_register_page(self):
        """Test if the register page loads correctly"""
        response = self.client.get(reverse('register'))  # Ensure this matches your URL name
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/register.html')  # Fix template path

    def test_register_post(self):
        """Test user registration via POST request"""
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password1': 'TestPass123',
            'password2': 'TestPass123'
        })
        self.assertEqual(response.status_code, 302)  # Expect redirect after success
        self.assertRedirects(response, reverse('login'))  # Should redirect to login

    def test_login_page(self):
        """Test if the login page loads correctly"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/login.html')  # Fix template path

    def test_login_valid_user(self):
        """Test valid user login"""
        user = User.objects.create_user(username='validuser', password='validpass')
        response = self.client.post(reverse('login'), {'username': 'validuser', 'password': 'validpass'})
        self.assertEqual(response.status_code, 302)  # Expect redirect
        self.assertRedirects(response, reverse('home'))  # Should go to home

    def test_logout(self):
        """Test if logout redirects to login"""
        self.client.login(username='validuser', password='validpass')  # Log in first
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Expect redirect
        self.assertRedirects(response, reverse('login'))  # Should redirect to login
