from django.http import JsonResponse
from django.core import serializers
from ..models import Books
from ..models import BookDetails
from django.views import View
import json
from datetime import date

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


def get_all_book_details_view(request):
    model_values = BookDetails.objects.all()
    data = serializers.serialize('json', model_values)
    return JsonResponse(data, safe=False)


def get_book_details_by_isbn_view(request):
    model_values = BookDetails.objects.all()
    isbn = request.GET.get('isbn', None)
    if isbn is not None:
        model_values = model_values.filter(ISBN=isbn)
        data = serializers.serialize('json', model_values)
        return JsonResponse(data, safe=False)
    else:
        data = {
            'message': 'Given Query Param not found'
        }
        return JsonResponse(data)


class CreateBookDetailsView(View):
    def post(self, request):
        # Extract JSON data from the request body
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            data = {}

        # Extract first_name, last_name, biography and publisher details from the JSON data
        isbn = data.get('isbn')
        name = data.get('name')
        description = data.get('description')
        price = float(data.get('price'))
        author = data.get('author')
        genre = data.get('genre')
        publisher = data.get('publisher')
        year = int(data.get('year'))
        copies_sold = int(data.get('copies_sold'))

        # Check if all author details are provided
        if isbn and name and description and price and author and genre and publisher and year and copies_sold:

            # Create a new book instance
            today = date.today()

            book = Books.objects.create(
                name=name,
                created_at=today
            )

            book_details = BookDetails.objects.create(
                book_id=book.id,
                ISBN=isbn,
                description=description,
                price=price,
                author=author,
                publisher=publisher,
                year=year,
                copies_sold=copies_sold
            )

            data = {
                'message': 'Book created successfully',
                'book_id': book.id,
                'book_details_id': book.id,
            }
            return JsonResponse(data)
        else:
            data = {
                'error': 'isbn, name, description, price, author, genre, publisher, year and copies_sold are required'
            }
            return JsonResponse(data, status=400)
