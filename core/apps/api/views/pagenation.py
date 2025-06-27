from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import math

class ProductPagination(PageNumberPagination):
    page_size = 12
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


class BaseViewSetMixin:
    action_serializer_class = {}
    action_permission_classes = {}

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)

        if isinstance(response.data, dict) and "status" in response.data:
            return response

        if response.status_code >= 400:
            response.data = {
                "status": False,
                "data": {
                    "links": {
                        "previous": None,
                        "next": None
                    },
                    "total_items": 0,
                    "total_pages": 0,
                    "page_size": 0,
                    "current_page": 1,
                    "results": [response.data] if isinstance(response.data, dict) else []
                }
            }
            return response
        else:
            response.data = {
                "status": True,
                "data": response.data
            }

        return response

    def get_serializer_class(self):
        return self.action_serializer_class.get(self.action, self.serializer_class)

    def get_permissions(self):
        return [
            permission()
            for permission in self.action_permission_classes.get(
                self.action, self.permission_classes
            )
        ]
