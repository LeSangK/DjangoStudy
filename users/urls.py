from django.urls import path

from users.views import CreateUserView, UpdateUserView


urlpatterns = [
    path("signup/", CreateUserView.as_view(), name="signup"),
    path("profile/", UpdateUserView.as_view(), name="update_profile"),
]
