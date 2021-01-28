#importing packages
import selenium
from selenium import webdriver
#PATH = "C:\Program Files (x86)\chromedriver.exe"
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#this imports the installed chrome webdriver in order to work with selenium
driver = webdriver.Chrome(ChromeDriverManager().install())

#driver = webdriver.Chrome(PATH)
import os
import time
from selenium.webdriver.common.keys import Keys

#this class is set to send the user to the login page
#fill out the username and password with your spotify login.
#if no username, then replace it with an email
class bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = 'https://open.spotify.com/playlist/3f85bgkiDakfK2Y3rVB9z8'
        self.bot = webdriver.Chrome("D:\\Program Files\\chromedriver_win32")
        self.play()

#this function utilizes xpath as a means to select and automate the clicking and typing process
#it uses the html code to locate the button/text field
    def play(self):
        self.bot.get(self.base_url)
        time.sleep(3)
        self.bot.find_element_by_xpath('//*[@id="main"]/div/div[3]/div[1]/header/div[4]/button[2]').click()
        time.sleep(7)
        self.bot.find_element_by_xpath('//*[@id="login-username"]').send_keys(self.username)
        self.bot.find_element_by_xpath('//*[@id="login-password"]').send_keys(self.password)
        self.bot.find_element_by_xpath('//*[@id="login-password"]').send_keys(Keys.RETURN)
        time.sleep(7)
        self.bot.find_element_by_xpath('//*[@id="main"]/div/div[3]/div[2]/nav/div[2]/div/div/div[2]/a').click()
        time.sleep(4)
        self.bot.find_element_by_xpath('//*[@id="main"]/div/div[3]/div[4]/div[1]/div/div[2]/section[1]/div[3]/div/button').click()
        time.sleep(100)

#this runs the bot/code above by passing those two parameters below.
if __name__ == "__main__":
    BOT = bot("email","password")
