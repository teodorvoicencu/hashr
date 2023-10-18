from api.serializers import PersonSerializer
from people.models import Person
from rest_framework import viewsets


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filterset_fields = ["first_name", "last_name", "industry", "email"]
