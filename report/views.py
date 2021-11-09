from django.shortcuts import render
from .user_data import user_data

# Create your views here.


def home(request):
    return render(request, "home.html")


def reportMain(request, id):
    data = user_data[str(id)]
    return render(
        request,
        "report.html",
        {
            "id": id,
            "data": data,
        },
    )
