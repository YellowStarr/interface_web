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


def case(request):
    """
    用例展示
    :param request:
    :return:
    """
    queryset = models.Case.objects.all()

    return render(request,"case_list.html", {"case_list":queryset})

def add_case(request):
    if request.method == 'POST':
        base_url = request.POST.get("BaseURL")
        case_name = request.POST.get("case_name")
        url = request.POST.get("url")
        method = request.POST.get("method")
        args_json = request.POST.get("args_json")
        models.Case.objects.create(base_url=base_url,case_name=case_name,url=url,method=method,args_json=args_json)
        return redirect("/case_list/")

    return render(request,"case_add.html")