from logging import exception
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import BlogPost
from .serializers import BlogPostSerializer, CommentSerializer

class CreateBlogPostAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            serializer = BlogPostSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "message": "Blog has been created.", "data": serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status": "error", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"status": "error", "message": "Oops! Something went wrong."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def get(self, request):
        try:
            blogs = BlogPost.objects.all().order_by('-created_at')
            if not blogs:
                return Response(
                    {"status": "error", "message": "No records found."},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = BlogPostSerializer(blogs, many=True)
            return Response(
                {"status": "success", "message": "All blogs.", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"status": "error", "message": "Oops! Something went wrong."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class MineBlogPostAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    '''
    To get only user specific blogs
    '''
    def get(self, request):
        try:
            blogs = BlogPost.objects.filter(author=request.user).all().order_by('-created_at')
            if not blogs:
                return Response(
                    {"status": "error", "message": "No records found."},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = BlogPostSerializer(blogs, many=True)
            return Response(
                {"status": "success", "message": "All blogs.", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"status": "error", "message": "Oops! Something went wrong."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )



class CreateCommentAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, blog_id):
        try:
            data = request.data
            data['post'] = blog_id
            data['author'] = request.user.pk
            serializer = CommentSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "message": "Comment added successfully.", "data": serializer.data},
                    status=status.HTTP_201_CREATED)
            # addition of two numbers

            return Response(
                {"status": "error", "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response({"status": "error", "message": "Oops! Something went wrong."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

