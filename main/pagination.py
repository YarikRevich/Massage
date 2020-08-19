from rest_framework.pagination import LimitOffsetPagination

class PaginationWithMax(LimitOffsetPagination):
    max_limit = 10