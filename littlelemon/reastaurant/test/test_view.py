from django.test import TestCase
from reastaurant.models import Menu
from django.core import serializers


class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(Title='food_one', Price='10.99', Inventory=5)
        self.item2 = Menu.objects.create(Title='food_two', Price='12.99', Inventory=10)
        self.item3 = Menu.objects.create(Title='food_tree', Price='5.99', Inventory=15)




    def test_get_all_menu(self):
        food_one = Menu.objects.get(Title='food_one')
        food_two = Menu.objects.get(Title='food_two')
        food_tree = Menu.objects.get(Title='food_tree')

        self.assertEqual(str(food_one), 'food_one : 13.00')
        self.assertEqual(str(food_two), 'food_two : 17.00')
        self.assertEqual(str(food_tree), 'food_tree : 10.00')

