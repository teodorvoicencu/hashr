import datetime

from api.serializers import PersonSerializer
from django.test import TestCase


class PersonSerializerTests(TestCase):
    def setUp(self):
        self.serializer_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@gmail.com",
            "gender": "M",
            "date_of_birth": datetime.date(1990, 12, 4),
            "industry": "IT",
            "salary": 100.00,
            "years_of_experience": 5,
        }
        self.serializer_class = PersonSerializer

    def test_invalid_first_name(self):
        self.serializer_data["first_name"] = "aj8*1"
        serializer = self.serializer_class(data=self.serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), set(["first_name"]))

    def test_invalid_last_name(self):
        self.serializer_data["last_name"] = "aj8*1"
        serializer = self.serializer_class(data=self.serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), set(["last_name"]))

    def test_date_cannot_be_in_the_future(self):
        self.serializer_data["date_of_birth"] = (datetime.date(3000, 12, 4),)
        serializer = self.serializer_class(data=self.serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), set(["date_of_birth"]))

    def test_underaged(self):
        self.serializer_data["date_of_birth"] = (datetime.date(2023, 12, 4),)
        serializer = self.serializer_class(data=self.serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), set(["date_of_birth"]))
