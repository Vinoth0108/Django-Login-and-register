# from django.contrib import admin
# from django.urls import path, include
# from Myapp import views


# urlpatterns = [
#     path('', views.index, name="index"),
#     path('signup/', views.signup, name="signup"),
#     path('signin/', views.signin, name="signin"),
#     path('signout/', views.signout, name="signout"),

# ]

from django.contrib import admin
from django.urls import path, include
from Myapp import views
urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
]