# ymdhms_to_jd.py
# Access Python through CMD: cd Desktop\Phyton
# Clear Sreen on CMD: cls
#
# Usage: ymdhms_to_jd.py year month day hour minute second
#  Example: python3 ymdhms_to_jd.py 1970 1 1 12 0 0.0
#  Output: 
#          2440588.0
#           
# Parameters:
#  year month day hour minute second [integers except second], [second are decimals]
#  ...
# Output:
#  Fraction Julian Date
#
# Written by Ryo Jumadiao
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import math # math module
import sys # argv

# initialize script arguments

# Time variables
year = 0
month = 0
day = 0
hour = 0
minute = 0
second = 0.0

# parse script arguments
# How many arguments are passed to python -- 6 arguments pass 7
# Converts string to float

if len(sys.argv)==7:
    year = float(sys.argv[1])
    month = float(sys.argv[2])
    day = float(sys.argv[3])
    hour = float(sys.argv[4])
    minute = float(sys.argv[5])
    second = float(sys.argv[6])
    
else:
   print(\
    'Usage: '\
    'python3 ymdhms_to_jd.py year month day hour minute second'\
   )
   exit()

#======================================
JDt1 = year + 4800 + (month-14) / 12
JDt2 = month - 2 - (month-14) / 12 * 12
JDt3 = (year + 4900 + (month-14) / 12) / 100

JD = day - 32075 + 1461*JDt1/4 + 367*JDt2/12 - 3*JDt3/4

JDmid = JD - 0.5
Dfrac = (second + 60*(minute+60*hour))/86400

jd_frac = JDmid + Dfrac

#======================================
jd_frac = "%.1f" % math.floor(jd_frac)
print(jd_frac)