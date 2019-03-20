import sys
#异常处理-ZeroDivisionError:
#raise 抛出异常
try:
    x = int(input('Plase enter a number'))
    y = 10/x
    print('result:',y)
except ZeroDivisionError as err:
    print('x is not 0',err)
    raise
finally:
    print('mast run')

#异常处理-
try:
    x = int(input('Plase enter a number'))
    y = 10/x
    print('result:',y)
except OSError  as err:
    print('err is oserror',err)
    raise
except:
    print('Unexpect error:',sys.exc_info()[0])
