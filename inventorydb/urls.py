from django.urls import path
from .views import AssignedInventoryListView, InventoryListCreateView, InventoryDetailView, CustomInventoryView, UnassignedInventoryListView

urlpatterns = [
    path('inventory/', InventoryListCreateView.as_view(),
         name='inventory-list-create'),
    path('inventory/<int:pk>/', InventoryDetailView.as_view(),
         name='inventory-detail'),
    path('custom-inventory/', CustomInventoryView.as_view(),
         name='custom-inventory'),
    path('inventory/assigned/', AssignedInventoryListView.as_view(),
         name='assigned-inventory-list'),
    path('inventory/unassigned/', UnassignedInventoryListView.as_view(),
         name='unassigned-inventory-list'),

]
