#Django
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

class LottAPIView(GenericAPIView):

    def __init__(self, **kwargs):
        super(LottAPIView, self).__init__()
        self.response = {"error":"", "result":""}

class LottAPIGetView(LottAPIView):

    def __init__(self, **kwargs):
        super(LottAPIGetView, self).__init__()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={"request": request})
        self.response["result"] = serializer.data
        return Response(self.response)

class LottListView(LottAPIView):

    def __init__(self, **kwargs):
        super(LottListView, self).__init__()
    
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={"request": request})
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True, context={"request": request})
        self.response["result"] = serializer.data
        return Response(self.response) 

class LottListPaginatedView(LottAPIView):

    def __init__(self, **kwargs):
        super(LottListPaginatedView, self).__init__()

    def get(self, request, *args, **kwargs):
        queryset                = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer              = self.get_serializer(queryset, many=True, context={"request": request})
        self.response["result"] = serializer.data
        return Response(self.response)