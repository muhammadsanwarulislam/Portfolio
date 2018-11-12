from django.urls import path
from article.views import ArticleListView
from.import views

urlpatterns = [
    # path('', views.article_list,name = 'article-list'),
    path('', ArticleListView.as_view(),name = 'article-list'),
    path('detail/<int:pk>/', views.article_detail,name = 'article-detail'),
    path('create/', views.article_create,name = 'article-create'),
    path('update/<int:pk>/', views.article_update,name = 'article-update'),
    path('delete/<int:pk>/', views.article_delete,name = 'article-delete'),
]