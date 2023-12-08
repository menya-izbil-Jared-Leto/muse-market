from django.urls import path
from . import views

app_name = 'market_app'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
        name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
        name='product_detail'),
]