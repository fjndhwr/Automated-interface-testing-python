import xlrd
import json
from constans.file_constants import file_type


def read():
    try:
       data = xlrd.open_workbook("test.xlsx")
    except:
        print("读取测试用例异常关闭程序")
        exit()
    return check_data(data)


def check_data(data):
    if data is None:
        print("导入数据为空关闭程序")
    table = data.sheets()[0]
    nrows = table.nrows

    if nrows < 2:
        print("导入数据为空关闭程序")

    result = []
    for i in range(nrows):
        row_values = table.row_values(i)
        if i == 0:
            if not row_values[file_type['path']] == 'path' and row_values[file_type['params']] == 'params' \
                    and row_values[file_type['method']] == 'method' and row_values[file_type['return']] == 'return' \
                    and row_values[file_type['error_msg']] == 'error_msg' and row_values[file_type['name']] == 'name'\
                    and row_values[file_type['author']] == 'author':
                print("excel格式不正确关闭程序")
                exit()
        else:
            if not is_json(row_values[file_type['params']]) is dict:
                print("第", i+1, "行params格式不正确")
                continue
            if not row_values[file_type['method']] == 'post' and not row_values[file_type['method']] == 'get':
                print("第", i+1, "行method格式不正确")
                continue
            if not is_json(row_values[file_type['result']]) is dict:
                print("第", i + 1, "行result格式不正确")
                continue
            if not row_values[file_type['error_msg']] == "" and not is_json(row_values[file_type['error_msg']]) is list:
                print("第", i + 1, "行error_msg格式不正确")
                continue
            result.append(row_values)
    return result


def is_json(str):
    try:
        return type(json.loads(str))
    except:
        return int
