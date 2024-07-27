# from django.shortcuts import render
# from book_api.models import Book
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from book_api.serializers import BookSerializers

# @api_view(['GET'])
# def book_list(request):
#     books = Book.objects.all()
#     serializers = BookSerializers(books, many=True)
#     return Response(serializers.data)
    
# @api_view(['POST'])
# def book_create(request):
#     serializer = BookSerializers(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)


# @api_view(['GET', 'PUT', 'DELETE'])
# def book(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Book not found!'})
    
    
#     if request.method == 'GET':
#         serializer = BookSerializers(book) 
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         serializer = BookSerializers(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    
#     if request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_200_OK, data={'message': 'Book deleted successfully!'})
    


##########################################
##########################################
##########################################



from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from book_api.serializers import BookSerializers
from book_api.models import Book

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializers = BookSerializers(books, many=True)
        return Response(serializers.data)    

    
class Bookcreate(APIView):

    def post(self, request):
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    
class BookModify(APIView):
    def get_book_by_id(self, pk):
        try:
            book =  Book.objects.get(pk=pk)
        except:
            return Response({'error': 'Book not found!'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        book = self.get_book_by_id(pk)
        serializer = BookSerializers(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, request, pk):
        book = self.get_book_by_id(pk)
        book.delete()
        return Response({'message': 'Book deleted successfully!'}, status=status.HTTP_200_OK)
 