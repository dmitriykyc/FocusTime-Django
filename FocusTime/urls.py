
from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp
from django.conf.urls import include
from filebrowser.sites import site
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
    path('', mainapp.main, name='index'),
    path('auth/', include("authapp.urls", namespace='auth')),
    path('tasks/', include("tasksapp.urls", namespace='tasks')),
    path('socnetw/', include("socnetwapp.urls", namespace='socnetw')),
    path('blog/', include("blogapp.urls", namespace='blog')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
