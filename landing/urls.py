from django.urls import path, include

app_name = "landing"

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("pricing/", views.pricing, name="pricing"),
    path("business/", views.business, name="business"),
    path("web/", views.web, name="web"),
    path("mobile/", views.mobile, name="mobile"),
]
