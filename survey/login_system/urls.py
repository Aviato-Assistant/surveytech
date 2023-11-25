from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.signup_view, name='signup'),
    path('sign-in/', views.signin_view, name='login'),
    path('sign-out/', views.signout_view, name='signout'),

]
