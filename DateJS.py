#!/usr/bin/env python3

import datetime
import pytz
from py_mini_racer import py_mini_racer

class DateJS():
    def __init__(self, JS_STRING):
        self.YEAR = 0
        self.MONTH = 0
        self.DATE = 0
        self.HOUR = 0
        self.MINUTE = 0
        self.SECOND = 0
        self.MILLISECONDS = 0
        self.TZ = None
        self.JS_TIME = JS_STRING
        self.PYTIME = datetime.datetime.now()
        self.SPLIT_JS_TIME = self.JS_TIME.split(" ")
        
    def setAllValues(self):
        self.setYear()
        self.setMonth()
        self.setDate()
        self.setHour()
        self.setMinute()
        self.setSecond()
        self.setMillisecond()
        self.setTZ()
    
    def naiveDatetime(self):
        self.PYTIME = self.PYTIME.replace(year=self.YEAR, month=self.MONTH, day=self.DATE, hour=self.HOUR, minute=self.MINUTE, second=self.SECOND, microsecond=self.MILLISECONDS, tzinfo=pytz.timezone(self.TZ))
    
    def setYear(self):
        js = py_mini_racer.MiniRacer()
        js.eval(" var f = (x) => new Date(x).getFullYear()")
        self.YEAR = js.call("f", self.JS_TIME)
        return

    def setMonth(self):
        js = py_mini_racer.MiniRacer()
        js.eval(" var g = (x) => new Date(x).getMonth()")
        self.MONTH = js.call("g", self.JS_TIME) + 1 # This +1 moves month numbers from 0-11 to 1-12
        return
    
    def setDate(self):
        js = py_mini_racer.MiniRacer()
        js.eval(" var h = (x) => new Date(x).getDate()")
        self.DATE = js.call("h", self.JS_TIME)
        return
    
    def setHour(self):
        js = py_mini_racer.MiniRacer()
        js.eval(" var i = (x) => new Date(x).getHours()")
        self.HOUR = js.call("i", self.JS_TIME)
        return
    
    def setMinute(self):
        js = py_mini_racer.MiniRacer()
        js.eval(" var j = (x) => new Date(x).getMinutes()")
        self.MINUTE = js.call("j", self.JS_TIME)
        return

    def setSecond(self):
        js = py_mini_racer.MiniRacer()
        js.eval(" var p = (x) => new Date(x).getSeconds()")
        self.SECOND = js.call("p", self.JS_TIME)
        return
    
    def setMillisecond(self):
        js = py_mini_racer.MiniRacer()
        js.eval(" var w = (x) => new Date(x).getMilliseconds()")
        self.MILLISECONDS = js.call("w", self.JS_TIME)
        return
        
    def setTZ(self):
        js = py_mini_racer.MiniRacer()
        js.eval(" var k = (x) => new Date(x).getTimezoneOffset()")
        offset = js.call("k", self.JS_TIME)
        offset = self.offsetFormat(offset)
        sorted_tzs = self.allTimezones()
        for zone in sorted_tzs:
            if offset in zone[1]:
                self.TZ = zone[0]
                return
        raise Exception("No Timezone Found!")
    
    def offsetFormat(self, offset):
        west = True
        if offset == "-":
            west = False
        hours_offset = int(offset/60)
        if abs(hours_offset) < 10:
            hours_offset = "0" + str(hours_offset)
        minutes_offset = int(offset%60)
        if minutes_offset < 10:
            minutes_offset = "0" + str(minutes_offset)
        if west:
            return "-" + str(hours_offset) + str(minutes_offset)
        return str(hours_offset) + str(minutes_offset)
        
    def allTimezones(self):
        tz = [(item, datetime.datetime.now(pytz.timezone(item)).strftime('%z') + " " + item) for item in pytz.common_timezones]
        sorted_tzs = sorted(tz, key=lambda x: int(x[1].split()[0]))
        return sorted_tzs
    
    
d = DateJS("Thu Oct 19 2017 08:51:23 GMT-0400 (EDT)")
d.setAllValues()
d.naiveDatetime()
print(d.YEAR, d.MONTH, d.DATE, d.HOUR, d.MINUTE, d.SECOND, d.MILLISECONDS, d.TZ)
print(d.PYTIME)
