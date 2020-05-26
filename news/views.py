from rest_framework.views import Response, APIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

from news.models import News
from news.serializers import NewSerializer


class MyPageNumber(PageNumberPagination):
    page_size = 25  # 每页显示多少条
    page_size_query_param = 'size'  # URL中每页显示条数的参数
    page_query_param = 'page'  # URL中页码的参数
    max_page_size = None  # 最大页码数限制


class NewsView(APIView):

    def get(self, request):
        news = News.objects.order_by('-id').all()
        page_obj = MyPageNumber()
        page_news = page_obj.paginate_queryset(queryset=news, request=request, view=self)
        
        ret = NewSerializer(page_news, many=True)
        return Response(ret.data)
