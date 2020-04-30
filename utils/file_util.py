from utils.config import read_yaml
import time
import os

cf = read_yaml()


class md:
    fd = None

    def __init__(self):
        dirs = cf.get("out_path")
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        dirs += "测试报告+" + time.strftime("%Y.%m.%d+%H-%M-%S") + ".md"

        # self.fd = os.open(dirs + "test" + time.strftime("%Y-%m-%d %H:%M:%S") + ".md", os.O_WRONLY | os.O_CREAT)
        self.fd = open(dirs, mode="wb+")

    def write(self, text):
        self.fd.write(text.__str__().encode(encoding="utf-8", errors="strict"))

    def close(self):
        self.fd.close()

    def __del__(self):
        if self.fd is not None:
            print("关闭输出流")
            self.fd.close()
