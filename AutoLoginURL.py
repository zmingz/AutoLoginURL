#!/usr/bin/env python
# -*- coding: utf-8 -*-

# v1_0_0 by zhangmingzhi date: 2017.4.9 16:55

import time
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image

class LoginUrl(object):
	#初始化类的属性
	def __init__(self, driver, url, username, password):
		self.__driver = driver
		self.__url = url
		self.__username = username
		self.__password = password
	#打开网页的方法
	def openwebsite(self):
		self.__driver.maximize_window()
		self.__driver.get(self.__url)
	#输入网页账号
	def inputusername(self, find_element_method, element):
		if(find_element_method == "id"):		
			WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.ID, element)))#等待10s,每500ms查询一次,直到元素加载完毕或超过10s结束
			usrName = self.__driver.find_element_by_id(element)
		elif(find_element_method == "name"):
			WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.NAME, element)))
			usrName = self.__driver.find_element_by_name(element)
		elif(find_element_method == "xpath"):
			WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
			usrName = self.__driver.find_element_by_xpath(element)
		else:
			print "find element error!"	
		usrName.clear()
		usrName.click()
		usrName.send_keys(self.__username)
	#输入网页密码
	def inputpassword(self, find_element_method, element):
		if(find_element_method == "id"):
			WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.ID, element)))
			passWrd = self.__driver.find_element_by_id(element)
		elif(find_element_method == "name"):
			WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.NAME, element)))
			passWrd = self.__driver.find_element_by_name(element)
		elif(find_element_method == "xpath"):
			WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
			passWrd = self.__driver.find_element_by_xpath(element)
		else:
			print "find element error!"
		passWrd.clear()
		passWrd.click()
		passWrd.send_keys(self.__password)
	#识别验证码并且输入到文本框
	def verifyimgcode(self, find_image_method, image_element, find_text_method, text_element):
		if(find_image_method == "id"):
			WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.ID, image_element)))
			imgCode = self.__driver.find_element_by_id(image_element)
		elif(find_image_method == "name"):
			WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.NAME, image_element)))
			imgCode = self.__driver.find_element_by_name(image_element)
		elif(find_image_method == "xpath"):
			WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.XPATH, image_element)))
			imgCode = self.__driver.find_element_by_xpath(image_element)
		else:
			print "find element error!"
		imgCode.screenshot("code.png")
		img = Image.open("code.png")
		img.load()
		txt = pytesseract.image_to_string(img, lang = "yilong") #识别验证码, 须提前对tesserct进行验证码训练,这里的训练包使用"yilong"是提前训练好的
		time.sleep(10)
		print u"验证码:", txt
		if(find_text_method == "id"):
			WebDriverWait(self.__driver, 5).until(EC.presence_of_element_located((By.ID, text_element)))
			txtCode = self.__driver.find_element_by_id(text_element)
		elif(find_text_method == "name"):
			WebDriverWait(self.__driver, 5).until(EC.presence_of_element_located((By.NAME, text_element)))
			txtCode = self.__driver.find_element_by_name(text_element)
		elif(find_text_method == "xpath"):
			WebDriverWait(self.__driver, 5).until(EC.presence_of_element_located((By.XPATH, text_element)))
			txtCode = self.__driver.find_element_by_xpath(text_element)
		else:
			print "find element error!"
		txtCode.send_keys(txt)
	#点击登陆
	def clicksubmit(self, find_element_method, element):
		if(find_element_method == "id"):
			WebDriverWait(self.__driver, 5).until(EC.presence_of_element_located((By.ID, element)))
			self.__driver.find_element_by_id(element).click()
		elif(find_element_method == "name"):
			WebDriverWait(self.__driver, 5).until(EC.presence_of_element_located((By.NAME, element)))
			self.__driver.find_element_by_name(element).click()
		elif(find_element_method == "xpath"):
			WebDriverWait(self.__driver, 5).until(EC.presence_of_element_located((By.XPATH, element)))
			self.__driver.find_element_by_xpath(element).click()
		else:
			print "find element error!"	
	#切换到frame中,如果账号密码输入框在frame框架内,须要先切换到frame中,不然是查找不到账号和密码输入框的元素的
	def switch2iframe(self, find_element_method, element):
		WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.XPATH, element)))
		self.__driver.switch_to_frame(self.__driver.find_element_by_xpath(element))

def main():
	#登录去哪儿商家网
	browser1 = webdriver.Firefox()
	qunar = LoginUrl(browser1, "http://ebooking.qunar.com/ebPage/login.html", u"你的账号", u"你的密码")
	qunar.openwebsite()
	qunar.inputusername("name", "username")
	qunar.inputpassword("name", "password")
	qunar.clicksubmit("xpath", "//*[@id='QunarPopBox']/div/div[2]/div[2]/form/div[12]/button") #提前点击一下提交来显示验证码
	time.sleep(3)
	qunar.verifyimgcode("id", "QunarPopBoxvcodeImg", "name", "vcode")
	qunar.clicksubmit("xpath", "//*[@id='QunarPopBox']/div/div[2]/div[2]/form/div[12]/button")
	print "succeess..."

	#登录艺龙商家网
	browser2 = webdriver.Firefox()
	elong = LoginUrl(browser2, "http://ebooking.elong.com/ebkauth/login", u"你的账号", u"你的密码")
	elong.openwebsite()
	elong.inputusername("id", "hotel_user")
	elong.inputpassword("id", "password")
	elong.clicksubmit("id", "submit") 
	time.sleep(3)
	elong.verifyimgcode("id", "imgCode", "id", "valicode")
	elong.clicksubmit("id", "submit")
	print "succeess..."
	
	#登录美团商家网
	browser3 = webdriver.Firefox()
	meituan = LoginUrl(browser3, "http://eb.meituan.com/account/login?redirect=http%3A%2F%2Feb.meituan.com%2Feb%2Froomstatus/", u"你的账号", u"你的密码")
	meituan.openwebsite()
	meituan.switch2iframe("xpath", "//*[@id='login']/div[2]/iframe") #该网站加载了frame,先切换到里面去再输入账号密码
	meituan.inputusername("id", "login")
	meituan.inputpassword("id", "password")
	meituan.clicksubmit("xpath", "//*[@id='login-form']/button") 
	print "succeess..."

	#登录携程商家网
	browser4 = webdriver.Firefox()
	xiecheng = LoginUrl(browser4, "http://ebooking.ctrip.com/ebkassembly/login.aspx?targetPath=%2febooking%2fHome.aspx", "你的账号", "你的密码")
	xiecheng.openwebsite()
	xiecheng.inputusername("id", "userName")
	xiecheng.inputpassword("id", "userPwd")
	xiecheng.clicksubmit("id", "accSubmit") 
	print "succeess..."
	

if __name__ == "__main__":
	main()
