# flask web practice for project
import pytest
from app import app
    #GET /
    #HTTP Status Code: 200
    #hello, world
@pytest.fixture
def client():
    return app.test_client()


def do_get(client, path):
    response = client.get(path)
    return response.status_code, str(response.data), response.get_json()


def test_home(client):
    # client = app.test_client()
    status_code, body, data = do_get(client, '/')
    # response = client.get('/')
    #assert response.status_code == 200
    old_count = data['count']
    
    assert status_code == 200
    #assert '"text":"Hello, world"' in str(response.data)
    assert '"text":"Hello, world"' in body


    #data = response.get_json()
    # assert '"count":0' in str(response.data)
    # response.data가 binary 값이므로 str을 취해서 해줌 혹은 앞에 b를 붙이는 방식으로도 가능 함 
    for i in range(5) :
        status_code, body, data = do_get(client, '/') 
        new_count = data['count']
        #response = client.get('/')
       # assert status_code == 200
    # assert '"count":1' in str(response.data)
    
        assert status_code == 200
        assert new_count == old_count + i + 1

def test_abuse(client):
    status_code, body, data = do_get(client, '/')
    old_count = data['count']

    assert status_code == 200
    
    status_code, _, _ = do_get(client, '/abuse')

    assert status_code == 200

    status_code, body, data = do_get(client, '/')
    new_count = data['count']

    assert status_code
    assert new_count == old_count + 100 + 1
