import pytest
import unittest
import requests
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
        assert 'placeholder' == 'placeholder'

    def test_03_post_payout(self):
        # test for the route that will post consumer point redemption requests
        assert 'placeholder' == 'placeholder'

    def test_04_get_balance(self):
        # test for the route that will provide the payer balances in a
        # dictionary
        assert 'placeholder' == 'placeholder'


if __name__ == "__main__":
    unittest.main()
