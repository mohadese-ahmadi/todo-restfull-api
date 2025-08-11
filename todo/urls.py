from django.urls import path
from . import views
urlpatterns=[
    path('',views.TodoSerialzerView, name='TodoSerialized'),
    path('<int:id>', views.TodoSerializerDetail, name='TodoDetail'),
    path('api-view/', views.TodoApiView.as_view(), name='api-view'),
    path('api-view/<int:todo_id>', views.TodoDetailApiView.as_view(), name='api-detail-view'),
    path('mixin-view/', views.MixinViewApi.as_view(), name='mixin-view'),
    path('mixin-view/<int:pk>', views.MixinDetailViewApi.as_view(), name='mixin-view'),
]