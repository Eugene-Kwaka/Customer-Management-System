from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [

    # REGISTER & lOGIN URL PATHS
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),


    # USER-CUSTOMER ACCESS URL PATHS
    path('', views.home, name='home'),
    path('user/', views.userPage, name='user_page'),
    path('account/', views.accountSettings, name='account_settings'),
    path('products/', views.products, name='products'),


    # ADMIN-CUSTOMER ACCESS URL PATHS
    path('customers/<str:pk>/', views.customers, name='customers'),
    path('CreateCustomer/', views.CreateCustomer, name='CreateCustomer'),
    path('UpdateCustomer/<str:pk>/', views.UpdateCustomer, name='UpdateCustomer'),
    path('DeleteCustomer/<str:pk>/', views.DeleteCustomer, name='DeleteCustomer'),


    # ADMIN-PRODUCT ACCESS URL PATHS
    path('CreateProduct/', views.CreateProduct, name='CreateProduct'),
    path('UpdateProduct/<str:pk>/', views.UpdateProduct, name='UpdateProduct'),
    path('DeleteProduct/<str:pk>/', views.DeleteProduct, name='DeleteProduct'),






    # ORDER URL PATHS
    path('CreateOrder/<str:pk>/', views.CreateOrder, name='CreateOrder'),
    path('UpdateOrder/<str:pk>/', views.UpdateOrder, name='UpdateOrder'),
    path('DeleteOrder/<str:pk>/', views.DeleteOrder, name='DeleteOrder'),


    # PASSWORD RESET URL PATHS
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name="accounts/password_reset.html"), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_sent.html"), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="accounts/password_reset_form.html"), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="accounts/password_reset_done.html"), name="password_reset_complete"),
]
