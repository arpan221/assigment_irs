from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from food_app.models import Food
from django.core import serializers
from django.db.models import Q
import json
from simple_search import search_filter

def get_response(message="", data={}, error=[], success=False):
   return {

      "success" : success,
      "error": error,
      "data": data,
      "message" : message,
   }


def values(request):

    query = request.GET.get('value')
    search_fields = ['text']
    food_val = Food.objects.filter(search_filter(search_fields, query)).order_by('-score').order_by('-helpfulness')
    tmpJson = serializers.serialize("json",food_val)
    data = json.loads(tmpJson)
    # data = serializers.serialize('json',food_val)
    # return HttpResponse(data, content_type="application/json")

    # data = food_val
    response = get_response(
               message="Result Present",
               error= None,
               data = data,
                success = True
           )
    return JsonResponse(response)