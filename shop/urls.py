# from django.conf.urls import url #old version

from django.urls import path
from . import views
from django.urls import path, include  # 確保包含 include

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('login/', views.User_login),
    path('personal/', views.personal),
    path('logout/', views.User_logout),
    path('reset', views.reset_password),
    # path('car/', views.view_cart, name='view_cart'),  # 添加這行
    path('car/', views.car, name='car'),  # 將'car'路徑連接到'car'視圖

    path('detail/<int:product_id>/', views.product_detail, name='product_detail'),  # 修改成這樣
    path('accounts/', include('allauth.urls')),  # FB,Google帳號登入, 更新此行
    


]

