# Django
from django.urls import path
# Project
from . import views as shopViews

urlpatterns = [
    path('list', shopViews.ListShow.as_view(), name='listShow'),
]