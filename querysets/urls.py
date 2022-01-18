from django.urls     import path
from querysets.views import get_all

urlpatterns = [
    path('/all', get_all)
]