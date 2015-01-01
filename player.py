#!/usr/bin/env python
#coding:utf-8

import subprocess

import redis

from doubanFM import DoubanFM


class Player:
    def __init__(self):
        self.r = redis.Redis()
        self.doubanfm = DoubanFM()

    def play(self):
        while True:
            song_url = self.r.rpop('song_list')
            if song_url is None:
                self.doubanfm.get_song_list()
                continue

            print song_url
            self.to_fm(song_url)

    def to_fm(self, song_url):
        subprocess.call('mpg123 -m -C -q -s %s | ./pifm - 101.1 ' % song_url, shell=True)


if __name__ == "__main__":
    player = Player()
    player.play()
