"""
URL configuration for projetG11 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from products import views
from django.contrib.auth import views as auth_view
from products.views import hd, CustomLoginView

urlpatterns = [
    path("home", views.home, name='home'),
    path("admin/", admin.site.urls),
    path("products/", include("products.urls")),
    path("<int:product_id>", views.detail),
    path('create', views.create_product, name='create_product'),
    path('edit/<int:product_id>', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>', views.delete_product, name='delete_product'),
    path("checkout", views.checkout),
    path("", views.hd, name='Hd2'),
    path('confirm', views.confirm , name='confirm'),
    path('about/', views.about, name='about'),
    path('signup',views.SignupPage,name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='Hd2.html'), name="logout"),
    path('contact', views.contact , name='contact'),






]
