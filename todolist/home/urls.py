from django.contrib import admin
from django.urls import path
from home import views
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('tasks',views.tasks,name='tasks'),

]