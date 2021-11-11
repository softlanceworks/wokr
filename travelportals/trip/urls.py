from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.trip_home,name="trip_home"),
    # path('location/', views.LocationView.as_view(),name="trip_home"),
    path('Tour/', views.TourView.as_view(),name="TourView"),

    path('location/<int:pk>/', views.LocationViewDetail.as_view(),name="trip"),

    path('addtour/', views.add_trip,name="trip_add"),
    path('edit/', views.edit_trip,name="edit_trip"),

    path('categories_trip/', views.categories_trip,name="categories_trip"),

    path('attr_trip/', views.attr_trip,name="attr_trip"),
    path('trip_recovery/', views.trip_recovery,name="trip_recovery"),
    path('trip_availbility/', views.trip_availbility,name="trip_availbility"),


]

urlpatterns = format_suffix_patterns(urlpatterns)
