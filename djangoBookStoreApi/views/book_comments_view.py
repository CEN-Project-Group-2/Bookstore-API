import json
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404
from ..models import Books, BookComments, Users

class BookCommentsView(View):
    def post(self, request, id):
        try:
            book = get_object_or_404(Books, id=id)
        
            body = json.loads(request.body)
            comment = body.get('comment')
            if comment is None:
                return HttpResponse("comment is missing from request", status=400)
            
            userId = body.get('user_id')
            if userId is None:
                return HttpResponse("user_id is missing from request", status=400)
            
            user = get_object_or_404(Users, id=userId)
            
            bookComment = BookComments.objects.create(book=book, comment=comment, user=user)

            return JsonResponse({
                "message": "Book comment added successfully",
                "comment_id": bookComment.id,
                "book_id": id,
                "comment": comment,
                "user_id": userId,
            })
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}", status=500)

