from django.shortcuts import render ,redirect,HttpResponse
from  gamelives import models
from  gamelives.MyFrom import FM,register
from gamelives.yzm.check_code import create_validate_code
from django.utils.safestring import mark_safe
from io import BytesIO
def yzm(request,timerandom):
    stream=BytesIO()
    img,str=create_validate_code(font_type='static/Monaco.ttf')
    img.save(stream,'PNG')
    request.session['yzm']=str
    return HttpResponse(stream.getvalue())

def login(request,type):
    if request.method=='GET':
        obj=FM()
        obj2=register()
        return render(request,'login.html',{'obj':obj,'obj2':obj2})
    elif request.method=="POST":
            obj=FM(request.POST)
            obj2=register(request.POST)
            if type=="1" or not type:
                sign = obj.is_valid()
                if sign:
                    data=obj.cleaned_data
                    if request.session['yzm'].upper()!=data['yzm'].upper():
                        return render(request,'login.html',{'obj':obj,'obj2':obj2,'check_code':'验证码错误'})
                    if models.userinfo.objects.filter(user=data['user'],pwd=data['pwd']).count():
                        request.session['name']=data['user']
                        request.session['is_login']=True
                        request.session.set_expiry(0)
                        if request.POST.getlist('overtime'):
                            request.session.set_expiry(3*24*60*60)
                        return redirect('/home/')
                    return render(request,'login.html',{'obj':obj,'obj2':obj2,'msg':'用户名或密码错误'})
                else:
                    return render(request,'login.html',{'obj':obj,'obj2':obj2})
            elif type=='2':
                print(type)
                sign2 = obj2.is_valid()
                if sign2:
                    data2=obj2.cleaned_data
                    if request.META.get('HTTP_X_FORWARDED_FOR'):
                        ip = request.META.get('HTTP_X_FORWARDED_FOR')
                    else:
                        ip = request.META.get('REMOTE_ADDR')
                    data2['createip']=ip
                    models.userinfo.objects.create(**data2)
                    registerMsg='alert("注册成功,请登陆")'
                    registerMsg=mark_safe(registerMsg)
                    return render(request, 'login.html', {'obj': obj, 'obj2': obj2,'registerMsg':registerMsg})
                else:
                    jsStr="""
                    $("#lgin").removeClass('active')
                    $("#home").removeClass('active')
                    $("#reg").addClass('active')
                    $("#profile").addClass('active')
                    """
                    registerMsg=mark_safe(jsStr)
                    return render(request, 'login.html', {'obj': obj, 'obj2': obj2,'registerMsg':registerMsg})
    return redirect('/')
def logout(request):
    request.session.clear()
    return redirect('/')


def home(request):
    if not models.userinfo.objects.filter(user=request.session.get('name')).count():
        request.session.clear()
    if request.session.get('is_login'):
        return render(request,'home.html',{'name':request.session['name']})
    return redirect('/login/')
def news(request):
    imgcontect=models.news.objects.filter(newstype=1)
    link=models.news.objects.filter(newstype=2)
    return render(request,'news.html',{'imgcontect':imgcontect,'link1':link[0:9],'link2':link[9:]})
def sina(request):
    contect=models.sina.objects.all()
    return render(request,'sina.html',{'contect':contect})
def acfun(request):
    imgcontent=models.acf.objects.filter(id__range=[1,10])
    rankcontent=models.acf.objects.filter(id__gte=11)
    return render(request,'acfun.html',locals())

def lives(request):
    content=models.lives.objects.all()
    return render(request,'lives.html',locals())