from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =[

    path('login/', views.loginPage, name='login'),
    path('register/' , views.registerPage, name= 'register'),
    path('logout/' , views.logoutUser, name= 'logout'),
    path('user/' , views.userPage, name='user'),
    path('settings/',views.accountSettings , name='settings' ),

    path("", views.home, name='home'),
    path("products/", views.products, name='products') ,
    path("customer/<str:pk>/", views.customer, name='customer' ),
    path('create_order/<str:pk>', views.createOrder, name='create_order'),
    path('update_order/<str:pk>', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>', views.delete_order, name='delete_order'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view() , name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
