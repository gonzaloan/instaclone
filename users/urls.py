"""Users Urls"""

from django.urls import path

# Views
from users import views

urlpatterns = [

    # Management
    path(route='users/login/',
         view=views.LoginView.as_view(),
         name='login'),
    path(route='users/logout/',
         view=views.LogoutView.as_view(),
         name='logout'),
    path(route='users/signup/',
         view=views.SignUpView.as_view(),
         name='signup'),
    path(route='users/me/profile/',
         view=views.UpdateProfileView.as_view(),
         name='update_profile'),

    # Posts
    path(
        route='users/<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
]
