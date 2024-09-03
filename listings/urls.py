from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='listings'), #/Listings/
   path('<int:listing_id>', views.listing, name='listing'), #/Listings/id [1,2,3,4]
   path('search', views.search, name='search'), #/Listings/Search
]
