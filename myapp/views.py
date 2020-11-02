from django.shortcuts import render
from myapp.models import Article

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def DbShow(request):
    # ORM을 통한 QuerySet 얻기
    datas = Article.objects.all() # 내부적으로 select 문이 수행됨.
    print(datas)
    print(datas[0].name)
    
    return render(request, 'articlelist.html', {'articles': datas}) # QuerySet을 전달