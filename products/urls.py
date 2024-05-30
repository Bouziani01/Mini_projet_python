from django.urls import path
from products import views
from django.contrib.auth import views as auth_view
app_name = 'products'

urlpatterns = [
    path('home', views.home, name='home'),
    path('<int:product_id>', views.detail, name="detail"),
    path('create', views.create_product, name='create_product'),
    path('edit/<int:product_id>', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>', views.delete_product, name='delete_product'),
    path('checkout', views.checkout, name='checkout'),
    path('', views.hd, name='Hd2'),
    path('confirm', views.confirm , name='confirm'),
    path('about/', views.about , name='about'),
    path('signup',views.SignupPage,name='signup'),
    path('login/', auth_view.LoginView.as_view(template_name='Hd2.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='Hd2.html'), name="logout"),
    path('contact/', views.contact, name='contact'),





] 
