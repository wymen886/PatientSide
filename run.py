# --coding:utf-8--

import pytest

'''
–cov参数 后面接的是测试的目录 （经给测试，不能指定某个特定的文件。），程序代码跟测试脚本必须在同一个文件下。 
--cov-report=html 生成报告 ，只需要python run.py 就可以运行
'''

if __name__ == '__main__':
	pytest.main(["--cov=./cases/"])