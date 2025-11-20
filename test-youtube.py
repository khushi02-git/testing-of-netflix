from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

service = Service()
driver = webdriver.Chrome(service=service)

driver.maximize_window()

print("Opened Chrome")

driver.get("https://www.youtube.com")
print("Opened YouTube")
time.sleep(3)

search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("Lecture 1 : Flowchart & Pseudocode Shradha Khapra DSA")
search_box.send_keys(Keys.RETURN)
print("Searched for video")

time.sleep(3)

video = driver.find_element(By.XPATH, "//a[@id='video-title']")
video_title = video.text
video.click()
print("Opened video:", video_title)

time.sleep(5)

video_player = driver.find_element(By.CSS_SELECTOR, "video")
video_player.click()
print("Clicked video player to activate keyboard controls")

time.sleep(1)

body = driver.find_element(By.TAG_NAME, "body")

body.send_keys("k")
print("Pressed K - Play/Pause")

time.sleep(2)

body.send_keys("f")      # Fullscreen
print("Pressed F - Fullscreen")

time.sleep(2)

body.send_keys("m")      # Mute
print("Pressed M - Mute")

time.sleep(2)

body.send_keys(Keys.ARROW_RIGHT)  # Seek forward 5 sec
print("Pressed → - Forward")

time.sleep(2)

body.send_keys(Keys.ARROW_LEFT)   # Seek backward 5 sec
print("Pressed ← - Backward")

time.sleep(3)

print("Automation Completed Successfully")

time.sleep(10)

driver.quit()
