from django.db.models import Q
from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, TemplateView, DetailView
from .models import Product



class IndexView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		return context

class ProductList(ListView):
	template_name = "products/products_list.html"

	def get_queryset(self):
		return Product.objects.all()

class ProductDetailView(DetailView):
	template_name = "products/detail.html"
	#queryset = Product.objects.all()

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		return context

	def get_object(self, *args, **kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		instance = Product.objects.get_by_id(pk)
		if instance is None:
			raise Http404("Product Not Forund!")
		return instance


	# another way to show data in detailview by id in a get_queryset method
	# def get_queryset(self, *args, **kwargs):
	# 	request = self.request
	# 	pk = self.kwargs.get('pk')
	# 	return Product.objects.filter(pk=pk)

class ProductSlugtDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_object(self, *args, **kwargs):
		request = self.request
		slug = self.kwargs.get('slug')
		try:
			instance = Product.objects.get(slug=slug)
		except Product.DoesNotExist:
			raise Http404('Not Forund')
		except Product.MultipleObjectsReturned:
			qs =Product.objects.filter(slug=slug)
			instance = qs.first()
		except:
			raise Http404('Ummmmh!')
		return instance
		


class FeaturedProductList(ListView):
	template_name = "products/products_list.html"

	def get_queryset(self):
		return Product.objects.all().featured()

class FeaturedProductDetailView(DetailView):
	template_name = "products/featured_detail.html"
	#also can show the detail featured view just giving the queryset=Product.objects.featured() line.
	queryset = Product.objects.all().featured()

	#also can show the featured detail view to write the below code...
	# def get_queryset(self, *args, **kwargs):
	# 	request = self.request
	# 	return Product.objects.featured()


	############################ Searching Products #####################

class SearchProductsList(ListView):
	template_name = "products/search_products.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['query'] = self.request.GET.get('q')
		return context


	def get_queryset(self):
		request = self.request
		print(request.GET) #printing the get parameter
		query = request.GET.get('q') #search product by q get parameter.
		print(query) # printing the get parameter which searched by request method.
		#Searching for just only title wise.....
		# if query is not None:
		# 	return Product.objects.filter(title__icontains=query) #Filtering the product by query variable.
		# return Product.objects.none()

		#Here Q is a django query object for making query simple and by this Q can do operations like and, or etc...
		# if query is not None:
		# 	lookups = Q(title__icontains=query) | Q(description__icontains=query)
		# 	return Product.objects.filter(lookups).distinct()
		# return Product.objects.none()

		#Searched by making model manager in the product model
		if query is not None:
			return Product.objects.search(query)
		return Product.objects.none()


