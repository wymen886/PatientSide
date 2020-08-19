# --coding:utf-8--

# Pytest测试框架
import datetime
import log

from time import sleep

import allure
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


@allure.feature('测试商城流程······ ')
class TestStore:
    order_num = ''

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

    # def teardown(self):
    #     for i in range(3):
    #         self.driver.back()

    @allure.story("测试商城搜索功能······")
    @allure.title("商品搜索用例")
    def test_drugSearch(self):
        """
        用例描述：测试商品搜索功能。
        :return:
        """
        driver = self.driver
        driver.find_element_by_xpath('//*[@text="商城"]').click()

        log.log.info("*********切换至商城**********\n")

        # driver.find_element_by_xpath('//*[@text="云南白药泰邦"]').click()

        log.log.info("正在搜索商品“痛经暖贴”......")
        driver.find_element_by_id('com.kjjk.znyy.patient:id/layout_to_search_re_main_store').click()
        driver.activate_ime_engine('io.appium.android.ime/.UnicodeIME')
        driver.find_element_by_id('com.kjjk.znyy.patient:id/et_search').send_keys("痛经暖贴")
        driver.find_element_by_id('com.kjjk.znyy.patient:id/tv_cancle').click()

        drug_name = driver.find_element_by_xpath('//*[contains(@text,"泰邦 痛经暖贴")]').text

        assert drug_name == "云南白药泰邦 痛经暖贴 130mm*95mm"
        log.log.info("商品搜索成功！")

    @allure.story("测试商城支付功能······")
    @allure.title("商城支付用例")
    def test_pay(self):
        """
        用例描述：测试商品支付功能。
        :return:
        """
        driver = self.driver

        driver.find_element_by_xpath('//*[contains(@text,"泰邦 痛经暖贴")]').click()
        sleep(2)
        log.log.info("**********进入商品详情页*********\n")
        driver.find_element_by_xpath('//*[@resource-id="com.kjjk.znyy.patient:id/tv_buy_now"][@text="立即购买"]').click()

        sleep(2)
        driver.find_element_by_xpath('//*[@resource-id="com.kjjk.znyy.patient:id/buy"][@text="确定"]').click()

        log.log.info("*********订单确认！将提交订单。。。**********\n")

        sleep(2)
        print(driver.page_source)
        driver.find_element_by_xpath('//*[@resource-id="com.kjjk.znyy.patient:id/tv_submit"][@text="提交订单"]').click()

        # print(driver.page_source)
        # toast = driver.find_element_by_xpath('//*[@class = "android.widget.Toast"]').text
        # print(toast)

        log.log.info("*********提交订单完成！**********\n")
        driver.find_element_by_xpath('//*[@resource-id="com.kjjk.znyy.patient:id/btn_pay"][@text="立即支付"]').click()

        log.log.info("*********支付金额确认界面**********\n")

        sleep(3)
        driver.find_elements_by_class_name('android.widget.ImageView')[1].click()
        # driver.find_elements_by_xpath('//*[@class="android.widget.ImageView"]')[1].click()
        log.log.info("输入密码完成支付......")
        driver.press_keycode(8)  # 1
        driver.press_keycode(10)  # 3
        driver.press_keycode(12)  # 5
        driver.press_keycode(9)  # 2
        driver.press_keycode(11)  # 4
        driver.press_keycode(13)  # 6

        sleep(2)
        driver.find_elements_by_class_name('android.widget.ImageView')[0].click()

        driver.find_element_by_id('com.kjjk.znyy.patient:id/tv_show_order').click()

        global order_num
        order_num = driver.find_element_by_id('com.kjjk.znyy.patient:id/tv_order_id').text
        log.log.info('pay获取的值:', order_num)

        order_status = driver.find_element_by_id('com.kjjk.znyy.patient:id/tv_order_state').text
        # self.assertEqual(order_status, "待发货", "订单状态异常，请检查，当前的订单状态为：" + order_status)
        assert order_status == "待发货", "订单状态异常，请检查，当前的订单状态为：" + order_status

        # 返回APP首页
        for i in range(4):
            driver.back()

    @allure.story('测试商城退款功能······')
    @allure.title("商城退款用例")
    def test_refund(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@text="个人中心"]').click()
        driver.find_element_by_xpath('//*[@text="商城订单"]').click()
        global order_num
        order_id = order_num
        driver.find_element_by_xpath(f'//*[contains(@text,"{order_id}")]').click()
        # driver.find_element(MobileBy.XPATH, f"//*[contains(@text,'{order_id}')]").click()
        driver.find_element_by_id('com.kjjk.znyy.patient:id/tv_refund').click()
        driver.find_elements_by_class_name('android.widget.ImageView')[1].click()
        driver.find_element_by_id('com.kjjk.znyy.patient:id/rb2_order_cancel').click()  # 选择退款原因：订单信息有误
        driver.find_element_by_id('com.kjjk.znyy.patient:id/btn_cancel_submit').click()

        driver.find_element_by_id('com.kjjk.znyy.patient:id/tv_refund').click()

        order_status = driver.find_element_by_id('com.kjjk.znyy.patient:id/tv_order_state').text

        assert order_status == "退款中", "订单状态异常，请检查，当前的订单状态为：" + order_status
        driver.back()
        sleep(45)

        # 获取手机屏幕尺寸
        x = driver.get_window_size()['height']
        y = driver.get_window_size()['width']

        # 计算下拉坐标的开始和结束值
        sx = x * 0.35
        sy = y * 0.50
        ex = 0
        ey = y

        # 下拉刷新
        driver.swipe(sx, sy, ex, ey, 1000)

        driver.find_element_by_xpath(f'//*[contains(@text,"{order_id}")]').click()
        order_status = driver.find_element_by_id('com.kjjk.znyy.patient:id/tv_order_state').text
        assert order_status == "退款完成", "订单状态异常，请检查，当前的订单状态为：" + order_status