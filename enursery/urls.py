"""enursery URL Configuration

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
from django.contrib import admin
from django.urls import path
from nursery.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('flower/', flower, name='flower'),
    path('fruits/', fruits, name='fruits'),
    path('timber/', timber, name='timber'),
    path('herbal/', herbal, name='herbal'),
    path('indoor/', indoor, name='indoor'),
    path('foreign/', foreign, name='foreign'),
    path('spices/', spices, name='spices'),
    path('seed/', seed, name='seed'),
    path('bouquet/', bouquet, name='bouquet'),
    path('fertilizer/', fertilizer, name='fertilizer'),
    path('vegetable/', vegetable, name='vegetable'),
    path('accessories/', accessories, name='accessories'),
    path('tips/', tips, name='tips'),
    path('cart/', cart, name='cart'),
    path('contact/', contact, name='contact'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),

]
