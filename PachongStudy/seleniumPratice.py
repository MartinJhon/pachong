#webdriver实例应用
from selenium import webdriver

browser = webdriver.Chrome()

url = 'http://www.zhihu.com/explore'

browser.get(url)

input = browser.find_element_by_class_name('zu-top-add-question')

print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)