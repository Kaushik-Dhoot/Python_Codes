import pywhatkit
number = input('Enter the mobile number :')
number = '+91'+number
message = input('Enter the message to send :')
time = list(map(int, input('Enter the time in 24 hours:').split(':')))

pywhatkit.sendwhatmsg(number,message,time[0],time[1])
