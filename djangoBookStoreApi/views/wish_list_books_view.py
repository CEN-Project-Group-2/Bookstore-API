from django.http import JsonResponse
from django.core import serializers

from ..models.WishListBooks import WishListBooks
from ..models.Books import Books

#Get Request via WishList Id
def wish_list_books_view(request, id):
    queryset = WishListBooks.objects.filter(wish_list=id).select_related('book')
    data = serializers.serialize('json', queryset)
    return JsonResponse(data, safe=False)
