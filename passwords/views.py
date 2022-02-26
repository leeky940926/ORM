import json
import jwt
from django.conf import settings
from django.views import View
from django.http import JsonResponse
from django.db import transaction
from django.contrib.auth.hashers import make_password, check_password
from passwords.models import AuthUser
from rest_framework import status

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


class AuthSignInView(View):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body)
        
        phone_number = data["phone_number"]
        password = data["password"]
        
        user = AuthUser.objects.get(phone_number=phone_number)
        
        if not check_password(password=password, encoded=user.password):
            return 1
        token = jwt.encode(
            payload={"user_id": user.id}, 
            key=settings.SECRET_KEY,
            algorithm=settings.ALGORITHMS
        )
        
        return JsonResponse({"token" : token}, status=201)
