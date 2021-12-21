import folium
import pandas as pd
from folium.features import CustomIcon

class MapMake():
  def __init__(self, mon_b, tue_b, wen_b, thu_b, fri_b, mon_data, tue_data, wen_data, thu_data, fri_data):
    self.center = [37.633248, 127.077831]  
    self.m=folium.Map(location=self.center, zoom_start=15) 
    # 좌표 데이터들 
    self.mon_data = mon_data
    self.tue_data = tue_data
    self.wen_data = wen_data
    self.thu_data = thu_data
    self.fri_data = fri_data
    # 건물 좌표
    self.mon_b = mon_b
    self.tue_b = tue_b
    self.wen_b = wen_b
    self.thu_b = thu_b
    self.fri_b = fri_b
    # 월별 색깔 
    self.mon_color = "#ff6161"
    self.tue_color = "#ff9145"
    self.wen_color = "#ffd64c"
    self.thu_color = "#3cb65e"
    self.fri_color = "#6a52f1"     
    
  # 지도 만들기 이때 지도 반환
  def make(self):
    if len(self.mon_data) != 0:
      folium.PolyLine(locations=self.mon_data, color=self.mon_color ,tooltip='Polyline').add_to(self.m)
    if len(self.tue_data) != 0:
      folium.PolyLine(locations=self.tue_data,color=self.tue_color, tooltip='Polyline').add_to(self.m)
    if len(self.wen_data) != 0:
      folium.PolyLine(locations=self.wen_data,color=self.wen_color, tooltip='Polyline').add_to(self.m)
    if len(self.thu_data) != 0:
      folium.PolyLine(locations=self.thu_data,color=self.thu_color, tooltip='Polyline').add_to(self.m)
    if len(self.fri_data) != 0:
      folium.PolyLine(locations=self.fri_data,color=self.fri_color, tooltip='Polyline').add_to(self.m)

    # 마커 표시 
    #iconMon = CustomIcon('img/mon.png',icon_size=(75, 75),icon_anchor=(10, 30))
    #iconTue = CustomIcon('img/tue.png',icon_size=(75, 75),icon_anchor=(10, 30))
    #iconWen = CustomIcon('img/wen.png',icon_size=(75, 75),icon_anchor=(10, 30))
    #iconThu = CustomIcon('img/thu.png',icon_size=(75, 75),icon_anchor=(10, 30))
    #iconFri = CustomIcon('img/fri.png',icon_size=(75, 75),icon_anchor=(10, 30))
    
    for mon in self.mon_b:
        marker1 = folium.Marker(location=mon)
        self.m.add_child(marker1)
    for tue in self.tue_b:
        marker2 = folium.Marker(location=tue)
        self.m.add_child(marker2)
    for wen in self.wen_b:
        marker3 = folium.Marker(location=wen)
        self.m.add_child(marker3)
    for thu in self.thu_b:
        marker4 = folium.Marker(location=thu)
        self.m.add_child(marker4)
    for fri in self.fri_b:
        marker5 = folium.Marker(location=fri)
        self.m.add_child(marker5)
    
    self.m.save('map.html')





