# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .models import Memo, User
from .serializers import MemoSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
# Create your views here.


class UserAPIView(APIView):
    @staticmethod
    def get(request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class GenericUserAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                         mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                     viewsets.ModelViewSet):
    serializer_class = MemoSerializer
    queryset = Memo.objects.all()

    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class MemoAPIView(APIView):
    @staticmethod
    def get(request):
        memos = Memo.objects.all()
        serializer = MemoSerializer(memos, many=True)
        return Response(serializer.data)


class MemoDetails(APIView):

    @staticmethod
    def get_object(pk):
        try:
            return Memo.objects.get(pk=pk)
        except Memo.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        memo = self.get_object(pk)
        serializer = MemoSerializer(memo)
        return Response(serializer.data)

    def put(self, request, pk):
        memo = self.get_object(pk)
        serializer = MemoSerializer(memo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        memo = self.get_object(pk)
        memo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(["GET", "POST"])
# def memo_list(request):
#     if request.method == 'GET':
#
#     elif request.method == 'POST':
#
#
# @api_view(["GET", "PUT", "DELETE"])
# def memo_detail(request, pk):
#     try:
#
#     if request.method == 'GET':
#         serializer = MemoSerializer(memo)
#         return Response(serializer.data)
#     elif request.method == "PUT":
#         serializer = MemoSerializer(memo, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == "DELETE":
#         memo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# def homePage(request, *args, **kwargs):
#     return render(request, 'pages/home.html', context={}, status=200)
# def specific_memo(request, memo_id, *args, **kwargs):
#     data = {
#         "id": memo_id,
#     }
#     status = 200
#     try:
#         obj = Memos.objects.get(id=memo_id)
#         data['content'] = obj.content
#     except:
#         data['message'] = 'This user has no content or content not found'
#         status = 404
#     return JsonResponse(data, status=status)
