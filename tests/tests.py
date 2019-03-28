import requests
import unittest


class ApiStatusTest(unittest.TestCase):
    def setUp(self):
        requests.post('http://127.0.0.1:8080/status', json={'value1': 'GAME TITLE', 'value2': 'Player 1', 'value3': '1'})

    def test_get_status(self):
        get_resp = requests.get('http://127.0.0.1:8080/status')
        print(get_resp.json())
        self.assertEqual(get_resp.json()["name"], 'GAME TITLE')
        self.assertEqual(get_resp.json()["player"], "Player 1")
        self.assertEqual(get_resp.json()["turn"], "1")

    def test_post_status(self):
        post_resp = requests.post('http://127.0.0.1:8080/status', json={'value1': 'POST GAME',
                                                                        'value2': 'POST PLAYER',
                                                                        'value3': '15'})
        self.assertEqual(post_resp.json()['name'], 'POST GAME')
        self.assertEqual(post_resp.json()['player'], 'POST PLAYER')
        self.assertEqual(post_resp.json()['turn'], '15')
