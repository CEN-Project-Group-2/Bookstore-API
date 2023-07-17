from django.http import JsonResponse
from django.core import serializers
from ..models import BookDetails

def book_details_view(request, id):
    model_values = BookDetails.objects.all()
    data = serializers.serialize('json', model_values)
    return JsonResponse(data, safe=False)

def genre_view(request):
    genre = BookDetails.objects.values_list('genre', flat=True).distinct()
    return JsonResponse(list(genre), safe=False)

def best_selling_books(request):
    copies_sold = BookDetails.objects.values_list('copies_sold', flat=True).distinct()
    return JsonResponse(list(copies_sold), safe=False)

