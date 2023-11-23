from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #path("admin/", admin.site.urls),
    path("",views.home,name='home'),
    path("signup",views.signup,name='signup'),
    path("login",views.user_login,name='user_login'),
    path("logout",views.user_logout,name='user_logout'),
    path("tasks",views.tasks,name='tasks'),
    path("addtask",views.addtask,name='addtask'),
    path('delete',views.delete,name='delete'),
    path('update',views.update,name='update'),

]
