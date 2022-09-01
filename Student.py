class StudentInfo:

    def __init__(self, name, age, sex, address):
        self.name = name
        self.age = age
        self.sex = sex
        self.address = address

    def __str__(self):
        return f'姓名:{self.name},年龄:{self.age},性别:{self.sex},地址:{self.address}'


if __name__ == '__main__':
    stu = StudentInfo('张三', 22, '男', '地球')
    print(stu)
