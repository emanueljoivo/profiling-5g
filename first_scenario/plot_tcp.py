import matplotlib.pyplot as plt
import csv

intervals = []
data_transfer = []
bandwidth = []

def to_mega(b):
    return b / (10**6)

def filter_intervals(intervals):
    filtered = []
    for interval in intervals:
        i = interval.split("-")
        filtered.append(float(i[-1]))

    return filtered

with open('data/tcp.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        bandwidth.append(to_mega(int(row[-1])))
        data_transfer.append(to_mega(int(row[-2])))
        intervals.append(row[-3])

results = [intervals.pop(), data_transfer.pop(), bandwidth.pop()]
intervals = filter_intervals(intervals)

plt.plot(intervals, bandwidth)
plt.show()
