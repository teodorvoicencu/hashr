from rest_framework import viewsets
from people.models import Person
from api.serializers import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filterset_fields = ['first_name', 'last_name', 'industry', 'email']