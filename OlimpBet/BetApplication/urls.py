"""OlimpBet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name="main"),
    # path('admin', views.admin),
    path('bet_place', views.bet_place),
    path('my_bet', views.my_bet),
    path('rules_info', views.rules_info),
    path('rules', views.rules),
    path('matches', views.matches),
    path('enter', views.enter),
    path('support', views.support),
    path('logout', views.logging_out_view)

]
