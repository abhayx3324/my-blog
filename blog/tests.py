# blog/tests.py

from django.test import TestCase
from django.urls import reverse, resolve


class GenericTestCase(TestCase):
    """General sanity checks for Django project"""

    def test_homepage_access(self):
        """Test if homepage (/) responds with 200 or 404 without crashing."""
        response = self.client.get('/')
        self.assertIn(response.status_code, [200, 404])

    def test_url_resolves(self):
        """Test reverse and resolve mechanisms."""
        try:
            view = resolve('/')
            self.assertIsNotNone(view)
        except Exception:
            self.fail("Unable to resolve '/' URL")

    def test_django_setup(self):
        """Confirm that Django is set up and ready to run."""
        import django
        try:
            django.setup()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Django setup failed with error: {e}")

