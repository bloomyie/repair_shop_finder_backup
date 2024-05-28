from django.contrib import admin
from django.urls import path, include
from shops import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.shop_list, name='shop_list'),  # This ensures the root URL calls shop_list
]
