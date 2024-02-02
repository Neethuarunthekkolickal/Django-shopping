from django.shortcuts import render
from . models import Product
def index(request):
    item=Product.objects.all()
    return render (request,"index.html",{"item":item}) 



