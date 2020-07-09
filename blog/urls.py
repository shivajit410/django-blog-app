from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.ArticlesList.as_view(), name='article'),
    path('about/', views.about, name='about'),
    # path('articles/', views.ArticlesList.as_view(), name='article'),
    path('create/', views.article_create, name='create'),
    path('<str:slug>/detail/', views.ArticleDetail.as_view(), name='detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
