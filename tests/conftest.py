import pytest
from model_bakery import baker
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def course_fixture():
    def factory(**kwargs):
        return baker.make('Course', **kwargs)
    return factory


@pytest.fixture
def student_fixture():
    def factory(**kwargs):
        return baker.make('Student', **kwargs)
    return factory
