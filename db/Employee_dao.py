def insert_into(file_content_list):
    Query = "INSERT INTO EMPLOYEE () VALUES ('"


    for emp in file_content_list:
        Query += emp.f_name + "','" + emp.l_name  + "','" + emp.roll_num + "','" + emp.age + "','" + str(emp.addr_1.address_line_1) + " ," + str(emp.addr_1.address_line_2) + " ," + \
                 str(emp.addr_1.city) + " ," + str(emp.addr_1.zip_code) + " ," + str(emp.addr_1.country) + "','" + str(emp.addr_2.address_line_1) + " ," + str(emp.addr_2.address_line_2) + " ," + \
                 str(emp.addr_2.city)  + " ," + str(emp.addr_2.zip_code) + "," + str(emp.addr_2.country) + "' )"
        print(Query)