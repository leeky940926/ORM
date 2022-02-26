import json
from django.views import View
from django.http import JsonResponse
from django.db import transaction
from django.contrib.auth.hashers import make_password, check_password

from passwords.models import AuthUser

class AuthSignUpView(View):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body)
        
        phone_number = data["phone_number"]
        password = data["password"]
        password = make_password(password=password)
        
        AuthUser.objects.create(
            phone_number=phone_number,
            password=password
        )
        
        return JsonResponse({'message' : 'created'}, status=201)