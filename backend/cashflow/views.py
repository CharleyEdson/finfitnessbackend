from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Cashflow
from .serializers import CashflowSerializer
from django.shortcuts import get_object_or_404
from authentication.models import User
from datetime import date

# Create your views here.

today = date.today()

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_cash_flow(request):
    cash_flow = Cashflow.objects.filter(user_id=request.user.id).order_by('-id')[:1]
    serializer = CashflowSerializer(cash_flow, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_historical_net_cash_flow(request):
    cash_flow = Cashflow.objects.filter(user_id=request.user.id).order_by('-date')
    serializer = CashflowSerializer(cash_flow, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_net_cash_flow(request, pk):
    if request.method == 'DELETE':
        cash_flow = get_object_or_404(Cashflow,pk=pk)
        cash_flow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)