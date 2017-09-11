# http://www.pythonchallenge.com/
import re
import string
from urllib2 import urlopen


# Level 1
# http://www.pythonchallenge.com/pc/def/map.html
def map():
    # decode a string message#
    message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. " \
              "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. " \
              "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    result = ''
    for c in message:
        # Using the chr() and ord() values in python.
        # But need to
        # 1. 2. make this circular; calculate it's distance from 'a'
        # (ord(c) + 2) - ord('a')
        # 2. Deal with > 26; if it is larger than 26, go back to the beginning
        # (ord(c) + 2) - ord('a')) % 26
        #   and add to 'a'
        # chr(((ord(c) + 2) - ord('a')) % 26 + ord('a'))
        if c >= 'a' and c <= 'z':
            result += chr(((ord(c) + 2) - ord('a')) % 26 + ord('a'))
        else:
            result += c
    print result
    #  translated clue to use string.maketrans()
    mapper = string.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab");
    print '\nUsing string.maketrans(raw, encodemap):\n', message.translate(mapper)
    # need to use mapper for the html as suggested.
    print 'map'.translate(mapper)


# Level 2
# http://www.pythonchallenge.com/pc/def/ocr.html
def ocr():
    from collections import Counter
    # use a counter, but now out of order....
    text = open('level2.txt', 'rb+').read()
    print Counter(text).most_common()[-10:]

    # regex it!
    print "".join(re.findall("[A-Za-z]", text))

    # don't even need a second file!
    html = urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()
    # The pattern <!--(.*)--> will capture all blocks inside <!-- and -->.
    # We only care about the last part, thus [-1]
    comments = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]
    print "".join(re.findall("[A-Za-z]", comments))


# Level 3
# http://www.pythonchallenge.com/pc/def/equality.html

def equality():
    # [a - z]: 1 lower case letter
    # [A - Z]: 1 upper case letter
    # [A - Z] {3}: 3 consecutive upper case letters
    # [A - Z] {3}[a - z][A - Z] {3}:
    # 3 consecutive upper case letters
    # 1 lower case letter
    # 3 consecutive upper case letters
    # [ ^ A - Z]: any character BUT upper case letter
    # [ ^ A - Z]+: at least one such character

    # [ ^ A - Z]+[A - Z] {3} [a - z][A - Z]  {3}[ ^ A - Z]+:

    html = urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
    comments = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]
    print "".join(re.findall("[^A-Z]+"
                             "[A-Z]{3}([a-z])[A-Z]{3}"
                             "[^A-Z]+", comments))


# Level 4
# http://www.pythonchallenge.com/pc/def/linkedlist.php

def linkedlist():
    # mimicking the url php
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
    # from the source code!
    # num = "12345"
    # What we are directed to do!
    num = 16044 / 2

    # Content pattern we are matching and extracting the next 'nothing' from
    s_pattern = re.compile("and the next nothing is (\d+)")

    while True:
        content = urlopen(url % num).read().decode('utf-8')
        print content
        next = s_pattern.search(content)
        # next = re.search("and the next nothing is (\d+)", content).group(1)
        # # next = <_sre.SRE_Match object; span=(0, 29), match='and the next nothing is 44827'>
        # # Note .group(0) will return the whole text that matches the pattern,
        # # while the captured segments start from .group (1)

        if next == None:
            break
        num = next.group(1)


# Level 5
# http://www.pythonchallenge.com/pc/def/peak.html

def peak():
    # source :
    # <br> < peakhell src = "banner.p" / >  < / body > < / html >
    #
    # < !-- peak  hell  sounds  familiar ? -->
    #
    # "peak hell" apparently this is supposed to sound like pickle

    url = "http://www.pythonchallenge.com/pc/def/peak.html"
    html = urlopen(url).read()
    print html

    # .decoed() didn't help us! So one needs to deserialize it!
    # 'getit peak hell <==> pickle
    import pickle

    url2 = "http://www.pythonchallenge.com/pc/def/banner.p"

    bannerfile = pickle.load(urlopen(url2))
    print bannerfile[0:20]
    # returned a string of tuples for each line:
    # ASCII ART!
    # [[(' ', 95)], [(' ', 14), ('#', 5), (' ', 70), ('#', 5),...
    for line in bannerfile:
        print("".join([a * b for a, b in line]))


# Level 6
# http://www.pythonchallenge.com/pc/def/channel.html
def channel():
    print " < html > <!-- < -- zip -->, " \
          "so replace unzip and download http://www.pythonchallenge.com/pc/def/channel.zip"

if __name__ == '__main__':
    # map()         # Level 1
    # ocr()         # Level 2
    # equality()    # Level 3
    # linkedlist()  # Level 4
    # peak(         # Level 5
    channel()  # Level 6
