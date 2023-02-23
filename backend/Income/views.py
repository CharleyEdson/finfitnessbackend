from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Income
from .serializers import IncomeSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def incomeinfo(request):
    print(
    'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'GET':
        incomes = Income.objects.filter(user_id=request.user.id)
        serializer = IncomeSerializer(incomes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = IncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE', 'PATCH'])
@permission_classes([IsAuthenticated])
def edit_income(request,pk):
    income = get_object_or_404(Income,pk=pk)
    if request.method == 'PUT':
        serializer = IncomeSerializer(income, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = IncomeSerializer(income, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        income.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)