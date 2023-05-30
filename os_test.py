import os
current_dirctory = os.getcwd()
print(current_dirctory)

folder_path ='D:\GITHUB\python practice'
result=os.listdir(folder_path)

print(result)

# os.mkdir('test')
#
os.rename('test','new-test')


