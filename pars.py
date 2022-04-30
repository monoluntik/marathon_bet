from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

def data_prepair(list_,team_main, team):
    data = []
    for i in range(len(list_)):
        if list_[i] == 'Последние матчи ' and list_[i+1] == team:
            break
        if list_[i] == team_main:
            if list_[i+1] == ' - ':
                points = ''.join([i for i in list_[i+3] if i in [' ', ':'] or i.isdigit()])
                points = [i.split(':') for i in points.split(' ')[1:]]
                team1 = [int(i[0]) for i in points]
                data.extend(team1)
            elif list_[i-1] == ' - ':
                points = ''.join([i for i in list_[i+1] if i in [' ', ':'] or i.isdigit()])
                points = [[i.split(':')[1],i.split(':')[0]] for i in points.split(' ')[1:]]
                team1 = [int(i[0]) for i in points]
                data.extend(team1)
    data.sort()
    return data[:2]


def open_window(url):
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    browser.get(url)    
    lis_ = browser.find_elements(by=By.CLASS_NAME, value='broadcast-statistic')
    if lis_ != []:
        browser.find_element(by=By.CLASS_NAME, value='broadcast-statistic').click()
        data = browser.find_element(by=By.CLASS_NAME, value='desktop')
        url = data.find_elements(by=By.CLASS_NAME, value='broadcast-embed')[1].get_attribute('src')
        browser.get(url=url)
        dt = browser.find_element(by=By.CLASS_NAME, value='base-live-statistic_table').text
        return dt
    else:
        return False

def pars():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    browser.get('https://www.marathonbet.com/su/live/45356')
    category_containers = browser.find_elements(by=By.CLASS_NAME, value='category-container')
    for category_container in category_containers:
        matchess = category_container.find_elements(by=By.CLASS_NAME,value='bg')
        for match in matchess:
            matchs = match.find_elements(by=By.CLASS_NAME, value='coupon-row-item')
            for i in matchs:
                I = i.text.split('\n')
                if I[0] not in ['1.', '2.'] or I[5] == 'Пер.' or I==[''] or I[5][0] == '—':
                    continue
                if len(I[4].split(', ')) > 2 and int(I[5][0]) in range(9,13):
                    a = datetime.now()
                    points = ''.join([i for i in I[4] if i in [' ', ':'] or i.isdigit()]) 
                    total = points.split(' ')[0].split(':')
                    points = [i.split(':') for i in points.split(' ')[1:]]
                    team1 = [int(i[0]) for i in points]
                    team2 = [int(i[1]) for i in points]
                    if max(team1) - min(team1) <= 5:
                        team_main = I[1], team1, I[3]
                    elif max(team2) - min(team2) <= 5:
                        team_main = I[3], team2, I[1]
                    else:
                        continue
                    print(I)
                    print(total,points)
                    print(team_main)
                    print(team1, team2)
                    min_point_4_set = (sum(team_main[1])/len(team_main[1]))*0.8
                    hist = match.find_elements(by=By.CLASS_NAME, value='event-statistics')
                    if hist == []:
                        btt = i.find_element(by=By.CLASS_NAME, value='member-area-buttons-label')
                        time.sleep(1)
                        btt.click()
                        time.sleep(1)
                    hist = match.find_element(by=By.CLASS_NAME, value='event-statistics')
                    data_text = hist.text.split('\n')
                    min_hist_point = data_prepair(data_text, team_main[0], team_main[2])
                    percent = 20
                    dt = all([i<=min_point_4_set for i in min_hist_point])
                    if dt:
                        percent += 5
                    if abs(int(total[0]) - int(total[1])) <= 4:
                        percent -= 7
                    url = match.find_element(by=By.CLASS_NAME, value='member-link').get_attribute('href')
                    list_ = open_window(url=url)
                    if list_:
                        for i in range(len(list_)):
                            if list_[i] == 'Бросков всего':
                                print(list_[i+1], list_[i+2])
                                if int(list_[i+1]) - int(list_[i+2]) in range(3,10):
                                    percent -= 3
                    print(percent)
                    print((sum(team_main[1])/len(team_main[1]))*((100-percent)/100))
                    b = datetime.now()
                    print(b-a)
    time.sleep(20)


while True:
    pars()
    time.sleep(20)



