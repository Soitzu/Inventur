from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.redirect_start, name="redirect_start"),
    path("output/", views.output_data, name="output_data"),
    path("download/", views.download_excel, name="download_excel"),
    path("success/", views.success, name="success"),
    path("start/", views.start, name="start"),
    path("form/", views.user_form, name="user_form"),
]
