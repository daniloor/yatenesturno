from django.shortcuts import render, HttpResponse

from yatenesturnoapp.models import Client

# Create your views here.

def unique(list1):
    # intilize a null list
    unique_list = []
     
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # return list
    return unique_list

def home(request): 

    return render(request,'yatenesturnoapp/home.html')

def categories(request): 
    
    return render(request,"yatenesturnoapp/categories.html")

def categorytype(request,categoryName):
    filterData = Client.objects.filter(category=categoryName)
    if (request.GET):
        filterType = request.GET["type"]
    else:
        filterType = ''
    if (filterData):
        typeList = []
        for element in filterData:
            typeList.append(element.type)
        uniqueList = unique(typeList)
        return render(request,"yatenesturnoapp/index.html",{"clients":filterData,"typeList":uniqueList,"filterType":filterType})
    else:
        return HttpResponse('No hay data pa')

def contact(request):

    return render(request,"yatenesturnoapp/contact.html")

def steps(request):

    return render(request,"yatenesturnoapp/steps.html")