from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from nh48_user.views import index, member
from authentication.views import signup_view, login_view, logout_view

urlpatterns = [
    path('', index, name='homepage'),
    path('login/', login_view),
    path('logout/', logout_view),
    path('signup/', signup_view),
    path('admin/', admin.site.urls),
    path('<str:username>/', member, name="member"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
