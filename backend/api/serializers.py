import datetime
import re

from dateutil.relativedelta import relativedelta
from people.models import Person
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "gender",
            "date_of_birth",
            "industry",
            "salary",
            "years_of_experience",
        ]

    def validate_last_name(self, value):
        if not re.match(r"[a-zA-Z0-9_. -]+$", value):
            raise serializers.ValidationError("Invalid last name!")
        return value

    def validate_first_name(self, value):
        if not re.match(r"[a-zA-Z0-9_. -]+$", value):
            raise serializers.ValidationError("Invalid first name!")
        return value

    def validate_date_of_birth(self, value):
        if value > datetime.date.today():
            raise serializers.ValidationError("Date of birth cannot be in the future!")

        eighteen_years_ago = datetime.date.today() - relativedelta(years=18)

        if value > eighteen_years_ago:
            raise serializers.ValidationError("Person is underage!")

        return value
