import pickle

lines = open("cities_and_times.txt").readlines()
lines.sort()

cities = []
for line  in lines:
    *city, day, time = line.split()
    hours, minutes = time.split(":")
    cities.append((" ".join(city), day, (int(hours), int(minutes)) ))

fh = open("cities_and_times.pkl", "bw")
pickle.dump(cities, fh)
fh.close()

f = open("cities_and_time.pkl", "rb")
villes = pickle.load(f)
f.close()
print(villes)