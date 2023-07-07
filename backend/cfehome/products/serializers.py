from rest_framework import serializers
from rest_framework import  validators
from .models import Product
from rest_framework import reverse
from .validation import validate_title
from api.serializers import UserPublicSerializer

#api.models
class   ProductInlineserializer(serializers.Serializer):
     edit_url = serializers.HyperlinkedIdentityField(view_name='product-edit',read_only=True,lookup_field='pk')
     title =  serializers.CharField(read_only=True)


class ProductSerailizer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True) # owner = UserPublicSerializer(source='user',read_only=True)   ===user=owner field Name
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.HyperlinkedIdentityField(view_name='product-edit',read_only=True)
    title = serializers.CharField()
    secondTitle = serializers.CharField(source='title',read_only=True)
    email = serializers.CharField(source='user.email',read_only=True)
    user_name = serializers.CharField(source='user.username',read_only=True)
    my_user_data = serializers.SerializerMethodField()
    related_product = ProductInlineserializer(source='user.product_set.all',many=True,read_only=True)
    # def validate_title(self,value):
    #     qs  = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value}:Is Already Exist")
    #     return value
    def validate(self, attrs):
        if len(attrs['title'])<=4:
            raise serializers.ValidationError("Characte must be 5")
        return attrs
    
    
    class Meta:
        model = Product
        fields = ['pk','user','title','content','price','sale_price','my_discount','url','edit_url','secondTitle','email','user_name','my_user_data','related_product']
        
    def get_my_discount(self,obj):
        if not hasattr(obj,'id'):
            return None
        if not isinstance(obj,Product):
            return None
        return obj.get_discount()
    
    def get_url(self,obj):
        request = self.context.get('request',"ankit")
        if request is not None:
            return None
        return reverse("product-edit",kwargs={"pk":obj.pk},request=request)
    
    def get_my_user_data(self,obj):
        return {
            'user' : obj.user.username,
            'email' : obj.user.email,
            'name' : obj.user.first_name,
        }
        