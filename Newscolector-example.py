#! /usr/bin/env python
# coding: utf-8
import time
# import wechatsogou
import pandas as pd
import smtplib    
from email.mime.multipart import MIMEMultipart    
from email.mime.text import MIMEText    
from email.mime.image import MIMEImage 
from email.header import Header
from selenium import webdriver   


TitleToday = []
UrlToday = []
Date = time.strftime('%Y-%m-%d',time.localtime(time.time()))


############################### 筛选当日通知列表 ############################
def make_newslist(TitleToday,UrlToday):
    for k in range(0,4):
        if time_list[k] == Date:
            TitleToday.append(title_list[k])
            UrlToday.append(url_list[k])
    return TitleToday,UrlToday

################################# 国家科技部 ###############################
class kjb:
    def __init__(self):
        self.dr = webdriver.Chrome()
        self.dr.get('http://www.most.gov.cn/mostinfo/')
        self.dr.switch_to.frame("DataList")        
    def save_content(self):
        title_list = []
        time_list = []
        url_list = []
        for i in range(2,6):
            titlepath = "//*[@id='documentContainer']/div/table/tbody/tr[" + str(i) + "]/td[2]/table/tbody/tr/td/a" 
            curr_title = self.dr.find_element_by_xpath(titlepath)
            title_list.append(curr_title.text)
            curr_url = self.dr.find_element_by_xpath(titlepath).get_attribute("href")
            url_list.append(curr_url)
            timepath = "//*[@id='documentContainer']/div/table/tbody/tr["+ str(i) + "]/td[3]/div"
            curr_time = self.dr.find_element_by_xpath(timepath)
            time_list.append(curr_time.text) 
        self.quit()
        return title_list,time_list,url_list        
    def quit(self):
        self.dr.quit()

print ('科技部 searching...')
title_list,time_list,url_list = kjb().save_content()
TitleToday,UrlToday = make_newslist(TitleToday,UrlToday)


####################################### 国家发改委 ####################################
class gjfgw:
    def __init__(self):
        self.dr = webdriver.Chrome()
        self.dr.get('http://www.ndrc.gov.cn/zwfwzx/tztg/')    
    def save_content(self):
        title_list = []
        time_list = []
        url_list = []
        for i in range(1,5):
            titlepath = "//*[@id='out-content']/div[2]/div[4]/div[2]/div/ul[2]/li[" + str(i) + "]/a" 
            curr_title = self.dr.find_element_by_xpath(titlepath)
            title_list.append(curr_title.text)
            curr_url = self.dr.find_element_by_xpath(titlepath).get_attribute("href")
            url_list.append(curr_url)
            timepath = "//*[@id='out-content']/div[2]/div[4]/div[2]/div/ul[2]/li["+ str(i) + "]/font"
            curr_time = self.dr.find_element_by_xpath(timepath)
            time_list.append(curr_time.text) 
        self.quit()
        return title_list,time_list,url_list        
    def quit(self):
        self.dr.quit()

print ('国家发改委 searching...')
title_list,time_list,url_list = gjfgw().save_content()
TitleToday,UrlToday = make_newslist(TitleToday,UrlToday)


####################################### 北京市发改委####################################
class bjfgw:
    def __init__(self):
        self.dr = webdriver.Chrome()
        self.dr.get('http://fgw.beijing.gov.cn/zwxx/tztg/')    
    def save_content(self):
        title_list = []
        time_list = []
        url_list = []
        for i in range(1,5):
            titlepath = "//*[@id='container']/div[6]/ul/li[" + str(i) + "]/a" 
            curr_title = self.dr.find_element_by_xpath(titlepath)
            title_list.append(curr_title.text)
            curr_url = self.dr.find_element_by_xpath(titlepath).get_attribute("href")
            url_list.append(curr_url)
            timepath = "//*[@id='container']/div[6]/ul/li[" + str(i) + "]/p"
            curr_time = self.dr.find_element_by_xpath(timepath)
            time_list.append(curr_time.text) 
        self.quit()
        return title_list,time_list,url_list        
    def quit(self):
        self.dr.quit()

print ('北京市发改委 searching...')
title_list,time_list,url_list = bjfgw().save_content()
TitleToday,UrlToday = make_newslist(TitleToday,UrlToday)


####################################### 北京市科委 #####################################
class bjkw:
    def __init__(self):
        self.dr = webdriver.Chrome()
        self.dr.get('http://www.bjkw.gov.cn/col/col19/')    
    def save_content(self):
        title_list = []
        time_list = []
        url_list = []
        for i in range(1,5):
            titlepath = "//div[@class='default_pgContainer']/ul/li" + "[" + str(i) + "]/a" 
            curr_title = self.dr.find_element_by_xpath(titlepath)
            title_list.append(curr_title.text)
            curr_url = self.dr.find_element_by_xpath(titlepath).get_attribute("href")
            url_list.append(curr_url)
            timepath = "//div[@class='default_pgContainer']/ul/li" + "[" + str(i) + "]/span"
            curr_time = self.dr.find_element_by_xpath(timepath)
            time_list.append(curr_time.text) 
        self.quit()
        return title_list,time_list,url_list        
    def quit(self):
        self.dr.quit()

print ('市科委 searching...')
title_list,time_list,url_list = bjkw().save_content()
TitleToday,UrlToday = make_newslist(TitleToday,UrlToday)


##################################### 北京市经信委 ##################################
class bjeit:
    def __init__(self):
        self.dr = webdriver.Chrome()
        self.dr.get('http://jxw.beijing.gov.cn/jxdt/tzgg/index.htm')          
    def save_content(self):
        title_list = []
        time_list = []
        url_list = []
        for i in range(1,5):
            titlepath = "//div[@class='mainrf_cont']/ol/li[" + str(i) + "]/a" 
            curr_title = self.dr.find_element_by_xpath(titlepath)
            title_list.append(curr_title.text)
            curr_url = self.dr.find_element_by_xpath(titlepath).get_attribute("href")
            url_list.append(curr_url)  
            timepath = "//div[@class='mainrf_cont']/ol/li[" + str(i) + "]/i"
            curr_time = self.dr.find_element_by_xpath(timepath)
            time_list.append(curr_time.text)                       
        self.quit() 
        return title_list,time_list,url_list         
    def quit(self):
        self.dr.quit()

print ('市经信委 searching...')
title_list,time_list,url_list = bjeit().save_content()
TitleToday,UrlToday = make_newslist(TitleToday,UrlToday)

################################### 中关村管委会 ####################################
class zgc:
    def __init__(self): 
        self.dr = webdriver.Chrome() 
        self.dr.get('http://www.zgc.gov.cn/zgc/zwgk/tzgg/index.html')   
    def save_content(self): 
        title_list = [] 
        time_list = [] 
        url_list = [] 
        for i in range(1,5): 
            titlepath = "//div[@id='wuhang']/ul/li[" + str(i) + "]/span[1]/a"
            curr_title = self.dr.find_element_by_xpath(titlepath) 
            title_list.append(curr_title.text) 
            curr_url = self.dr.find_element_by_xpath(titlepath).get_attribute("href") 
            url_list.append(curr_url) 
            timepath = "//div[@id='wuhang']/ul/li[" + str(i) + "]/span[2]"
            curr_time = self.dr.find_element_by_xpath(timepath) 
            time_list.append(curr_time.text) 
        self.quit() 
        return title_list,time_list,url_list 
    def quit(self): 
        self.dr.quit() 

print ('中关村管委会 searching...')     
title_list,time_list,url_list  = zgc().save_content()
TitleToday,UrlToday = make_newslist(TitleToday,UrlToday)


######################################## 开发区 ##################################
class kfq:
    def __init__(self): 
        self.dr = webdriver.Chrome() 
        self.dr.get('http://kfqgw.beijing.gov.cn/zwgk/tzgg/')   
    def save_content(self): 
        title_list = [] 
        time_list = [] 
        url_list = [] 
        for i in range(1,5): 
            titlepath = "/html/body/div[3]/div/div/div[1]/ul/li[" + str(i) + "]/a"
            curr_title = self.dr.find_element_by_xpath(titlepath) 
            title_list.append(curr_title.text) 
            urlpath = titlepath
            curr_url = self.dr.find_element_by_xpath(urlpath).get_attribute("href") 
            url_list.append(curr_url) 
            timepath = "/html/body/div[3]/div/div/div[1]/ul/li[" + str(i) + "]/span"
            curr_time = self.dr.find_element_by_xpath(timepath) 
            time_list.append(curr_time.text) 
        self.quit() 
        return title_list,time_list,url_list 
    def quit(self): 
        self.dr.quit() 
print ('开发区 searching...')    
title_list,time_list,url_list = kfq().save_content()
TitleToday,UrlToday = make_newslist(TitleToday,UrlToday)

print('Searching Done!')
################################## Send emails ########################################
if len(TitleToday):   
    smtpserver = 'smtp.163.com'  ## 以163邮箱为例
    username = 'sender@example.com'
    password='XXXXXXX'
    sender='sender@example.com'
    receiver='receiver@example.com'
    subject = '每日通知更新'
    subject=Header(subject, 'utf-8').encode()

    msg = MIMEMultipart('mixed') 
    msg['Subject'] = subject
    msg['From'] = 'Name<sender@example.com>'
    msg['To'] = 'receiver@example.com'
    msg['Date'] = Date

    text = "今日更新通知：\n" 
    for i in range (0,len(TitleToday)):
    	text = text + TitleToday[i] + "   (" + UrlToday[i] + ")\n"
    text_plain = MIMEText(text,'plain', 'utf-8')    
    msg.attach(text_plain) 

    smtp = smtplib.SMTP()    
    smtp.connect('smtp.163.com') 
    smtp.login(username, password)    
    smtp.sendmail(sender, receiver, msg.as_string())    
    smtp.quit()
    print('Mail has been sent!')
else:
    print('There is no new news today.')
################################## print the result #################################

if len(TitleToday):
	News_num = len(TitleToday)
	show_summery = '【' + str(Date) + '】There are ' + str(News_num) + ' news today'
	print(show_summery)
	print(TitleToday)
	# 数据保存到本地 
	dataframe = pd.DataFrame({'title':TitleToday,'url':UrlToday})
	file_name = str(Date) + ".csv"
	dataframe.to_csv(file_name,index=False,sep=',')
	print ('Finish saving csv file')



