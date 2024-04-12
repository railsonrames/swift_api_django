from django.urls import path
from . import views

urlpatterns = [
    # path('list/', views.list_items, name='list_items'),  # URL pattern for listing items
    # path('detail/<int:item_id>/', views.item_detail, name='item_detail'),  # URL pattern for item detail with item ID
    path('filter/', views.filter_list, name='filter_list'),  # URL pattern for filtering items
]