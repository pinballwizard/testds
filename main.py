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
    item[1] = float(item[1])
    item[2] = float(item[2])
    item[0] = datetime.datetime.strptime(item[0], '%Y-%m-%d %H:%M') + datetime.timedelta(days=date_increase)
    return item


def all_for_day(date, dc):
    return scipy.array([item for item in dc if item[0].date() == date])


def my_plot(*data):
    fig, ax = plt.subplots()
    ax.plot_date(*data, '-')
    # ax.set_xlim(dc[0, 0], dc[-1, 0])
    # ax.xaxis.set_major_locator(DayLocator())
    # ax.xaxis.set_minor_locator(HourLocator(scipy.arange(0, 25, 6)))
    # ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
    ax.autoscale_view()
    ax.grid()
    fig.autofmt_xdate()


def correlation_search():
    first_day = all_for_day(min_date, dc)
    mfd = scipy.mat(first_day[:, 2]).T
    mdc = scipy.mat(dc[:, 2])
    correlation = scipy.sum(mfd * mdc, 0)/len(dc)
    return correlation.T

if __name__ == '__main__':
    es = open_csv('ES.csv')[1:]
    es = list(map(fix_24, es))
    dc = scipy.array(es)
    date_tuple = set([item[0].date() for item in dc])
    min_date = min(date_tuple)

    dc1 = all_for_day(min_date, dc)
    # my_plot(dc1[:, 0], dc1[:, 2])

    dc2 = all_for_day(min_date+datetime.timedelta(days=21), dc)
    # my_plot(dc2[:, 0], dc2[:, 2])
    # print(len(dc1[:,2]))
    corr = correlation_search()
    # print(dc[:, 0])
    # print(scipy.ravel(corr.T))
    my_plot(dc[:, 0], corr)
    my_plot(dc[:, 0], dc[:, 2]-corr)
    plt.show()