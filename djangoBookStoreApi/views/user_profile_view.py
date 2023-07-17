from django.http import JsonResponse
from django.core import serializers
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
import json

from ..models.Users import Users

class UserProfileView(View):
    def get(self, request, user_id):
        user = get_object_or_404(Users, id=user_id)
        data = serializers.serialize('json', [user])
        return JsonResponse(data, safe=False)


class CreateUserView(View):
    def post(self, request):
        # Extract JSON data from the request body
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            data = {}

        # Extract username from the JSON data
        username = data.get('username')

        # Check if username is provided and not empty
        if username and password:
            password = data.get('password')
            name = data.get('name')
            email = data.get('email')
            home_address = data.get('home_address')

            hashed_password = make_password(password)

            # Create and save the user with the provided username
            user = Users.objects.create(
                username=username,
                password=hashed_password,
                name=name,
                email=email,
                home_address=home_address
            )

            response = {
                'message': 'User created successfully',
                'user_id': user.id
            }
            return JsonResponse(response)
        else:
            response = {
                'error': 'Username is required'
            }
            return JsonResponse(response, status=400)

class UserDetailView(View):
    def get(self, request):
        username = request.GET.get('username')
        user = get_object_or_404(Users, username=username)
        data = {
            'id': user.id,
            'name': user.name,
            'created_at': user.created_at,
            'deleted_at': user.deleted_at,
            'username': user.username,
            'password': user.password,
            'email': user.email,
            'home_address': user.home_address,
        }
        return JsonResponse(data)
