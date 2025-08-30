from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, CreateAPIView

from .models import Question, Answer
from .serializers import QuestionListSerializer, QuestionDetailSerializer, AnswerSerializer


class QuestionListView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer


class QuestionDetailView(RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer


class AnswerCreateView(CreateAPIView):
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        question_id = self.kwargs['pk']
        question = get_object_or_404(Question, pk=question_id)
        serializer.save(question=question)


class AnswerDetailView(RetrieveDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
