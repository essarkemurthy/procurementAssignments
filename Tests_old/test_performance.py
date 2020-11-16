from selenium import webdriver

import pyexcel_ods3

doc=pyexcel_ods3.read_data("../Testdata/testdata_sites.ods")

print(doc)
data=doc.values()
data=list(data)
print(type(data))
print(data)

headers=data[0][0]
print(headers)
for row in range(0,len(data[0])):
    headers










# print(doc.keys())
# print(doc.values())
# print(doc['Sheet1'][0])
# data_dict.keys


# driver = webdriver.Firefox(executable_path="../Config/geckodriver")
# driver.open