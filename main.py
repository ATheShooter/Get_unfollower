from selenium import webdriver
from time import sleep


# enter your user name 
name = ""

#  enter your password  
password = ""

class FollowerChecker :
      def __init__(self, username, pw):
          self.driver = webdriver.Chrome()
          self.username = username
          self.driver.get("https://instagram.com")
          sleep(2)
          self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')\
              .send_keys(username)
          self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')\
            .send_keys(pw)
          sleep(1)
          self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')\
            .click()
          sleep(4)
          self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')\
            .click()
          self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")\
            .click()
          

      def get_unfollowers(self):
           self.profile =  self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a')   
           new_url = self.driver.current_url +self.profile.text
           self.driver.get(new_url) 
           # fins the people You following              
           self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')\
              .click()
           following  = self.get_info()
        
           self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')\
               .click()  
           followers  = self.get_info()
           not_following_back = [user for user in following if user not in followers]
           print(not_following_back)

      def get_info(self):
          sleep(2)
          
          scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div")

          self.driver.execute_script('arguments[0].scrollIntoView(true);', scroll_box)
          last_ht, ht = 0, 1
          while last_ht != ht:
              last_ht = ht
              sleep(1)
              ht = self.driver.execute_script("""
                  arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                  return arguments[0].scrollHeight;
                  """, scroll_box)
          links = scroll_box.find_elements_by_tag_name('a')
          names = [name.text for name in links if name.text != '']
          # close button
          self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")\
              .click()
          return names
         
Mmy_followerchecker = FollowerChecker(name, password)
Mmy_followerchecker.get_unfollowers()