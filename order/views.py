from crypt import methods
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from order.models import Shop, Menu, Order, Orderfood
from order.serializers import ShopSerializer


@csrf_exempt
def shop(request):
    if request.methods == 'GET':
        shop = Shop.objects.all()
        serializer = ShopSerializer(shop, many=True)
        return JsonResponse(serializer.data, safe=False)

    # elif request.methods == 'POST':
