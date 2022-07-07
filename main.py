# 크롤링시 필요한 라이브러리 불러오기
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import os
import json
from datetime import datetime

def fun():
    url = 'https://kauth.kakao.com/oauth/token'
    rest_api_key = '6c0736494efa732f35139b892eee0e21'
    redirect_uri = 'https://naver.com'
    authorize_code = 'VbhYQZElx_gtymW2t3AW1hYa1OIOSzIJd46Qa3vnMN33G9kljMhU7M_5FdHXV2HIf2NNIAorDKcAAAGB1xvvEQ'

    data = {
        'grant_type': 'authorization_code',
        'client_id': rest_api_key,
        'redirect_uri': redirect_uri,
        'code': authorize_code,
    }

    response = requests.post(url, data=data)
    tokens = response.json()
    print(tokens)

    # json 저장
    import json

    with open("kakao_code.json", "w") as fp:
        json.dump(tokens, fp)

    with open("kakao_code.json", "r") as fp:
        tokens = json.load(fp)

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    headers = {
        "Authorization": "Bearer " + tokens["access_token"]
    }

    data = {
        "template_object": json.dumps({
            "object_type": "text",
            "text": "학섹 버스 자리뜸!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
            "link": {
                "web_url": "헤헤. text와 link 객체는 필수로 넣어야 하는 거구나? button_title과 buttons는 안 넣어도 상관 없지만 말이야!",
                "mobile_web_url": "헤헤. text와 link 객체는 필수로 넣어야 하는 거구나? button_title과 buttons는 안 넣어도 상관 없지만 말이야!"
            },
            "button_title": "헤헤"
        })
    }

    response = requests.post(url, headers=headers, data=data)
    var = response.status_code
    print(var)


driver = webdriver.Chrome(r"C:\chromedriver.exe")
url = "https://www.kobus.co.kr/mrs/alcnSrch.do"
driver.get(url)

driver.implicitly_wait(10000)

time.sleep(15)

driver.switch_to.window(driver.window_handles[-1])
# 새로고침 클릭
i = 0

while True:
    now = datetime.now()
    time.sleep(0.5)
    time1 = driver.find_element_by_xpath('//*[@id="contents"]/div[3]/div[1]/div[2]/div[2]/div/div/p[1]/a/span[1]').text
    seat1 = driver.find_element_by_xpath('//*[@id="contents"]/div[3]/div[1]/div[2]/div[2]/div/div/p[1]/a/span[6]').text

    # time2 = driver.find_element_by_xpath('//*[@id="contents"]/div[3]/div[1]/div[2]/div[2]/div/div/p[2]/a/span[1]').text
    # seat2 = driver.find_element_by_xpath('//*[@id="contents"]/div[3]/div[1]/div[2]/div[2]/div/div/p[2]/a/span[6]').text
    print("--------------------------------------------------")
    print("시도 횟수:{}    시간 - {}    남은 자리 - {}      현재 시간 - {}".format(i, time1, seat1, now))
    # print("시간 - {}    남은 자리 - {}".format(time2, seat2))

    if seat1.split(' ')[0] != '0':
        fun()
        print("자리뜸!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        break
    # driver.find_element_by_xpath('//*[@id="reloadBtn"]/span').click()
    driver.refresh()
    i = i + 1

while True:
    pass
