from django.conf.urls.defaults import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    'blog.views',

    #Admin overrides
    url(r'^blogpost/add/$', 'blogpost_changeform'),
    url(r'^blogpost/(?P<id>.*?)/$', 'blogpost_changeform'),
    url(r'^blogpost/$', 'blogpost_changelist'),

    url(r'^comment/(?P<reference_type>.*?)/(?P<reference_to>.*?)/create/$', 'comment_edit', name='comment_create'),
    url(r'^post/action/create/$', 'blog_edit', name='blogpost_create'),
    url(r'^post/(?P<parent>.*?)/(?P<pk>.*?)/edit/$', 'blog_edit', name='blogpost_edit'),
    url(r'^post/(?P<parent>.*?)/(?P<pk>.*?)/delete/$', 'blog_delete', name='blogpost_delete'),
    url(r'^post/(?P<parent>.*?)/(?P<pk>.*?)/$', 'blog_detail', name='blogpost_detail'),
    url(r'^post/(?P<slug>.*?)/$', 'blog_detail_slug', name='blogpost_detail_by_slug'),
    url(r'^posts/$', 'blog_list', name='blogpost_list'),
    url(r'^$', 'blog_list'),
)


