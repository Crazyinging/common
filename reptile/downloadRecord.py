#! /usr/bin/python
# coding: utf-8

import os, sys, json




def record(dirpath):
    '''
    记录爬虫下载过的文件夹（注意了，是文件夹），可以当每次爬虫程序终止时运行一次。
    记录的内容不会减少，既不删除过往的记录。
    '''

    path = os.path.join(dirpath, 'DownloadRecord.json')

    if not os.path.isfile(path):
        with open(path, 'w+') as f:
            print u'文件%s不存在'%(path)
            print u'创建%s成功'%(path)
            tmp = ['just for temp']
            f.write(json.dumps(tmp))

    records = []
    with open(path, 'r+') as f:
        records = json.load(f)
    before  = len(records)

    dir0 = os.listdir(os.path.dirname(path))
    for d in dir0:
        c = d.decode('utf-8')
        if os.path.isdir(os.path.join(dirpath, c)) and c not in records:        #  c一定是utf-8么？？？
            records.append(c)
    after   = len(records)

    with open(path, 'w+') as f:
        f.write(json.dumps(records))


    print u'文件%s更新成功。原含有%d个、现有%d个，新增%d个'%(os.path.basename(path), before, after, after-before)


#if __name__ == '__main__':
#    if len(sys.argv) != 2:
#        print 'param error1'
#
#    else:
#        dirpath = os.path.abspath(sys.argv[1])
#
#
#        tmp = recordDownload()
#        tmp.record(dirpath)



