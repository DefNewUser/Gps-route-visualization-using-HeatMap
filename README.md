# Задача на собеседовании Belaz
------------------

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

-----------
#### Задача выполнена в двух файлах, где один комбинирует и вычесляет данные в один csv, а второй реализует визуализацию данных на карте при помощи HeatMap. 




### Gps-HeatMap

![Снимок](https://user-images.githubusercontent.com/77128020/140654865-56613b40-0893-4b0b-a778-5393bc56c104.PNG)
![Снимок2](https://user-images.githubusercontent.com/77128020/140655120-7af447de-1817-40de-891b-a8f511e7e71e.PNG)
