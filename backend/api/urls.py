from django.urls import include
from django.urls import path
from django.urls import re_path
from rest_framework import routers

from .views.pandas_views import AvgAgePerIndustryView
from .views.pandas_views import AvgSalaryPerAgeView
from .views.pandas_views import AvgSalaryPerIndustryView
from .views.pandas_views import AvgSalaryPerYearsOfExperienceView
from .views.person_views import PersonViewSet


router = routers.SimpleRouter()

router.register(r"person", PersonViewSet)

pandas_urlpatterns = [
    re_path(
        r"avg-age-per-industry/$", AvgAgePerIndustryView.as_view(), name="avg-age-per-industry"
    ),
    re_path(
        r"avg-salary-per-industry/$",
        AvgSalaryPerIndustryView.as_view(),
        name="avg-salary-per-industry",
    ),
    re_path(
        r"avg-salary-per-years-of-experience/$",
        AvgSalaryPerYearsOfExperienceView.as_view(),
        name="avg-salary-per-years-of-experience",
    ),
    re_path(r"avg-salary-per-age/$", AvgSalaryPerAgeView.as_view(), name="avg-salary-per-age"),
]

urlpatterns = [path("pandas/", include(pandas_urlpatterns))]
urlpatterns += router.urls
