#!/usr/bin/env python2
# News Websote Log Analysis Program
from loganaldb import get_loginfo

print("News Website Log Analysis Report")
print
print("----Most Popular Three Articles of All Time----")
for text in get_loginfo('1'):
    print(text[0])
print
print("----Most Popular Article Authors of All Time----")
for text in get_loginfo('2'):
    print(text[0])
print
print("----Days with More Than 1% of Requests Leading to Errors----")
for text in get_loginfo('3'):
    print(text[0])
