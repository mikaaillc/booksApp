
from rest_framework import status
from rest_framework.response import Response


from booksApp.models import BooksModel
from booksApp.api.serializers import BoooksSerializers

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.generics import get_object_or_404


class BooksGetPostAPIView(APIView):
    
    def get(self,request):
        books =BooksModel.objects
        seralizer=BoooksSerializers(books,many=True)
        returnData=seralizer.data
        return Response(returnData)

    def post(self,request):
            serializer=BoooksSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class BooksGetByStatusAPIView(APIView):
    
    def get(self,request,pk):
        books =BooksModel.objects.filter(status=pk)
        seralizer=BoooksSerializers(books,many=True)
        return Response(seralizer.data)
        
class BooksUpdateAPIView(generics.GenericAPIView):
    serializer_class=BoooksSerializers
    
    def get_object(self,pk):
        book_instance=get_object_or_404(BooksModel,pk=pk)
        return book_instance
        
    def put(self,request,pk):
        book=self.get_object(pk=pk)
        serializer=BoooksSerializers(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class BooksDeleteAPIView(generics.GenericAPIView):
    serializer_class=BoooksSerializers

    def get_object(self,pk):
        book_instance=get_object_or_404(BooksModel,pk=pk)
        return book_instance
    
    def delete(self,pk):
        book=self.get_object(pk)
        book.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )