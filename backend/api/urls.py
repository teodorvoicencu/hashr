from django.urls import re_path
from rest_framework import routers
from .views import PersonViewSet
from .views import AvgAgePerIndustryView
from .views import AvgSalaryPerIndustryView
from .views import AvgSalaryPerYearsOfExperienceView
from .views import AvgSalaryPerAgeView

router = routers.SimpleRouter()

router.register(r'person', PersonViewSet)

urlpatterns = [
    re_path(r'pandas/avg-age-per-industry/', AvgAgePerIndustryView.as_view(), name="avg-age-per-industry"),
    re_path(r'pandas/avg-salary-per-industry/', AvgSalaryPerIndustryView.as_view(), name="avg-salary-per-industry"),
    re_path(r'pandas/avg-salary-per-years-of-experience/', AvgSalaryPerYearsOfExperienceView.as_view(), name="avg-salary-per-years-of-experience"),
    re_path(r'pandas/avg-salary-per-age/', AvgSalaryPerAgeView.as_view(), name="avg-salary-per-age")
]

urlpatterns += router.urls