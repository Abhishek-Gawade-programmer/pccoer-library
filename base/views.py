from django.shortcuts import render


def home(request):
    context={
        # 'items':Item.objects.all()
    }
    return render(request,'index.html',context)


def about(request):
    context={
        # 'items':Item.objects.all()
    }
    return render(request,'about.html',context)


def event(request):
    context={
        # 'items':Item.objects.all()
    }
    return render(request,'event.html',context)




