# Django
from django.urls import path
# Project
from . import views as numberLotteryViews

urlpatterns = [
    path('list', numberLotteryViews.ListNumberLottery.as_view(), name='listNumberLottery'),
    path('add', numberLotteryViews.addNumberApi, name='addNumberApi'),
]