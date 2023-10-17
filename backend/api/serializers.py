from rest_framework import serializers
from people.models import Person

class PersonSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'email', 'gender', 'date_of_birth', 'industry', 'salary', 'years_of_experience']