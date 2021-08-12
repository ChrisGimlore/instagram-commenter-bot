from selenium import webdriver
import random
PATH = "C:\Program Files (x86)\chromedriver.exe"
from time import sleep 


username = ""
password = ""
hashtags = ["hiphop", "streetwear", "berlinstreet", "deutschrap", "cloudrap"]
comments = ["yo this is sick", "fye", 'nicee']


class instabot():
    links = []

    def __init__(self):
        self.login(username, password)
        self.like_comment_hashtag(hashtags, comments)
        
    def login(self, username, password):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get('https://www.instagram.com')
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
        sleep(random.randint(3,10))
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
        sleep(random.randint(3,10))
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
        sleep(random.randint(3,10))
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        sleep(random.randint(3,10))
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        sleep(random.randint(3,10))
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
        sleep(random.randint(3,10))

    def like_comment_hashtag(self, hashtags, comments):
        count = 0
        while count < 5: 
            self.driver.get("https://www.instagram.com/explore/tags/" + random.choice(hashtags))
            sleep(random.randint(3,6))
            links = self.driver.find_elements_by_tag_name('a')

            def condition(link):
                return '.com/p/' in link.get_attribute('href')
            valid_links = list(filter(condition, links))
            
            for i in range(2, 5):
                link = valid_links[i].get_attribute('href')
                if link not in self.links:
                    self.links.append(link) #each post on hasht has unique link, this finds them so that we can go on the posts 
            for link in self.links:
                self.driver.get(link)
                sleep(3)
            with open('URLS.txt') as f:
                if str(link) in f.read():
                    return
                else:
                    pass
            #like
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
            sleep(5)
            #comment
            self.driver.find_element_by_class_name('RxpZH').click() 
            sleep(random.randint(3,10))
            self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(random.choice(comments))
            sleep(random.randint(3,10))
            self.driver.find_element_by_xpath("//button[@type='submit']").click()
            with open('URLS.txt', 'a') as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0 :
                    file_object.write("\n")
                file_object.write(str(self.driver.current_url) )
            sleep(10)
            count =+ 1

            


#need to get it to loop around without opening a new instance 
#need it to pick up links of posts that have been commented on or liked and store them so it doesn't post on them twice 
#if link in urls pass else (carry on code) then get current url append to urls then loop 
def main():
    while True:
        my_bot = instabot()
        sleep(60) # one minute

if __name__ == '__main__':
    main()
