import time
import webbrowser

totalBreaks = 3

print ("Break Time program has started on {}".format (time.ctime ()))
while totalBreaks > 0:
    time.sleep (10)
    webbrowser.open ("https://udacity.com/course/programming-foundations-with-python--ud036")
    totalBreaks -= 1
