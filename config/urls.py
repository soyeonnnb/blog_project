from django.contrib import admin
from django.urls import path
from blogapp import views as blogapp_views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", blogapp_views.home, name="home"),
    # HTML FORM 을 이용해 블로그 객체 만들기
    path("new/", blogapp_views.new, name="new"),
    path("create/", blogapp_views.create, name="create"),
    # Django FORM 을 이용해 블로그 객체 만들기
    path("djangonew/", blogapp_views.djangonew, name="djangonew"),
    # Django modelFORM 을 이용해 블로그 객체 만들기
    path("djangomodel/", blogapp_views.djangomodel, name="djangomodel"),
    path("detail/<int:blog_id>", blogapp_views.detail, name="detail"),
    # media 파일에 접근할 수 있는 url도 추가
    path(
        "create_comment/<int:blog_id>",
        blogapp_views.create_comment,
        name="create_comment",
    ),
    path("login/", accounts_views.login, name="login"),
    path("logout/", accounts_views.logout, name="logout"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
