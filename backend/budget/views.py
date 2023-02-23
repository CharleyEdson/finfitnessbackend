from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Budget
from .serializers import budgetSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def budget_info(request):
    print(
    'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'GET':
        budgets = Budget.objects.filter(user_id=request.user.id).order_by('-id')
        serializer = budgetSerializer(budgets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = budgetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_budget_info(request):
    if request.method == 'GET':
        budgets = Budget.objects.filter(user_id=request.user.id).order_by('-date')[:1]
        serializer = budgetSerializer(budgets, many=True)
        return Response(serializer.data)

@api_view(['PUT', 'DELETE', 'PATCH'])
@permission_classes([IsAuthenticated])
def edit_budget(request,pk):
    budget = get_object_or_404(Budget,pk=pk)
    if request.method == 'PUT':
        serializer = budgetSerializer(budget, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = budgetSerializer(budget, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        budget.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)