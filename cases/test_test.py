# --coding:utf-8--

# Pytest测试框架
import allure

class TestPatientSide:

    @allure.testcase("https://www.baidu.com")
    def test_case1(self):
        assert 1 == 2, "两者不等"

    @allure.testcase("https://ceshiren.com/t/topic/5399")
    def test_case2(self):
        assert 6 == 6, "两者不等"
