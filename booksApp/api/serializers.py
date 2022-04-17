

from rest_framework import serializers
from booksApp.models import BooksModel
from django.db.models import Sum

class BoooksSerializers(serializers.ModelSerializer):
    
    status = serializers.SerializerMethodField()#önemli
    stock=serializers.SerializerMethodField()
    sum_books=serializers.SerializerMethodField()#eksik
    
    class Meta:
        model = BooksModel
        fields = ('pk','name','status','numberOfBook','stock','sum_books')
        #read_only_fields=['pk','total_numberOfBook']
        
    def get_status(self,object):
        if object.status=='0':
            return  'Mevcut'
        elif object.status=='1':
            return   'Satıldı'
        elif object.status=='2':
            return   'Kiralandı'
    def get_stock(self,object):
        if object.numberOfBook>0:
            return 1
        elif object.numberOfBook==0:
            return -1
    def get_sum_books(self,objects):
        return  BooksModel.objects.all().aggregate(Sum('numberOfBook'))
    

      