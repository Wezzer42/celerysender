from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from unittest.mock import patch

class SendEmailAPITestCase(TestCase):
    def setUp(self):
        self.url = reverse("api_send_email")

    @patch("emailer.tasks.send_email_task.delay")
    def test_send_email_success(self, mock_send_email):
        payload = {
            "email": "test@example.com",
            "subject": "Hello",
            "message": "Test message"
        }

        response = self.client.post(self.url, payload, content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {"message": "Email queued successfully"})
        mock_send_email.assert_called_once_with(
            "test@example.com",
            "Hello",
            "Test message"
        )

    def test_send_email_invalid_data(self):
        payload = {
            "email": "",
            "subject": "",
            "message": ""
        }

        response = self.client.post(self.url, payload, content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)