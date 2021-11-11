from django.core.serializers import serialize
from django.db.models import fields, manager
from django.http import response
from django.http.response import Http404
from django.shortcuts import render
from django.views.generic import CreateView
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from Hotels.forms import HotelForm
from Hotels.models import Hotel, RoomImage, Rooms
from rest_framework.parsers import JSONParser
from .serializers import HotelSerializers, RoomSerializers,RoomImageSerializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework import generics

from rest_framework.response import Response
from rest_framework.reverse import reverse

@permission_classes({AllowAny})
@csrf_exempt
def hotelpage(request):
    form_class=HotelForm
    content={'forms':form_class}
    return render(request,'hotel/hotel.html',content)
    
def add_hotel(request):
    return render(request,'hotel/addNew.html')
def edit_hotel(request):
    return render(request,'hotel/hotel_edit.html')


def edit_room(request):
    return render(request,'hotel/room_edit.html')

def add_hotel_room_attr(request):
    return render(request,'hotel/add_room.html')



def add_hotel_attribute(request):
    return render(request,'hotel/attribute.html')
    
class HotelAdd(CreateView):
    model=Hotel
    fields='__all__'
    template_name='hotel/hotel.html'








@api_view(['GET'])
@permission_classes({AllowAny})
@csrf_exempt
def api_root(request):
  api_urls={
      'List':'/hotel/',
      'Detail View':'/hotel/<str:pk>/',

  }
  return Response(api_urls)

# @api_view(['GET','POST',"PUT","DELETE"])
# @permission_classes({AllowAny})
# @csrf_exempt
# def Roomlist(request):
    
#     if request.method == 'GET':
#         data = Rooms.objects.all()
#         serializer = RoomSerializers(data, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = RoomSerializers(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


# @api_view(['GET','POST',"PUT","DELETE"])
# @permission_classes({AllowAny,})
# @csrf_exempt
# def RoomDetail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Rooms.objects.get(pk=pk)
#     except Hotel.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = RoomSerializers(snippet)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = RoomSerializers(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)


class RoomImageView(generics.ListCreateAPIView):
    queryset=RoomImage.objects.all()
    serializer_class=RoomImageSerializers

class Roomlist(generics.ListCreateAPIView):
    # queryset = Rooms.objects.all()

    def get_queryset(self):
        queryset = Rooms.objects.filter(manager_id=self.kwargs["pk"])
        return queryset    
    serializer_class = RoomSerializers
    
class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializers

class HotelList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()

    serializer_class = HotelSerializers

class HotelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()

    serializer_class = HotelSerializers


@api_view(['GET',"POST"])
def hotelCreate(request):
    
    if request.method == 'GET':
        snippets = Hotel.objects.all()
        serializer = HotelSerializers(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HotelSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(["GET","POST"])
def hotels_list(request):
    
    if request.method == 'GET':
        snippets = Hotel.objects.all()
        serializer = HotelSerializers(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HotelSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(["GET"])
@csrf_exempt
def hotels_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Hotel.objects.get(pk=pk)
    except Hotel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = HotelSerializers(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = HotelSerializers(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=204)