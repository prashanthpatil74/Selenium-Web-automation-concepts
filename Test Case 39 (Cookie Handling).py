from xml.dom.xmlbuilder import Options

from selenium import webdriver
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
a=driver.get_cookies()

#print detail of all cookies
for i in a:
    # print(i)
    print(i.get("name"),":",i.get("value"))


#add new cookie to browser
# driver.add_cookie({"name":"my cookies","value":"122"})
# a=driver.get_cookies()
# print(len(a))
# for i in a:
#     print(i)

#delete specific cookie
# driver.delete_cookie("my cookies")
# a=driver.get_cookies()
# print(len(a))

#delete all cookie
driver.delete_all_cookies()
a=driver.get_cookies()
print(len(a))
driver.close()