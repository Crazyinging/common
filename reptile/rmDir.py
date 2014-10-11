#! /usr/bin/python
# coding: utf-8
import os
import shutil

'''
！！！
清理之前，记得先运行一遍DownloadRecord.py
'''

def rmDir(path0, filenum=0):

    path = os.path.abspath(path0)

    if not os.path.isdir(path):
        print 'in rmVoidDir: path error'
        return 

    rmnum   = 0
    dirnum  = 0
    dir1 = os.listdir(path)

    for c in dir1:
        path_c = os.path.join(path, c)
        if not os.path.isdir(path_c):
            continue

        dirnum += 1
        if len(os.listdir(path_c)) <= filenum:
            if len(os.listdir(path_c))> 0:
                shutil.rmtree(path_c)
            else:
                os.rmdir(path_c)
            print '成功删除%s'%(path_c)
            rmnum += 1

    print '发现%d个文件夹，删除%d个'%(dirnum, rmnum)




