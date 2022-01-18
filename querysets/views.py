from django.views import View
from django.http  import JsonResponse


def get_all(request) :
    return JsonResponse({'message' : 'hihi'}, status=200)
