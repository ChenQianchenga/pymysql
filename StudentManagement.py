from Studentmanagement.mysqlutil import MysqlUtil


class StudentManagement:
    def __init__(self):
        self.util = MysqlUtil('127.0.0.1', 3306, 'root', 'root', 'student_management', 'utf8')

    def menum(self):
        print('学生信息管理系统'.center(30, '='))  # 字符串的居中操作,长度20,填充'='
        print('功能菜单'.center(30, '-'))
        print('1.录入学生信息'.center(25, ' '))
        print('2.查找学生信息'.center(25, ' '))
        print('3.删除学生信息'.center(25, ' '))
        print('4.修改学生信息'.center(25, ' '))
        print('5.统计学生总人数'.center(27, ' '))
        print('6.显示所有学生信息'.center(28, ' '))
        print('0.退出系统'.center(23, ' '))
        print('功能菜单'.center(30, '-'))

    def main(self):
        while True:
            self.menum()  # 显示菜单
            choice = int(input("请选择操作"))
            if choice in [0, 1, 2, 3, 4, 5, 6]:
                if choice == 0:
                    answer = input('您确定要退出系统吗?y/n')  # 输入的时候会有异常
                    if answer == 'y' or answer == 'Y':
                        print('谢谢您的使用')
                        self.util.close()
                        break  # 退出系统
                    else:
                        continue
                elif choice == 1:
                    self.insert()
                elif choice == 2:
                    self.search()
                elif choice == 3:
                    self.delete()
                elif choice == 4:
                    self.modify()
                elif choice == 5:
                    self.total()
                elif choice == 6:
                    self.show()

    def insert(self):
        name = input('请输入姓名:')
        age = int(input('请输入年龄:'))
        sex = input('请输入性别:')
        address = input('请输入家庭地址:')
        self.util.update('insert into student_info values(%s,%s,%s,%s)', (name, age, sex, address))

    def search(self):
        name = input('请输入你要查找人的姓名:')
        result = self.util.query('select * from student_info where name=%s', name)
        # 如果结果为空,输出没有此人
        print(result)

    def delete(self):
        name = input('请输入你要删除人的姓名:')
        self.util.update('delete from student_info where name=%s', name)
        # print(a)

    def modify(self):
        name_old = input('请输入你要修改人的姓名:')
        # 判断人是否存在,存在开始修改,否者提示没有改学生
        print('开始修改!')
        name_new = input('请输入姓名:')
        age = int(input('请输入年龄:'))
        sex = input('请输入性别:')
        address = input('请输入家庭地址:')
        self.util.update('update student_info set name=%s,age=%s,sex=%s,address=%s where name=%s',
                         (name_new, age, sex, address, name_old))

    def total(self):
        result = self.util.query('select * from student_info')
        print(f'一共有{len(result)}人')

    def show(self):
        result = self.util.query('select * from student_info')
        print(result)

    def close(self):
        self.util.close()


if __name__ == '__main__':
    studentManagement = StudentManagement()
    studentManagement.main()
