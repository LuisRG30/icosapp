from django.urls import path, include

app_name = "landing"

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("pricing/", views.pricing, name="pricing")
]
