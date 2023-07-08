"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.shortcuts import render
from .sitemaps import StaticViewSitemap,ProductViewSitemap
from django.contrib.sitemaps.views import sitemap
from os import getenv
from .import views



sitemaps={
    'static':StaticViewSitemap,
    'product':ProductViewSitemap
}



urlpatterns = [
    path(getenv('ADMIN_URL'), admin.site.urls),
    path('robots.txt',views.robots),
    path("sitemap.xml",sitemap,{"sitemaps": sitemaps},name= "django.contrib.sitemaps.views.sitemap"),
    path("i18n/", include("django.conf.urls.i18n")),
] + i18n_patterns(
    path('',include('shop.urls')),
    path('customer/',include('customer.urls')),
    path('payment/',include('payment.urls')),
)

