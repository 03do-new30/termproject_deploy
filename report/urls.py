from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("report/<int:id>", reportMain, name="report")

]
