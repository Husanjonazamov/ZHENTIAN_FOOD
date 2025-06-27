from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import math

class ProductPagination(PageNumberPagination):
    page_size = 18
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            "status": True,
            "data": {
                "links": {
                    "previous": self.get_previous_link(),
                    "next": self.get_next_link(),
                },
                "total_items": self.page.paginator.count,
                "total_pages": math.ceil(self.page.paginator.count / self.page_size),
                "page_size": self.page_size,
                "current_page": self.page.number,
                "results": data,
            }
        })
