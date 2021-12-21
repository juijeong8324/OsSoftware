# 시간표 가져오는 모듈 
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from openpyxl import Workbook,load_workbook

# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
chromedrvier = 'C:\\Users\\USER\\OneDrive - 서울과학기술대학교\\OS 프로젝트\\chromedriver.exe'
driver = webdriver.Chrome(chromedrvier)

# url에 접근한다.
driver.get('https://everytime.kr/login')
# 암묵적으로 웹 자원 로드를 위해 5초까지 기다려 준다.
driver.implicitly_wait(5)

# 아이디/비밀번호를 입력해준다. (직접 입력)
driver.find_element_by_name('userid').send_keys('----본인 에타 아이디----')
driver.find_element_by_name('password').send_keys('----본인 에타 비번')

# 로그인 버튼을 눌러주자.
driver.find_element_by_xpath('//*[@id="container"]/form/p[3]/input').click()

# 시간표 접근 
driver.get('https://everytime.kr/timetable')

# 2021학년도 2학기 수업 시간표 클릭 (수업시간표 지정 이때 6은 왼쪽의 시간표 목록 중 6번째에 해당하는 시간표를 의미)
driver.find_element_by_xpath('//*[@id="container"]/aside/form/select/option[10]').click() 
sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

results = []
trs = soup.select('#container > div.wrap > div.tablebody > table > tbody > tr > td > div.cols') # 시간표에 접근 
i = 0 # 요일 번호 
f = open("result.txt", "w") # timetable 결과 

for div in trs: # 각 요일마다 접근  
    i = i + 1
    for subject in div: # 각 요일의 시간표에 접근 
        sub = subject.find('h3')
        #result.append(sub.text) # 과목명
        prof = subject.find('em') 
        #result.append(sub.text) # 교수님 성함
        loc = subject.find('span')
        #result.append(sub.text) # 장소 
        #results.append(result)
        f.write(f'{i}'+ "," + sub.text + "," + prof.text + "," + loc.text+"\n")

f.close

