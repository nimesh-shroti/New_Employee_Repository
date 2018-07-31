from address import Address


class Employee:
    def __init__(self,f_name, l_name,roll_num, age, addr_1,addr_2):
        self.f_name = f_name
        self.l_name = l_name
        self.roll_num = roll_num
        self.age = age

        address_1 = addr_1.split("|")
        address_2 = addr_2.split("|")

        self.addr_1 = Address(address_1[0],address_1[1],address_1[2],address_1[3],address_1[4])
        self.addr_2 = Address(address_2[0],address_2[1],address_2[2],address_2[3],address_2[4])

