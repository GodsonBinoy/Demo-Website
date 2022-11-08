
from django.urls import path
from . import views
app_name='webapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('book/<int:bookid>/',views.detail,name='detail'),
    path('add/',views.add_book,name='add_book'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),

]
