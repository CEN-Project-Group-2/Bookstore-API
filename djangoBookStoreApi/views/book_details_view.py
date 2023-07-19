from django.http import JsonResponse
from django.core import serializers
from ..models.BookDetails import BookDetails

def book_details_view(request, id):
    model_values = BookDetails.objects.all()
    data = serializers.serialize('json', model_values)
    return JsonResponse(data, safe=False)