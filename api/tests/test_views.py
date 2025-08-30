import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from uuid import uuid4

from api.models import Question, Answer


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def question():
    return Question.objects.create(text='Тестовый вопрос')


@pytest.fixture
def answer(question):
    return Answer.objects.create(
        question=question,
        user_id=uuid4(),
        text='Тестовый ответ'
    )


@pytest.mark.django_db
class TestQuestionsView:
    def test_get_questions_list(self, api_client, question):
        response = api_client.get(reverse('question-list-create'))
        assert response.status_code == 200
        assert response.data[0]['text'] == 'Тестовый вопрос'

    def test_create_question(self, api_client):
        response = api_client.post(
            reverse('question-list-create'),
            data={'text': 'Новый вопрос'},
            format='json'
        )
        assert response.status_code == 201
        assert response.data['text'] == 'Новый вопрос'

    def test_get_question_detail(self, api_client, question, answer):
        response = api_client.get(reverse('question-detail', args=[question.id]))
        assert response.status_code == 200
        assert response.data['text'] == 'Тестовый вопрос'
        assert len(response.data['answers']) == 1
        assert response.data['answers'][0]['text'] == 'Тестовый ответ'

    def test_delete_question(self, api_client, question, answer):
        response = api_client.delete(reverse('question-detail', args=[question.id]))
        assert response.status_code == 204

    def test_create_question_with_empty(self, api_client):
        response = api_client.post(
            reverse('question-list-create'),
            data={'text': ''},
            format='json'
        )
        response2 = api_client.post(
            reverse('question-list-create'),
            data={'text': '     '},
            format='json'
        )
        assert response.status_code == 400
        assert 'text' in response.data
        assert 'Это поле не может быть пустым.' in response.data['text'][0]
        assert response2.status_code == 400
        assert 'text' in response2.data


@pytest.mark.django_db
class TestAnswersView:
    def test_create_answer(self, api_client, question):
        response = api_client.post(
            reverse('answer-create', args=[question.id]),
            data={'user_id': str(uuid4()), 'text': 'Ответ'},
            format='json'
        )
        assert response.status_code == 201
        assert response.data['text'] == 'Ответ'

    def test_get_answers_detail(self, api_client, answer):
        response = api_client.get(reverse('answer-detail', args=[answer.id]))
        assert response.status_code == 200
        assert response.data['text'] == 'Тестовый ответ'

    def test_delete_answer(self, api_client, answer):
        response = api_client.delete(reverse('answer-detail', args=[answer.id]))
        assert response.status_code == 204

    def test_create_answer_with_empty(self, api_client, question):
        response = api_client.post(
            reverse('answer-create', args=[question.id]),
            data={'user_id': str(uuid4()), 'text': ''},
            format='json'
        )
        response2 = api_client.post(
            reverse('answer-create', args=[question.id]),
            data={'user_id': str(uuid4()), 'text': '     '},
            format='json'
        )
        assert response.status_code == 400
        assert 'text' in response.data
        assert 'Это поле не может быть пустым.' in response.data['text'][0]
        assert response2.status_code == 400
        assert 'text' in response2.data
