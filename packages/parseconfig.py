# --coding:utf-8--

from configobj import ConfigObj


class parseConfig():
    def __init__(self, section, config_dir):
        """
        :param section: ini文件的主题
        :param config_dir: ini文件的路径
        """
        self.file = config_dir
        self.section = section
        self.configfile = ConfigObj(self.file, encoding='utf-8')

    def get_all_sections(self):
        # 获取所有的section
        return self.configfile.sections

    def get_all_options(self):
        # 获取指定的section内容
        return self.configfile[self.section]

    def split_content(self, option):
        # 拆解对应的数据
        section = self.section
        try:
            xpath_result = self.configfile[section][option]
            if '$' in xpath_result:
                xpath_result = self.configfile[section][xpath_result]
            if '>>' in xpath_result:
                return xpath_result.split('>>')
            else:
                return ['By.XPATH', xpath_result]  # 默认xpath格式
        except Exception as  e:
            print('error', e)


if __name__ == '__main__':
    value = parseConfig('test_baidu')
    print(value)

    # print (value.get_all_sections())
    # print (value.get_all_options())
    print(value.split_content('设置'))