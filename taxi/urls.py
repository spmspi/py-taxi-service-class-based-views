from django.urls import path

from .views import index

from taxi.views import (ManufacturerListView,
                        CarListView,
                        DriverListView,
                        DriverDetailView,
                        CarDetailView)

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/", ManufacturerListView.as_view(),
         name="manufacturer-list"),
    path("cars/", CarListView.as_view(),
         name="cars-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(),
         name="car-detail"),
    path("drivers/", DriverListView.as_view(),
         name="drivers-list"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(),
         name="drivers-detail"),
]

app_name = "taxi"
