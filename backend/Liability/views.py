from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Liability
from .serializers import LiabilitySerializer
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def liabilityinfo(request):
    print(
    'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'GET':
        liabilities = Liability.objects.filter(user_id=request.user.id)
        serializer = LiabilitySerializer(liabilities, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LiabilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

@api_view(['PUT', 'DELETE', 'PATCH'])
@permission_classes([IsAuthenticated])
def edit_liabilities(request,pk):
    liability = get_object_or_404(Liability,pk=pk)
    if request.method == 'PUT':
        serializer = LiabilitySerializer(liability, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = LiabilitySerializer(liability, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        liability.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)