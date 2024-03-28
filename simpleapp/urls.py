from django.urls import path
# Импортируем созданное нами представление
from .views import ProductsList, ProductDetail,PostList,PostDetail,ProductCreate, ProductUpdate, ProductDelete, NewsCreate,NewsUpdate,NewsDelete #,create_product

urlpatterns = [
    path('', ProductsList.as_view(), name='product_list'),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('News_all', PostList.as_view(), name='news_list'),
    path('News_all/<int:id>', PostDetail.as_view(), name= 'news_or_art_detail'),
    # path('create/',create_product, name = 'product_create'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    path('create_news/', NewsCreate.as_view(), name= 'create_news'),
    path('art/create_news/', NewsCreate.as_view(), name= 'create_art'),
    path('news_or_art/update/<int:pk>/', NewsUpdate.as_view(), name='news_update'),
    path('news_or_art/delete/<int:pk>/', NewsDelete.as_view(), name='news_delete')


]