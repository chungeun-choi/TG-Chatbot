from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from app.main import app
import app.schemas as schemas
import app.models as models
import app.api.deps as deps
from app.service import user



def test_read_users(client,mock_db_users,depend_super_user):
    # mock 데이터베이스 의존성
    response = client.get("/users")

    assert response.status_code == 200
    result = response.json()
    print(response.json())
    #assert response.json() == test_users
