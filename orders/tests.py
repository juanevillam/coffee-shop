from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class MyOrderViewTest(TestCase):
    def test_no_logged_user_should_redirect_to_login(self):
        url = reverse("my_order")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/users/login/?next=/orders/my-order")

    def test_logged_user_should_redirect(self):
        url = reverse("my_order")
        user = get_user_model().objects.create_user(username="testuser")
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
