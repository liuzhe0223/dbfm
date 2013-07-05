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
            self.song_list = self.r.get('song_list')
            for song_url in song_list:
                self.to_fm(song_url)
            self.doubanfm.get_song_list()

    def to_fm(self, song_url):
        subprocess.call('mpg123 -m -C -q -s %s | pifm - 101.1 44100',shell=True)


if __name__ == "__main__":
    player = Player()
    player.play()