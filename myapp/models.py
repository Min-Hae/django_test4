from django.db import models

# Create your models here.
# ORM 기법 사용 : SQL문 직접 기술하지 않음.

class Article(models.Model): # 테이블을 클래스로 정의
    # 칼럼은 속성(멤버변수)으로 부여
    code = models.CharField(max_length=10) # 최대 길이를 10자리로 할당.
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    pub_date = models.DateTimeField()
    
    