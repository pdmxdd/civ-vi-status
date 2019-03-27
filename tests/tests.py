import requests
import unittest


class ApiStatusTest(unittest.TestCase):
    def setUp(self):
        requests.post('http://127.0.0.1:8080/status', json={'test_key_1': 'test_value_1'})

    def test_get_status(self):
        get_resp = requests.get('http://127.0.0.1:8080/status')
        print(get_resp.json())
        self.assertEqual(get_resp.json()["test_key_1"], 'test_value_1')

    def test_post_status(self):
        post_resp = requests.post('http://127.0.0.1:8080/status', json={'test_key': 'test_value'})
        self.assertEqual(post_resp.json()["test_key"], "test_value")
