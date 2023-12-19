from django.test import TestCase

from unittest.mock import patch
from fusion.forms import ContactForm


class ContactFormTest(TestCase):

    def test_valid_data(self):
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'message': 'This is a test message.',
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_missing_data(self):
        # Test with missing data, expecting the form to be invalid
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'subject': '',
            'message': 'This is a test message.',
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('subject', form.errors)

    def test_send_mail(self):
        # Mocking the send method of EmailMessage
        with patch('django.core.mail.message.EmailMessage.send') as mock_send:
            form_data = {
                'name': 'John Doe',
                'email': 'john@example.com',
                'subject': 'Test Subject',
                'message': 'This is a test message.',
            }
            form = ContactForm(data=form_data)
            form.is_valid()  # Ensuring the form is valid before calling send_mail
            form.send_mail()

        # Asserting that the send method was called once
        mock_send.assert_called_once()
