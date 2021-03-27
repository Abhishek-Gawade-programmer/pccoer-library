from django.shortcuts import render


def home(request):
    return render(request,'index.html')


def about(request):
    context={
        # 'items':Item.objects.all()
    }
    return render(request,'about.html')


def event(request):
    return render(request,'event.html')

def rules_regulation(request):
    return render(request,'rules.html')


def services(request):
    return render(request,'services.html')

def collection(request):
    return render(request,'collection.html')

def ebooks_list(request):
    return render(request,'ebooks_list.html')

def question_paper(request):
    return render(request,'question_papers.html')

def hod_desk(request):
    return render(request,'hod_desk.html')






