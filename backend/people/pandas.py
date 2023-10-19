import datetime

from django_pandas.io import read_frame

from .models import Person


def age(date_of_birth):
    today = datetime.date.today()
    return (
        today.year
        - date_of_birth.year
        - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    )


def get_person_data(fieldnames=()):
    queryset = Person.objects.all()
    dataframe = read_frame(queryset)
    dataframe["age"] = dataframe["date_of_birth"].apply(age)
    if len(fieldnames):
        return dataframe[[*fieldnames]]
    return dataframe


def get_avg_by_fields(first, second):
    data = get_person_data(fieldnames=(first, second))
    return data.groupby(first)[second].mean()
