from django.urls import path
from . import views

urlpatterns = [
    path('phones/', views.phone_list, name='phone-list'),
    path('phones/create/', views.phone_create, name='phone-create'),
    path('phones/<int:pk>/', views.phone_detail, name='phone-detail'),
    path('phones/<int:pk>/update/', views.phone_update, name='phone-update'),
    path('phones/<int:pk>/delete/', views.phone_delete, name='phone-delete'),
    path('phones/search/', views.phone_search, name='phone-search'),
    path('phones/stock/', views.phone_search_stock, name='phone-search-stock'),
    path('phones/filter/', views.filter_location, name='filter-location'),

]
