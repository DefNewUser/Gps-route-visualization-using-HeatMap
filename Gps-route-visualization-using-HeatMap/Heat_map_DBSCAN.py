import pandas as pd, numpy as np, time
from sklearn.cluster import DBSCAN
from geopy.distance import great_circle
from shapely.geometry import MultiPoint
import folium
from folium import plugins

df = pd.read_csv("combined.csv", index_col=False)

# points for a typical route
coords = df[['x', 'y']].to_numpy()

# points for a Heatmap
gps = df[['x', 'y']]
points = [tuple(p) for p in gps.to_numpy()]
# print(points)

# mid for a Heatmap
ave_lat = sum(p[0] for p in points) / len(points)
ave_lon = sum(p[1] for p in points) / len(points)

# define the number of kilometers in one radian
kms_per_radian = 6371.0088

# define epsilon as 10 meters, converted to radians for use by haversine
epsilon = 0.01 / kms_per_radian

# point clustering
start_time = time.time()
db = DBSCAN(eps=epsilon, min_samples=1, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
cluster_labels = db.labels_

# get the number of clusters
num_clusters = len(set(cluster_labels))
clusters = pd.Series([coords[cluster_labels == n] for n in range(num_clusters)])
# print(clusters)

message = 'Clustered {:,} points down to {:,} clusters, for {:.1f}% compression in {:,.2f} seconds'
print(message.format(len(df), num_clusters, 100 * (1 - float(num_clusters) / len(df)), time.time() - start_time))


# Нахождение центральной точки кластера.
# Функция сначала вычисляет координаты центроида. /
# Затем я использую встроенную в Python  функцию min, /
# чтобы найти наименьший член кластера с точки зрения расстояния /
# до этого центроида. Ключевой аргумент делает это с помощью /
# лямбды - функцией , которая вычисляет расстояние каждой точки /
# на центроид в метрах, через geopy в большом круге функции. /
# Наконец, я возвращаю координаты точки, /
# которая находилась на наименьшем расстоянии от центроида.
def get_centermost_point(cluster):
    centroid = (MultiPoint(cluster).centroid.x, MultiPoint(cluster).centroid.y)
    centermost_point = min(cluster, key=lambda point: great_circle(point, centroid).m)
    return tuple(centermost_point)


centermost_points = clusters.map(get_centermost_point)

# Затем я превращаю эти центральные точки в фрейм данных pandas точек, /
# которые пространственно представляют мои кластеры /
# (и, в свою очередь, мой исходный полный набор данных):
lons, lats = zip(*centermost_points)
rep_points = pd.DataFrame({'x': lons, 'y': lats})
# print(rep_points.tail())

gps_points = [tuple(p) for p in rep_points.to_numpy()]
print(gps_points)

my_map = folium.Map(location=[ave_lat, ave_lon], zoom_start=14)

# add Marker2
marker_R = plugins.MarkerCluster().add_to(my_map)

# Отображаем только тех маркиров, где is_80 = True
for t, x, y, r, label in zip(df.t, df.x, df.y, df.R, df.is_80.astype(str)):
    if label == 'True':
        folium.Marker(
            location=[x, y],
            icon=None,
            popup=f"Data: {t}, R: {r}",
        ).add_to(marker_R)

# add HeatMap for a typical route
folium.plugins.HeatMap(gps_points, radius=14).add_to(my_map)

# Polyline for a typical route (does not work...)
# folium.PolyLine(locations=sorted(zip(gps.x, gps.y))).add_to(my_map)

# Save map
my_map.save("map.html")
