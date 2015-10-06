from .base import SdkBaseTestCase


class ClientTestCase(SdkBaseTestCase):

    def test_invoices(self):
        response = self.client.invoices()
        self.assertEqual(response.status_code, 200)
