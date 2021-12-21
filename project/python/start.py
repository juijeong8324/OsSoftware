# 메인 파일 
import webbrowser  # 웹브라우저를 뛰어야 하니까 
#import timetable # 시간표 불러오기 
import pandas as pd # 
import make_map as m
import location_data as ld

# 에타 데이터를 데이터 프레임으로 변환 
def dataToFrame():
   file_path = "result.txt"
   my_timetable = []
   with open(file_path, "r") as f:
      lines = f.read().splitlines()
      my_timetable = [line.split(',') for line in lines]

   my_t = pd.DataFrame(my_timetable)
   my_t.columns=['요일','과목명','성함','건물']
   
   return my_t

# 좌표 데이터를 리스트로 변환
def coorToFrame():
   file_path = "techbuild.txt"
   my_build = []
   with open(file_path, "r", encoding = "utf-8") as f:
      lines = f.read().splitlines()
      my_build = [line.split(',') for line in lines]
   return my_build 

# 장소 리스트를 set으로 변환   
def locToSet(list):
   result_list = []
   if len(list) == 0 or len(list) == 1:
      return result_list
   else:
      for i in range(0,len(list)-1):
         if list[i] == list[i+1]:
            i = i+1         
         else:
            result_list.append((list[i], list[i+1]))

   return result_list

# 장소 set이 존재하면 좌표 추가 
def isSet(set_list):
   result_list = []
   if len(set_list) == 0:
      return result_list
   else:
      for i in set_list:
         result_list.append(ld.Coordinate(i))
      
      return sum(result_list, []) 

# 메인 실행
if __name__ == '__main__':
   #timetable # 시간표 불러오기 

   # 데이터들을 리스트로 반환 후 데이터 프레임으로 변환 
   my_t = dataToFrame()

   # 해당 건물이 존재하는 것들을 요일끼리 묶는다
   mon = my_t[(my_t['요일'] == '1') & (my_t['건물'] != '')]
   tue = my_t[(my_t['요일'] == '2') & (my_t['건물'] != '')]
   wen = my_t[(my_t['요일'] == '3') & (my_t['건물'] != '')]
   thu = my_t[(my_t['요일'] == '4') & (my_t['건물'] != '')]
   fri = my_t[(my_t['요일'] == '5') & (my_t['건물'] != '')]
 
   # 장소 리스트를 만든다 
   mon_location = [ mon_l[:2] for mon_l in mon.iloc[:,-1]]    # 앞 두글자만 빼기 
   tue_location = [ tue_l[:2] for tue_l in tue.iloc[:,-1]]
   wen_location = [ wen_l[:2] for wen_l in wen.iloc[:,-1]]
   thu_location = [ thu_l[:2] for thu_l in thu.iloc[:,-1]]
   fri_location = [ fri_l[:2] for fri_l in fri.iloc[:,-1]]

   # 장소 set을 만든다. 
   monSet = locToSet(mon_location)
   tueSet = locToSet(tue_location)
   wenSet = locToSet(wen_location)
   thuSet = locToSet(thu_location)
   friSet = locToSet(fri_location)

   # 총 장소 좌표들 반환 
   monSetCor = isSet(monSet)
   tueSetCor = isSet(tueSet)
   wenSetCor = isSet(wenSet)
   thuSetCor = isSet(thuSet)
   friSetCor = isSet(friSet)


   # 건물 좌표 데이터들을 가져옴
   my_build = coorToFrame()

   # 건물 좌표 리스트를 만든다. 
   monCoor_list = []
   tueCoor_list = []
   wenCoor_list = []
   thuCoor_list = []
   friCoor_list = []

   for i in mon_location:
      for target in my_build:
         if target[0] == i:
            monCoor_list.append([float(target[1]), float(target[2])])

   for i in tue_location:
      for target in my_build:
         if target[0] == i:
            tueCoor_list.append([float(target[1]), float(target[2])])
            
   for i in wen_location:
      for target in my_build:
         if target[0] == i:
            wenCoor_list.append([float(target[1]), float(target[2])])

   for i in thu_location:
      for target in my_build:
         if target[0] == i:
            thuCoor_list.append([float(target[1]), float(target[2])])

   for i in fri_location:
      for target in my_build:
         if target[0] == i:
            friCoor_list.append([float(target[1]), float(target[2])])


   myMap = m.MapMake(monCoor_list, tueCoor_list, wenCoor_list, thuCoor_list, friCoor_list, monSetCor, tueSetCor, wenSetCor, thuSetCor, friSetCor) # 지도 클래스 생성
   myMap.make()




