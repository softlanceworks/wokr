from django.core import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from django.core import serializers
from django.db.models import fields, manager
from rest_framework import serializers
from urllib import request
from rest_framework import routers, serializers, viewsets
from django.http import HttpResponse
from rest_framework import serializers

from Hotels.models import Hotel, RoomImage, Rooms


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model=Hotel
        fields="__all__"


class RoomSerializers(serializers.ModelSerializer):
    manager_id = HotelSerializers(many=True, read_only=True)

    class Meta:
        model=Rooms
        fields="__all__"


class RoomImageSerializers(serializers.ModelSerializer):
    room = RoomSerializers(many=True, read_only=True, required=False)

    class Meta:
        model=RoomImage
        fields="__all__"
