from django.urls import path

from users.views import CreateUserView, LoginView, UpdateUserView


urlpatterns = [
    path("signup/", CreateUserView.as_view(), name="signup"),
    path("profile/", UpdateUserView.as_view(), name="update_profile"),
    path("login/", LoginView.as_view(), name="login"),
]
