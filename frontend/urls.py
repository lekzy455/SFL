from django.urls import path
from .views import index, schedule, result, table

app_name = "frontend"

urlpatterns = [
    path('home/', index, name="index"),
    path('fixtures/', schedule, name="schedule"),
    path('results/', result, name="result"),
    path('table/', table, name="table")
]