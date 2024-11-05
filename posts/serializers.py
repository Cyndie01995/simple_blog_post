from rest_framework import serializers
from .models import Post

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)  # Add this line to include the post ID in the serialized response.
#     title = serializers.CharField(max_length=50)
#     content = serializers.CharField()
#     created = serializers.DateTimeField(read_only=True)

class PostSerializer(serializers.ModelSerializer):
    # for custom validation
    title = serializers.CharField(max_length=50)
    class Meta:
        model = Post  # Use the Post model from the posts app.
        # fields = "__all__"  # Include all fields from the model in the serialized response.
        fields = ["id", "title", "content", "created"]

       
