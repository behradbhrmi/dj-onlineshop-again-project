from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404

from .models import Products, Comments
from .forms import CommentForm


class ProductsListView(ListView):
    queryset = Products.objects.filter(availability=True)
    context_object_name = 'products'
    template_name = 'products/products_list.html'


class ProductDetailView(DetailView):
    model = Products
    context_object_name = 'product'
    template_name = 'products/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(CreateView):
    model = Comments
    form_class = CommentForm
    template_name = ProductDetailView.template_name

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        pk = int(self.kwargs['pk'])
        product = get_object_or_404(Products, id=pk)
        obj.product = product
        return super().form_valid(form)
