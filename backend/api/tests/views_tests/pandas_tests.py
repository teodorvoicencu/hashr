import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from people.models import Person

class BasePandasAvgViewTests:
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.first_person = Person.objects.create(
            first_name = "John",
            last_name = "Doe",
            email = "john.doe@gmail.com",
            date_of_birth = datetime.date(1999, 12, 4),
            industry = "IT&C",
            salary = 120000,
            years_of_experience = 10,
        )

        cls.second_person = Person.objects.create(
            first_name = "John",
            last_name = "Toe",
            email = "john.toe@gmail.com",
            date_of_birth = datetime.date(1999, 12, 4),
            industry = "IT&C",
            salary = 150000,
            years_of_experience = 10,
        )


class AvgAgePerIndustryViewTests(BasePandasAvgViewTests, APITestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.url = reverse('avg-age-per-industry')
    
    def test_returns_expected_response(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{'industry': 'IT&C', 'age': 23.0}])

class AvgSalaryPerIndustryViewTests(BasePandasAvgViewTests, APITestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.url = reverse('avg-salary-per-industry')
    
    def test_returns_expected_response(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{'industry': 'IT&C', 'salary': 135000.0}])


class AvgSalaryPerYearsOfExperienceViewTests(BasePandasAvgViewTests, APITestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.url = reverse('avg-salary-per-years-of-experience')
    
    def test_returns_expected_response(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{'years_of_experience': 10, 'salary': 135000.0}])

class AvgSalaryPerAgeViewTests(BasePandasAvgViewTests, APITestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.url = reverse('avg-salary-per-age')
    
    def test_returns_expected_response(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{'age': 23, 'salary': 135000.0}])