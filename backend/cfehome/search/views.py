from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from products.models import *
from products.serializers import *
class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer

    def get_queryset(self,*args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        user = None
        q = self.request.GET.get('q')
        result = Product.objects.none()
        if q is not None:
            if self.request.user.is_authenticated:
                user = self.request.user
            result = qs.search(q,user=user)
        return result
    
