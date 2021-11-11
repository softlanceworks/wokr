from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import generics

from .models import Location, Tour
from .serializers import LocationSerializers, TourSerializers
from rest_framework.response import Response
# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view,permission_classes
from django.views.decorators.csrf import csrf_exempt

def trip_home(request):
    return render(request,'tour/alltrip.html')

def add_trip(request):
    return render(request,'tour/add_trip.html')


def categories_trip(request):
    return render(request,'tour/categories_trip.html')


def attr_trip(request):
    return render(request,'tour/attr_trip.html')

def trip_availbility(request):
    return render(request,'tour/trip_availbility.html')
def trip_recovery(request):
    return render(request,'tour/trip_recovery.html')

def edit_trip(request):
    return render(request,'tour/edit_trip.html')





class TourView(generics.ListCreateAPIView):
    queryset=Tour.objects.all()
    serializer_class=TourSerializers
class TourDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Tour.objects.all()
    serializer_class=TourSerializers



class LocationView(generics.ListCreateAPIView):
    queryset=Location.objects.all()
    serializer_class=LocationSerializers



class LocationViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Location.objects.all()
    serializer_class=LocationSerializers


# class RoomImageView(generics.ListCreateAPIView):
#     queryset=RoomImage.objects.all()
#     serializer_class=RoomImageSerializers


@api_view(['GET','POST',"PUT","DELETE"])
@permission_classes({AllowAny})
@csrf_exempt
def locations_list(request):
    loc=Location.objects.all()
    serializer=LocationSerializers(loc)
    return Response(serializer)


