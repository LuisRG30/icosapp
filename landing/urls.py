from django.urls import path, include

app_name = "landing"

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("select", views.select, name="select"),
    path("contacto", views.contacto, name="contacto"),
    path("desarrollo", views.desarrollo, name="desarrollo"),
    path("pricing", views.pricing, name="pricing"),
    path("message", views.receive_message, name="message"),
    path("business", views.business, name="business"),
    path("web", views.web, name="web"),
    path("mobile", views.mobile, name="mobile"),
]
