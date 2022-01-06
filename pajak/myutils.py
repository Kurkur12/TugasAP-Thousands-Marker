from time import ctime

from django.http import response


def number_of_vowels(s):
    vowels = 'aiueo'
    c = 0
    for i in s.lower():
        if i in vowels:
            c = c + 1
    return c

def number_of_consonants(a):
    consonants = 'qwrtypsdfghjklzxcvbnm'
    m = 0
    for i in a.lower():
        if i in consonants:
            m = m + 1
    return m

def showDate():
    now    = ctime()
    _day   = now[0:3]
    _month = now[4:7]
    _date  = now[8:10]
    _time  = now[11:19]
    _year  = now[20:24]
    sekarang = day[_day]+" "+ _date +" "+ month[_month] +" "+ _year +" Pukul "+" "+ _time
    return sekarang


day = {'Mon' : 'Senin',
        'Tue' : 'Selasa',
        'Wed' : 'Rabu',
        'Thu' : 'Kamis',
        'Fri' : 'Jumat',
        'Sat' : 'Sabtu',
        'Sun' : 'Minggu'}

month = {'Jan' : 'Januari',
        'Feb' : 'Februari',
        'Mar' : 'Maret',
        'Apr' : 'April',
        'May' : 'Mei',
        'Jun' : 'Juni',
        'Jul' : 'Juli',
        'Aug' : 'Agustus',
        'Sep' : 'September',
        'Oct' : 'Oktober',
        'Nov' : 'November',
        'Dec' : 'Desember'}


def thousandsMaker(x):
    a = (f"{x:,}" .replace(',', '.'))
    str(a)
    return a


brackets = {       0:0,
             1000000:5,
             3000000:10,
             6000000:15,
            10000000:20,
            20000000:25,
            35000000:30,
            55000000:35,
            80000000:40,
          }
def calculateTax(param):
    lPoint,lPercent,totalTax, has, totalBracket, resultData = 0, 0, 0, param, len(brackets), []
    for enum,(key,item) in enumerate(brackets.items(),1):
        lOc = key - lPoint
        if lOc > 0 :
            if has > lOc:
                added = lOc * lPercent / 100
                totalTax += added
                resultData.append((str(thousandsMarkerCur(lPoint))+" ⎯⎯ "+str(thousandsMarkerCur(key)),(str(lPercent)+"%"), thousandsMarkerCur(int(added))))
                has -= lOc
            else:
                added = has * lPercent / 100
                totalTax += added
                resultData.append((str(thousandsMarkerCur(lPoint))+" ⎯⎯ "+str(thousandsMarkerCur(key)),(str(lPercent)+"%"), thousandsMarkerCur(int(added))))
                has = 0
            if enum == totalBracket:
                added = has * item / 100
                totalTax += added
                resultData.append((str(thousandsMarkerCur(key))+" ⎯⎯ ...", (str(item)+"%"), thousandsMarkerCur(int(added))))
        lPercent = item
        lPoint = key
    return resultData

def thousandsMarker(param):
    reversed = str(param)[::-1]
    result =  '.'.join(reversed[x:x+3] for x in range(0, len(reversed), 3))
    return result[::-1]

def thousandsMarkerCur(param):
    reversed = str(param)[::-1]
    result =  '.'.join(reversed[x:x+3] for x in range(0, len(reversed), 3))
    return "Rp "+str(result[::-1])