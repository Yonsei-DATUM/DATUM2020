import time
import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser= webdriver.Chrome("D:/Python/web/chromedriver.exe")
browser.get("http://ysweb.yonsei.ac.kr:8888/curri120601/curri_new.jsp#top")
# Search->name of class
browser.find_element_by_xpath("//*[@id='myForm']/table/tbody/tr[2]/td[2]/select/option[2]").click()
# Put the name of class and click the button
try:
    name= input("input the name of class : ")
    browser.find_element_by_xpath("//*[@id='myForm']/table/tbody/tr[2]/td[2]/input[2]").send_keys(name)
    browser.find_element_by_xpath("//*[@id='myForm']/table/tbody/tr[2]/td[2]/a/img").click()
    time = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[5]/form[2]/table/tbody/tr[3]/td/div/div[2]/div/div[3]/div[2]/div/div[1]/div[1]")))
except:
    print("There is no such name of class")
# set variable of paper number
total_page_element=browser.find_element_by_xpath("/html/body/div[5]/form[2]/table/tbody/tr[3]/td/div/div[2]/div/div[8]/div/div/div[3]")
total_page =int(total_page_element.text.split()[2])
page_number = total_page // 15
if total_page >16:
    last_number_first_page = 15
else:
    last_number_first_page = total_page
number_click = 0  
while number_click != page_number + 1:
    for k in range(0,last_number_first_page):
        year = browser.find_element_by_xpath("//*[@id='row"+str(k)+"jqxgrid']/div[1]/div")
        class_names= browser.find_elements_by_xpath("/html/body/div[5]/form[2]/table/tbody/tr[3]/td/div/div[2]/div/div[3]/div[2]/div/div["+str(k+1)+"]/div[9]/span")
        class_name = class_names[0].text
        for s in [1,2]:
                # Check the class name with our result
                if class_name == name+" " :
                    for n in range(20, 15, -1):     
                        if str(int("2000")+n)+str(s)== year.text :
                            # Type of class , name of professor
                            name_second= browser.find_element_by_xpath("/html/body/div[5]/form[2]/table/tbody/tr[3]/td/div/div[2]/div/div[3]/div[2]/div/div["+str(k+1)+"]/div[5]/div").text
                            name_third= browser.find_element_by_xpath("/html/body/div[5]/form[2]/table/tbody/tr[3]/td/div/div[2]/div/div[3]/div[2]/div/div["+str(k+1)+"]/div[14]/span").text
                            # result of each semestry
                            browser.find_element_by_xpath("//*[@id='row"+str(k)+"jqxgrid']/div[7]/span/a[4]/img").click()
                            # switch to new page
                            browser.switch_to.window(browser.window_handles[1])
                            # Trun to bs4 for collecting the data
                            soup= BeautifulSoup(browser.page_source,'lxml')
                            # Error1
                            try:
                                error_message = browser.find_elements_by_xpath("/html/body/form/center")[0].text
                            except:
                                error_message = "good"
                            if error_message != "해당 과목은 신청자가 없었거나, 마일리지선택제로 진행되지 않았으므로 결과가 존재하지 않습니다.":
                                table=soup.find("table",attrs={"width":["960"]}).find_all("tr")
                                filename= name +"-" +str(int("2000")+n)+"-"+str(s)+str("학기")+"-"+name_second+"-"+name_third+".csv"
                                f=open(filename, 'w', encoding="utf-8-sig", newline="")
                                writer=csv.writer(f)
                                for row in table:
                                    columns = row.find_all("td")
                                    data=[column.get_text() for column in columns]
                                    writer.writerow(data)
                                browser.quit                    
                                browser.switch_to.window(browser.window_handles[0])
                            else:
                                browser.quit                    
                                browser.switch_to.window(browser.window_handles[0])
                                pass              
                        else:
                            pass
                else:
                    pass
    # Turn the page
    browser.find_element_by_xpath("/html/body/div[5]/form[2]/table/tbody/tr[3]/td/div/div[2]/div/div[8]/div/div/div[2]").click()
    total_page_element=browser.find_element_by_xpath("/html/body/div[5]/form[2]/table/tbody/tr[3]/td/div/div[2]/div/div[8]/div/div/div[3]")
    number_click = number_click + 1