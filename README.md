Task:
Sorry for my English :(

"RU"
Массив данных gps.csv содержит координаты gps за 1 месяц для одной машины, которая движется по одному маршруту. 
Координаты поступают с разной частотой и редко (примерно 1-3 раза в минуту),
поэтому за этот промежуток времени машина успевает проехать достаточно большое расстояние. 
Плюс бывает погрешность позиционирования.

Задание 1.
На основе месячного массива данных, обобщив их, построить типичный маршрут движения машины. 
Если данных будет достаточно, то с одним шагом, равным 5-10 метров. 
Отобразить его на карте и сохранить координаты в файл. 

Задание 2.
Для всех координат gps из файла gps.csv  рассчитать параметр R = (P1 + P3) – (P2 + P4), если v > 5 (data.csv). 
При расчете R параметры P1, P3, P2, P4 брать средние за 5 сек. Рассчитать Rmax. 
Отобразить на маршруте, рассчитанным в задании 1, точки, где R > 0.8*Rmax  
(использовать heatmap для отображения того, насколько часто встречается данное условие в данной точке)


"ENG"
The gps.csv dataset contains gps coordinates for 1 month for one car moving along one route.
Coordinates are received with different frequencies and rarely (about 1-3 times per minute),
therefore, during this period of time, the car has time to travel a sufficiently long distance.
Plus, there is a positioning error.

Exercise 1.
Based on the monthly data array, summarizing them, build a typical route of the car.
If there is enough data, then with one step equal to 5-10 meters.
Display it on the map and save the coordinates to a file.

Exercise 2.
For all gps coordinates from the gps.csv file, calculate the parameter R = (P1 + P3) - (P2 + P4) if v> 5 (data.csv).
When calculating R, take the average parameters P1, P3, P2, P4 for 5 seconds. Calculate Rmax.
Show on the route calculated in task 1 points where R> 0.8 * Rmax
(use heatmap to display how often a given condition occurs at a given point) 

"My solution"
1. Files_combined - Performs 2nd task by combining two files. Description:
Creates one of two files --common.csv, in which it calculates data from the second task.

2. Heat_map_DBSCAN - Clusters gps data within a radius of 10 meters and visualizes the data on a map using HeatMap
