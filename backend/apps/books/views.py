from django.shortcuts import get_object_or_404

from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import BookSerializer


class BookCreateAPIView(ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()
    

class BookUpdateAPIView(UpdateAPIView):
    serializer_class = BookSerializer

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(self.serializer_class.Meta.model, pk=pk)
    
    def put(self, request, *args, **kwargs):
        author = self.get_object()
        serializer = BookSerializer(author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Libro actualizado con exito'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        