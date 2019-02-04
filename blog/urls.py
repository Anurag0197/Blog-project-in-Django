from django.conf.urls import url
from blog import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "blog"

urlpatterns = [

    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^post/new/$',views.CreatePostView.as_view(),name='post_new'),
    url(r'^post/(?P<pk>[-\w]+)/$',views.PostDetailView.as_view(),name='post_detail'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^post/(?P<pk>[-\w]+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),
    url(r'^post/(?P<pk>[-\w]+)/remove/$',views.PostDeleteView.as_view(),name='post_remove'),
    url(r'^drafts/$',views.PostDraftView.as_view(),name='post_draft_list'),
    url(r'^post/(?P<pk>[-\w]+)/comment/$',views.add_comment_to_post,name = 'add_comment_to_post'),
    url(r'^post/(?P<pk>[-\w]+)/publish/$',views.post_publish,name = 'post_publish'),
    url(r'^post/(?P<pk>[-\w]+)/like/$',views.add_like_to_post,name = 'like'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
