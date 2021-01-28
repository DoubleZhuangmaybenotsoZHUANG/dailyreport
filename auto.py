# 需要准备部分：
# 1.谷歌浏览器以及对应版本的chromedrive.exe文件
# 2.python环境并安装selenium依赖 pip insatll selenium

#注意：目前所在地默认为上海地区，其他地区需要自行改动Xpat


from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

#对应版本的chromedriver.exe的路径
wd = webdriver.Chrome(r'xx\chromedriver.exe')
wd.implicitly_wait(10)
#账号
user = 'xxxxxxxxx'
#密码
password = 'xxxxxx'

def get_system(wd):
    # 进入登录页面
    print("正在进入页面")
    wd.get('https://cas.paas.lixin.edu.cn/cas/login?service=https://portal-theme.paas.lixin.edu.cn/')
    # 输入用户名密码，登录
    wd.find_element_by_id('username').send_keys(user)
    wd.find_element_by_id('password').send_keys(password)
    wd.find_element_by_name('submit').click()
    # 找到每日一报
    time.sleep(1)
    wd.find_element_by_xpath("//span[text()='校园生活']/following-sibling::b").click()
    wd.find_element_by_xpath("//span[@class='vertical_app-name' and text()='每日一报']").click()
    # 切换窗口
    handles = wd.window_handles
    for handle in handles:
        wd.switch_to.window(handle)
        if wd.title == "我的填报": break

    # 点击新建
    wd.find_element_by_id('dw_nBtn').click()

    # 切换iframe
    wd.switch_to.frame('side_dw_m_page_frame')

    # 修改信息，并提交
    wd.find_element_by_xpath("//label[text()='健康']").click()
    wd.find_element_by_xpath("//label[text()='在沪']").click()
    Select(wd.find_element_by_id("selCity_SF")).select_by_visible_text("市辖区")
    Select(wd.find_element_by_id("SFZX")).select_by_visible_text("不在校")
    wd.find_element_by_id('BTN_SAVE').click()
    print("填报完成")


if __name__ == '__main__':
    get_system(wd)