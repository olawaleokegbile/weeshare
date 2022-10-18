from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_post', views.new_post, name='new-post'),
    path('my_profile', views.profile_form, name='my-profile'),
    path('my_profile/edit', views.edit_profile, name='edit-profile'),
    path('user_profile/<str:username>', views.user_profile, name='user-profile'),
    path('my_post', views.my_post, name='my-post'),
    path('post_detail/<str:pk>', views.post_detail, name='post-detail'),
    path('post_detail/<str:pk>/delete', views.delete_post, name='post-delete'),
    path('post_detail/<str:pk>/update', views.update_post, name='post-update'),
    path('comment/<int:post_id>', views.add_comment, name='add-comment'),
]
