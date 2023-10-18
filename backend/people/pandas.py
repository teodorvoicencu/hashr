from django.db.models import F, Func, IntegerField, Value
from django.utils import timezone
from django_pandas.io import read_frame

from .models import Person

def get_person_data(fieldnames=()):
    queryset = Person.objects.annotate( 
        age=Func(
            Value("year"),
            Func(Value(timezone.now().date()), F("date_of_birth"), function="age"),
            function="date_part",
            output_field=IntegerField()
    )).all()
    return read_frame(queryset, fieldnames=fieldnames)

def get_avg_by_fields(first, second):
    data = get_person_data(fieldnames=(first, second))
    return data.groupby(first)[second].mean()
