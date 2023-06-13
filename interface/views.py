from django.shortcuts import render
from interface import models
from django.shortcuts import redirect
from interface import myForm
from django import forms
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

class CaseModelForm(forms.ModelForm):
    class Meta:
        model = models.Case
        fields = ["case_name","base_url", "url", "method", "args_json"]

def case(request):
    """
    用例展示
    :param request:
    :return:
    """
    queryset = models.Case.objects.all()

    return render(request,"case_list.html", {"case_list":queryset, "showBlock": "case_list"})

def add_case(request):
    caseform = myForm.CaseForm(data=request.POST)

    # if request.method == 'POST':
    #     base_url = request.POST.get("BaseURL")
    #     case_name = request.POST.get("case_name")
    #     url = request.POST.get("url")
    #     method = request.POST.get("method")
    #     args_json = request.POST.get("args_json")


    if caseform.is_valid():
        data = caseform.cleaned_data
        # models.Case.objects.create(base_url=base_url,case_name=case_name,url=url,method=method,args_json=args_json)
        models.Case.objects.create(**data)
        return redirect("/case_list/")

    return render(request,"case_add.html", {"case_form":caseform})

def delete_case(request):
    if_id = request.GET.get("if_id")
    models.interface.objects.filter(id=if_id).delete()
    print(if_id)
    return redirect("/case_list/")

def edit_case(request):
    form  = CaseModelForm()
    id = request.GET.get("if_id")
    case_set = models.Case.objects.filter(id=id).first()
    return render(request,"case_add.html", {"case_form":case_set})

