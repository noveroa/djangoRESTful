# http://www.pythonchallenge.com/
import re
import string
from urllib2 import urlopen


# Level 1
# http://www.pythonchallenge.com/pc/def/map.html
def mapthis():
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

import zipfile
def channel():
    file = zipfile.ZipFile("channel.zip")
    print " < html > <!-- < -- zip -->, " \
          "so replace unzip and download http://www.pythonchallenge.com/pc/def/channel.zip"
    print file.read('readme' + ".txt").decode("utf-8")

    start = 90052
    comments = []

    s_pattern = re.compile("Next nothing is (\d+)")
    while True:
        content = file.read(str(start) + ".txt").decode("utf-8")
        # print(content)
        # How to access objects within a zipped file!!
        # https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.comment
        comments.append(file.getinfo(str(start) + ".txt").comment.decode("utf-8"))
        next = s_pattern.search(content)

        if next == None:
            break
        start = next.group(1)

    print "".join(comments)


# Level 7
# http://www.pythonchallenge.com/pc/def/oxygen.html
def oxygen():
    # You see a image with a grayscale so try accessing it and getting info from there?
    import requests
    from io import BytesIO
    from PIL import Image
    img = Image.open(BytesIO(requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png').content))
    print 'Basic image stuff: \n', img.width, img.height, \
        img.getpixel((0, 0)), '<== the pixels are a tuple of (R, G, B, alpha).'
    # to get gray scale, we need the pixels for for each in the the gray scale image row pixel by pixel
    row = [img.getpixel((x, img.height / 2)) for x in range(img.width)]
    # the row  has duplicates, since each block is greater than 1x1:
    # [(115, 115, 115, 255), (115, 115, 115, 255), (115, 115, 115, 255), ..
    # each is 7 wide:
    row = row[::7]  # skip by 7s
    # now let's map characters again!
    ords = [r for r, g, b, a in row if r == g == b]
    print "".join(map(chr, ords))
    newrow = [105, 110, 116, 101, 103, 114, 105, 116, 121]
    print "".join(map(chr, newrow))


# Level 8
# http://www.pythonchallenge.com/pc/def/integrity.html
def integrity():
    """< !--
    un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    -->"""
    html = urlopen("http://www.pythonchallenge.com/pc/def/integrity.html").read().decode()
    # The pattern <!--(.*)--> will capture all blocks inside <!-- and -->.
    # We only care about the last part, thus [-1]
    comments = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]
    print comments
    un = comments.split("'")[1]
    pw = comments.split("'")[3]
    print un
    print pw
    import bz2

    print bz2.decompress(
        b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
    print bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

if __name__ == '__main__':
    # mapthis()         # Level 1
    # ocr()         # Level 2
    # equality()    # Level 3
    # linkedlist()  # Level 4
    # peak(         # Level 5
    # channel()     # Level 6
    # oxygen()      # Level 7
    integrity()  # Level 8
    # good()        # Level 9
