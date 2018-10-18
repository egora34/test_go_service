import pytest
# import requests
import json

@pytest.fixture(scope="class", autouse=True)
def test_data(request):
	test_data = {"json": json.load(open("test_data/data.json")), "url": "http://localhost:8078/get_config"}
	if request.cls is not None:
		request.cls.test_data = test_data