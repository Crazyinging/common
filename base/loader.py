# coding: utf-8
import os, sys

def loadconf(HOME):
    '''加载模块的搜索路径，以及使用指定配置文件'''

    # 加载库文件
    # 默认加载项目路径下得lib和conf模块
    paths = [os.path.join(os.path.dirname(HOME), 'lib'),
             os.path.join(os.path.dirname(HOME), 'conf'),
             os.path.dirname(HOME)
             ]

    for path in paths:
        sys.path.append(path)

    # 若有参数表明是指定配置文件、则使用指定配置文件
    if len(sys.argv) == 2:
        config_file = 'config_' + sys.argv[1]
        sys.modules['config'] = __import__(config_file)
    
