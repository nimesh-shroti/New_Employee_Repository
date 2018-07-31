from db.Employee_dao import insert_into
from employee import Employee


if __name__ == '__main__':
    myfile = open("names.csv")
    row_content = myfile.read()
    print(row_content)
    rows = row_content.splitlines()
    print(rows)

    file_content_list = []

    for row in rows:
        data = row.split(",")
        employee = Employee(data[0],data[1],data[2],data[3],data[4],data[5])

        file_content_list.append(employee)

    print(file_content_list[1].addr_1.address_line_1)

insert_into(file_content_list)








































# from address import Address
# from employee import Employee
#
#
# if __name__ == '__main__':
#     # st1 = "name,l_name,age, addr_line_1, addr_line_2,city, pin_code,country"
#     st1 = "Nimesh,Shroti,25, flat 101 vaishnavi park, viman nagar,Pune, 411014,IND"
#     emp_arr = st1.split(",")
#     print(emp_arr[0])
#     print(emp_arr[7])
#     addr = Address(emp_arr[3],emp_arr[4],emp_arr[5],emp_arr[6],emp_arr[7])
#     emp = Employee(emp_arr[0], emp_arr[1], emp_arr[2], addr)
#
#
#     myfile = open("names.csv")
#     row_content = myfile.read()
#     rows = row_content.splitlines()
#
#     employees = []
#     l = []
#
#     # employees.append(l)
#     for row_data in rows:
#         data = row_data.split(",")
#         print(data)
#         addr = Address(data[3], data[4], data[5], data[6], data[7])
#         emp = Employee(data[0], data[1], data[2], addr)
#         employees.append(emp)
#
#     print(employees)
#
#     for emp in employees:
#         print(emp)
#         print("heheh....")
#
#     csv = "WXY,ZZ,25, flat 101 vaishnavi park|viman nagar|Pune|411017|IND,flat 101 vaishnavi park|viman nagar|Pune|411017|IND,flat 101 vaishnavi park|viman nagar|Pune|411017|IND"
#
#     emp_arr = csv.split(",")
#
#     print(emp_arr)
#
#     addr_1 = emp_arr[3].split("|")
#     addr_2 = emp_arr[4].split("|")
#
#     addresses = []
#     addrObj1 =  Address(addr_1[0], addr_1[1], addr_1[2], addr_1[3], addr_1[4])
#     addrObj2 =  Address(addr_2[0], addr_2[1], addr_2[2], addr_2[3], addr_2[4])
#
#     addresses.append(addrObj1)
#     addresses.append(addrObj2)
#
#     emp = Employee(emp_arr[0], emp_arr[1], emp_arr[2], addresses)
#
#     print(emp)