import unittest
from unittest.mock import patch
from main.MainModule import MainModule
from Entity.Customer import Customer
from Entity.Product import Product
from myExceptions.myExceptions import ProductNotFoundException, CustomerNotFoundException


class TestOrderProcessor(unittest.TestCase):

    def setUp(self):
        self.main_module = MainModule()

    @patch('builtins.input', side_effect=["Test Product", 100, "Test Description", 50])
    def test_create_product(self, mock_inputs):
        self.assertTrue(self.main_module.service.create_product(Product()))

    @patch('builtins.input', side_effect=["Test Customer", "test@test.com", "password"])
    def test_create_customer(self, mock_inputs):
        self.assertTrue(self.main_module.service.create_customer(Customer()))

    def test_delete_product(self):
        # Assuming there's a product with ID 1 in the database
        self.assertTrue(self.main_module.service.delete_product(1))

        # Testing ProductNotFoundException
        with self.assertRaises(ProductNotFoundException):
            self.main_module.service.delete_product(9999)  # Assuming ID 9999 doesn't exist

    def test_delete_customer(self):
        # Assuming there's a customer with ID 1 in the database
        self.assertTrue(self.main_module.service.delete_customer(1))

        # Testing CustomerNotFoundException
        with self.assertRaises(CustomerNotFoundException):
            self.main_module.service.delete_customer(9999)  # Assuming ID 9999 doesn't exist

    @patch('builtins.input', side_effect=["1", "1", "5"])
    def test_add_to_cart(self, mock_inputs):
        # Assuming customer ID 1 and product ID 1 exist in the database
        self.assertTrue(self.main_module.service.add_to_cart(Customer(), Product(), 5))

    @patch('builtins.input', side_effect=["1", "1", "5"])
    def test_remove_from_cart(self, mock_inputs):
        # Assuming customer ID 1 and product ID 1 exist in the database
        self.assertTrue(self.main_module.service.remove_from_cart(Customer(), Product()))

    def test_place_order(self):
        # Assuming customer ID 1 and product ID 1 exist in the database
        self.assertTrue(self.main_module.service.place_order(Customer(), [{"product": Product(), "quantity": 5}]))

    def test_get_orders_by_customer(self):
        # Assuming customer ID 1 exists in the database
        self.assertIsNotNone(self.main_module.service.get_orders_by_customer(1))


if __name__ == '__main__':
    unittest.main()
