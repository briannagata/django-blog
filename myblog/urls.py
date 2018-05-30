from django.conf.urls import url
import myblog.views


urlpatterns = [
    url(r'^$', myblog.views.list_view, name='blog_index'),
    url(r'^posts/(?P<post_id>\d+)/$', myblog.views.detail_view, name="blog_detail"),
]
