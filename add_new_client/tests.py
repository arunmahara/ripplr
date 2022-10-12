from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase


# for client detail
class ClientDetailTestCase(APITestCase):
    def test_create_client_detail(self):
        '''Create client detail'''
        data = {
            "client_name": "Aachi Group of Companies",
            "client_short_name": "aachi",
            "legal_structure": "Company",
            "contact_person_first_name": "Aachi Group of Companies",
            "contact_person_middle_name": "null",
            "contact_person_last_name": "Aachi Group of Companies",
            "gender": "M",
            "primary_cost_center": "Distribution"
        }
        response = self.client.post('/client_detail/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_client_detail(self):
        '''List all client detail'''
        response = self.client.get('/client_detail/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_client_detail(self):
        '''Retrive specific client detail'''
        response = self.client.get('/client_detail/', kwargs={'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_client_detail(self):
        '''Delete client detail'''
        response = self.client.get('/client_detail/', kwargs={'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# for communication detail
class CommunicationDetailTestCase(APITestCase):
    def test_create_communication_detail(self):
        '''Create communication detail'''
        data = {
            "client": 1,
            "address": "No 1, Ponniamman Nagar, Keal Ayanambakkam",
            "pin_code": "600095",
            "zone": "Central Zone",
            "state": "Bihar",
            "city": "none",
            "email": "admin@xyz.com",
            "mobile_no": "+918888888821",
            "alternate_no": "+915698888821"
        }
        response = self.client.post('/communication_detail/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_communication_detail(self):
        '''List all communication detail'''
        response = self.client.get('/communication_detail/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_communication_detail(self):
        '''Retrive specific communication detail'''
        response = self.client.get('/communication_detail/', kwargs={'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_communication_detail(self):
        '''Delete communication detail'''
        response = self.client.get('/communication_detail/', kwargs={'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# for billing detail
class BillingDetailTestCase(APITestCase):
    def test_create_billing_detail(self):
        '''Create billing detail'''
        data = {
            "address": "No 1, Ponniamman Nagar, Keal Ayanambakkam",
            "pin_code": "600095",
            "zone": "Central Zone",
            "state": "Bihar",
            "city": "none",
            "client": 1
        }
        response = self.client.post('/billing_detail/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_billing_detail(self):
        '''List all billing detail'''
        response = self.client.get('/billing_detail/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_billing_detail(self):
        '''Retrive specific billing detail'''
        response = self.client.get('/billing_detail/', kwargs={'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_billing_detail(self):
        '''Delete billing detail'''
        response = self.client.get('/billing_detail/', kwargs={'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# for shipping detail
class ShippingDetailTestCase(APITestCase):
    def test_create_shipping_detail(self):
        '''Create shipping detail'''
        data = {
            "address": "No 1, Ponniamman Nagar, Keal Ayanambakkam",
            "pin_code": "600095",
            "zone": "Central Zone",
            "state": "Bihar",
            "city": "none",
            "client": 1
        }
        response = self.client.post('/shipping_detail/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_shipping_detail(self):
        '''List all shipping detail'''
        response = self.client.get('/shipping_detail/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_shipping_detail(self):
        '''Retrive specific shipping detail'''
        response = self.client.get('/shipping_detail/', kwargs={'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_shipping_detail(self):
        '''Delete shipping detail'''
        response = self.client.get('/shipping_detail/', kwargs={'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# for banking detail
class BankingDetailTestCase(APITestCase):
    def test_create_banking_detail(self):
        '''Create banking detail'''
        data = {
            "client": 1,
            "account_code": "345456456",
            "account_no": "45643445",
            "ifsc_code": "45643534",
            "bank_name": "here",
            "bank_city": "here",
            "bank_branch": "here",
            "bank_document": "document.pdf"
        }
        response = self.client.post('/banking_detail/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_banking_detail(self):
        '''List all banking detail'''
        response = self.client.get('/banking_detail/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_banking_detail(self):
        '''Retrive specific banking detail'''
        response = self.client.get('/banking_detail/', kwargs={'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_banking_detail(self):
        '''Delete banking detail'''
        response = self.client.get('/banking_detail/', kwargs={'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# for document_proof
class DocumentProofTestCase(APITestCase):
    def test_create_document_proof_detail(self):
        '''Create document_proof detail'''
        data = {
            "client": 1,
            "pan_number": "34555726B",
            "adhar_number": "AAFCI1726B",
            "gst_reg_type": "Registered",
            "gst_number": "29AAFCI1726B1ZW",
            "pan_document": "document.pdf",
            "adhar_document": "document.pdf",
            "gst_document": "document.pdf",
        }
        response = self.client.post('/document_proof/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_document_proof_detail(self):
        '''List all document_proof detail'''
        response = self.client.get('/document_proof/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_document_proof_detail(self):
        '''Retrive specific document_proof detail'''
        response = self.client.get('/document_proof/', kwargs={'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_document_proof_detail(self):
        '''Delete document_proof detail'''
        response = self.client.get('/document_proof/', kwargs={'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# for other detail
class OtherDetailTestCase(APITestCase):
    def test_create_other_detail(self):
        '''Create other detail'''
        data = {
            "client": 1,
            "related_party": 1,
            "black_listed": 0,
            "same_as_billing_location": 1,
            "document_currency": "here",
            "credit_period": "here",
            "credit_amount": 345634.45,
            "payment_terms_and_condition": "this is term and condition",
            "exempt_from_tax": 0
        }
        response = self.client.post('/other_detail/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_other_detail(self):
        '''List all other detail'''
        response = self.client.get('/other_detail/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_other_detail(self):
        '''Retrive specific other detail'''
        response = self.client.get('/other_detail/', kwargs={'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_other_detail(self):
        '''Delete other detail'''
        response = self.client.get('/other_detail/', kwargs={'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# for login credential detail
class LoginCredentialDetailTestCase(APITestCase):
    def test_create_login_credential(self):
        '''Create login credential detail'''
        data = {
            "username": "admin",
            "password": "here"
        }
        response = self.client.post('/login_credential/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_login_credential_detail(self):
        '''List all login credential detail'''
        response = self.client.get('/login_credential/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_login_credential_detail(self):
        '''Retrive specific login credential detail'''
        response = self.client.get('/login_credential/', kwargs={'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_login_credential(self):
        '''Delete login credential detail'''
        response = self.client.get('/login_credential/', kwargs={'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)