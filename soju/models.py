from django.db import models
from django.urls import reverse


class Beer(models.Model):
    # 주종
    category = models.CharField(max_length=20, db_index=True, null=True)
    # 제품 이름
    name = models.CharField(max_length=200, db_index=True, null=True)
    # 사진
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    # 설명
    description = models.TextField(blank=True)
    # 간단한 설명
    meta_description = models.CharField(max_length=40, null=True, blank=True)
    # 도수를 소수점으로 나타낸다. 10의자리까지 소수아래 한자리까지만
    ABV = models.DecimalField(max_digits=2, decimal_places=1, blank=True)
    # 당도를 숫자로 나타낸다. 양의 정수만 가능함
    sugar = models.PositiveIntegerField(blank=True)
    # 산미
    sanmi = models.PositiveIntegerField(blank=True)
    # 향
    s = models.CharField(max_length=20, null=True, blank=True)

    # # 링크
    # link = models.TextField(blank=True)
    # # 별점
    # star = models.IntegerField(null=True, blank=True)
    # # 좋아요
    # like = models.IntegerField(null=True, blank=True)

    # # 리뷰
    # re = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
        ordering = ['category']  # 이름으로 정렬

    def __str__(self):
        return self.name

    # url 넘겨줄 때 views.py 의 beer_detail 이용하고 id와 slug 를 넘겨준다.
    def get_absolute_url(self):
        return reverse('shop:beer_detail', args=[self.id])


# class User(models.Model):
#     user_name = models.CharField(max_length=10, db_index=True)
#     password = models.CharField(max_length=64, verbose_name='Password')
#     registered = models.DateTimeField(auto_now_add=True, verbose_name='AddDate')
#
#     def __self__(self):
#         return self.username
#
#     class Meta:
#         db_table = 'user'
#         verbose_name = 'user'
#         verbose_name_plural = 'user'


# class Like(models.Model):
#     user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
#     user_like = models.ForeignKey(Beer, on_delete=models.SET_NULL, null=True, related_name='beer')


# class Userstar(models.Model):
#     name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='name', null=True)
#     category = models.ForeignKey(Beer, on_delete=models.SET_NULL, related_name='star_category', null=True)
#     # 제품 이름
#     name = models.ForeignKey(Beer, on_delete=models.SET_NULL, related_name='star_name', null=True)
#     # 도수를 소수점으로 나타낸다. 10의자리까지 소수아래 한자리까지만
#     ABV = models.ForeignKey(Beer, on_delete=models.SET_NULL, related_name='star_ABV', null=True)
#     # 당도를 숫자로 나타낸다. 양의 정수만 가능함
#     sugar = models.ForeignKey(Beer, on_delete=models.SET_NULL, related_name='star_sugar', null=True)
#     # 별점
#     star = models.ForeignKey(Beer, on_delete=models.SET_NULL, related_name='star_star', null=True)
#     # 산미
#     sanmi = models.ForeignKey(Beer, on_delete=models.SET_NULL, related_name='star_sanmi', null=True)
#     # 향
#     s = models.ForeignKey(Beer, on_delete=models.SET_NULL, related_name='star_s', null=True)