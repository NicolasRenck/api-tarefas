from django.shortcuts import render
from rest_framework import viewsets
from .models import Tarefa
from .serializers import TarefaSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response


class TarefaViewSet(viewsets.ModelViewSet):
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['concluida']
    search_fields = ['titulo', 'descricao']

    def get_queryset(self):
        return Tarefa.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)   


    @action(detail=True, methods=['post']) #function de concluir uma tarefa
    def concluir(self, request, pk=None):
        tarefa = self.get_object()
        tarefa.concluida = True
        tarefa.save()
        return Response({'status': 'tarefa concluída'})    