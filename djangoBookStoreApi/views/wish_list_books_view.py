from django.http import JsonResponse
import json

from ..models.WishLists import WishLists
from ..models.WishListBooks import WishListBooks
from ..models.Books import Books
from ..models.Users import Users
from ..models.ShoppingCartBooks import ShoppingCartBooks
from ..models.ShoppingCarts import ShoppingCarts

#Get Request via Wish List Id
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

#Post Request - Create new book entry inside wish_list_books table via existing Book ID and Wish list ID
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
        WishListBooks.objects.create(
            book_id = bookID,
            wish_list_id = wishlistID
        )

        response = {
            'Message' : 'Book has been successfully added to the associated wish list.',
            'book_id' : bookID,
            'wish_list_id' : wishlistID
        }
        return JsonResponse(response, safe=False)

#Post Request - Create a new wish list via existing User ID and unique name for wish list
#Maximum number of wish lists per user is 3.    
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
    
#Delete Request - Remove a book and transfer to associated shopping cart via Book ID and Wish list ID
def delete_book_to_cart(request):
    book_set = Books.objects.all()
    wish_list_set = WishLists.objects.all()

    #Checks used for existing ids and //
    book_id_list = []
    for bID in book_set:
        book_id_list.append(bID.id)

    wish_list_id_list = []
    for wID in wish_list_set:
        wish_list_id_list.append(wID.id)

    #Get data for wish list id variable and book id variable
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        data = {}

    wl_id = data.get('wish_list_id')
    b_id = data.get('book_id')

    #Check whether the two IDs are missing. If so, send error. If not, continue.
    if wl_id == None or b_id == None:
        response = {
            'Error' : 'wish_list_id or book_id are missing. Please enter it again.'
        }
        return JsonResponse(response, safe=False)

    #Check if wish list ID exists in the database. If not, send error. Else, continue.
    if wl_id not in wish_list_id_list:
        response = {
            'Error' : 'wish_list_id does not exist within the database.'
        }
        return JsonResponse(response, safe=False)
    
    #Check if book ID exists in the database. If not, send error. Else, continue.
    if b_id not in book_id_list:
        response = {
            'Error' : 'book_id does not exist within the database.'
        }
        return JsonResponse(response, safe=False)
    
    #Check if id combination exist in wish list books table. If not, send error. Else, continue.
    if WishListBooks.objects.filter(book_id=b_id, wish_list_id=wl_id).exists():
        #Get the user ID to find associated shopping cart.
        user_field_name = 'user_id'
        user_set = WishLists.objects.get(id = wl_id)
        u_id = getattr(user_set, user_field_name)

        shoppign_field_name = 'id'
        shopping_carts_set = ShoppingCarts.objects.get(user_id = u_id)
        sc_id = getattr(shopping_carts_set, shoppign_field_name)

        #Remove book from wish list.
        WishListBooks.objects.filter(book_id=b_id, wish_list_id=wl_id).delete()

        #Add book to associated shopping cart.
        ShoppingCartBooks.objects.create(
            book_id = b_id,
            shopping_cart_id = sc_id
        )

        response = {
            'Message' : 'book_id from wish_list_id has been removed and placed within associated shopping cart.',
        }
        return JsonResponse(response, safe=False)

    else:
        response = {
            'Error' : 'The book_id does not exist within wish_list_id wish list.'
        }
        return JsonResponse(response, safe=False)