from django.shortcuts import render, get_object_or_404
from myblog.models import Post


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request,
                  'myblog/list.html',
                  context)


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    post = get_object_or_404(published, pk=post_id)
    context = {'post': post}
    return render(request,
                  'myblog/detail.html',
                  context)
