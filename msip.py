"""MSIPモジュール
村松正吾　「多次元信号・画像処理の基礎と展開」

サンプルスクリプト用のユーティリティ

Copyright (c) Shogo MURAMATSU, 2018
All rights reserved
"""
import os.path
from PIL import Image
from urllib.request import urlopen

class MsipException(Exception):
    """MSIP例外クラス
    """
    def __init__(self, message):
        Exception.__init__(self, message)

def download_img(isVerbose=True):
    """download_img
    画像サンプルをダウンロード
    """
    dstdir = '../../data/'
    if os.path.isdir(dstdir):
        fnames = [ 'lena', 'baboon', 'goldhill', 'barbara' ]
        for idx in range(len(fnames)):
            fname = fnames[idx] + '.png'
            if not os.path.isfile('{0}{1}'.format(dstdir,fname)):
                url = 'http://homepages.cae.wisc.edu/~ece533/images/{0}'.format(fname)
                img = Image.open(urlopen(url))
                img.save('{0}{1}'.format(dstdir,fname))
                if isVerbose:
                    print('Downloaded and saved {0} in {1}'.format(fname,dstdir))
            else:
                if isVerbose:
                    print('{0} already exists in {1}'.format(fname,dstdir))
    else:
        me = MsipException('Folder {0} does not exist'.format(dstdir))
        raise me


def ipynb2py(fname, isVerbose=True):
    """ipynb2py
    Notebook を Python スクリプトに変換
    """
    if not os.path.isfile('{0}.py'.format(fname)):
        os.system('jupyter nbconvert --to python {0}.ipynb'.format(fname))
        if isVerbose:
            print('Convert notebook {0}.ipynb to python script.'.format(fname))
    else:
        print('File {0}.py exists.'.format(fname))
