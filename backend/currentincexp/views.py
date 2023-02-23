from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Currentincexp
from .serializers import CurrentincexpflowSerializer
from django.shortcuts import get_object_or_404
from authentication.models import User
from datetime import date
from cashflow.models import Cashflow
from cashflow.serializers import CashflowSerializer

# Create your views here.
today = date.today()
month = today.month - 1
if month == 0:
    month = 12


print(today)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_historical_curents(request):
    currents = Currentincexp.objects.filter(user_id=request.user.id).order_by('-date')
    serializer = CurrentincexpflowSerializer(currents, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_currents(request):
        serializer = CurrentincexpflowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def calculate_cash_flow(request):
    currents = Currentincexp.objects.filter(user_id=request.user.id).order_by('-date')[:1]
    current = []
    for obj in currents:
        current.append(obj.current_income)
        current.append(obj.current_expense)
    net_cash_flow = current[0]-current[1]
    today = date.today()
    month = today.month - 1
    year = today.year
    if month == 0:
        month = 12
        year = year - 1
    new_net_cash_flow = Cashflow.objects.create(user=request.user,net_cash_flow=net_cash_flow, year=year, month=month, date=today)
    cash_flow = Cashflow.objects.filter(user_id=request.user.id)
    serializer = CashflowSerializer(cash_flow, many=True)
    return Response(serializer.data)


@api_view(['PUT', 'DELETE', 'PATCH'])
@permission_classes([IsAuthenticated])
def edit_currents(request,pk):
    current = get_object_or_404(Currentincexp,pk=pk)
    if request.method == 'PUT':
        serializer = CurrentincexpflowSerializer(current, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = CurrentincexpflowSerializer(current, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        current.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

