from src.swen344_db_utils import *

def print_des_order():
    print("Question 1: Customer that is attached to Agent in Decsending order")

    list_of_agents = exec_get_all('SELECT * FROM agents ORDER BY agent_name DESC')
    list_of_cust = exec_get_all('SELECT * FROM customers ORDER BY agent_code DESC')

    for agent in list_of_agents:
        for cust in list_of_cust:
            if(agent[0]==cust[5]):
                current_agent = cust[1]
        print(agent[1],',', current_agent)

def unique_customer():
    
    num_of_customers = exec_get_all('SELECT COUNT(DISTINCT cust_code) FROM customers')

    num = num_of_customers[0][0]

    print("")
    print("Question 2: Number of Unique Customers:", num)

def avg_num_of_orders_placed():

    avg_num = exec_get_all('SELECT ROUND(AVG(ord_amount),2) FROM orders')

    print("")
    print("Question 3: Average order amount placed:", avg_num[0][0])

def most_order_agent():

    list_of_orders = exec_get_all('SELECT * FROM orders')
    list_of_agents = exec_get_all('SELECT * FROM agents')

    num_of_orders = 0
    max_order = 0
    agent_name =""

    for agent in list_of_agents:
        num_of_orders = 0
        for order in list_of_orders:
            if(agent[0]==order[5]):
                num_of_orders += 1
        if(max_order <num_of_orders):
            max_order = num_of_orders
            agent_name = agent[1]

    print("")
    print("Question 4: Agent with the most orders:", agent_name ,"-",max_order,"orders" )

def agent_with_least_orders():

    list_of_orders = exec_get_all('SELECT * FROM orders ORDER BY ord_amount DESC')
    list_of_agents = exec_get_all('SELECT * FROM agents')

    num_of_orders = 0
    lowest_order = 0
    agent_name =""

    for agent in list_of_agents:
        num_of_orders = 0
        for order in list_of_orders:
            if(agent[0]==order[5]):
                num_of_orders += 1
        if(num_of_orders < lowest_order and lowest_order != 0):
            lowest_order = num_of_orders
            agent_name = agent[1]
        elif(lowest_order == 0):
            lowest_order = num_of_orders

    print("")
    print("Question 5: Agent with the lowest orders:", agent_name ,"-",lowest_order,"order" )


def agent_with_highest_sales():

    list_of_orders = exec_get_all('SELECT * FROM orders ORDER BY ord_amount DESC')
    list_of_agents = exec_get_all('SELECT * FROM agents')

    order_value = 0
    highest_order_value = 0
    agent_name =""

    for agent in list_of_agents:
        order_value = 0
        for order in list_of_orders:
            if(agent[0]==order[5]):
                order_value +=order[1]
        if(order_value > highest_order_value):
            highest_order_value = order_value
            agent_name = agent[1]

    print("")
    print("Question 6: Agent with the highest amount of sales:", agent_name ,"- $",highest_order_value)

def agent_with_the_lowest_sales():

    list_of_orders = exec_get_all('SELECT * FROM orders ORDER BY ord_amount DESC')
    list_of_agents = exec_get_all('SELECT * FROM agents')

    order_value = 0
    lowest_order_value = 0
    agent_name =""

    for agent in list_of_agents:
        order_value = 0
        for order in list_of_orders:
            if(agent[0]==order[5]):
                order_value += order[1]
        if(order_value < lowest_order_value and lowest_order_value != 0):
            lowest_order_value = order_value
            agent_name = agent[1]
        elif(lowest_order_value == 0):
            lowest_order_value = order_value

    print("")
    print("Question 7: Agent with the lowest amount of sales:", agent_name ,"- $",lowest_order_value)

    
def customer_spent_the_most():

    list_of_orders = exec_get_all('SELECT * FROM orders ORDER BY ord_amount DESC')
    list_of_customers = exec_get_all('SELECT * FROM customers')

    current_value = 0
    highest_value = 0
    customer_name =""

    for customer in list_of_customers:
        current_value = 0
        for order in list_of_orders:
            if(customer[0]==order[4]):
                current_value += order[1]
        if(current_value > highest_value ):
            highest_value = current_value
            customer_name = customer[1]
        

    print("")
    print("Question 8: Customer that spent the most:", customer_name ,"- $", highest_value)


def city_with_most_orders():

    list_of_city = exec_get_all('SELECT customers.cust_city, COUNT(orders.ord_num)\
    FROM customers INNER JOIN orders ON customers.cust_code = orders.cust_code \
    GROUP BY customers.cust_city \
    ORDER BY COUNT(orders.ord_num) DESC')

    highest_num = list_of_city[0][1]
    highest_city = list_of_city[0][0]

    print("")
    print("Question 9: City that order the most times:", highest_city, "orderd:", highest_num, "times")

def avg_commission():

    avg = exec_get_all('SELECT ROUND(AVG(orders.ord_amount * agents.commission), 2)\
    FROM agents INNER JOIN orders ON agents.agent_code = orders.agent_code')

    min_coms = exec_get_all('SELECT ROUND(MIN(orders.ord_amount * agents.commission), 2)\
    FROM agents INNER JOIN orders ON agents.agent_code = orders.agent_code')

    max_coms = exec_get_all('SELECT ROUND(MAX(orders.ord_amount * agents.commission), 2)\
    FROM agents INNER JOIN orders ON agents.agent_code = orders.agent_code')

    avg_num = avg[0][0]
    min_num = min_coms[0][0]
    max_num = max_coms[0][0]

    print("")
    print("Question 10: Average commssion is: - $", avg_num, "min: - $", min_num, "max: - $", max_num)

def rebuildTables():
    #exec_commit("DROP TABLE IF EXISTS ORDERS")
    #exec_commit("DROP TABLE IF EXISTS CUSTOMERS")
    #exec_commit("DROP TABLE IF EXISTS ORDERS")
    exec_sql_file('./orders_system.sql')