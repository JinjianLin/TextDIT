from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


#
#from .TestData import TestData
from lab.mongo_db import *


def index(request, keyword='rivaroxaban', page=1):
    if request.method == 'POST':
        keyword = request.POST.get('keyword', 'rivaroxaban')
        page = request.POST.get('page', 1)
    #test_data_set = TestData()

    # real
    data = query_gene(keyword)
    if not data:
         data = query_compound(keyword)
    # -----------------------
    print(data)
    # Test
    #data = test_data_set.get_test_data(keyword)
    # -----------------------
    data = sorted(data, key=lambda x: x['avg_score'], reverse=True)
    paginator = Paginator(data,10)
    if int(page) < 1:
        page = 1
    elif int(page) > paginator.num_pages:
        page = paginator.num_pages
    context = {
        'data': paginator.get_page(page),
        'keyword': keyword,
        'num_pages': paginator.num_pages,
        'page': page,
    }
    return render(request, 'lab/semanticwb.html', context=context)



def search(request, keyword):
    pass