from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post

# @api_view()
# def hello_world(request):
#     return Response('Hello, world!')
from .serializers import PostSerializer


@api_view()
def posts_list(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True, context={'request', })
    serializer.is_valid(raise_exception=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
