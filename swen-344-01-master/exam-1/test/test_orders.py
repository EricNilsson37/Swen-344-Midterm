import unittest
from src.orders import *
from src.swen344_db_utils import connect

class TestExam(unittest.TestCase):
    def setUp(self):
        """Setup"""
        rebuildTables()
        #print("Setup done")

    def test_tables(self):
        """Check existence of the tables"""
        result = exec_get_all('SELECT * FROM agents')
        self.assertNotEqual([], result, "no rows in agents table")
        result = exec_get_all('SELECT * FROM orders')
        self.assertNotEqual([], result, "no rows in orders table")
        #print("test_tables done")

    def test_a_print_des_order(self):
        print_des_order()

    def test_b_unique_customer(self):
        
        unique_customer()

    def test_c_avg_num_of_orders_placed(self):

        avg_num_of_orders_placed()

    def test_d_most_order_agent(self):

        most_order_agent()

    def test_e_agent_with_least_orders(self):

        agent_with_least_orders()
    
    def test_f_agent_with_highest_sales(self):

        agent_with_highest_sales()

    def test_g_agent_with_the_lowest_sales(self):

        agent_with_the_lowest_sales()
        
    def test_h_customer_spent_the_most(self):

        customer_spent_the_most()


    def test_i_city_with_most_orders(self):

        city_with_most_orders()

       
    def test_j_avg_commission(self):

        avg_commission()