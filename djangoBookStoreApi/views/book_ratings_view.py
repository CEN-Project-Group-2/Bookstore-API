import json
from django.db.models import F
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404
from ..models import Books, BookRatings, Users

def get_books_by_rating(request):
    if request.method == 'GET':
        rating = request.GET.get('rating')
        if rating is not None:
            try:
                rating = float(rating)
                books = Books.objects.filter(rating__gte=rating)
                data = [
                    {
                        'title': book.title,
                        'author': book.author,
                        'rating': book.rating,
                        # Add other fields you want to include in the response
                    }
                    for book in books
                ]
                return JsonResponse(data, safe=False)
            except ValueError:
                return JsonResponse({'error': 'Invalid rating value.'}, status=400)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)



def discount_books_by_publisher(request):
    if request.method in ['PUT', 'PATCH']:
        discount_percent = request.GET.get('discount_percent')
        publisher_id = request.GET.get('publisher')
        if discount_percent is not None and publisher_id is not None:
            try:
                discount_percent = float(discount_percent)
                books = Books.objects.filter(publisher=publisher_id)
                for book in books:
                    book.price -= (book.price * discount_percent) / 100
                    book.save()
                return JsonResponse({'message': 'Books discounted successfully.'})
            except ValueError:
                return JsonResponse({'error': 'Invalid discount percent value.'}, status=400)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)

class BookRatingsView(View):
    def post(self, request, id):
        try:
            book = get_object_or_404(Books, id=id)
        
            body = json.loads(request.body)
            rating = body.get('rating')
            if rating is None:
                return HttpResponse("rating is missing from request", status=400)
            
            if rating > 5 or rating < 1:
                return HttpResponse("Invalid rating", status=400)
            
            userId = body.get('user_id')
            if userId is None:
                return HttpResponse("user_id is missing from request", status=400)
            
            user = get_object_or_404(Users, id=userId)
            
            BookRating = BookRatings.objects.create(book=book, rating=rating, user=user)

            return JsonResponse({
                "message": "Book rating added successfully",
                "rating_id": BookRating.id,
                "book_id": id,
                "rating": rating,
                "user_id": userId,
            })
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}", status=500)
        
