
# coding: utf-8

# # 例1.1（配列表現）
# 村松正吾　「多次元信号・画像処理の基礎と展開」
# 
# 動作確認： Python 3.6
# 
# Copyright (c) Shogo MURAMATSU, 2018
# All rights reserved

# In[1]:


import sys
sys.path.append('../../')
import msip


# ##画像のダウンロード

# In[2]:


msip.download_img(True)


# %% (a) グレースケール画像
# %%
# fprintf('(a) グレースケール画像\n')
# V = imread('./data/barbara.png');
# fprintf('配列次元： D = %d\n',ndims(V))
# imshow(V)
# %% (b) RGB画像
# %%
# fprintf('(b) RGB画像\n')
# V = imread('./data/lena.png');
# fprintf('配列次元： D = %d\n',ndims(V))
# imshow(V)
# %% (c) 動画像
# %%
# fprintf('(c) RGB動画像\n')
# vrObj = VideoReader('shuttle.avi');
# V = zeros(vrObj.Height,vrObj.Width,3,2,'uint8');
# V(:,:,:,1) = readFrame(vrObj);
# V(:,:,:,2) = readFrame(vrObj);
# fprintf('配列次元： D = %d\n',ndims(V))
# imshow(V(:,:,:,1))
# title('第0フレーム')
# imshow(V(:,:,:,2))
# title('第1フレーム')
# %% (d) ボリュームデーデータ
# %%
# fprintf('(d) ボリュームデータ\n')
# load mri
# V = squeeze(D);
# fprintf('配列次元： D = %d\n',ndims(V))
# imshow(V(:,:,1))
# title('第0スライス(xy)')
# imshow(V(:,:,2))
# title('第1スライス(xy)')
