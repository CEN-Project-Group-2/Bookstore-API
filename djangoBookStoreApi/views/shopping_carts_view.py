import json
from django.http import JsonResponse
from django.views import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from ..models.ShoppingCarts import ShoppingCarts
from ..models.ShoppingCartBooks import ShoppingCartBooks
from ..models.Books import Books
from ..models.BookDetails import BookDetails

class ShoppingCartsView(View):
    def get(self, request, id):
        shopping_cart = ShoppingCarts.objects.get(user_id=id)
        book_details = BookDetails.objects.filter(book__in=shopping_cart.shoppingcartbooks_set.values('book'))
        subtotal = sum(book_detail.price for book_detail in book_details)
        data = {
            'shopping_cart_books_subtotal': subtotal
        }
        return JsonResponse(data, safe=False)
    
    def post(self, request, id):
        try:
            shopping_cart = get_object_or_404(ShoppingCarts.objects.select_related('user'), user_id=id)
            
            # ensure book_id is set in body
            body = json.loads(request.body)
            book_id = body.get('book_id')
            if book_id is None:
                return HttpResponse("book_id is missing from request", status=400)
            
            try:
                book = Books.objects.get(id=book_id)
            except Books.DoesNotExist:
                return HttpResponse("Book does not exist", status=404)
                
            shopping_cart_books = ShoppingCartBooks.objects.filter(shopping_cart=shopping_cart, book=book)
            
            if shopping_cart_books.exists():
                return HttpResponse("Book already exists in the shopping cart", status=400)
            
            ShoppingCartBooks.objects.create(shopping_cart=shopping_cart, book=book)

            return HttpResponse("Book successfully added to shopping cart")
        except ShoppingCarts.DoesNotExist:
            return HttpResponse("Shopping cart does not exist", status=404)
