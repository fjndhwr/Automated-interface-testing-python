import copy
from utils.random_utils import get_code
import json


def all_params(params):
    params = json.loads(params)
    params_list = []
    self_params(params_list, params)
    none_params(params_list)
    random_params(params_list)
    return params_list


def self_params(params_list, params):
    son_params = {}
    params_list.append(son_params)
    for key in params.keys():
        item_value = params[key]
        if type(item_value) is str:
            value_list = item_value.split('#')
            temp_params_list = []
            for value in value_list:
                copy_list = copy.deepcopy(params_list)
                for item in copy_list:
                    item[key] = value
                temp_params_list += copy_list
            params_list.clear()
            params_list += temp_params_list
        else:
            for item in params_list:
                item[key] = item_value


def none_params(params_list):
    params = params_list[0]
    for key in params.keys():
        temp = copy.deepcopy(params)
        if not temp[key] is None:
            temp[key] = None
            params_list.append(temp)


def random_params(params_list):
    params = params_list[0]
    for i in range(10):
        temp = copy.deepcopy(params)
        for key in params.keys():
            if not temp[key] is None and type(temp[key]) is str:
                temp[key] = get_code()
        params_list.append(temp)
