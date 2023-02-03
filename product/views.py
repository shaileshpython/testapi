from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from .utility import get_paginated_object

# Create your views here.

class ProductView(APIView):
	"""
	To show products
	"""
	def get(self,request):
		"""
		to search product by product name
		"""
		queryset = Product.objects.all().values()
		product_name = request.GET.get("product_name","")
		if product_name:
			queryset = queryset.filter(Product=product_name).values()
		result = ProductSerializer(queryset, many=True).data	
		return JsonResponse({"result":result})
	
	def post(self,request):  
		queryset = Product.objects.all().values()
		product_name = request.POST.get("product_name","")
		page = int(request.POST.get('page', 1))
		paginate_by = int(request.POST.get('paginate_by', 5)) ###pagination concept used .
		queryset = get_paginated_object(queryset, page, paginate_by)
		result = ProductSerializer(queryset, many=True).data
		return Response({"status": "success","results":result},status=200)
	
	
