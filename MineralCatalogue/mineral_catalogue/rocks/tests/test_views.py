from django.urls import reverse
from django.test import TestCase, Client
from rocks.models import Mineral
from django.utils import timezone



class Test_views(TestCase):
    '''BELOW I HAVE SET UP MY TESTCASE BY USING CLIENT AND THE REVERSE URL FUNCTION.
       EACH TESTCASE CHECKS FOR A 200 RESPONSE FROM THE URL AND ALSO CHECKS IF
       THE CORRECT HTML TEMPLATE HAS BEEN USED.
    '''
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('rocks:index', args=['a'])
        self.random_url = reverse('rocks:random')
        self.details_url = reverse('rocks:details', args=[1])



    def test_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rocks/index.html')



    def test_random_GET(self):
        response = self.client.get(self.random_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rocks/random.html')


    def test_details_GET(self):
        reponse = self.client.get(self.details_url)
        self.assertEqual(reponse.status_code, 200)
        self.assertTemplateUsed(reponse, 'rocks/details.html')
