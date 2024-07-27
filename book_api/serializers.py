from rest_framework import serializers
from book_api.models import Book

# class BookSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=120)
#     publish_date = serializers.DateField()
#     number_of_pages = serializers.IntegerField()
#     quantity = serializers.IntegerField()

#     def create(self, data):
#         return Book.objects.create(**data)
    
#     def update(self, instance, data):
#         instance.title = data.get('title', instance.title)
#         instance.publish_date = data.get('publish_date', instance.publish_date)
#         instance.number_of_pages = data.get('number_of_pages', instance.number_of_pages)
#         instance.quantity = data.get('quantity', instance.quantity)
        
#         instance.save()
#         return instance


class BookSerializers(serializers.ModelSerializer):
    
    description = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = '__all__'
    
    # validate the title field
    def validate_title(self, value):
        if value == "Diet Coke":
            raise serializers.ValidationError("Title cannot be Diet Coke")
        return value
    
    #validate the number_of_pages and quantity fields
    def validate(self, data): 
        if data["number_of_pages"] > 200 and data["quantity"] < 5:
            raise serializers.ValidationError("Number of pages cannot be greater than 200 and quantity cannot be less than 5")
        return data
    
    # add the description field to the response
    def get_description(self, obj):
        return obj.title + " is a good book"