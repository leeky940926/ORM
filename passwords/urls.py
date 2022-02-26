from django.urls import path

from passwords.views import AuthSignInView, AuthSignUpView

urlpatterns = [
    path("/signup", AuthSignUpView.as_view()),
    path("/signin", AuthSignInView.as_view())
]

