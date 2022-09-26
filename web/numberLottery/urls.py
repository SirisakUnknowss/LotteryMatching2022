# Django
from django.urls import path
# Project
from . import views as numberLotteryViews

urlpatterns = [
    path('list', numberLotteryViews.ListNumberLottery.as_view(), name='listNumberLottery'),
    path('listMatching', numberLotteryViews.ListNumberLotteryMatching.as_view(), name='listNumberLotteryMatching'),
    path('addDuplicateNumber', numberLotteryViews.addDuplicateNumber, name='addDuplicateNumber'),
]