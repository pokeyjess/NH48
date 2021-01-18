from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from nh48_user.views import index, member
from nh48_app.views import post_form_view, post_detail, delete_post
from authentication.views import signup_view, login_view, logout_view

urlpatterns = [
    path('', index, name='homepage'),
    path('login/', login_view),
    path('logout/', logout_view),
    path('signup/', signup_view),
    path('newpost/', post_form_view),
    path('post/<int:post_id>', post_detail, name='post'),
    path('post/<int:post_id>/delete/', delete_post, name='delete_post'),
    path('admin/', admin.site.urls),
    path('<str:username>/', member, name='profile'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
