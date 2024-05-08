from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import *
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Avg
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status


class VendorListCreateView(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaceOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaceOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class HistoricalPurchaseOrderView(generics.RetrieveAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializers_class = HistoricalSerializer

class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'on_time_delivery_rate': serializer.data['on_time_delivery_rate'],
                 'quality_rating_avg': serializer.data['quality_rating_avg'],
                 'average_response_time': serializer.data['average_response_time'],
                 'fulfillment_rate': serializer.data['fulfillment_rate']})
    

class PurchaseOrderAcknowledgeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaceOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def create(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.acknowledgment_date = timezone.now()
        instance.save()
        response_time = PurchaceOrder.objects.filter(vendor=instance.vendor, acknowledgment_date__isnull=False).values_list('acknowledgment_date', 'issue_date')
        average_response_time = sum(abs((ackdate - issue_date).total_seconds()) for ackdate,issue_date in response_time)
        if response_time:
            average_response_time = average_response_time / len(response_time)
        else:
            average_response_time = 0
        instance.vendor.average_response_time = average_response_time
        instance.vendor.save()
        return Response({'acknowledgment_date': instance.acknowledgment_date})


        

        
        



