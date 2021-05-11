import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# make up some data
x = [datetime.datetime.now() + datetime.timedelta(minutes=i) for i in range(12)]
y = [i + random.gauss(0, 1) for i, _ in enumerate(x)]

# plot
plt.plot([], [])
plt.scatter(x, y)

# beautify the x-labels
plt.gcf().autofmt_xdate()
myFmt = mdates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_formatter(myFmt)

plt.show()
plt.close()
