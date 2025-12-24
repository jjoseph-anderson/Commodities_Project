from ORE import *

print ("Loading parameters...")
params = Parameters()
print ("   params is of type", type(params))
params.fromFile(r"C:\Users\josep\Desktop\ORE-SWIG-master\ORE-SWIG-master\OREAnalytics-SWIG\Python\Examples\Input\ore.xml")
print ("   setup/asofdate = " + params.get("setup","asofDate"))

print ("Building OREApp...")
ore = OREApp(params)
print ("   ore is of type", type(ore))

ore.run()
print ("ORE process done");

analytic = ore.getAnalytic("NPV")
print("Got the NPV analytic")

market  = analytic.getMarket()
print ("Got market object built by the NPV analytic");
asof = market.asofDate();
print ("Market asof date is", asof)

ccy = "EUR"
index = "EUR-EURIBOR-6M"

print ("Get term structures for ccy ", ccy, "and index", index);

discountCurve = market.discountCurve(ccy)
print ("   discount curve is of type", type(discountCurve))

iborIndex = market.iborIndex(index)
print ("   ibor index is of type", type(iborIndex))

forwardCurve = iborIndex.forwardingTermStructure()
print ("   forward curve is of type", type(forwardCurve))

date = asof + 10*Years;
zeroRateDc = Actual365Fixed()

discount = discountCurve.discount(date)
zero = discountCurve.zeroRate(date, zeroRateDc, Continuous)

fwdDiscount = forwardCurve.discount(date)
fwdZero = forwardCurve.zeroRate(date, zeroRateDc, Continuous)

print ("   10y discount factor (discount curve) is", discount)
print ("   10y discout factor (forward curve) is", fwdDiscount)

print ("   10y zero rate (discount curve) is", zero)
print ("   10y zero rate (forward curve) is", fwdZero)

dc = Actual365Fixed()

# date grid
dates = []
times = []
zeros1 = []
zeros2 = []
date = asof
previousDate = asof
for i in range (1,10*53):
    date = date + Period(1, Weeks);
    time = dc.yearFraction(asof, date)
    dates.append(date)
    times.append(time)
    zero1 = discountCurve.forwardRate(previousDate, date, zeroRateDc, Continuous).rate()
    zero2 = forwardCurve.forwardRate(previousDate, date, zeroRateDc, Continuous).rate()
    zeros1.append(zero1)
    zeros2.append(zero2)
    previousDate = date
    #print (date, time, zero1, zero2)

#print(times)

import matplotlib.pyplot as plt
import numpy as np

plt.plot(times, zeros1, label='discount')
plt.plot(times, zeros2, label='forward')
plt.xlabel('Time/Years')
plt.ylabel('Rate')
plt.title('Discount and Forward Curve')
plt.legend()
plt.show()