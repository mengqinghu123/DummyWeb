from django.urls import path

from .views import form, success

urlpatterns = [
    path('', form, name='metadata_form'),
    path('success/', success, name='success'),
]
