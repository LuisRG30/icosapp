from django.urls import path, include

app_name = "landing"

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("select", views.select, name="select"),
    path("contacto", views.contacto, name="contacto"),
    path("desarrollo", views.desarrollo, name="desarrollo"),
    path("pricing", views.pricing, name="pricing"),
]
