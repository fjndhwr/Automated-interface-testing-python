import json
import traceback


def check_data(data, error_msg, result):
    back = {
        "code": 200,
        "msg": ""
    }
    msg = ""
    try:
        result = json.loads(result)
        error_msg = json.loads(error_msg)
        if data['code'] == 200:
            if type(data) is list:
                data = data[0]
            for key in result.keys():
                if data.get(key) is None:
                    if key in data:
                        continue
                    back["code"] = 400
                    msg += key + "字段未返回,"
                elif type(data[key]) is dict and type(data[key]) is type(result[key]):
                    msg += key + ":{" + check_dict(data[key], result[key], msg, back) + "}"
                elif type(data[key]) is list:
                    if len(data[key]) > 0 and type(data[key][0]) is type(result[key][0]):
                        msg += key + ":{" + check_dict(data[key][0], result[key][0], msg, back) + "}"
                elif not type(data[key]).__name__ == result[key]:
                    back["code"] = 400
                    msg += key + ":" + "返回类型不匹配,"
        else:
            if not exist_in_error_msg(error_msg, data["msg"]):
                back["code"] = 401
                msg += "报错：" + data["msg"] + ","
            else:
                back["code"] = 201
        if len(data) > len(result):
            msg += "多返回参数,"
    except Exception:
        print('traceback.format_exc():\n%s' % traceback.format_exc())

    back['msg'] = msg
    return back


def exist_in_error_msg(error_msg, msg):
    for item in error_msg:
        if msg == item:
            return True
    return False


def check_dict(value, result, msg, back):
    for key in result.keys():
        if value.get(key) is None:
            back["code"] = 400
            msg += key + "字段未返回,"
        elif type(value[key]) is dict and type(value[key]) is type(result[key]):
            msg += key + ":{" + check_dict(value[key], result[key], msg, back) + "}"
        elif type(value[key]) is list:
            if len(value[key]) > 0 and type(value[key][0]) is type(result[key][0]):
                msg += key + ":{" + check_dict(value[key][0], result[key][0], msg, back) + "}"
        elif not type(value[key]).__name__ == result[key]:
            back["code"] = 400
            msg += key + "返回类型不匹配,"
    return msg
