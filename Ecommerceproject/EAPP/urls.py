
from . import views
from django.urls import path
app_name='EAPP'

urlpatterns = [
    
    path('',views.allProductCategory,name='allProductCategory'),
    path('<slug:c_slug>/',views.allProductCategory,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='productcatdetail'),
]
