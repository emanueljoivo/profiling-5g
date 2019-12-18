import matplotlib.pyplot as plt
import csv

def to_mega(b):
    return b / (10**6)

intervals = []
data_transfer = []
bandwidth = []

with open('data/udp_upload.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        bandwidth.append(to_mega(int(row[-6])))
        data_transfer.append(to_mega(int(row[-7])))
        intervals.append(row[-8])

results = [intervals.pop(), data_transfer.pop(), bandwidth.pop()]
intervals = list(map(lambda interval: float(interval.split("-")[-1]), intervals))

# the bandwidth needs to be calculate considering the amount of the data transfer 

plt.plot(intervals, bandwidth)
plt.ylabel("bandwidth in Mb/s")
plt.xlabel("time in sec")
plt.title("Scenario I - UDP upload")
plt.show()
