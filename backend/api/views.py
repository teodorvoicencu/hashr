from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from people.models import Person
from people.pandas import get_avg_by_fields
from .serializers import PersonSerializer
from .utils import dataframe_to_json

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filterset_fields = ['first_name', 'last_name', 'industry', 'email']


class PandasAvgBaseView(APIView):
    authentication_classes = []
    permission_classes = []
    fields = []

    def get(self, *args, **kwargs):
        dataframe = get_avg_by_fields(*self.fields)
        return Response(dataframe_to_json(dataframe, self.fields))

class AvgAgePerIndustryView(PandasAvgBaseView):
    fields = ["industry", "age"]
    
class AvgSalaryPerIndustryView(PandasAvgBaseView):
    fields = ["industry", "salary"]

class AvgSalaryPerYearsOfExperienceView(PandasAvgBaseView):
    fields = ["years_of_experience", "salary"]

class AvgSalaryPerAgeView(PandasAvgBaseView):
    fields = ["age", "salary"]
