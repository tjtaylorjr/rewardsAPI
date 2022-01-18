import json
import pytest
import unittest
from flask import current_app
from rewards_service import app

class TestRewardService(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()
        self.app = None
        self.app_context = None

    def test_01_app(self):
        assert self.app is not None
        assert current_app == self.app

    def test_02_app_post_transaction(self):
        # test for the route responsible for posting transaction objects
        # to app's data store

        # test 1: positive points
        result = self.client.post(
            '/api/v1/account',
            json={"payer": "KRAFT",
                  "points": 3000,
                  "timestamp": "2022-01-03T15:00:00Z"}
        )
        response = json.loads(result.get_data(as_text=True))
        expected = {'payer': 'KRAFT',
                    'points': 3000}

        assert response == expected
        assert result.status_code == 200

        # test 2: negative points
        result2 = self.client.post(
            '/api/v1/account',
            json={"payer": "KRAFT",
                  "points": -500,
                  "timestamp": "2022-01-05T16:00:00Z"}
        )

        response2 = json.loads(result2.get_data(as_text=True))
        expected2 = {'payer': 'KRAFT',
                    'points': -500}

        assert response2 == expected2
        assert result2.status_code == 200

    # test 3: excessive negative points
        result3 = self.client.post(
            '/api/v1/account',
            json={"payer": "KRAFT",
                  "points": -10000,
                  "timestamp": "2022-01-09T13:00:00Z"}
        )

        response3 = json.loads(json.dumps(result3.get_data(as_text=True)))
        expected3 = 'Request rejected. Insufficient points to complete this transaction.'

        assert response3 == expected3
        assert result3.status_code == 400

    def test_03_post_redemption(self):
        # test for the route that will post consumer point redemption requests

        # test 1: request for a deliverable amount of points
        result = self.client.post(
            '/api/v1/account/rewards',
            json={"points": 2000}
        )
        response = json.loads(result.get_data(as_text=True))
        expected = [{'payer': 'KRAFT', 'points': -2000}]

        assert response == expected
        assert result.status_code == 200

        # test 2: request for an undeliverable amount of points
        result = self.client.post(
            '/api/v1/account/rewards',
            json={"points": 10000}
        )
        response = json.loads(json.dumps(result.get_data(as_text=True)))
        expected = 'Request rejected. Insufficient points to complete this transaction.'

        assert response == expected
        assert result.status_code == 400

    def test_04_get_balance(self):
        # test for the route that will provide the payer balances in a
        # dictionary

        result = self.client.get('/api/v1/account')
        response = json.loads(result.get_data(as_text=True))
        expected = {'KRAFT': 500}

        assert response == expected
        assert result.status_code == 200


if __name__ == "__main__":
    unittest.main()
