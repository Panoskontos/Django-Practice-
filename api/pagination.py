
from rest_framework_json_api.pagination import JsonApiPageNumberPagination, JsonApiLimitOffsetPagination


class MyPagePagination(JsonApiPageNumberPagination):
    page_query_param = 'page_number'
    page_size_query_param = 'page_length'
    page_size = 3
    max_page_size = 1000


class MyLimitPagination(JsonApiLimitOffsetPagination):
    offset_query_param = 'offset'
    limit_query_param = 'limit'
    default_limit = 3
    max_limit = None
