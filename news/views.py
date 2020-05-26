from rest_framework.views import Response, APIView
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination,
)

from news.models import News
from news.serializers import NewSerializer
from news.filters import NewsFilters


class MyPageNumber(PageNumberPagination):
    page_size = 25  # 每页显示多少条
    page_size_query_param = "size"  # URL中每页显示条数的参数
    page_query_param = "page"  # URL中页码的参数
    max_page_size = None  # 最大页码数限制


class NewsView(viewsets.ModelViewSet):
    serializer_class = NewSerializer
    queryset = News.objects.order_by("-id").all()
    pagination_class = MyPageNumber
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    # filter_class = NewsFilters
    filterset_class = NewsFilters
    search_fields = (
        "infotitle",
        "=infolevel",
    )


class NewsCategoryView(APIView):
    def get(self, request):
        query = News.objects.values_list("category").distinct()
        query = [x[0] for x in query]
        return Response(query)
