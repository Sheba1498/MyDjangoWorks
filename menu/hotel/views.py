from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from menu.models import menu_items


class MenuView(APIView):
    def get(self,request,*args,**kwargs):
        print(request.query_params)
        if "price_lte" in request.query_params:
            price_lte=int(request.query_params.get("price_lte"))
            data=[item for item in menu_items if item["price"]<=price_lte].pop()
            return Response(data=data)
        return Response(data=items)


    def post(self,request,*args,**kwargs):
        data=request.data
        menu_items.append(data)
        return Response(data=menu_items)


class MenuDetailView(APIView):
    def get(self,request,*args,**kwargs):
        print(kwargs)
        menucode=kwargs.get("menucode")
        item=[item for item in menu_items if item["id"]==menucode].pop()
        return Response(data=item)


    def put(self,request,*args,**kwargs):
        pid = kwargs.get("pid")
        item = [item for item in items if item["id"] == pid].pop()
        item.update(request.data)
        return Response(data=items)

    def delete(self,request,*args,**kwargs):
        pid = kwargs.get("pid")
        item = [item for item in items if item["id"] == pid].pop()
        items.remove(item)
        return Response(data=items)
