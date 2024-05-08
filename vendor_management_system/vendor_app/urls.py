# vendor_app/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('vendors/', VendorListCreateView.as_view(), name='vendor-list-create'), 
    path('vendors/<int:pk>/', VendorRetriveUpdateDeleteView.as_view(), name='vendor-retrieve-update-delete'),
    path('purchase_orders/',PurchaseOrderListCreateView.as_view(), name='purchase-order-list'),
    path('purchase_orders/<int:pk>/',PurchaseOrderRetriveUpdateDeleteView.as_view(), name='purchase-order-retrive-update-delete'),
    path('vendors/<int:pk>/performance/', VendorPerformanceView.as_view(),name='vendor-performance-data'),
    path('purchase_orders/<int:pk>/acknowledge/',PurchaseOrderAcknowledgeView.as_view(), name='purchase-order-retrive-update-delete'),
    path('//<int:pk>/', HistoricalPurchaseOrderView.as_view(), name='historical_view')
]