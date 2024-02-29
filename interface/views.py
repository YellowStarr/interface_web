from django.shortcuts import render
from interface import models
from django.shortcuts import redirect
from interface.myForm import InterfaceModelForm,CaseModelForm
import requests
import json
# Create your views here.

def headers(header_str):
        header = {}
        if isinstance(header_str, dict):
            return header
        for line in header_str.splitlines():
            elem = line.split(":", 1)
            if len(elem) == 2:
                header[str(elem[0]).strip()] = str(elem[1]).strip()
        return header

def index(request):
    if request.method == 'POST':
        baseurl = request.POST.get("baseurl")
        name = request.POST.get("name")
        header_str = request.POST.get("header")
        print(header_str)
        if header_str:
            header = headers(header_str)
        else:
            header = ''
        url = request.POST.get("api")
        method = request.POST.get("method")
        args = request.POST.get("args")

        models.interface.objects.create(base_url=baseurl,name=name,header=header,url=url,method=method,args=args)
    interface_set = models.interface.objects.all()
    return render(request,"index.html", {"if_list":interface_set})

def case(request):
    """
    用例展示
    :param request:
    :return:
    """
    # 通过外键关联，能获取interface的对象，在templates中可以访问对象
    caseset = models.Case.objects.select_related("interf")
    return render(request,"case_list.html", {"case_list":caseset})

def add_case(request):
    """
    添加用例，应该带入baseurl等信息.add和edit合并
    :param request:
    :return:
    """
    #post是发送保存请求
    if request.method == 'GET':
        cid = request.GET.get("if_id")
        interfaceset = models.interface.objects.get(id=cid)
        interfaceform = InterfaceModelForm(instance=interfaceset)

        caseform = CaseModelForm(initial={'interf': cid})
        return render(request,"case_add.html", {'interface_form': interfaceform, "case_form": caseform})

    if request.method == "POST":
        print("-------------",request.POST.get("interf"))
        caseform = CaseModelForm(request.POST)
        #     提交数据合法性校验
        if caseform.is_valid():
            data = caseform.cleaned_data
            print("======interf=========")
            # 处理验证点保存的数据。
            try:
                json.loads(data['assertion'])
            except ValueError as e:
                print(e)
            if data['args_json'] == '{}' or data['args_json'] == '':
                data['args_json'] = ""
                #     modelform才能使用save（）且会新增。想要修改，要在实例化时传入一个instance=xxobj
            caseform.save()
            return redirect("/case_list/")
        else:
            print("校验未通过",caseform.errors)

def delete_case(request):
    if_id = request.GET.get("c_id")
    models.Case.objects.filter(id=if_id).delete()
    return redirect("/case_list/")

def edit_case(request, c_id):
    """
    编辑用例，带回数据
    :param request:
    :return:
    """
    if request.method == 'GET':
        id = c_id    # 获取用例id
        caseset = models.Case.objects.filter(id=id).first()
        caseform = CaseModelForm(instance=caseset)
        # 通过用例id查到接口id
        interfaceset = models.interface.objects.get(id=caseset.interf_id)
        interfaceform = InterfaceModelForm(instance=interfaceset)
        return render(request,"case_edit.html", {'interface_form': interfaceform, "case_form": caseform})
    elif request.method == 'POST':
        print(c_id)
        caseset = models.Case.objects.filter(id=c_id).first()
        caseform = CaseModelForm(data=request.POST, instance=caseset)
        # interform = InterfaceModelForm(request.POST)
        #     提交数据合法性校验
        if caseform.is_valid():
            data = caseform.cleaned_data
            print("======interf=========")
            # 处理验证点保存的数据。
            try:
                json.loads(data['assertion'])
            except ValueError as e:
                print(e)
            if data['args_json'] == '{}' or data['args_json'] == '':
                data['args_json'] = ""
            caseform.save()
            return redirect("/case_list/")
        else:
            print("校验未通过",caseform.errors)
def execute_case(request):
    """
    执行按钮
    :param request:
    :return:
    """
    id = request.GET.get("c_id")
    case_set = models.Case.objects.filter(id=id).first()
    if case_set.args_json == None:
        case_set.args_json = {}
    interface_set = models.interface.objects.filter(id=case_set.interf.id).first()
    print(interface_set.base_url)
    if interface_set.header != '':
        header_str = interface_set.header.replace("'", "\"")
        header = json.loads(header_str)
    else:
        header = {}
    if interface_set.get_method_display() == "get":
        res = requests.get(interface_set.base_url+interface_set.url, params= case_set.args_json, headers=header)
        response = res.json()
        # print(response)
        case_set.response = response
        # 要增加容错处理
        try:
            assert_dic = json.loads(case_set.assertion)
            print(type(assert_dic))
        except Exception as e:
            print(e)
        isPass = False
        for k,v in assert_dic.items():
            if response[k] == v:
                isPass &= True
            else:
                isPass = False
        case_set.result = str(isPass)
        case_set.save()
    return redirect("/case_list/")

# 对于response的解包和校验，还要分情况处理
# 比如响应是list， str， 等等情况
# 系统还缺少关联接口，关键字提取，菜单，分接口展示case，批量导入，批量删除，批量执行，执行测试suit等功能