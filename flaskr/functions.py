import sched
import time

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

scheduler = sched.scheduler(time.time, time.sleep)
initial = time.time()
currentTime = {}
iterator = 1

def testSched():
    # testAlpha()
    # scheduler.enter(5, 1, testSched, ())  
    present = time.time()-initial
    currentTime.update( { ('ITERATION ' + str(iterator)): present} )
    # iterator+=1
    print("From print_time", present)

def testAlpha():
    ts = TimeSeries(key='apiKey', output_format='json')
    data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='compact')
    # data['close'].plot()
    # plt.title('Intraday Times Series for the MSFT stock (1 min)')
    # plt.show()
    print(data["2019-08-27 12:12:00"])

def printTimes():
    currentTime.update( {'START': initial} )
    global iterator
    while iterator < 6:
        scheduler.enter(1, 1, testSched, ())
        scheduler.run()
        iterator+=1
    currentTime.update( {'END': time.time()} )
    total = currentTime['END'] - currentTime['START']
    currentTime.update( {'TOTAL TIME': total} )
    return currentTime
