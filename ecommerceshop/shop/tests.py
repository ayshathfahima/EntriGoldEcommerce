#testing views

from django.test import TestCase,Client
from django.urls import resolve, reverse
from shop.views import allproducts,cart

class Testviewshome(TestCase):

    def setUp(self):
        self.client=Client()
        self.allproducts=reverse('allproducts')
        self.carturl=reverse('cart')

    def testviewshome(self):

        response=self.client.get(self.allproducts)
        print("Response: ", response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'home.html')

    def testviewcart(self):
        response = self.client.get(self.carturl)
        print("Response: ", response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')

