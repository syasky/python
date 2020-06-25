
#1.导入模块,当成 掏出浏览器工具箱
from selenium import webdriver

#2.打开浏览器
browser=webdriver.Chrome()

#3.准备一个网址
url='http://www.baidu.com'

#4.浏览器访问网址
browser.get(url)

#退出浏览器
browser.quit()











