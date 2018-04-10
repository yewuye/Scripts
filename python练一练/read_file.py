#! usr/bin/env python
# encoding:utf-8

try:
    f = open(r'/home/qianran/下载/py/文件分类脚本.py', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 更简洁的办法with
# with open(r'filepath', 'r'):
#     print(f.read())
# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
