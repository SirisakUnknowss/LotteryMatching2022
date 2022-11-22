from rest_framework import pagination
from rest_framework.response import Response

class BasePageCount(pagination.PageNumberPagination):

    def get_paginated_response(self, data):
        if(self.page.has_next()):
            nextPage_num = self.page.next_page_number()
        else:
            nextPage_num = self.page.paginator.num_pages

        if(self.page.has_previous()):
            previousPage_num = self.page.previous_page_number()
        else:
            previousPage_num = 1

        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'nextPage_num': nextPage_num,          
            'previousPage_num': previousPage_num,                
            'result': data
        })
class FiftyPerPagination(BasePageCount):
    page_size = 50
class TwentyPerPagination(BasePageCount):
    page_size = 20
class TenPerPagination(BasePageCount):
    page_size = 10
class EightPerPagePagination(BasePageCount):
    page_size = 8
class SixPerPagePagination(BasePageCount):
    page_size = 6