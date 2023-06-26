from django.http import JsonResponse
from django.core import serializers
from ..models.ShoppingCarts import ShoppingCarts

def shopping_carts_view(request, id):
    model_values = ShoppingCarts.objects.all()
    data = serializers.serialize('json', model_values)
    return JsonResponse(data, safe=False)