import sys

print('The commmand line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

#可以通过运行import os;print(os.getcwd())来查看程序目前所在的目录
