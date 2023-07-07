from django.shortcuts import render
from rest_framework import generics

from .models import Product
from .serializers import ProductSerailizer
# Create your views here.
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from api.authentication import TokenAuthentication
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer
    authentication_classes = [SessionAuthentication,TokenAuthentication]

    
    permission_classes =[IsAdminUser,IsAdminUser]
    def perform_create(self,serializer):
        title = serializer.validated_data.get('title')
        #print("Title:",title)
        content = serializer.validated_data.get('content') or None
        if content==None:
            content=title
        print("CONTENT:",content)
        serializer.save(content=content)

    def get_queryset(self,*args, **kwargs):
        #qs = super().get_queryset(*args, **kwargs)
        request = self.request
        #print(request.user)
        user = request.user
        if not user.is_authenticated:
            return Product.objects.none()
        return super().get_queryset().filter(user=user)
    

product_list_create_view = ProductListCreateAPIView.as_view()



class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer
    def perform_create(self,serializer):
        title = serializer.validated_data.get('title')
        #print("Title:",title)
        content = serializer.validated_data.get('content') or None
        if content==None:
            content=title
        print("CONTENT:",content)
        serializer.save(content=content)

product_create_view = ProductCreateAPIView.as_view()


class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer
    
product_detail_view = ProductDetailApiView.as_view()


class ProductUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        print(instance.content)
        #print("instnace",instance)
        if not instance.content:
            instance.content = instance.title
            print(instance.content)
            instance.save()
            
class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer
    lookup_field = 'pk'
    
    # def perform_update(self, serializer):
    #     instance = serializer.save()
    #     print(instance.content)
    #     #print("instnace",instance)
    #     if not instance.content:
    #         instance.content = instance.title
    #         print(instance.content)
    #         instance.save()
    
    #*************************************Mixings api *********************************#
from .permisions import IsStaffEditorPermission
from rest_framework import authentication,permissions
from rest_framework.generics import mixins
class ProductMixinView(generics.GenericAPIView,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditorPermission]

    def get(self,request,*args, **kwargs):  # if you want pk=None your choice
        print(args,kwargs)
        #print(kwargs.get('pk'))
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request,*args, **kwargs)
        return self.list(request,*args, **kwargs)
    
    def post(self,request, *args, **kwargs):
        print(args,kwargs)
        return self.create(request,*args, **kwargs)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            print(title)
            content = serializer.validated_data.get('content') or None
            print(content)
            if content==None:
                content=title
            serializer.save(content=content)
                
        
        
            
        





from rest_framework.response import Response
#function based view
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
@api_view(['GET','POST'])
def product_alt_view(request,pk=None,*args, **kwargs):
    if request.method =="GET":
        if pk is not None:
            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerailizer(obj,many=False).data
            return Response(data)
        queryset = Product.objects.all()
        serializer = ProductSerailizer(queryset,many=True)
        return Response(serializer.data)
    
    if request.method =="POST":
        serializer = ProductSerailizer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None
            if content ==None:
                content=title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"message":"Invalid Data"},status=400)
        