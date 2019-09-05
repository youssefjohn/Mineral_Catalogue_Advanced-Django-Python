'''TESTING MODELS AND VIEWS'''

from django.urls import reverse
from django.test import TestCase, Client
from .models import Mineral
from django.utils import timezone


# Create your tests here.


class Test_Mineral_Model(TestCase):
    '''BELOW I HAVE TESTED MY MINERAL MODEL.
       THE FIRST TEST CHECKS TO SEE IF A NEW INSTANCE OF A MODEL
       CAN BE CREATED. THE SECOND TEST CHECKS WHETHER TWO
       INSTANCES OF A MODEL ARE UNIQUE AND DIFFERENT FROM ONE ANOTHER
    '''
    def test_model_creation(self):
        self.a = Mineral.objects.create(name="daa",
                                  image_filename="kasma",
                                  image_caption="ansdkq",
                                  category="kdCJXA",
                                  formula="wDNA",
                                  strunz_classification="KCDAX",
                                  color="",
                                  crystal_system="",
                                  unit_cell="",
                                  crystal_symmetry="",
                                  cleavage="",
                                  mohs_scale_hardness="",
                                  luster="",
                                  streak="",
                                  diaphaneity="",
                                  optical_properties="",
                                  refractive_index="",
                                  crystal_habit="",
                                  specific_gravity="")


        self.assertTrue(self.a)

    def test_two_instances_are_same(self):
        self.a = Mineral.objects.create(name="daa",
                                   image_filename="kasma",
                                   image_caption="ansdkq",
                                   category="kdCJXA",
                                   formula="wDNA",
                                   strunz_classification="KCDAX",
                                   color="",
                                   crystal_system="",
                                   unit_cell="",
                                   crystal_symmetry="",
                                   cleavage="",
                                   mohs_scale_hardness="",
                                   luster="",
                                   streak="",
                                   diaphaneity="",
                                   optical_properties="",
                                   refractive_index="",
                                   crystal_habit="",
                                   specific_gravity="")

        self.b = Mineral.objects.create(name="daa",
                                   image_filename="kasma",
                                   image_caption="ansdkq",
                                   category="kdCJXA",
                                   formula="wDNA",
                                   strunz_classification="KCDAX",
                                   color="",
                                   crystal_system="",
                                   unit_cell="",
                                   crystal_symmetry="",
                                   cleavage="",
                                   mohs_scale_hardness="",
                                   luster="",
                                   streak="",
                                   diaphaneity="",
                                   optical_properties="",
                                   refractive_index="",
                                   crystal_habit="",
                                   specific_gravity="")



        self.assertNotEqual(self.a,self.b)
        self.assertIsInstance(self.a, Mineral)
        self.assertIsInstance(self.b, Mineral)

class Test_views(TestCase):
    '''BELOW I HAVE SET UP MY TESTCASE BY USING CLIENT AND THE REVERSE URL FUNCTION.
       EACH TESTCASE CHECKS FOR A 200 RESPONSE FROM THE URL AND ALSO CHECKS IF
       THE CORRECT HTML TEMPLATE HAS BEEN USED.
    '''
    def setUp(self):


        self.client = Client()
        self.details = reverse("rocks:details", args=[1]) # The details view requires a pk argument. Here I gave it the value of 1
        self.random = reverse("rocks:random")
        self.index = reverse("rocks:index")


    def test_details_view(self):
        response1 = self.client.get(self.details)
        self.assertEqual(response1.status_code, 200)
        self.assertTemplateUsed(response1, "rocks/details.html")

    def test_random_view(self):
        # resp = self.client.get(reverse("rocks:random"))
        # self.assertEqual(resp.status_code,200)
        # self.assertIn(self.a1, resp.context['random_mineral'])
        # self.assertIn(self.a2, resp.context['random_mineral'])


        response2 = self.client.get(self.random)
        self.assertEqual(response2.status_code, 200)
        self.assertTemplateUsed(response2, "rocks/random.html")




    def test_index_view(self):
        response3 = self.client.get(self.index)
        self.assertEqual(response3.status_code, 200)
        self.assertTemplateUsed(response3, "rocks/index.html")




