from django.shortcuts import render
# from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets
from rest_framework.decorators import api_view, APIView, permission_classes
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import ReadOnly, AuthorOrReadOnly
from rest_framework.pagination import PageNumberPagination
# Create your views here.

# for custom pagination
class CustomPaginator(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    page_size_query_param = "page_size"
    

# def homepage(request: HttpRequest):
#     response = {"message": "Hello, world!"}
#     return JsonResponse(data=response)

# posts=[
#     {
#         "title": "First Post",
#         "content": "This is the first post content.",
#         "author": "John Doe"
#     },
#     {
#       "title": "Second Post",
#       "content": "This is the second post content.",
#       "author": "Jane Smith"
#     },
#     {
#         "title": "Third Post",
#         "content": "This is the third post content.",
#         "author": "Michael Johnson"
#     },
#     {
#         "title": "Fourth Post",
#         "content": "This is the fourth post content.",
#         "author": "Emily Davis"
#     }
# ]

# for function based views (api_view)
@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def homepage(request: Request):
    
    if request.method == "POST":
        # Process POST request
        data = request.data
        response = {"message": "Hello, world!", "data": data}
        return Response(data=response, status=status.HTTP_201_CREATED)
    
    response = {"message": "Hello, world!"}
    return Response(data=response, status=status.HTTP_200_OK)

# for filtering
class ListPostsForAuthor(
    generics.GenericAPIView,
    mixins.ListModelMixin
):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPaginator
    
    def get_queryset(self):
        username = self.request.query_params.get('username') or None
        
        queryset = Post.objects.all()
        
        if username is not None:
            return Post.objects.filter(author__username=username)
        
        return queryset
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        
    

# @api_view(http_method_names=["GET", "POST"])
# def list_posts(request: Request):
#     posts = Post.objects.all()
    
#     if request.method == "POST":
#         data = request.data
#         serializer = PostSerializer(data=data)
        
#         if serializer.is_valid():
#             serializer.save()
            
#             response={
#                 "message": "Post created successfully",
#                 "data": serializer.data,
#                 "status": "created"
#             }
#             return Response(data=response, status=status.HTTP_201_CREATED)
        
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     serializer = PostSerializer(instance=posts, many=True)
    
#     response = {"message": "posts", "data":serializer.data}
    
#     return Response(data=response, status=status.HTTP_200_OK)



# @api_view(http_method_names=["GET"])
# def post_detail(request: Request, post_id: int):
#     post = get_object_or_404(Post, pk=post_id)
    
#     serializer = PostSerializer(instance=post)
#     response={
#         "message": "post",
#         "data": serializer.data,
#         "status": "ok"
#     }
    
#     return Response(data=response, status=status.HTTP_200_OK)

# @api_view(http_method_names=["GET"])
# def get_post_by_id(request: Request, post_id: int):
#     pass

# @api_view(http_method_names=["PUT"])
# def update_post(request: Request, post_id: int):
#     post = get_object_or_404(Post, pk=post_id)
    
#     data = request.data
    
#     serializer = PostSerializer(instance=post, data=data, partial=True)
    
#     if serializer.is_valid():
#         serializer.save()
        
#         response={
#             "message": "Post updated successfully",
#             "data": serializer.data,
#             "status": "updated" 
#         }
#         return Response(data=response, status=status.HTTP_200_OK)
    
#     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(http_method_names=["DELETE"])
# def delete_post(request: Request, post_id: int):
#     post = get_object_or_404(Post, pk=post_id)
    
#     post.delete()
    
#     response={
#         "message": "Post deleted successfully",
#         "status": "deleted"
#     }
    
#     return Response(data=response, status=status.HTTP_200_OK)
   

# # for class based views (APIView)
# class PostListCreateView(APIView):
#     serializer_class= PostSerializer
    
#     def get(self, request: Request, *args, **kwargs):
#         posts = Post.objects.all()
#         serializer = self.serializer_class(instance=posts, many=True)
        
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request: Request, *args, **kwargs):
#         data = request.data
        
#         serializer=self.serializer_class(data=data)
        
#         if serializer.is_valid():
#             serializer.save()
            
#             response={
#                 "message": "Post created successfully",
#                 "data": serializer.data,
#                 "status": "created"
#             }
#             return Response(data=response, status=status.HTTP_201_CREATED)
        
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PostRetrieveUpdateDeleteView(APIView):
#     serializer_class= PostSerializer
    
#     def get(self, request: Request, post_id: int):
#         post = get_object_or_404(Post, pk=post_id)
#         serializer = self.serializer_class(instance=post)
        
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    
    
#     def put(self, request: Request, post_id: int, *args, **kwargs):
#         post = get_object_or_404(Post, pk=post_id)
        
#         data = request.data
        
#         serializer = self.serializer_class(instance=post, data=data)
        
#         if serializer.is_valid():
#             serializer.save()
            
#             response={
#                 "message": "Post updated successfully",
#                 "data": serializer.data,
#                 "status": "updated" 
#             }
#             return Response(data=response, status=status.HTTP_200_OK)
        
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request: Request, post_id: int, *args, **kwargs):
#         post = get_object_or_404(Post, pk=post_id)
        
#         post.delete()
        
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# using the generics api_view method and modelmixins

class PostListCreateView(generics.GenericAPIView,
                         mixins.CreateModelMixin,
                         mixins.ListModelMixin): 
    
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
        return super().perform_create(serializer)
    
    def get(self, request:Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class PostRetrieveUpdateDeleteView(generics.GenericAPIView,
                                   mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin):
    
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AuthorOrReadOnly] 
    
    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
            

# using the viewset class
# import the module from rest_framework impor viewset

# class PostViewSet(viewsets.ViewSet):
    
#     def list(self, request: Request):
#         queryset = Post.objects.all()
#         serializer = PostSerializer(instance=queryset, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
    
#     def retrieve(self, request: Request, pk=None):
#         post = get_object_or_404(Post, pk=pk)
        
#         serializer = PostSerializer(instance=post)
        
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

# using the modelviewset
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    