# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 01:28:36 2021

@author: saulb
"""

import pandas as pd
songs = pd.read_csv("songs(2).csv")

import numpy as np
songs["index"] = np.array(range(len(songs)))


songs["lyrics"] = None

import json
from lyricsgenius import Genius
f = open('Genius.json')
token = json.load(f)["token"]
f.close()
genius = Genius(token)

def search_lyrics(name):
  try:
    song = genius.search_song(name)#per_page=1, sort="popularity"
    return song.lyrics
  except:
    return None

for index in range(len(songs)):
  songs["lyrics"][index] = search_lyrics(songs["song_name"][index]) 
  if(index%100 ==0):
      songs.to_csv("songs(4).csv")
songs.to_csv("songs(4).csv")