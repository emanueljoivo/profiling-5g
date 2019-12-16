import matplotlib.pyplot as plt
import csv

intervals = []
data_transfer = []
bandwidth = []

def to_mega(b):
    return b / (10**6)

with open('data/udp.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        bandwidth.append(to_mega(int(row[-1])))
        data_transfer.append(to_mega(int(row[-2])))
        intervals.append(row[-3])

results = [intervals.pop(), data_transfer.pop(), bandwidth.pop()]
intervals = list(map(lambda interval: float(interval.split("-")[-1]), intervals))

plt.plot(intervals, bandwidth)
plt.ylabel("bandwidth in Mb/s")
plt.xlabel("time in sec")
plt.title("Scenario I - TCP traffic")
plt.show()
