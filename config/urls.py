from django.contrib import admin
from django.urls import path
from blogapp import views as blogapp_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", blogapp_views.home, name="home"),
    # HTML FORM 을 이용해 블로그 객체 만들기
    path("new/", blogapp_views.new, name="new"),
    path("create/", blogapp_views.create, name="create"),
    # Django FORM 을 이용해 블로그 객체 만들기
    path("djangonew/", blogapp_views.djangonew, name="djangonew"),
]
