from unittest.mock import MagicMock

import pytest

from fastapi.testclient import TestClient

import schemas
from main import app
from app.models.user import User
from app.api import deps
from service import user


@pytest.fixture
def client():
    return TestClient(app=app)

@pytest.fixture
def super_user() -> User:
    # mock 현재 활성화된 수퍼 사용자 의존성
    return User(
        id=1,
        email="example@gmail.com",
        is_active=True,
        is_superuser=True,
        full_name="cucuridas",
        team_id=1,
        hashed_password="testPass",
    )

@pytest.fixture
def depend_super_user():
    # mock 현재 활성화된 수퍼 사용자 의존성
    mock_user = User(
        id=1,
        email="example@gmail.com",
        is_active=True,
        is_superuser=True,
        full_name="cucuridas",
        team_id=1,
        hashed_password="testPass",
    )
    app.dependency_overrides[deps.get_current_active_superuser] = lambda: mock_user

@pytest.fixture
def mock_db_users():
    mock_db = MagicMock()
    test_users = [
        schemas.User(
            id=1,
            email="example@gmail.com",
            is_active=True,
            is_superuser=True,
            full_name="cucuridas",
            team_id=1,
        ),
        schemas.User(
            id=2,
            email="example2@gmail.com",
            is_active=True,
            is_superuser=False,
            full_name="testCooked",
            team_id=1,
        ),
    ]
    mock_db.return_value = test_users
    app.dependency_overrides[user.get_multi] = lambda: mock_db