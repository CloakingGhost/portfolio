from cmath import isnan
from dataclasses import replace
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time
import json
def Take_Field(result):
    options = webdriver.ChromeOptions()
    options.add_argument('lang=ko_KR')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) 
    
    _id = 1
    for i in range(1100, 1105): # 구장 번호 1658개
        try:
            driver.get("https://www.iamground.kr/futsal/detail/" + str(i))
            html = driver.page_source
            bs4 = BeautifulSoup(html, 'html.parser')
            time.sleep(0.1)
            fPrice1 = 100000
            fPrice2 = 120000
            fPic1 = "https://i.ibb.co/SxBmcG2/Kakao-Talk-20221017-205135968.png"
            fPic2 = "https://i.ibb.co/m5tGT0m/Kakao-Talk-20221017-205135968-01.png"
            fPic3 = "https://i.ibb.co/JRyXz1Y/Kakao-Talk-20221017-205135968-02.png"
            fPic4 = "https://i.ibb.co/F8yzWm5/Kakao-Talk-20221017-205135968-03.png"
            fPhoneNo = "010-8223-4864"
            shoesRent = "https://i.ibb.co/5Gw80zy/image.png"
            uniformRent = "https://i.ibb.co/kJzvZbx/image.png"
            ballRent = "https://i.ibb.co/BBmQ6MC/image.png"
            shower = "https://i.ibb.co/jRDGrG3/image.png"
            parking = "https://i.ibb.co/Dtkj5tM/image.png"
            coldHot = "https://i.ibb.co/vB7qKSg/image.png"
            fRule = "■ 풋살장 예약시간 준수\n■ 풋살장 내 취사, 흡연 및 음주행위, 지나친 소음행위 금지(적발 시 이용불가)\n■ 시설 사용 후 정리정돈 ( 쓰레기 반드시 처리 )\n■ 고의 및 과실로 인한 시설물 훼손 및 파손시 사용자가 배상하며 경기중 부상은 본인이 책임집니다.\n■ 잔디보호와 부상방지를 위하여 스터드가 있는 축구화(SG, FG, HG, AG)는 착용이 금지되며 풋살화(TF)만 착용 가능 합니다.\n■ 실내구장에서는 마스크를 꼭 착용해주셔야합니다. 호흡이 어려운 경우 운동템포와 휴식시간을 조정해주세요.\n■ 위 내용이 지켜지지 않을 경우 무환불 퇴장조치 될 수 있으니 예약 시 꼭 참고부탁드립니다.\n■ 위 내용을 지키지 않아 발생하는 문제는 예약자 본인에게 있습니다."
            fRefundRule = "- 이용 5일 전까지 : 100% 환불\n- 4일 전 ~ 3일 전: 50% 환불\n- 2일 전 ~ 대관 당일 : 환불 불가\n■ 다음과 같은 경우에는 상단 규정대로 처리됩니다.\nㅇ 고객의 사정으로 예약된 날짜에 구장 이용을 못하는 경우\nㅇ 구장, 날짜, 시간 등을 실수로 잘못 선택했을 경우\nㅇ 단순 변심으로 인해 환불이나 변경을 요청하는 경우"
            fChangeRule = "■ 변경은 상단 환불 규정 기준 100% 환불인 경우에만 가능하며, 변경 가능한 횟수는 1회입니다.\n■ 1회 변경된 예약은 환불 및 재변경이 불가능합니다."
            fWeatherRefundRule = "■ 아래의 환불 및 변경 조건에 해당될 경우 이용 시작 '1시간 전'까지 고객센터로 문의 주시면 고객센터 운영 시간에 확인 후 처리해 드리겠습니다.\n■ 다음과 같은 경우에는 환불 및 변경 모두 불가능합니다.\nㅇ 이용 시작까지 1시간 이내로 남았을 경우\nㅇ 구장 혹은 고객센터에 문의 없이 구장 이용을 하지 않는 경우 ( No-Show )\n■ 구장 이용 도중 비가 오기 시작할 경우 환불 및 변경 가능 여부는 구장 관리자가 결정합니다."
            fRefund = "■ 날씨에 의한 환불은 야외구장에만 적용됩니다.\n■ 다음과 같을 때는 환불이 가능합니다.\nㅇ 예약 당일, 기상청에서 천재지변에 해당하는 특보를 예약한 지역에 발표한 경우에 적용\n(특보가 해제된 후에는 적용이 불가능합니다.)\nㅇ 천재지변 : 호우경보, 대설경보, 태풍주의보, 태풍경보만 적용\nㅇ 구장 환불규정에 천재지변의 기준이 없을 경우 호우경보, 대설경보, 태풍주의보, 태풍경보만 천재지변으로 적용"
            fChange = "■ 날씨에 의한 변경은 야외구장에만 적용됩니다.\n■ 다음과 같을 때는 변경이 가능합니다.\nㅇ 1시간 강수량이 1mm 이상일 때 ( 신 날씨누리 기준 '~1'은 변경 불가능합니다 )"
            fName = driver.find_element("id", "infoName").text
            fAddress = driver.find_element("id", "infoAddr").text
            fAddress = fAddress.replace("길찾기", "")
            tags = bs4.select("div.col-xs-12>h4")
            capacity = ""
            review = ""
            longitude = ""
            latitude = ""

            scripts = bs4.select('script')
            for script in scripts:
                if 'SERVER' in script.text:
                    # print(script)
                    # print()
                    string = script.text
                    string = string.replace("\n","")
                    string = string.replace("\t","")
                    string = string.split(",")
                    for i in range(len(string)):
                        if string[i].__contains__('longitude'):
                            longitude = string[i]
                        if string[i].__contains__('latitude'):
                            latitude = string[i]
                        
            latitude = latitude.replace("latitude: ", "")
            longitude = longitude.replace("longitude: ", "")
	
            
            for tag in tags:
                if(tag.string is not None):
                    if("구장크기" in tag.string):
                        capacity = tag.string
                    if("추천인원" in tag.string):
                        fSize = tag.string
                    if("구장정보" in tag.string):
                        fInfo = tag.string 
            reserve = ""
            try:
                cantReserve = driver.find_element("id", "cannotResv")
                if(cantReserve is not None):
                    reserve = "불가"
            except NoSuchElementException:
                    reserve = "가능"
                            
        except:
            continue
        result.append([_id]+[fAddress]+[fName]+[fPhoneNo]+[fPic1]+[fPic2]+[fPic3]+[fPic4]+[fSize]+[capacity]+[fInfo]+[fPrice1]+[fPrice2]+[shoesRent]+[uniformRent]+[ballRent]+[shower]+[parking]+[coldHot]+[fRule]+[fRefundRule]+[fChangeRule]+[fWeatherRefundRule]+[fRefund]+[fChange]+[review]+[latitude]+[longitude]+[reserve])
        _id += 1
    return    

def main():
    result = []
    print("풋살 구장 위치 가져오기 >> ")
    # [CODE 1]
    Take_Field(result)
    df = pd.DataFrame(result, columns=('_id','fAddress','fName','fPhoneNo','fPic1','fPic2','fPic3','fPic4','fSize','capacity','fInfo','fPrice1','fPrice2','shoesRent','uniformRent','ballRent','shower','parking','coldHot','fRule','fRefundRule','fChangeRule','fWeatherRefundRule','fRefund','fChange','review','latitude','longitude','reserve'))
    df.to_csv('./FieldInfo.csv', encoding='utf8', mode='w', index=False)

if __name__ == '__main__':
    main()
