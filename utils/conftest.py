import pytest

@pytest.fixture(scope="class")
def api_connection(request):
    return request.param
