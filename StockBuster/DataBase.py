import mysql.connector

my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    # database = "StockBuster"
)

my_cursor = my_db.cursor()

my_cursor.execute("DROP DATABASE StockBuster")

my_cursor.execute("CREATE DATABASE StockBuster")

my_cursor.execute("USE StockBuster")

my_cursor.execute(
    "CREATE TABLE inventory ( product_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, product VARCHAR(100) NOT NULL, nr_of_products INT NOT NULL)")
my_cursor.execute(
    "CREATE TABLE sales_history(product_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, product VARCHAR(100) NOT NULL, nr_of_products INT NOT NULL, timestamp_sale FLOAT)")

# populate the sale_history table
file = open('Sale_history.csv', 'r')
Lines = file.readlines()

count = 0

for line in Lines:
    if count >0:
        line= line[:-1]
        line=line.split(',')
        my_cursor.execute(" INSERT INTO sales_history(product,nr_of_products, timestamp_sale) VALUES(%s,%s,%s)",(line[0],line[1],line[2]))

    else:
        count+=1

# populate the inventory table
file2 = open('Inventory.csv', 'r')
Lines = file2.readlines()

count = 0

for line in Lines:
    if count >0:
        line= line[:-1]
        line=line.split(',')
        print(line[0], line[1])
        my_cursor.execute(" INSERT INTO inventory(product,nr_of_products) VALUES(%s,%s)",(line[0],line[1]))
    else:
        count+=1

my_db.commit()
print("Sale history:")
my_cursor.execute(" SELECT * FROM sales_history")
for x in my_cursor:
    print(x)

print("Inventory:")
my_cursor.execute(" SELECT * FROM inventory")
for x in my_cursor:
    print(x)
