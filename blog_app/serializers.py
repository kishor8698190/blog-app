from rest_framework import serializers
from .models import BlogPost, Comment

class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id','post','author','author_name','content','created_at','updated_at']
        read_only_fields = ['created_at', 'updated_at']


class BlogPostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)  # Nested comments

    class Meta:
        model = BlogPost
        fields = ['id', 'author', 'title', 'content', 'image', 'created_at', "comments"]
        read_only_fields = ['id', 'created_at', 'author']


    # Optional: set author here instead of in the view
    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['author'] = request.user
        return super().create(validated_data)



