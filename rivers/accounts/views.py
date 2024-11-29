from django.shortcuts import render


def accounts_view(request):
    return render(request, "homepage/home.html", {})
