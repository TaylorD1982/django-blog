{"filter":false,"title":"urls.py","tooltip":"/posts/urls.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":8,"column":1},"action":"insert","lines":["from django.conf.urls import url","from .views import get_posts, post_detail, create_or_edit_post","","urlpatterns = [","    url(r'^$', get_posts, name='get_posts'),","    url(r'^(?P<pk>\\d+)/$', post_detail, name='post_detail'),","    url(r'^new/$', create_or_edit_post, name='new_post'),","    url(r'^(?P<pk>\\d+)/edit/$', create_or_edit_post, name='edit_post')","]"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":8,"column":1},"end":{"row":8,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1584615835546,"hash":"9f223081bea76c47b5aac1acd5000eedddfacf98"}