from django.urls import path

from passwords.views import AuthSignUpView

urlpatterns = [
    path("", AuthSignUpView.as_view())
]

