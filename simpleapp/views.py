from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Product, News_All
from datetime import datetime
from .filters import ProductFilter, NewsFilter
from .forms import ProductForm, NewsForm
from django.urls import reverse_lazy
# Create your views here.

class ProductsList(ListView):
    model = Product
    ordering = 'name'

    # queryset= Product.objects.filter(
    #     price__lt = 100
    # ).order_by(
    #     'name'
    # )
    paginate_by = 1
    template_name = 'flatpages/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context

class ProductDetail(DetailView):
    model = Product
    template_name = 'flatpages/product.html'
    context_object_name = 'product'

class PostList(ListView):
    model = News_All
    ordering = '-time_in'

    template_name = 'flatpages/News_all.html'
    context_object_name = 'news'

    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    model = News_All
    pk_url_kwarg = 'id'

    template_name = 'flatpages/News_all_post.html'
    context_object_name = "news"


# def create_product(request):
#     form = ProductForm()
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/products/')
#
#
#     return  render(request, 'flatpages/product_edit.html',{'form': form})


class ProductCreate(CreateView):
    form_class = ProductForm
    model = Product
    template_name = 'flatpages/product_edit.html'

class ProductUpdate(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'flatpages/product_edit.html'

class ProductDelete(DeleteView):
    model = Product
    template_name = 'flatpages/product_delete.html'
    success_url = reverse_lazy('product_list')


#Создание обновление и удаление новостей/статей

class NewsCreate(CreateView):
    form_class = NewsForm
    model = News_All
    template_name = 'flatpages/News_all_create_news.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/products/art/create_news/':
            post.news_or_art = 'Ст'
        post.save()
        return super().form_valid(form)

class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = News_All
    template_name = 'flatpages/News_all_create_news.html'

class NewsDelete(DeleteView):
    model = News_All
    template_name = 'flatpages/news_delete.html'
    success_url = reverse_lazy('news_list')