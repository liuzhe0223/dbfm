#!/usr/bin/env python
#coding:utf-8

import json
import urllib
import redis
import config

class DoubanFM:
    def __init__(self):
        self.r = redis.Redis()

        try:
            self.get_pass()             #获取豆瓣认证相关
        except:
            print "failed to get pass"
            exit()
        try:
            self.get_song_list()
        except:
            print "failed to get songs list"
            exit()

    def get_song_list(self):
        params = urllib.urlencode({
            'app_name':'radio_desktop_win',
            'version':100,
            'user_id':self.r.get('user_id'),
            'expire':self.r.get('expire'),
            'token':self.r.get('token'),
            'type':'n',
            'channel':0,
            })

        j_str = urllib.urlopen('http://www.douban.com/j/app/radio/people?%s' % params).read()
        j = json.loads(j_str)
        song_list=[]
        for song in j['song']:
            song_list.append(song['url'])

        print song_list

        self.r.set('song_list',song_list)



    def get_pass(self):
        params = urllib.urlencode({
            'app_name':'radio_desktop_win',
            'version':100,
            'email':config.email,
            'password':config.password,
            })

        j_str = urllib.urlopen('http://www.douban.com/j/app/login',params).read()
        print j_str
        j = json.loads(j_str)

        self.r.set('user_id',j['user_id']) 
        self.r.set('expire',j['expire'])
        self.r.set('token',j['token'])


if __name__ == "__main__":
    d = DoubanFM()