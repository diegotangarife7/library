from django.shortcuts import get_object_or_404

from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AuthorSerializer, ListAuthorSerializer



class CreateAuthorAPIView(CreateAPIView):
    serializer_class = AuthorSerializer


class ListAllAuthorAPIView(ListAPIView):
    serializer_class = ListAuthorSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()


class UpdateAuthorAPIView(UpdateAPIView):
    serializer_class = AuthorSerializer

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(self.serializer_class.Meta.model, pk=pk)

    def put(self, request, *args, **kwargs):
        author = self.get_object()
        serializer = AuthorSerializer(author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    