from django.test import TestCase
from django.db import models
from .models import education, job, pictures, user
from django.contrib.auth.models import User

# Create your tests here.
class EducationTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.abugaeducate = education(title="rick", description="my first degree", qualification = "undegraduate",start = '2020-10-20', finish='2020-10-21')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.abugaeducate,education))

class JobTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.abugajob = job(title="rick", description="my first degree",start = '2020-10-20', finish='2020-10-21')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.abugajob,job))

class PicturesTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.abugapics = pictures(title="rick", alt_tag="my first degree", image = "xyz")
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.abugapics,pictures))

class UserTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.abugapics = pictures(title="rick", alt_tag="my first degree", image = "xyz")
        self.abugajob = job(title="rick", description="my first degree",start = '2020-10-20', finish='2020-10-21')
        self.abugaeducate = education(title="rick", description="my first degree", qualification = "undegraduate",start = '2020-10-20', finish='2020-10-21')
        self.abuga = User(username="rick", password="password")
        self.abuga.save()
        self.abugapics.save()
        self.abugajob.save()
        self.abugaeducate.save()

        self.abugauser = user(user=self.abuga, first_name="Rick", last_name="ricardo", admin=True,about="Abuga is not rick")
        self.abugauser.pictures.add(self.abugapics)
        self.abugauser.education.add(self.abugajob)
        self.abugauser.career.add(self.abugaeducate)

    def test_instance(self):
        self.assertTrue(isinstance(self.abugauser,user))
