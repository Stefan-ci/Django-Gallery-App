from gallery import views
from django.urls import path



urlpatterns = [
    path('', views.home_view, name="home"),
    path('my-gallery/', views.user_gallery_view, name="user-gallery"),
    
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]

