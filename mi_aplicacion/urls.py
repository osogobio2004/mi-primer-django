from django.urls import path
from . import views
urlpatterns = [
    path('lista/', views.Lista.as_view(), name='milista'),
]
