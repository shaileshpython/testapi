from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def get_paginated_object(result, page, paginate_by):
	""" 
	getting the pagination objects
	"""
	paginator = Paginator(result, paginate_by)
	try:
		result = paginator.page(page)
	except PageNotAnInteger:
		result = paginator.page(1)
	except EmptyPage:
		result = paginator.page(paginator.num_pages)
	return result