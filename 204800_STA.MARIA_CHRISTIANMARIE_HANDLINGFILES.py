products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    return products[code]


def get_property(code,property):
    return get_product(code)[property]


def main():
    dict_total = {}
    order_list = []

    # input loop:
    session_term = "Y"
    while session_term == "Y":
        code_n_qty = input("Enter product code and quantity (enter / to terminate the session): ")
        if code_n_qty == "/":
            session_term = "N"
            break
        else:
            order = list(code_n_qty.split(","))
            product_code = order[0]
            quantity = int(order[1])
            subtotal = (get_property(product_code,"price") * quantity)

            # check if key exists in dict_total
            if product_code in order_list:
                new_quantity = dict_total[product_code]["quantity"]
                dict_total[product_code]["quantity"]=(quantity+new_quantity)
                new_subtotal = dict_total[product_code]["subtotal"]
                dict_total[product_code]["subtotal"]=(subtotal+new_subtotal)
            else:
                order_list.append(product_code)
                # append to dict: product_code:{get_property(product_code,"name"), quantity, subtotal}
                dict_total[product_code]={"name":get_property(product_code,"name"),"quantity":quantity,"subtotal":subtotal}

    # total:
    total = 0
    for i in order_list:
        total += (get_product(i)["price"] * dict_total[i]["quantity"])

    # receipt file:
    order_list.sort()
    fheader = """==
CODE\t\t\t\t\t\tNAME\t\t\t\t\t\t\tQUANTITY\t\t\tSUBTOTAL"""
    ftotal="""
\nTotal:\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{}
=="""
    with open("receipt.txt","w+") as f:
        forder = """"""
        for i in order_list:
            forder += f'\n{i:<15} {dict_total[i]["name"]:<17} {dict_total[i]["quantity"]:<13} {dict_total[i]["subtotal"]}'  # source 1
        fcontents = fheader + forder + ftotal.format(total)
        f.write(fcontents)


main()
