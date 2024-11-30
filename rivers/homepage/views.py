from django.shortcuts import render


def homepage_view(request):
    return render(request, "base.html", {})


def about_view(request):
    if request.user.is_authenticated:
        # Сюда же проверку на роль и перенаправление
        return render(request, "homepage/order_trip.html", {})
    else:
        # Ну это заглушка пока что, для проверки авторизации поставить "about_auth.html"
        return render(request, "homepage/order_trip.html", {})