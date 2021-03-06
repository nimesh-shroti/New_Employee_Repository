from db.Employee_dao import EmployeeDao
from mappers.csv_mapper import CSVMapper


class Controller:

    def __init__(self):
        self.dao = EmployeeDao()  ## creating instance of dao layer here...

    def start_processing(self):
        employees = CSVMapper.map("names.csv")
        # print(file_content_list)

        self.dao.insert_data(employees)


#ctrl + alt + l :: format code
#ctrl + alt + o :: optimized import