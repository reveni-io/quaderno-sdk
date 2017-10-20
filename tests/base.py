import pytest
import unittest
import quaderno_sdk


@pytest.mark.usefixtures('conf_class')
class SdkBaseTestCase(unittest.TestCase):

    def setUp(self):
        self.client = quaderno_sdk.Client(
            token=self.token, api_host=self.api_host)

    def tearDown(self):
        pass
