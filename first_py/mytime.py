#!/usr/bin/python
# -*- coding: UTF-8 -*-
# coding:utf-8
import calendar
from datetime import datetime
import time;


print ("time.time() 当前时间戳为:", time.time());
print("time.localtime(time.time()) :",time.localtime(time.time()))
print("time.asctime(time.localtime(time.time())) :",time.asctime(time.localtime(time.time())))

print(time.strftime('%Y',time.localtime()))  #获取完整年份
print(time.strftime('%y',time.localtime()))  #获取简写年份
print(time.strftime('%m',time.localtime()))  #获取月
print(time.strftime('%d',time.localtime()))  #获取日
print(time.strftime('%Y-%m-%d',time.localtime()))  #获取年-月-日

print(time.strftime('%H',time.localtime()))  #获取时，24小时制
print(time.strftime('%I',time.localtime()))  #获取时，12小时制
print(time.strftime('%M',time.localtime()))  #获取分
print(time.strftime('%S',time.localtime()))  #获取秒
print(time.strftime('%H:%M:%S',time.localtime()))  #获取时:分:秒

print(time.strftime('%a',time.localtime()))  #本地简化星期
print(time.strftime('%A',time.localtime()))  #本地完整星期
print(time.strftime('%b',time.localtime()))  #本地简化月份
print(time.strftime('%B',time.localtime()))  #本地完整月份
print(time.strftime('%c',time.localtime()))  #本地日期和时间表示

print(time.strftime('%j',time.localtime())) #一年中的第几天
print(time.strftime('%p',time.localtime())) #P.M等价符
print(time.strftime('%U',time.localtime())) #一年中的第几个星期，星期天为星期的开始
print(time.strftime('%w',time.localtime()))  #星期几,星期天为星期的开始
print(time.strftime('%W',time.localtime()))  #一年中的第几个星期，星期一为星期的开始
print(time.strftime('%x',time.localtime()))  #本地日期表示
print(time.strftime('%X',time.localtime()))  #本地时间表示
print(time.strftime('%Z',time.localtime()))  #当前时区
print(time.strftime('%%',time.localtime()))  #输出%本身
print(time.strftime('%Y-%m-%d %H:%M:%S %w-%Z',time.localtime())) 

strf_style = "%Y-%m-%d %H:%M:%S"
a4 = time.strftime(strf_style,time.localtime(time.time()))
print(a4)
a5 = time.strftime(strf_style,(2017,5,21,13,14,0,0,0,0))
print(a5)

def convert_time(time_str):
    str1 = time_str[-2:]  # 格式
    data = time_str[:-2]  # 时间
    if str1.lower() == "am" and int(time_str[-7:-5])==12:
        hour = "00"
        data = time_str[0:12] + hour + time_str[-5:-2]
    if str1.lower() == "pm":
        if int(time_str[-7:-5]) < 12 :
            hour = str(int(time_str[-7:-5])+12)
        else:  # int(time_str[-7:-5]) == 12
            hour = "12"
str1     data = time_str[0:12] + hour + time_str[-5:-2]
    str2 = time.mktime(time.strptime(data,"%d-%b-%Y %H:%M"))  # 转换为时间戳
    finally_result = str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(str2))) # 转换为指定格式
    return finally_result

restr1 convert_time("01-Jul-2018 11:52PM")
print(res)

a1 = time.time()
print(a1)
a2 = time.localtime(a1)
print(a2)
a3 = time.asctime(a2)
print(a3)
strf_style = "%Y-%m-%d %H:%M:%S"
a4 = time.strftime(strf_style,time.localtime(time.time()))
print(a4)
a5 = time.strftime(strf_style,(2017,5,21,13,14,0,0,0,0))
print(a5)
a6 = time.strptime(a5,strf_style)
print(a6)
a7 = time.mktime(a2)
print(a7) 

'''
格式  含义
%a  本地（locale）简化星期名称
%A  本地完整星期名称
%b  本地简化月份名称
%B  本地完整月份名称
%c  本地相应的日期和时间表示
%d  一个月中的第几天（01 - 31）
%H  一天中的第几个小时（24小时制，00 - 23）
%I  第几个小时（12小时制，01 - 12）
%j  一年中的第几天（001 - 366）
%m  月份（01 - 12）
%M  分钟数（00 - 59）
%p  本地am或者pm的相应符
%S  秒（01 - 61）
%U  一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。
%w  一个星期中的第几天（0 - 6，0是星期天）
%W  和%U基本相同，不同的是%W以星期一为一个星期的开始。
%x  本地相应日期
%X  本地相应时间
%y  去掉世纪的年份（00 - 99）
%Y  完整的年份
%Z  时区的名字（如果不存在为空字符）
%%  ‘%’字符
'''
'''
time.strftime(fmt[,tupletime])   接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
time.altzone              返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
time.asctime([tupletime]) 接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
time.clock( )             用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
time.ctime([secs])        作用相当于asctime(localtime(secs))，未给参数相当于asctime()
time.gmtime([secs])       接收时间辍（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
time.localtime([secs])    接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。
time.mktime(tupletime)    接受时间元组并返回时间辍（1970纪元后经过的浮点秒数）。
time.sleep(secs)          推迟调用线程的运行，secs指秒数。
time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')   根据fmt的格式把一个时间字符串解析为时间元组。
time.time( )             返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
time.tzset()             根据环境变量TZ重新初始化时间相关设置。

calendar.calendar(year,w=2,l=1,c=6)  返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
calendar.firstweekday( )             返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。
calendar.isleap(year)                是闰年返回True，否则为falstr1
calendar.leapdays(y1,y2)             返回在Y1，Y2两年之间的闰年总数。
calendar.month(year,month,w=2,l=1)   返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
calendar.monthcalendar(year,month)   返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
calendar.monthrange(year,month)      返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。
calendar.prcal(year,w=2,l=1,c=6)     相当于 print calendar.calendar(year,w,l,c).
calendar.prmonth(year,month,w=2,l=1) 相当于 print calendar.calendar（year，w，l，c）。
calendar.setfirstweekday(weekday)    设置每周的起始日期码。0（星期一）到6（星期日）。
calendar.timegm(tupletime)           和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间辍（1970纪元后经过的浮点秒数）。
calendar.weekday(year,month,day)     返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。
'''
#calendar.firstweekday返回当前每周起始日期的设置。默认情况下，首次载入calendar模块时返回0，即星期一。
print(calendar.firstweekday())

#calendar.setfirstweekday设置每周的起始日期码。0（星期一）到6（星期日）。
calendar.setfirstweekday(1)
print(calendar.firstweekday())


# calendar.isleap是闰年返回True，否则为false。
print(calendar.isleap(2017))

print(calendar.isleap(2020))


#calendar.leapdays返回在两年之间的闰年总数，但不包括末年
print(calendar.leapdays(2016,2020))
print(calendar.leapdays(2016,2021))


#calendar.monthcalendar返回一个整数的单层嵌套列表，每个子列表装载代表一个星期，月外的日期设为0
print(calendar.monthcalendar(2017,10))

print(calendar.month(2017,10))

#calendar.monthrange返回两个整数，第一个为该月的首日的星期（0-6），第二个为该月的总天数
print(calendar.monthrange(2017,10))


#calendar.timegm接受一个时间元组形式struct_time，返回该时刻的时间辍（1970纪元后经过的浮点秒数）
print(calendar.timegm((2017,10,19,14,50,0,0,0,0)))

print(calendar.timegm((2017,10,19,14,50,50,0,0,0)))

print(time.localtime(time.time()))

#calendar.weekday返回给定日期的星期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。
print(calendar.weekday(2017,10,19))
3
print(calendar.weekday(2017,10,20))

#time.altzone
#返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
print(time.altzone)

#time.asctime([tupletime])
#接受时间元组并返回一个可读的形式为"Thu Oct 19 15:07:31 2017"（2017年10月19日 周四15时07分31秒）的24个字符的字符串。
print(time.asctime(time.localtime()))


#time.clock()
#用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
def procedure():
    time.sleep(2.5)
procedure()

#time.ctime()作用相当于asctime(localtime(secs))，未给参数相当于asctime()
print(time.ctime())
print(time.asctime(time.localtime()))
print(time.asctime())

#time.gmtime()以元组方式返回格林威治时间
print(time.gmtime())

#time.localtime()以元组方式返回本地当前时间
print(time.localtime())

#time.mktime()将元组时间转换为时间戳
x = time.localtime()
print(x)
print(time.mktime(x))

#time.strftime(fmt[,tupletime])
#接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

print(datetime.now())
























