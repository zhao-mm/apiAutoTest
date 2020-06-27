import json

class ReadJson(object):

    def __init__(self, filename):
        self.filepath = "../data/" + filename

    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8-sig") as f:
            # 调用load方法加载文件流
            return json.load(f)