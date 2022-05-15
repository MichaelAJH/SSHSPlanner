import os
from datetime import datetime
import pickle

global cal, frame
cal = dict()
frame = []
year, month =  datetime.now().year, datetime.now().month
def ConfigureFrame():
    frame[0] = [str(year)+'.'+str(month)]
    frame[1] = ['\t', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    for t in range(8, 24):
        frame[t-6] = [None]*8
        frame[t-6][0] = str(t)+':00'
def CallFrame(year, month, week):
    for root, dir, files in os.walk('./'):
        for file in files:
            if file == f'frame{year}_{month}_{week}':
                with open(file, 'rb') as f:
                    frame = pickle.load(f)                  # call frame as Frame
def CallCalendar(year, month, week):
    for root, dir, files in os.walk('./'):
        for file in files:
            if file == f'calendar{year}_{month}_{week}':
                with open(file, 'rb') as f:
                    cal = pickle.load(f)
def CreateEvent(name, date, start, end, describtion=''):
    if name in cal.keys:
        return -1
    else:
        cal[name] = (date, start, end, describtion)
        for t in range(str(start)[:-3]):
            frame[t-6][datetime.]
        return None
def DeleteEvent(name):
    if name in cal.keys:
        del cal[name]
        return None
    else:
        return -1
def ShowFrame(calendar, week = None):
    print(frame[0])
def Confirm():
    global fin
    fin = cal
def SaveCalendar(frame, fin):
    with open(f'frame{y}_{m}_{w}.pickle', 'wb') as f:
        f.dump(frame, f)
    with open(f'calendar{y}_{m}_{w}.pickle', 'rb') as cl:
        f.dump(fin, cl)
def PrintCalendar(year, month, week):