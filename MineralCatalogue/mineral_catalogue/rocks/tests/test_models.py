from django.urls import reverse
from django.test import TestCase, Client
from rocks.models import Mineral
from django.utils import timezone




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
