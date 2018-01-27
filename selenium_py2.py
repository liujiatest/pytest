#coding=utf-8
from selenium import  webdriver
import time

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
time.sleep(0.2)
driver.close()
print '运行成功啦'