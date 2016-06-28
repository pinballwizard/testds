import scipy
import matplotlib.pyplot as plt
import csv
import datetime
from matplotlib.dates import DayLocator, HourLocator, DateFormatter

def open_csv(filename):
    with open(filename, newline='') as csvfile:
        return list(csv.reader(csvfile, delimiter=';'))


def fix_24(item):
    date_increase = 0
    if '24:' in item[0]:
        item[0] = item[0].replace('24:00', '00:00')
        date_increase = 1
    item[0] = datetime.datetime.strptime(item[0], '%Y-%m-%d %H:%M') + datetime.timedelta(days=date_increase)
    return item


def all_for_day(day, dc):
    return []

if __name__ == '__main__':
    es = open_csv('ES.csv')[1:]
    # es = scipy.array(es)
    es = list(map(fix_24, es))
    dc = scipy.array(es)
    day_tuple = set([item[0].date() for item in dc])
    print(day_tuple)
    fig, ax = plt.subplots()
    ax.plot_date(dc[:, 0], dc[:,2])
    # ax.set_xlim(dc[0, 0], dc[-1, 0])
    # ax.xaxis.set_major_locator(DayLocator())
    # ax.xaxis.set_minor_locator(HourLocator(scipy.arange(0, 25, 6)))
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
    ax.autoscale_view()
    ax.grid()
    fig.autofmt_xdate()
    plt.show()

    # plt.plot(dc[:,0], dc[:,1])
    # print(dc[:,1])