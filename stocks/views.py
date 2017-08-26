from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse, JsonResponse
from stocks.models import *
from django.core import serializers


def index(request):
    pname = Product.objects.get(id=1)
    res = {'pname':'','id': 0 ,'quantity': 0,'size': '','subcat':''}
    res['pname'] = pname.name
    res['id'] =pname.id
    res['quantity'] = pname.quantity
    res['size'] = pname.size
    subcat = SubCategory.objects.get(id = pname.subcat.id)
    res['subcat'] = subcat.name
    #jpname = json.dumps(pname)
    return JsonResponse(res)
