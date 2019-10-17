import os

print("这次拥护啥:",end="")
reason = input()

os.system('git add .')
os.system('git commit -m\"auto'+reason+'\"')
os.system('git push -u origin master')






