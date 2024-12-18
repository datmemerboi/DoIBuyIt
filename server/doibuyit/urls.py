"""
URL configuration for doibuyit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers

from products import views

r = routers.DefaultRouter(trailing_slash=False)
r.register(r"products", views.ProductViewSet)
r.register(r"prices", views.PriceViewSet)
r.register(r"vendors", views.VendorsViewSet)
r.register(r"vendor-products", views.VendorProductViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(r.urls)),
    # path('products/', views.product_list),
    # path('prices/', views.price_list),
]
