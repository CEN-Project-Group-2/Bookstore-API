from django.http import JsonResponse
from django.core import serializers
from django.views import View
from django.shortcuts import get_object_or_404

from ..models.Users import Users

class UserProfileView(View):
    def get(self, request, user_id):
        user = get_object_or_404(Users, id=user_id)
        data = serializers.serialize('json', [user])
        return JsonResponse(data, safe=False)
