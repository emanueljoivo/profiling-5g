import matplotlib.pyplot as plt
import csv
import sys

def to_mega(b):
    return b / (10**6)
    
def is_empty(v):
    return len(v) == 0

# py plotter.py protocol test_type device
if len(sys.argv) < 4:
    print("usage:\nplotter.py <protocol> <test_type> <device>")
    sys.exit(1)
else:
    protocol = str(sys.argv[1])
    test_type = str(sys.argv[2])
    device = str(sys.argv[3])

    intervals = []
    data_transfer = []
    bandwidth = []

    file_location = "data/{}_{}_{}.csv".format(protocol, test_type, device)

    with open(file_location) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        if protocol == "tcp":
            for row in csv_reader:
                bandwidth.append(to_mega(int(row[-1])))
                data_transfer.append(to_mega(int(row[-2])))
                intervals.append(row[-3])
        elif protocol == "udp":
            for row in csv_reader:
                bandwidth.append(to_mega(int(row[-6])))
                data_transfer.append(to_mega(int(row[-7])))
                intervals.append(row[-8])

    if is_empty(intervals) or is_empty(data_transfer) or is_empty(bandwidth):
        print("no valid data")
        sys.exit(1)

    results = [intervals.pop(), data_transfer.pop(), bandwidth.pop()]
    intervals = list(map(lambda interval: float(interval.split("-")[-1]), intervals))

    plt.plot(intervals, bandwidth)
    plt.ylabel("bandwidth in Mb/s")
    plt.xlabel("time in sec")
    plt.title("{} {} - {}".format(protocol, test_type, device))
    plt.show()
