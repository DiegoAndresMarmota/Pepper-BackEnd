from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer
from .models import Blog, Comment
from users.models import User


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getBlogs(request):
    blog = Blog.objects.filter().order_by('-date')
    serializer = BlogSerializer(blog, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSoloBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)
