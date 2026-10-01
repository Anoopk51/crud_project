from django.test import TestCase
from .models import User
# Create your tests here.

class HomePageTest(TestCase):

    def test_home_page(self):

        response = self.client.get("/")
        self.assertEqual(response.status_code,200)

class StudentCreateIntegerationTest(TestCase):

    def test_create_student(self):

        response = self.client.post(
            "/",
            {
                "name":"Anoop",
                "email":"anoopit@gmail.com",
                "password":"12345",
            }
        )

        # check that the request was successful
        self.assertEqual(response.status_code,200)


        # check that student was actually saved in database
        self.assertTrue(
            User.objects.filter(
                name="Anoop",
                email="anoopit@gmail.com"
            ).exists()
        )





        