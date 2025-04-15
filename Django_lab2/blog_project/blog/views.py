from django.shortcuts import render
from django.views import generic
from .models import Post
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import PostSerializer

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'



# Для запросов API

@csrf_exempt
def PostAPI(request, q_title = "Empty"):
    if request.method == "GET":
        posts = Post.objects.all()
        posts_ser = PostSerializer(posts, many = True)
        return JsonResponse(posts_ser.data, safe= False)
    elif request.method == "POST":
        post_data = JSONParser().parse(request)
        post_ser = PostSerializer(data = post_data)
        if post_ser.is_valid():
            post_ser.save()
            return JsonResponse("Added successfully", safe = False)
        return JsonResponse("Failed to add " , safe= False)
    elif request.method == "PUT":
        post_data = JSONParser().parse(request)
        post = Post.objects.get(title=post_data['title'])
        post_ser = PostSerializer(post, data = post_data)
        if post_ser.is_valid():
            post_ser.save()
            return JsonResponse("Updated Successfully", safe= True)
        return JsonResponse("Failed to update", safe= False)
    elif request.method == "DELETE":
        post = Post.objects.get(title=q_title)
        post.delete()
        return JsonResponse("Deleted Successfully", safe= False)