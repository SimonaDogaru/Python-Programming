import mysql.connector
import math
from datetime import datetime

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="StocKBuster"
)

my_cursor = my_db.cursor()



def stock_buster(nr_of_days):

    produs_perday=[]
    my_cursor.execute(
        "SELECT product, SUM(nr_of_products) sum_products, MIN(timestamp_sale) first_sale_day FROM sales_history group by product;")
    for item in my_cursor:
        # calculez numarul de zile de la prima vanzare a unui produs pana in trezent -- aceste calum ma va ajuta sa stiu cate produse se vand pe zi
        data = datetime.fromtimestamp(item[2])
        day_diference=(datetime.now()-data).days
        result= item[1]/day_diference
        # rotunjec result la doua zecimale - usurarea calculelor
        result = round(result, 2)
        # to make sure that are enough products
        if (result<0.5):
            result =0.5
        else:
            result =  math.ceil(result)
        produs_perday.append((item[0],result))

    inventory = []
    my_cursor.execute("SELECT product, nr_of_products FROM inventory;")
    for item in my_cursor:
        inventory.append(item)

    #initializarea listei de comenzi
    products_command = []
    for item in produs_perday:
        products_command.append((item[0], int(item[1]*nr_of_days)))

    # actualizarea noului inventar - luand in considerare si intervalul prezent
    products_name = [item[0] for item in products_command]
    for item in inventory:
        if item[0] in products_name:
            index_produs=products_name.index(item[0])
            if item[1] > products_command[index_produs][1]:
                products_command[index_produs] = (item[0], 0)
            else:
                products_command[index_produs] = (item[0], products_command[index_produs][1] - item[1])
        else:
            products_command.append((item[0],0))
    return products_command


if __name__ == "__main__":
    # make it to have 3 tries before
    tries=3
    print("*************************************")
    print("*** Perioada trebuie data in zile ***")
    print("*************************************")
    while tries:
        try:
            nr_of_days = int(input("Perioada pentru care se va realiza comanda este :"))
        except:
            print("\nTe rugam, oferane un numar de zile valid!\n")
            tries-=1
        else:
            result = stock_buster(nr_of_days)
            print("Comanda urmatoare:")
            for item in result:
                print(f"Produs: {item[0]} -- cantintate: {item[1]}")
            break

    # date_string = "27 November, 2022"
    # print("date_string =", date_string)
    #
    # date_object = datetime.strptime(date_string, "%d %B, %Y")
    # timestamp = datetime.timestamp(date_object)
    # print("timestamp =", timestamp)

