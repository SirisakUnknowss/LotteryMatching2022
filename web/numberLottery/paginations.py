from rest_framework import pagination
from rest_framework.response import Response

class BasePageCount(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'previous': self.get_previous_link(),
            'currentPage': self.page.number,
            'next': self.get_next_link(),
            'totalPages': self.page.paginator.num_pages,
            'results': data
        })

class TwentyPerPagination(BasePageCount):
    page_size = 20
class EightPerPagePagination(BasePageCount):
    page_size = 8
class SixPerPagePagination(BasePageCount):
    page_size = 6