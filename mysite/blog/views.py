from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request: HttpRequest) -> HttpResponse:
    posts = Post.published.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post/list.html', context=context)


def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    posts = get_object_or_404(Post,
                              id=id,
                              status=Post.Status.PUBLISHED)

    return render(request,
                  'blog/post/detail.html',
                  {"posts": posts}
                  )
