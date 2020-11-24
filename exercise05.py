"""
    编写一个程序删除、/home/tarena/图片文件夹中所有大不到10kb的普通文件
"""
import os
list_picture=os.listdir("/home/tarena/图片/")
for i in list_picture:
    filename= "/home/tarena/图片/"+i
    if os.path.getsize(filename)<10*1024 and os.path.isfile(filename):
        os.remove(filename)