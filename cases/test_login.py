# --coding:utf-8--

# Pytest测试框架
import datetime
import log

from time import sleep

import allure
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


@allure.feature('测试登录流程······ ')
class TestLogin:

    def setup_class(self):  # 每个测试用例执行前均执行以一边setUp方法
        desc = {}
        # desc["automationName"] = "uiautomator2" # 引入uiautomator2，用于定位toast
        desc["deviceName"] = "N8K5T16B18021779"
        desc["platformVersion"] = "9.0"
        desc["platformName"] = "Android"
        desc["appPackage"] = "com.kjjk.znyy.patient"
        desc["appActivity"] = "com.kjjk.znyy.patient.mvp.ui_re.activity.Others.FlashActivity"
        desc["unicodeKeyboard"] = "True"  # 使用unicode编码方式发送字符串
        desc["resetKeyboard"] = "True"  # 将键盘隐藏起来
        desc["noReset"] = "True"

        log.log.info("参数无误，准备启动APP......")
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desc)
        log.log.info("APP启动完成！！")
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        time_now = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d_%H%M%S')
        filename = "../images/tmp_" + time_now + ".png"
        self.driver.save_screenshot(filename)
        self.driver.quit()

    @allure.story('测试患者登录······')
    @allure.title("患者登录用例")
    def test_login(self):
        """
        用例描述：用于患者登录，若已登录，则直接判定登录手机号是否正确
        :return:
        """
        driver = self.driver
        log.log.info("登录>>>>>>>>")
        # driver.find_elements_by_id('com.kjjk.znyy.patient:id/tv_tab_title')[4].click()
        driver.find_element_by_android_uiautomator('new UiSelector().text("个人中心")').click()
        # driver.find_element_by_android_uiautomator('new UiSelector().textContains("个人")')  # 包含
        # driver.find_element_by_android_uiautomator('new UiSelector().textMatches("^个人.*")')  # 正则匹配，以“个人”开头的所有字符

        log.log.info("*********切换至个人中心**********\n")
        try:
            driver.find_element_by_id('com.kjjk.znyy.patient:id/et_phonenum_login').send_keys("17322275852")
            # el1 = driver.find_element_by_xpath('//android.widget.EditText[@text="请输入手机号码"]').send_keys("17322275852")

            driver.find_element_by_id('com.kjjk.znyy.patient:id/tv_get_sms_code').click()

            driver.find_element_by_id('com.kjjk.znyy.patient:id/et_sms_code').send_keys("123456")

            driver.find_element_by_id('com.kjjk.znyy.patient:id/btn_signin_login').click()

            log.log.info("**********登录成功**********\n")
            patient_phone_num = driver.find_element_by_id('com.kjjk.znyy.patient:id/textView2').text
            # self.assertEqual(patient_phone_num, "17322275852", "获取的手机号与登录的手机号不一致，请检查！")
            assert patient_phone_num == "17322275852", "获取的手机号与登录的手机号不一致，请检查！"

        except BaseException as e:
            print("这个一个报错获取：", e)
            patient_phone_num = driver.find_element_by_id('com.kjjk.znyy.patient:id/textView2').text
            # self.assertEqual(patient_phone_num, "17322275852", "获取的手机号与登录的手机号不一致，请检查！")
            assert patient_phone_num == "17322275852", "获取的手机号与登录的手机号不一致，请检查！"
