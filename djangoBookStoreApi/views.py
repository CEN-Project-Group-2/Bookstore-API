from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


from .models.Users import Users

class UserProfileView(View):
    def get(self, request, user_id):
        user = get_object_or_404(Users, id=user_id)
        profile_data = {
            'id': user.id,
            'name': user.name,
            'created_at': user.created_at,
            'deleted_at': user.deleted_at,
        }
        return JsonResponse(profile_data)

def test_view(request):
    return HttpResponse("This is a test view.")