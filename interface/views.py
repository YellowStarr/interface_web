from django.shortcuts import render
from interface import models
from django.shortcuts import redirect
# Create your views here.

def index(request):

    if request.method == 'POST':
        baseurl = request.POST.get("baseurl")
        name = request.POST.get("name")
        url = request.POST.get("url")
        method = request.POST.get("method")
        args = request.POST.get("args")
        models.interface.objects.create(base_url=baseurl,name=name,url=url,method=method,args=args)
    interface_set = models.interface.objects.all()
    return render(request,"index.html", {"if_list":interface_set})


def add_interface(request):
    """
    添加接口
    :param request:
    :return:
    """

    return render(request,"/interface/add")