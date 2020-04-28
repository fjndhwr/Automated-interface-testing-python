from web.url_utils import get, post
from utils.read_excel_util import read
from constans.file_constants import file_type
from utils.create_params import all_params
from web.ckeck_data import check_data
from utils.config import read_yaml
from utils.file_util import md
import time

import_list = read()
cf = read_yaml()


class test_class:
    def test_url(self):
        print("test start", time.strftime("%Y-%m-%d %H:%M:%S"))
        print("test is running,please wait a moment...")
        file = md()
        file.write("# 测试实验报告 \n")
        file.write("##### tester: " + cf.get('tester') + "\n")
        file.write("##### url: " + cf.get('url') + "\n")
        file.write("##### version: " + cf.get('version') + "\n")
        file.write("##### time: " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")

        for item in import_list:
            name = item[file_type['name']]
            path = item[file_type['path']]
            author = item[file_type['author']]
            if name == "":
                name = path
            if author == "":
                author = "undefined"

            file.write("### " + name + "\n")
            file.write("###### path:" + path + "\n")
            file.write("###### author: " + author + "\n")

            file.write("##### error \n")
            file.write("| params | error_msg |\n")
            file.write("| --- | --- | \n")

            params_list = all_params(item[file_type['params']])

            success_num = 0
            success_error_num = 0
            fail_num = 0
            fail_success_num = 0
            if item[file_type['method']] == 'get':
                for son_item in params_list:
                    data = get(path=item[file_type['path']], params=son_item)
                    back = check_data(data, item[file_type['error_msg']], item[file_type['result']])

                    if back['code'] == 400:
                        file.write("|" + str(son_item) + "|" + back['msg'] + "|\n")
                        fail_num += 1
                        fail_success_num += 1
                    elif back['code'] == 401:
                        file.write("|" + str(son_item) + "|" + back['msg'] + "|\n")
                        fail_num += 1
                    elif back['code'] == 201:
                        success_error_num += 1
                        success_num += 1
                    else:
                        success_num += 1
            else:
                success_num = 0
                fail_num = 0
                for son_item in params_list:
                    data = post(path=item[file_type['path']], params=son_item)
                    back = check_data(data, item[file_type['error_msg']], item[file_type['result']])

                    if back['code'] == 400:
                        file.write("|" + str(son_item) + "|" + back['msg'] + "|\n")
                        fail_num += 1
                        fail_success_num += 1
                    elif back['code'] == 401:
                        file.write("|" + str(son_item) + "|" + back['msg'] + "|\n")
                        fail_num += 1
                    elif back['code'] == 201:
                        success_error_num += 1
                        success_num += 1
                    else:
                        success_num += 1
                    time.sleep(3)
            file.write("###### 总结：\n")
            file.write("- 一共调用:" + len(params_list).__str__() + "次 \n")
            file.write("- 成功次数:" + success_num.__str__() + "次，")
            file.write("其中返回可预料的错误的次数:" + success_error_num.__str__() + "次，")
            file.write("真正成功的次数:" + (success_num - success_error_num).__str__() + "次。 \n")
            file.write("- 失败次数:" + fail_num.__str__() + "次，")
            file.write("其中成功调用但是参数的次数:" + fail_success_num.__str__() + "次，")
            file.write("报错次数:" + (fail_num - fail_success_num).__str__() + "次。 \n")
        print("test end")
        print("the test report output in ", cf["out_path"])
        file.close()
