from django.urls import path
from .views import HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,CategoryListView,LikeView

urlpatterns= [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('addpost/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name='update-post'),
    path('article/<int:pk>/remove',DeletePostView.as_view(),name='delete-post'),
    path('addcategory/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/',CategoryView,name='category'),
    path('category-list/',CategoryListView,name='category-list'),
    path('like/<int:pk>',LikeView,name='like_post'),
]