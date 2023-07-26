from django.http import JsonResponse
from django.core import serializers
from django.views import View
from django.shortcuts import get_object_or_404
import json

from ..models.Author import Author
from ..models.BookDetails import BookDetails


class CreateAuthorView(View):
    def post(self, request):
        # Extract JSON data from the request body
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            data = {}

        # Extract first_name, last_name, biography and publisher details from the JSON data
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        biography = data.get('biography')
        publisher = data.get('publisher')

        # Check if all author details are provided
        if first_name and last_name and biography and publisher:

            # Create a new author instance
            author = Author.objects.create(
                first_name=first_name,
                last_name=last_name,
                biography=biography,
                publisher=publisher
            )

            data = {
                'message': 'Author created successfully',
                'author_id': author.id
            }
            return JsonResponse(data)
        else:
            data = {
                'error': 'first_name, last_name, biography and publisher details are required'
            }
            return JsonResponse(data, status=400)


# Get book details list of the given author id
def get_book_details_list_given_author_id(request, author_id):
    # First find the author for given author id
    author = Author.objects.filter(id=author_id)
    if author and len(author) > 0:  # if author exist for given author_id
        book_details_list = []
        # Find the book details query set for given author
        queryset = BookDetails.objects.filter(author=author[0].first_name)
        for qs in queryset:
            book_details_list.append({
                'ID:': qs.id,
                'Book ID:': qs.book_id,
                'ISBN:': qs.ISBN,
                'Book Description:': qs.description,
                'Book Price:': qs.price,
                'Book Publisher:': qs.publisher,
                'Book Year:': qs.year,
                'Number of Copies Sold:': qs.copies_sold
            })
        return JsonResponse(book_details_list, safe=False)
    else:
        data = {
            'error': 'author not found'
        }
        return JsonResponse(data, status=400)
