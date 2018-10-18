import requests
import pytest


class TestGo:
	def test_sunny_day_test(self):
		req = requests.post(self.test_data["url"], data=str(self.test_data["json"]["sunny_day_test"]["data"]).replace('\'', '"'))
		assert req.json() == self.test_data["json"]["sunny_day_test"]["result"]

	def test_sunny_day_develop(self):
		req = requests.post(self.test_data["url"], data=str(self.test_data["json"]["sunny_day_develop"]["data"]).replace('\'', '"'))
		assert req.json() == self.test_data["json"]["sunny_day_develop"]["result"]		

	def test_without_url(self):
		req = requests.post(self.test_data["url"].replace("/get_config",""), data=str(self.test_data["json"]["sunny_day_develop"]["data"]).replace('\'', '"'))
		assert req.text == self.test_data["json"]["without_url"]["result"]

	def test_without_type(self):
		req = requests.post(self.test_data["url"], data=str(self.test_data["json"]["without_type"]["data"]).replace('\'', '"'))
		assert req.json() == self.test_data["json"]["without_type"]["result"]

	def test_without_data(self):
		req = requests.post(self.test_data["url"], data=str(self.test_data["json"]["without_data"]["data"]).replace('\'', '"'))
		assert req.json() == self.test_data["json"]["without_data"]["result"]

	def Test_type_empty_string(self):
		req = requests.post(self.test_data["url"], data=str(self.test_data["json"]["type_empty_string"]["data"]).replace('\'', '"'))
		assert req.json() == self.test_data["json"]["type_empty_string"]["result"]

	def test_data_empty_string(self):
		req = requests.post(self.test_data["url"], data=str(self.test_data["json"]["data_empty_string"]["data"]).replace('\'', '"'))
		assert req.json() == self.test_data["json"]["data_empty_string"]["result"]

	def test_type_not_string(self):
		req = requests.post(self.test_data["url"], data=str(self.test_data["json"]["type_not_string"]["data"]).replace('\'', '"'))
		assert req.json() == self.test_data["json"]["type_not_string"]["result"]

	def test_data_not_string(self):
		req = requests.post(self.test_data["url"], data=str(self.test_data["json"]["data_not_string"]["data"]).replace('\'', '"'))
		assert req.json() == self.test_data["json"]["data_not_string"]["result"]

	def test_with_host(self):
		req = requests.post(self.test_data["url"], data=str(self.test_data["json"]["with_host"]["data"]).replace('\'', '"'))
		assert req.json() == self.test_data["json"]["with_host"]["result"]
