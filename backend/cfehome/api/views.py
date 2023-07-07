from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerailizer
# Create your views here.
@api_view(['POST'])
def api_home(request,*args, **kwargs):
    # data = request.body
    # p_data =json.loads(data)
    # id = p_data['id']
    # model_data = Product.objects.all().order_by("?").first()
    # data = {}
    # if model_data:
        # data['id'] = model_data.pk
        # data['title'] = model_data.title
        # data['content'] =model_data.content
        # data['price'] = model_data.price
        # data = model_to_dict(model_data)
        # print(data)
    #data ={
    # instance = Product.objects.all().order_by("?").first()
    # if instance:
    #     data = ProductSerailizer(instance).data
    # data =request.data
    # print(data)
    serializer = ProductSerailizer(data=request.data)
    #print(serializer)  # show serializers all
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()

        print(instance)
        return Response(serializer.data)
    return Response({"invalid":"Data is not good"},status=400)
