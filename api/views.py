from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Question, Answer
from .serializers import QuestionListSerializer, QuestionDetailSerializer, AnswerSerializer


class QuestionListCreateView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionListSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetailView(APIView):
    def get(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        serializer = QuestionDetailSerializer(question)
        return Response(serializer.data)

    def delete(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnswerCreateView(APIView):
    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(question=question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerDetailView(APIView):
    def get(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)

    def delete(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
