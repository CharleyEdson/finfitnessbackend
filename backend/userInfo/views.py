from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import userInfo
from .serializers import userInfoSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def userinformation(request):
    print(
    'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'GET':
        user_info = userInfo.objects.filter(user_id=request.user.id)
        serializer = userInfoSerializer(user_info, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = userInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE', 'PATCH'])
@permission_classes([IsAuthenticated])
def edit_user_info(request,pk):
    user = get_object_or_404(userInfo,pk=pk)
    if request.method == 'PUT':
        serializer = userInfoSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = userInfoSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)