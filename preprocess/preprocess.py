from Reuters import *
data_streamer = ReutersStreamReader('reuters')
import pandas as pd
doc_list = list(data_streamer.iterdocs())
df = pd.DataFrame(doc_list)

import os
dir_name = '../dataset'
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

df.to_pickle(dir_name + '/dataset.plk')