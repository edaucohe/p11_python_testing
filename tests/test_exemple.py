import pytest

from server import index


@pytest.fixture
def client():
    app = index({"TESTING": True})
    with app.test_client() as client:
        yield client

# from exemple import reverse_str
#
#
# def test_should_reverse_string():
#     assert reverse_str('abc') == 'cba'