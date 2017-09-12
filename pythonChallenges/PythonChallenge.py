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


# Level 9
# http://www.pythonchallenge.com/pc/return/good.html
def good():
    from PIL import Image, ImageDraw

    first = [
        146, 399, 163, 403, 170, 393, 169, 391, 166, 386, 170, 381, 170, 371, 170, 355, 169, 346, 167, 335, 170, 329,
        170, 320, 170,
        310, 171, 301, 173, 290, 178, 289, 182, 287, 188, 286, 190, 286, 192, 291, 194, 296, 195, 305, 194, 307, 191,
        312, 190, 316,
        190, 321, 192, 331, 193, 338, 196, 341, 197, 346, 199, 352, 198, 360, 197, 366, 197, 373, 196, 380, 197, 383,
        196, 387, 192,
        389, 191, 392, 190, 396, 189, 400, 194, 401, 201, 402, 208, 403, 213, 402, 216, 401, 219, 397, 219, 393, 216,
        390, 215, 385,
        215, 379, 213, 373, 213, 365, 212, 360, 210, 353, 210, 347, 212, 338, 213, 329, 214, 319, 215, 311, 215, 306,
        216, 296, 218,
        290, 221, 283, 225, 282, 233, 284, 238, 287, 243, 290, 250, 291, 255, 294, 261, 293, 265, 291, 271, 291, 273,
        289, 278, 287,
        279, 285, 281, 280, 284, 278, 284, 276, 287, 277, 289, 283, 291, 286, 294, 291, 296, 295, 299, 300, 301, 304,
        304, 320, 305,
        327, 306, 332, 307, 341, 306, 349, 303, 354, 301, 364, 301, 371, 297, 375, 292, 384, 291, 386, 302, 393, 324,
        391, 333, 387,
        328, 375, 329, 367, 329, 353, 330, 341, 331, 328, 336, 319, 338, 310, 341, 304, 341, 285, 341, 278, 343, 269,
        344, 262, 346,
        259, 346, 251, 349, 259, 349, 264, 349, 273, 349, 280, 349, 288, 349, 295, 349, 298, 354, 293, 356, 286, 354,
        279, 352, 268,
        352, 257, 351, 249, 350, 234, 351, 211, 352, 197, 354, 185, 353, 171, 351, 154, 348, 147, 342, 137, 339, 132,
        330, 122, 327,
        120, 314, 116, 304, 117, 293, 118, 284, 118, 281, 122, 275, 128, 265, 129, 257, 131, 244, 133, 239, 134, 228,
        136, 221, 137,
        214, 138, 209, 135, 201, 132, 192, 130, 184, 131, 175, 129, 170, 131, 159, 134, 157, 134, 160, 130, 170, 125,
        176, 114, 176,
        102, 173, 103, 172, 108, 171, 111, 163, 115, 156, 116, 149, 117, 142, 116, 136, 115, 129, 115, 124, 115, 120,
        115, 115, 117,
        113, 120, 109, 122, 102, 122, 100, 121, 95, 121, 89, 115, 87, 110, 82, 109, 84, 118, 89, 123, 93, 129, 100, 130,
        108, 132, 110,
        133, 110, 136, 107, 138, 105, 140, 95, 138, 86, 141, 79, 149, 77, 155, 81, 162, 90, 165, 97, 167, 99, 171, 109,
        171, 107, 161,
        111, 156, 113, 170, 115, 185, 118, 208, 117, 223, 121, 239, 128, 251, 133, 259, 136, 266, 139, 276, 143, 290,
        148, 310, 151,
        332, 155, 348, 156, 353, 153, 366, 149, 379, 147, 394, 146, 399]

    second = [156, 141, 165, 135, 169, 131, 176, 130, 187, 134, 191, 140, 191, 146, 186, 150, 179, 155, 175, 157, 168,
              157, 163, 157, 159,
              157, 158, 164, 159, 175, 159, 181, 157, 191, 154, 197, 153, 205, 153, 210, 152, 212, 147, 215, 146, 218,
              143, 220, 132, 220,
              125, 217, 119, 209, 116, 196, 115, 185, 114, 172, 114, 167, 112, 161, 109, 165, 107, 170, 99, 171, 97,
              167, 89, 164, 81, 162,
              77, 155, 81, 148, 87, 140, 96, 138, 105, 141, 110, 136, 111, 126, 113, 129, 118, 117, 128, 114, 137, 115,
              146, 114, 155, 115,
              158, 121, 157, 128, 156, 134, 157, 136, 156, 136]

    img = Image.new('RGB', (500, 500))
    draw = ImageDraw.Draw(img)
    draw.polygon(first, fill='darkgray')
    draw.polygon(second, fill='gray')
    img.show()


# Level 10
# http://www.pythonchallenge.com/pc/return/bull.html

def bull():
    a = [1, 11, 21, 1211, 111221]
    ##In mathematics, the look-and-say sequence is the sequence of integers beginning as follows:
    # 1 , 11, 21, 1211, 111221, 312211, 13112221, 1113213211,
    # If we  start with any digit d from 0 to 9 then d will remain indefinitely as the last digit of the sequence.
    # For d different from 1, the sequence starts as follows:
    #
    # d, 1d, 111d, 311d, 13211d, 111312211 d, 31131122211
    # a = '1'
    # b = ''
    # for i in range(0, 30):
    #     j = 0
    #     k = 0
    #     while j < len(a):
    #         while k < len(a) and a[k] == a[j]: k += 1
    #         b += str(k - j) + a[j]
    #         j = k
    #     print b
    #     a = b
    #     b = ''
    #
    #
    # print len

    # x = "1"
    # for n in range(30):
    #     x = "".join([str(len(j) + 1) + i for i, j in re.findall(r"(\d)(\1*)", x)])
    #     print x
    # print len(x)

    import itertools

    lookSayTable = {
        ("1", "1", "1"): "31",
        ("1", "1"): "21",
        ("1",): "11",
        ("2", "2", "2"): "32",
        ("2", "2"): "22",
        ("2",): "12",
        ("3", "3", "3"): "33",
        ("3", "3"): "23",
        ("3",): "13"
    }

    a, b = "1", [1]

    for i in xrange(30):
        a = "".join(lookSayTable[tuple(l)] for e, l in itertools.groupby(a))
        b.append(a)

    print len(b[30])


# Level 11
# http://www.pythonchallenge.com/pc/return/5808.html
def oddeven():
    from PIL import Image
    # Go pixel by pixel through the image grid and if the pixel(i,j) even (i+j%2==0) it goes to the even image

    img = Image.open('cave.jpg')
    (w, h) = img.size

    even = Image.new('RGB', (w // 2, h // 2))
    odd = Image.new('RGB', (w // 2, h // 2))

    for i in range(w):
        for j in range(h):
            p = img.getpixel((i, j))
            if (i + j) % 2 == 1:
                odd.putpixel((i // 2, j // 2), p)
            else:
                even.putpixel((i // 2, j // 2), p)
    even.show('even.png')
    odd.show('odd.png')


# Level 12
# http://www.pythonchallenge.com/pc/return/evil.html
def evil():
    print 'hi'

if __name__ == '__main__':
    # # mapthis()         # Level 1
    # # ocr()         # Level 2
    # # equality()    # Level 3
    # # linkedlist()  # Level 4
    # # peak(         # Level 5
    # # channel()     # Level 6
    # # oxygen()      # Level 7
    # # integrity()   # Level 8
    # # good()        # Level 9
    # # bull()        # Level 10
    # # oddeven()     # Level 11
    evil()  # Level 12)
