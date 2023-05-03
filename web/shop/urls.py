# Django
from django.urls import path
# Project
from . import views as shopViews

urlpatterns = [
    path('list', shopViews.ListShow.as_view(), name='listShow'),
    path('deleteAll', shopViews.DeleteShopAll.as_view(), name='DeleteShopAll'),
    path('deleteshop', shopViews.deleteshoppage, name='deleteshoppage'),
]