from rest_framework.test import APITestCase
from .models import Invoice

class InvoiceAPITest(APITestCase):
    def test_create_invoice(self):
        data = {
            "date": "2023-08-10",
            "invoice_no": "INV123",
            "customer_name": "John Doe",
            "details": [
                {
                    "description": "Item 1",
                    "quantity": 2,
                    "unit_price": 10.0,
                    "price": 20.0
                }
            ]
        }

        response = self.client.post('/invoices/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Invoice.objects.count(), 1)
        self.assertEqual(Invoice.objects.get().invoice_no, 'INV123')
