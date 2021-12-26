# ✏ MyEveryMap.v0      
 
![image](https://user-images.githubusercontent.com/63052097/146947234-ad8320de-2499-4c20-8f0b-53596013135d.png)    
- 수강신청 전 (현)서울과학기술대학교 캠퍼스 경로 확인 프로그램입니다.
- 에브리 타임 계정과 시간표를 입력하면 요일마다 이동해야 하는 캠퍼스 건물의 최단 경로를 보여주는 프로그램입니다.        

<br>
<br>        

## 프로그램 사용 방법         
<img src="https://user-images.githubusercontent.com/63052097/146943647-c2c3ea3b-65ba-4c20-ab28-b6a41f336dad.png" width=500 />     
<img src="https://user-images.githubusercontent.com/63052097/146949864-4d1b34ca-ca6b-473c-b25b-8b27bb19e4f0.png" width=500 />
1. 먼저 timetable.py에 가서 에브리 타임 아이디와 비밀번호를 적어줍니다. 또한 어떤 시간표를 보고 싶은지 번호를 적어주세요! 제 시간표는 첨부해 두었습니다!        
<br>  
<img src="https://user-images.githubusercontent.com/63052097/146944041-182a6427-994c-4aef-a01c-95373be6e26f.png" width=500 />    
2. start.py에 가서 프로그램을 재생시켜줍니다. 이 파일에서 데이터를 가공하고 map을 생성해줍니다.          
<br>
<img src="https://user-images.githubusercontent.com/63052097/146944753-a528588c-9f39-4549-9f4d-9844c317e6f2.png" width=500 />
3. test.html에 가서 결과를 확인합니다!            
<br>
<img src="https://user-images.githubusercontent.com/63052097/146947362-2ac962b0-63e2-4dca-b12c-dd79d5ef1d57.png" width=500 />
짜잔 해당 건물과 경로가 나왔습니다! 경로가 없는 건물은 한 요일에 해당 건물만 사용하는 거에요!         
<br>
<img src="https://user-images.githubusercontent.com/63052097/146949267-a842c0dd-d11f-483e-8ee9-6935c7f1e42e.png" width=500 />
4. 경로를 추가하고 싶다면 location data에 해당 경로의 좌표를 하나씩 직접 추가하면 됩니다! -> 해당 프로그램을 개발해볼까요!?!?! 

## 프로젝트 구조 
- timetable.py = 에타시간표 크롤링
- start.py = 데이터 가공 및 지도 생성 호출
- make_map = 지도 생성
- test.html  = 지도 확인
---     

## 목표       
- 학교 포탈의 한 부분의 기능 혹은 수강신청 전에 잠깐 확인하는 프로그램으로서 사용되길 기대하고 있습니다.       
- 사용자가 경로를 업데이트 할 수 있는 동적인 프로그램입니다.        
- 현재는 서울과학기술대학교 학생들만 사용 가능하지만 모든 캠퍼스가 사용할 수 있는 서비스가 되도록 연구중입니다.         

<br>                

## 개발 동기              
**첫째**, 인터넷에서 부산대에서는 수강신청 전 캠퍼스 간 경로와 시간을 확인할 수 있는 서비스가 있다고 한다고 보았습니다. (그러나 찾을 수가 없었는데 아시는 분!)    
**둘째**, 현재는 비대면이라 필요성을 못 느끼지만 나중에 대면 수업을 진행한다면 캠퍼스 간 시간 확인은 필수입니다. 특히 통학러 혹은 새내기에게 필요하다고 생각합니다 (작년에 해당 건물이 어디있는지 몰라서 뛰어다닌 기억이 있습니다.)   
**셋째**, 카카오맵이나 네이버 지도로는 한계가 있습니다. 같은 길이라도 더 멀리 돌아서 가는 경로를 최단 경로라고 내놓은 경우가 많습니다. 실제로 학교를 다니는 대학생들이 캠퍼스에 대해서 더 잘 알고 캠퍼스가 바뀔 수 있기 때문에 업데이트가 필요합니다.       

<br> 


## 앞으로 고려해야 할 부분          
1. 모든 학교 홈페이지에서 사용할 수 있어야 한다고 할 때 지도 그림은 어디서 구할 수 있는가(지도 형태가 정확히 위에서 바라보는 것이 아닌 측면에서 바라보는 경우가 많음)              
2. 학교 홈페이지 중 어디 페이지에 연동할 것인가, 그리고 학교에서 허락은 해줄 수 있나? 만약 안 된다면 어떻게 구현해낼 것인가?(그냥 GUI를 만들어야 하는가?)           
3. 기존 지도 API를 최대한 활용할 수 있는가?    
4. 사용자가 에타 로그인만 해도 지도를 볼 수 있게 연동이 필요하다.     
5. 해당 요일에 경로와 마커를 구분하게 해야한다. 
6. 시간정보도 함께 보여준다. 

<br>

## 아쉬운 점        
- 기존의 지도 map을 이용하려고 했으나 길찾기 기능은 경로만 알려주거나 경로 외에 추가적인 정보는 제공을 안 함.
-> 카카오 api = 길찾기 경로만 제공 그 외의 시간대 최적의 이동 방법 등 과 같은 구체적인 정보는 제공 안 함 / 네이버 api = 웹서버가 있어야 사용 가능 길찾기의 경로의 경우  제공 안 함 /
오디세이 API = 비쌈..
- 크롤링이 잘 될 때가 있고 안 될 때가 있음
- 데이터 수집을 위해 경로를 그려주고 해당 좌표 값을 얻는 프로그램을 하나 더 개발해야 할 것 같다. 
- 일일이 프로그램을 돌려야 해서 아쉽다. 에타 로그인만 해도 경로를 볼 수 있게 더 연구해봐야 할 것 같다. 
- 해당 경로와 마커가 몇 요일에 해당하는지 보여줘야 했는데.. 자꾸 에러가 떴다. 
- 시간 정보도 깔끔하게 보여줘야 한다. 

<br>
라이센스는 LICENSE라는 해당 파일에 있습니다!    

### 참고자료        
- 에브리 타임 크롤링 (https://github.com/wwlee94/everytime-timetable-crawling/blob/master/test.py)
- 지도에 좌표 그리기 [https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=chandong83&logNo=221233832987&categoryNo=75&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView](https://blog.naver.com/PostView.nhnisHttpsRedirect=true&blogId=chandong83&logNo=221233832987&categoryNo=75&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView)

