"""
    完成登录业务层实现
"""

# 导包 unittest ApiLogin
import unittest
from api.api_login import ApiLogin
from parameterized import parameterized
from tools.read_json import ReadJson

# 读取数据函数
def get_data():
    data = ReadJson("login.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                data.get("mobile"),
                data.get("code"),
                data.get("expect_result"),
                data.get("status_code")))
    return arrs

# 新建测试类
class TestLogin(unittest.TestCase):
    # 新建测试方法
    @parameterized.expand(get_data())
    def test_login(self, url, mobile, code, expect_result, status_code):
        # 暂时存放数据 url mobile code
        # url = "http://ttapi.research.itcast.cn/app/v1_0/authorizations"
        # mobile = "18717852993"
        # code = "419104"

        # 调用登录方法
        s = ApiLogin().api_post_login(url, mobile, code)

        # 调试使用
        print(s.json())

        # 断言 响应信息 及 状态码
        self.assertEqual(expect_result, s.json()['message'])

        # 断言响应状态码
        self.assertEqual(status_code, s.status_code)


# 获取验证码code
# "http://ttapi.research.itcast.cn/app/v1_0/sms/codes/18717852993"

if __name__ == '__main__':
    unittest.main()

# token:
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTMxNjI4NzAsInVzZXJfaWQiOjEyNzY0MTI0MDk4MDM3MDIyNzIsInJlZnJlc2giOmZhbHNlfQ.iOn0cmnea_cLxpY-4QUUuplQnr4XOBRmMmfTo1Nqrh0