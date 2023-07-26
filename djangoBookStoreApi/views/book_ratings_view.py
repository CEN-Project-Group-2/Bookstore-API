import json
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404
from ..models import Books, Users
from ..models import BookRatings
from django.db.models import Avg

class BookRatingsView(View):
    def post(self, request, id):
        try:
            book = get_object_or_404(Books, id=id)
        
            body = json.loads(request.body)
            score = body.get('score')
            if score is None:
                return HttpResponse("score is missing from request", status=400)
            
            if score > 5 or score < 1:
                return HttpResponse("Invalid score", status=400)
            
            userId = body.get('user_id')
            if userId is None:
                return HttpResponse("user_id is missing from request", status=400)
            
            user = get_object_or_404(Users, id=userId)
            
            BookRating = BookRatings.objects.create(book=book, score=score, user=user)

            return JsonResponse({
                "message": "Book score added successfully",
                "rating_id": BookRating.id,
                "book_id": id,
                "score": score,
                "user_id": userId,
            })
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}", status=500)

class BookRatingsAvgView(View):
    def get(self, request, id):
        try:
            all_ratings = BookRatings.objects.all()
            average_rating = all_ratings.aggregate(Avg('score'))['score__avg']
            return JsonResponse({'average_rating': average_rating})
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}", status=500)