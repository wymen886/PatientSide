# coding=utf-8
import sys
from imp import reload

reload(sys)
# sys.setdefaultencoding('utf8')

import os

command0 = 'adb shell ime list -s'
command1 = 'adb shell settings get secure default_input_method'
command2 = 'adb shell ime set com.baidu.input_huawei/.ImeService'
command3 = 'adb shell ime set io.appium.android.ime/.UnicodeIME'


# 列出系统现在所安装的所有输入法
# os.system(command0)
# 打印系统当前默认的输入法
# os.system(command1)
# 切换latin输入法为当前输入法
# os.system(command2)
# 切换appium输入法为当前输入法
# os.system(command3)

class InputMethod:

    # 切换latin输入法为当前输入法
    def enableLatinIME(self):
        os.system(command2)

        # 切换appium输入法为当前输入法

    def enableAppiumUnicodeIME(self):
        os.system(command3)
