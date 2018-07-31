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

    print(file_content_list)

insert_into(file_content_list)