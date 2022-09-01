def dict2sql(table_name: str, table_data: dict):
    sql_express = f"INSERT INTO `{table_name}` ("
    for key in table_data.keys():
        sql_express += f"`{key}`, "
        print(sql_express)
    sql_express = sql_express.rstrip(", ")
    print(sql_express)
    sql_express += ") VALUE ("
    for val in table_data.values():
        sql_express += f"'{val}', "
    sql_express = sql_express.rstrip(", ")
    sql_express += ")"
    return sql_express


if __name__ == '__main__':
    # str1 = "     this is string example....wow!!!     ";
    # print(str1.lstrip());
    # str1 = "88888888this is string example....wow!!!8888888";
    # print(str1.lstrip('8'));
    mydata = {'name': 'austin', 'age': 18, 'address': 'Copenhagen'}

    print(dict2sql("person", mydata))
