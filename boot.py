# This file is executed on every boot (including wake-boot from deepsleep)

#import esp

#esp.osdebug(None)

exec(open('./numbers.py').read(),globals())
exec(open('./temperature.py').read(),globals())

exec(open('./main.py').read(),globals())

