from django.test import TestCase
from django.db import models
from .models import education, job, pictures

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
