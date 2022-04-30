# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# browser = webdriver.Chrome(ChromeDriverManager().install())
# browser.get('https://www.flashscore.com.ua/basketball/')
# time.sleep(100)
# button = browser.find_element(by=By.XPATH, value='/html/body/div[6]/div[1]/div/div[1]/div[2]/div[4]/div[2]/div/div[1]/div[1]/div[2]')
# button.click()
# # event = browser.find_element(by=By.CLASS_NAME, value='')

# time.sleep(100)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# import time


# browser = webdriver.Chrome(ChromeDriverManager().install())
# browser.get('https://www.marathonbet.com/su/live/45356')

# time.sleep(5)
# button = browser.find_element(by=By.XPATH, value='/html/body/div[6]/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div/table/tbody/tr/td[1]')
# button.click()
# time.sleep(3)
# button = browser.find_element(by=By.XPATH, value='/html/body/div[6]/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div/div/div/table/tbody/tr/td/div/div[3]')
# button.click()
# time.sleep(300)
import pandas as pd
list_ = ['Нортс Беаз', 'Сентрал Коуст Крузейдерз', '1/2 (50%)', 'Штрафные броски', '2/3 (67%)', '4/7 (57%)', '2-очковые броски', '9/16 (56%)', '4/9 (44%)', '3-очковые броски', '0/1 (0%)', '18', 'Бросков всего', '20', '5', 'Наибольшее количество очков подряд', '4', '5', 'Наибольший отрыв в счете', '3', '20', 'Фолы', '11']
for i in range(len(list_)):
    if list_[i] == 'Бросков всего':
        print(list_[i+1], list_[i+2])
print(list_)

