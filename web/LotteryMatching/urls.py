"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# Project
from base import views as baseViews
from account import views as accountViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accountViews.homepage, name='homepage'),
    path('signin', accountViews.signin, name='signinpage'),
    path('shop', accountViews.shoppage, name='shoppage'),
    path('user', accountViews.userpage, name='userpage'),
    path('shopmatching', accountViews.shopmatchingpage, name='shopmatchingpage'),
    path('logout', accountViews.logoutpage, name='logoutpage'),
    path('deletelottery', accountViews.deletelotterypage, name='deletelotterypage'),
    path('numberLottery', accountViews.addlotterypage, name='addlotterypage'),
    path('api/user/list', accountViews.ListAccount.as_view(), name='listAccount'),
    path('api/user/deleteUser', accountViews.deleteuserpage, name='deleteuserpage'),
    ## numberLottery ##
    path('api/numberLottery/', include('numberLottery.urls')), 
    ## shop ##
    path('api/shop/', include('shop.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)