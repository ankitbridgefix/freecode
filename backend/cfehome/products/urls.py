from django.urls import path
from products import views

urlpatterns = [
    path("",views.product_list_create_view,name='product-list'),
    path("<int:pk>/",views.product_detail_view,name='product-detail'),
    path("<int:pk>/update/",views.ProductUpdateAPIView.as_view(),name='product-edit'),
    path("<int:pk>/delete/",views.ProductDeleteAPIView.as_view()),
    path("product_m",views.ProductMixinView.as_view()),
    path("product_m/<int:pk>/",views.ProductMixinView.as_view()),
]
