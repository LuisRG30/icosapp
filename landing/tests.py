from django.test import TestCase, Client

# Create your tests here.
class LandingTestCase(TestCase):

    def test_load(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
        response = c.get("/pricing")
        self.assertEqual(response.status_code, 200)