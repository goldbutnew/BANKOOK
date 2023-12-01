from django.db import models
from django.conf import settings

# 게시판 모델
class Article(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Comment(models.Model):
#     articles = models.ForeignKey(Article, on_delete=models.CASCADE)
#     content = models.CharField(max_length=250)
#     created_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.content
    
    
# 예금 모델
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)

    dcls_month = models.TextField()
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()

    join_deny = models.IntegerField()
    join_way =  models.TextField()
    spcl_cnd = models.TextField()

    join_member = models.TextField()
    etc_note = models.TextField()
    
    

class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE, related_name='option')
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()


# 적금 모델
class SavingProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)

    dcls_month = models.TextField()
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()

    join_deny = models.IntegerField()
    join_way =  models.TextField()
    spcl_cnd = models.TextField()

    join_member = models.TextField()
    etc_note = models.TextField()

class SavingOptions(models.Model):
    product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE, related_name='option')
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()

    rsrv_type_nm = models.CharField(max_length=100)