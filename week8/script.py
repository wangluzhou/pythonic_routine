import os

result = os.popen("gitbook build").readlines()
result2 = os.popen("cp -R _book/* ../_book/*").readline()
