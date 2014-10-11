#! /usr/bin/python
# coding: utf-8



def getPart(str0, symbol, start_ts, end_ts, contain_boundary=False):
    '''
    用symbol字符对str0进行split，返回symbol第start_ts与第end_ts次出现之间的片段；
    如果contain_boundary为True，则对结果两侧加上必要的symbol字符。
    '''

    tmplist = str0.split(symbol)
    ans = []
    for i in range(start_ts, end_ts):
        ans.append(tmplist[i])
    ans = ('/').join(ans)

    if contain_boundary:
        if start_ts > 0:
            ans = symbol + ans
        if end_ts < len(tmplist):
            ans += symbol

    return ans


