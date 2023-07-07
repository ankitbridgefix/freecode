from rest_framework import serializers
from rest_framework.response import Response
from django.http.response import JsonResponse

# class ProductInlineserializer(serializers.Serializer):
#     edit_url = serializers.HyperlinkedIdentityField(view_name='product-edit',read_only=True,lookup_field='pk')
#     title =  serializers.CharField(read_only=True)


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField()
    id = serializers.IntegerField()
    # user_product = serializers.SerializerMethodField()

    # def get_user_product(self,obj):
        
    #     user = obj
    #     product = user.product_set.all()
    #     print(product)
    #     return ProductInlineserializer(product,many=True,context=self.context   ).data