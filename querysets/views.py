from django.db import transaction
from django.http import HttpResponse
from django.db.models import Sum, Avg, Prefetch
from django.views import View

from querysets.models import City, Dong, Goo, User, Book, Author, BookAuthor, Rating

#유저정보 전체를 불러오기 위해 all() 사용
def get_all(request) :
    user_all = User.objects.all()
    return HttpResponse(user_all)

#유저ID가 71번인 유저가 등록한 별점 QuerySet을 불러오기 위해 filter() 사용
def filter(request) :
    rating_filter = Rating.objects.filter(user_id=71)
    return HttpResponse(rating_filter)

#유저ID가 71번인 유저가 등록한 별점을 제외한 QuerySet을 불러오기 위해 filter() 사용
def exclude(request) :
    rating_exclude = Rating.objects.exclude(user_id=71)
    return HttpResponse(rating_exclude)

#집계함수 기능을 사용하기 위해 aggregate() 사용 -> aggregate는 집계된 결과만 나옴
def aggregate(request) :
    rating_sum = Rating.objects.filter(user_id=71).aggregate(Sum('rating'))
    rating_avg = Rating.objects.filter(user_id=71).aggregate(Avg('rating'))
    return HttpResponse(rating_sum, rating_avg)

#GroupBy 기능을 사용하기 위해, 설정한 변수로 집계되어 컬럼 추가돼서 SELECT 후 쿼리셋으로 리턴
def annotate(request) :
    rating_sum = Rating.objects.filter(user_id=71).annotate(Sum('rating'))
    rating_avg = Rating.objects.filter(user_id=71).annotate(Avg('rating'))
    return HttpResponse(rating_sum, rating_avg)

#annotate와 리턴되는 쿼리셋 결과는 같은데, DB Hits를 할 때 집계함수가 SELECT에 포함되지 않음
def alias(request) :
    rating_sum = Rating.objects.alias(r_sum=Sum('rating')).filter(user_id=71)
    rating_avg = Rating.objects.alias(r_avg=Avg('rating')).filter(user_id=71)
    return HttpResponse(rating_sum, rating_avg)

#정렬을 위한 order_by(), '?'를 쓰면 랜덤으로 아무거나 정렬됨
def order_by(request) :
    queryset1 = Rating.objects.filter(id=71).order_by('rating')
    queryset2 = Rating.objects.filter(id=71).order_by('-rating')
    queryset3 = Rating.objects.filter(id=71).order_by('?')
    return HttpResponse(queryset3)

#중복없이 식별하기 위한 dinstinct()
def distinct(request) :
    rating = Rating.objects.order_by('user').distinct('user', 'rating')
    return HttpResponse(rating)

#select_realted
def select_related(request) :
    rating = Rating.objects.select_related('book', 'user').filter(user_id=71)
    return HttpResponse(rating)

#prefetch_related
#ManyToMany 관계에는 prefetch_related를 사용해야 함
def prefetch_related(request) :
    books  = Book.objects.prefetch_related('author').filter(author__id=71)
    return HttpResponse(books)

#트랜잭션을 이용하여 데이터 락을 위해 select_for_update 사용
#nowait/skip_locked의 기본값은 False이며, 데이터에 락이 잡혀있다면 락이 풀릴때까지 대기 / 둘 중 하나만 True를 사용할 수 있음
def select_for_update(request) :
    authors = Author.objects.select_for_update()
    with transaction.atomic() :
        for author in authors :
            print(author)
    return HttpResponse(authors)


class BeforePrefetchView(View):
    def get(self, request, city_id):
       # citys = City.objects.prefetch_related("goo_set__dong_set").get(id=city_id)
        citys = City.objects.prefetch_related(
           Prefetch("goo_set",
                    queryset=Goo.objects.all().prefetch_related(
                        Prefetch(
                            "dong_set",
                            queryset=Dong.objects.all(),
                            to_attr="prefetch_dong_set"
                        )
                    ),
                    to_attr="prefetch_goo_set")
       ).get(id=city_id)
        
        dong_list = []
        goo_list = []
        
        # for goo in citys.goo_set.all():
        #     for dong in goo.dong_set.all():
        #         dong_list.append(dong.id)
        #         goo_list.append(goo)

        # for goo in citys.goo_set.all():
        #     for dong in goo.dong_set.all():
        #         dong_list.append(dong.id)
        #         goo_list.append(goo)
        
        
        for goo in citys.prefetch_goo_set:
            for dong in goo.prefetch_dong_set:
                dong_list.append(dong.id)
                goo_list.append(goo)
        
                
        for goo in citys.prefetch_goo_set:
            for dong in goo.prefetch_dong_set:
                dong_list.append(dong.id)
                goo_list.append(goo)

        
        return HttpResponse(dong_list, goo_list)