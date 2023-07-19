from django.http import JsonResponse
from django.core import serializers
from ..models.Books import Books

def books_view(request):
    model_values = Books.objects.all()
    data = serializers.serialize('json', model_values)
    return JsonResponse(data, safe=False)
