import os

os.popen("gitbook build").readlines()
os.popen("cp -R _book/* ../_book/").readline()
os.popen("git pull").readline()
os.popen("cd ../_book").readline()
os.popen("git checkout gh-pages").readline()
os.popen("git add .").readline()
message = input("输入你的上传备注")
os.popen("git commit -m {message}".format(message=message)).readline()
os.popen("git push origin gh-pages")
