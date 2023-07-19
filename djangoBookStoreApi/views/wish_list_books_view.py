from django.http import JsonResponse
from django.core import serializers
import json

from ..models.WishLists import WishLists
from ..models.WishListBooks import WishListBooks
from ..models.Books import Books
from ..models.Users import Users

#Get Request via WishList Id
def wish_list_books_view(request, id):
    #Generates a queryset of a inner join between wish_list_books and books tables
    queryset = WishListBooks.objects.filter(wish_list=id).select_related('book')
    book_list = []
    #Store book names inside an empty array by going through each object
    for qs in queryset:
        book_list.append({
            'Book Name:' : qs.book.name
        })
    return JsonResponse(book_list, safe=False)

#Post Request - Create new book entry inside wish_list_books table via existing Book ID and Wishlist ID
def add_book_to_wishlist(request):
    #Generate queryset of all book and wishlists.
    bookset = Books.objects.all()
    wishlistSet = WishLists.objects.all()

    #List to be filled with IDs for checks
    bookID_list = []
    for bID in bookset:
        bookID_list.append(bID.id)
    
    wishlist_list = []
    for wID in wishlistSet:
        wishlist_list.append(wID.id)
    
    #Obtain book ID and wishlist ID from POST request
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        data = {}

    #Obtain both IDs and set them to their associated variables for checks.
    bookID = data.get('book_id')
    wishlistID = data.get('wish_list_id')

    #Check if either ID is missing in request. If so, send error. Else, continue with bookID check.
    if bookID == None or wishlistID == None:
        response = {
            'Error' : 'book_id or wish_list_id missing. Please enter it again.'
        }
        return JsonResponse(response, safe=False)
    
    #Check for existing book ID. If not, send error. Else, continue to wishlistID check.
    if bookID not in bookID_list:
        response = {
            'Error' : 'book_id submitted does not exist within the database.'
        }
        return JsonResponse(response, safe=False)
    
    #Check for existing wishlist ID. If not, send error. Else, create new wishlist_book into associated table.
    if wishlistID not in wishlist_list:
        response = {
            'Error' : 'wish_list_id submitted does not exist within the database.'
        }
        return JsonResponse(response, safe=False)
    else:
        #Create new book entry in to the Wish_List_Books table on mysql. Then state its success.
        addbook = WishListBooks.objects.create(
            book_id = bookID,
            wish_list_id = wishlistID
        )

        response = {
            'Message' : 'Book has been successfully added to the associated wish list.',
            'book_id' : bookID,
            'wish_list_id' : wishlistID
        }
        return JsonResponse(response, safe=False)
    
def create_new_wishlist(request):
    #Generate two sets for checks. One for user IDs, the other for available names.
    userSet = Users.objects.all()
    wishlistSet = WishLists.objects.all()

    #Lists to be filled out with their associated info.
    userID_list = []
    for uID in userSet:
        userID_list.append(uID.id)

    wishlistName_List = []
    for wID in wishlistSet:
        wishlistName_List.append(wID.wishlist_name)

    #Obtain user ID and their wishlist name.
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        data = {}
    
    #Place the ID and wishlist into their associated variables.
    userID = data.get('user_id')
    wishlistName = data.get('wish_list_name')

    #Check whether userID or wishlist name is missing. If so, send error. If not, continue to next check.
    if userID == None or wishlistName == None:
        response = {
            'Error' : 'user_id or wish_list_name is missing. Please enter it again.'
        }
        return JsonResponse(response, safe=False)

    #Check if the associated user has more than 3 wishlists. If so, send error. Else, continue to next check.
    userCount = WishLists.objects.filter(user_id=userID).count()
    if userCount >= 3:
        response = {
            'Error' : 'The user has reached the max number of wish lists (3).'
        }
        return JsonResponse(response, safe=False)

    #Check if userID exists in the database. If not, send error. Else, continue to next check.
    if userID not in userID_list:
        response = {
            'Error' : 'User ID does not exist within the database.'
        }
        return JsonResponse(response, safe=False)
    
    #Check if wishlist name is available. If not, send error. Else, continue to final part.
    if wishlistName in wishlistName_List:
        response = {
            'Error' : 'Wishlist Name already exists within the database. Please enter a different name.'
        }
        return JsonResponse(response, safe=False)
    else:
        #Create new wishlist with user ID and wishlist name.
        WishLists.objects.create(
            user_id = userID,
            wishlist_name = wishlistName
        )

        response = {
            'Message' : 'New wishlist created.',
            'user_id' : userID,
            'wish_list_name' : wishlistName
        }

        return JsonResponse(response, safe=False)