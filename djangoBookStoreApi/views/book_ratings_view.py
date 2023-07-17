import json
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404
from ..models import Books, BookRatings, Users

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

