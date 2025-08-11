from django.urls import path
from .views import todoView,todoJson
urlpatterns=[
    path('',todoJson, name='home')
]