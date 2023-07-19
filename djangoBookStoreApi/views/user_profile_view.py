from django.http import JsonResponse
from django.core import serializers
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
import json

from ..models.Users import Users, CreditCard

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

class CreateCreditCardView(View):
    def post(self, request):
        # Extract JSON data from the request body
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            data = {}

        # Extract username and credit card details from the JSON data
        username = data.get('username')
        credit_card_number = data.get('credit_card_number')
        expiration_date = data.get('expiration_date')

        # Check if username and credit card details are provided
        if username and credit_card_number and expiration_date:
            # Get the user instance
            try:
                user = Users.objects.get(username=username)
            except Users.DoesNotExist:
                return JsonResponse({'error': 'User does not exist'}, status=400)

            # Create a new credit card instance
            credit_card = CreditCard.objects.create(
                user=user,
                credit_card_number=credit_card_number,
                expiration_date=expiration_date
            )

            data = {
                'message': 'Credit card created successfully',
                'credit_card_id': credit_card.id
            }
            return JsonResponse(data)
        else:
            data = {
                'error': 'Username, credit card number, and expiration date are required'
            }
            return JsonResponse(data, status=400)

class UserUpdateView(View):
    def put(self, request, user_id):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            data = {}

        # Retrieve the user object by user_id
        try:
            user = Users.objects.get(id=user_id)
        except Users.DoesNotExist:
            response = {
                'error': 'User not found'
            }
            return JsonResponse(response, status=404)

        # Update the user fields except for email
        for key, value in data.items():
            if key != 'email':
                setattr(user, key, value)

        # Save the updated user
        user.save()

        response = {
            'message': 'User updated successfully',
            'user_id': user.id
        }
        return JsonResponse(response)