from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('',views.TodoViewSet)
urlpatterns=[
    path('',views.TodoSerialzerView, name='TodoSerialized'),
    path('<int:id>', views.TodoSerializerDetail, name='TodoDetail'),
    path('api-view/', views.TodoApiView.as_view(), name='api-view'),
    path('api-view/<int:todo_id>', views.TodoDetailApiView.as_view(), name='api-detail-view'),
    path('mixin-view/', views.MixinViewApi.as_view(), name='mixin-view'),
    path('mixin-view/<int:pk>', views.MixinDetailViewApi.as_view(), name='mixin-detail-view'),
    path('generic-view/', views.GenericView.as_view(), name='generic-view'),
    path('generic-view/<int:pk>', views.GenericDetailView.as_view(), name='generic-detail-view'),
    path('view-set/', include(router.urls))
]