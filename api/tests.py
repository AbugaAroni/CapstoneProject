from django.test import TestCase
from django.db import models
from .models import education

class EducationTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.abugaeducate = education(title="rick", description="my first degree", start = '2020-10-20', finish='2020-10-21')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.abugaeducate,education))
# Create your tests here.
