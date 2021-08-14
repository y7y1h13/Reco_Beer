from django.db import models
from django.urls import reverse


class Category(models.Model):  # 카테고리에는 이름과 설명을 넣는다.
    name = models.CharField(max_length=200, db_index=True)  # 인덱스 추가
    meta_description = models.TextField(blank=True)  # 빈칸 허용, 설명쓰는 칸

    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    # 의미있는 url을 만들기 위해 slug를 써준다. 유일해야 url로 구별이 가능함

    class Meta:  # 관리자 페이지에 적용할 기능들과 이름들을 적어준다.
        ordering = ['name']  # 이름으로 정렬
        verbose_name = 'Category'  # 이름 단수형
        verbose_name_plural = 'Categories'  # 이름 복수형

    def __str__(self):  # 이걸 적어야 관리자페이지에서 제품 추가할 때 이름으로 나옴
        return self.name

    def get_absolute_url(self):
        return reverse('soju:beer_in_category', args=[self.slug])
    # 버튼 눌렀을 때 url을 어떻게 만들지. beer_in_category는 views.py에서 만들어준다.


class Beer(models.Model):
    # 카테고리 이름
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='products')
    # 제품 이름
    name = models.CharField(max_length=200, db_index=True)
    # url 연결위해 슬러그 생성
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    # 사진
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    # 설명
    description = models.TextField(blank=True)
    # 가격
    price = models.PositiveIntegerField()  # 양의 자연수만 가능하게 설정
    # 도수를 소수점으로 나타낸다. 10의자리까지 소수아래 한자리까지만
    ABV = models.DecimalField(max_digits=2, decimal_places=1)
    # 색을 숫자로 나타낸다. 양의 정수만 가능함//// 색은 좀 애매해서 빼놓음
    # color = models.PositiveIntegerField()
    # 당도를 숫자로 나타낸다. 양의 정수만 가능함
    sugar = models.PositiveIntegerField()

    class Meta:
        ordering = ['name']  # 이름으로 정렬
        index_together = [['id', 'slug']]  # 인덱스와 슬러그를 묶는다.

    def __str__(self):
        return self.name

    # url 넘겨줄 때 views.py 의 beer_detail 이용하고 id와 slug 를 넘겨준다.
    def get_absolute_url(self):
        return reverse('shop:beer_detail', args=[self.id, self.slug])

