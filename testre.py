import re
ss = "/images/branding/googleg/1x/googleg_standard_color_128dp.png"
print ss
gg = re.search(r'google',ss)
print gg.group();exit()