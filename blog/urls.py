from . import views
from django.urls import path
from . views import DeleteComment

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'),
    path("delete/<slug:pk>/", DeleteComment.as_view(), name="delete_comment"),
]