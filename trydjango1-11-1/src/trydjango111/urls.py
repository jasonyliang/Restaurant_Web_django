"""trydjango111 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView

from django.contrib.auth.views import LoginView, password_reset, PasswordResetDoneView



from restaurants.views import (
    restaurant_createview,
    restaurant_listview,
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView

)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name = 'home.html'), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^password_reset/$', password_reset, name='password_reset'),
    url(r'^password_reset_done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^items/', include('menus.urls', namespace='menus')),
    url(r'^restaurants/', include('restaurants.urls', namespace='restaurants')),
    url(r'^about/$', TemplateView.as_view(template_name = 'about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name = 'contact.html'), name='contact'), #need .as_view to function like a function
    ]
