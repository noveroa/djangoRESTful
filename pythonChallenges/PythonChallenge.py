# http://www.pythonchallenge.com/
import StringIO
import re
import string
import urllib
from urllib2 import urlopen

import requests
from PIL import Image


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
    # num = "12345"  <<---
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

    # Go pixel by pixel through the image grid and if the pixel(i,j) even (i+j%2==0) it goes to the even image
    url = 'http://huge:file@www.pythonchallenge.com/pc/return/cave.jpg'
    fin = urllib.urlopen(url).read()
    img = Image.open(StringIO.StringIO(fin))

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
    # evil1.jpeg is only thing in source.
    # navigte to evil2.jpeg since it says not jpeg, downloaded as .gfx and opened.

    data = open('evil2.gfx', 'rb').read()

    # 5 cards in original image and deal
    for i in range(5):
        open('%d.jpg' % i, 'wb').write(data[i::5])
        # dis pro port ional ity(with slash through it)


# Level 13
# http://www.pythonchallenge.com/pc/return/disproportional.html

def disproportional(phoneAFriend='Bert'):
    # clicking around 5 is clickable to http://www.pythonchallenge.com/pc/phonebook.php

    # MAKE A CALL - using xml rpc  https://en.wikipedia.org/wiki/XML-RPC
    import xmlrpclib
    proxyConnection = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
    print 'Whats available', proxyConnection.system.listMethods()
    print 'How to use the phone method', proxyConnection.system.methodHelp('phone')
    print 'The inputs', proxyConnection.system.methodSignature("phone")
    print proxyConnection.phone(phoneAFriend)
    # in level 12, if you kept going to evil4.jpg there
    # http://www.pythonchallenge.com/pc/return/evil4.jpg?login=username=huge&password=file
    # was raw html that said bert was evil!


# Level 14
# http://www.pythonchallenge.com/pc/return/italy.html
def italy():
    # src code comment  <!-- remember: 100*100 = (100+99+99+98) + (...  -->
    # # followed by wre.png 100X100
    # title : walkaround ; bun -> spiral through 100right99down99right 98 up? from initial image to create a new one

    url = 'http://huge:file@www.pythonchallenge.com/pc/return/wire.png'
    fin = urllib.urlopen(url).read()
    img = Image.open(StringIO.StringIO(fin))

    size = img.size
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    out = Image.new('RGB', [100, 100])
    x, y, p = -1, 0, 0
    d = 200
    while d / 2 > 0:
        for v in delta:
            steps = d // 2
            for s in range(steps):
                x, y = x + v[0], y + v[1]
                out.putpixel((x, y), img.getpixel((p, 0)))
                p += 1
            d -= 1
    out.show()


# Level 15
# http://www.pythonchallenge.com/pc/return/cat.html
# http://www.pythonchallenge.com/pc/return/uzi.html
def uzi():
    # its name is <b>uzi</b>. you'll hear from him later.
    # src comment : <!-- he ain't the youngest, he is the second -->
    # <!-- todo: buy flowers for tomorrow -->
    # January 1dot6; 26 circled
    # title whom?
    #### FIND OUT THE YEAR?  (leap year (feb 29);
    import datetime
    import calendar
    leapyrs = [x for x in range(1006, 1996, 10) if calendar.isleap(x)]
    years = [x for x in range(leapyrs[0], 1996, 20)]  # needs to end in 6

    print years
    # find *monday* january 26 1XX6
    mondays = [y for y in years if datetime.date(y, 1, 26).isoweekday() == 1]

    print 'To buy flowers tomorrow for the Second Youngest, dated on  January 26, {0} , what is on Jan 27'.format(
        mondays[-2])


# Level 16 mozart
# http://www.pythonchallenge.com/pc/return/mozart.html
def mozart():
    # find the pink pixels and straighten them

    def straight(line, pink):
        idx = 0
        while line[idx] != pink:  # 195 == pink
            idx += 1
        return line[idx:] + line[:idx]

    url = 'http://huge:file@www.pythonchallenge.com/pc/return/mozart.gif'
    fin = urllib.urlopen(url).read()
    img = Image.open(StringIO.StringIO(fin))
    new = Image.new(img.mode, img.size)

    # find pink (pink is in each row, so number of pink / height == 0
    pinkIDX = [x for x in img.histogram() if x % img.height == 0 and x != 0][0]
    # get pink pixel histogram idx:
    pinkpixel = img.histogram().index(2400)

    for y in range(img.size[1]):
        line = [img.getpixel((x, y)) for x in range(img.size[0])]
        line = straight(line, pinkpixel)
        [new.putpixel((x, y), line[x]) for x in range(img.size[0])]
    new.show()


# Level 17 romance
# http://www.pythonchallenge.com/pc/return/romance.html
def romance():
    # title eat; image cookies; embedded image from level 4 (chainsaw.jpg)
    """
    The Python Challenge #17: http://www.pythonchallenge.com/pc/return/romance.html

    This is similar to #4 and it actually uses its solution. However, the key is in
    the cookies. The page's cookie says: "you+should+have+followed+busynothing..."

    So, we follow the chain from #4, using the word "busynothing" and
    reading the cookies.

    """
    url = "http://huge:file@www.pythonchallenge.com/pc/return/romance.html"
    resp = requests.get(url)
    print 'AnyCookies?', resp.cookies

    # Level 4 # from the source code!
    # Content pattern we are matching and extracting the next 'nothing' from
    s_pattern = re.compile("busy nothing is (\d+)")
    num = 12345
    cookie = ''
    urlL4 = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=" + str(num)
    resp = requests.get(urlL4)
    print 'AnyCookies?', resp.cookies['info']

    # while True:
    #     urlL4 = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=" + str(num)
    #
    #     resp = requests.get(urlL4)
    #     content = resp.text
    #     try:
    #         next = re.search("and the next busynothing is (\d+)", content).group(1)
    #     except:
    #         next = None
    #
    #
    #     if resp.cookies['info']:
    #         cookie = cookie + resp.cookies['info']
    #
    #     if next == None:
    #         break
    #     num = next
    #     print num
    # print cookie
    # # it has BZ --> strip + signs and percents, then decompress
    # data = cookie#'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'
    #
    # data = urllib.unquote_plus(data)
    # decompressor = bz2.BZ2Decompressor()
    # data = decompressor.decompress(data)
    # print data# for i in range(3)

    print disproportional('Leopold')  # call his (mozart's father) :

    urlLeo = "http://www.pythonchallenge.com/pc/stuff/violin.php"
    msg = "the flowers are on their way"
    cookies = {'info': msg}
    resp = requests.get(urlLeo, cookies=cookies)

    print resp.text  # oh well, don't you dare to forget the balloons.</font>
    #



# Level 18
# http://www.pythonchallenge.com/pc/return/balloons.html
def balloons():
    # from PIL import ImageChops
    # url = 'http://huge:file@www.pythonchallenge.com/pc/return/balloons.jpg'
    # fin = urllib.urlopen(url).read()
    # img = Image.open(StringIO.StringIO(fin))
    # img.save('text.png')
    #
    # (w, h) = img.size
    #
    # imgA =  0,0, w/2, h
    # imgB = w/2, 0, w, h

    # diff = ImageChops.difference(img.crop(imgA), img.crop(imgB))
    # diff.show()
    # nothing... difference at /brightness.html <! try deltas.gz >

    # f = open('deltas', 'r+').read()
    import difflib
    f = open("deltas")
    deltaA = []
    deltaB = []

    # find the bytes of each image
    for line in f.readlines():
        deltaA.append(line[:55].strip() + "\n")
        deltaB.append(line[55:].strip() + "\n")
    # get the deltas
    differ = difflib.Differ()
    comparison = list(differ.compare(deltaA, deltaB))
    seq1_img = open("seq1_img.png", "wb")
    seq2_img = open("seq2_img.png", "wb")
    both_img = open("both_img.png", "wb")

    for res in comparison:
        r = [chr(int(b, 16)) for b in res[2:].split()]

        if res.startswith('-'):
            for byte in r: seq1_img.write(byte)
        elif res.startswith('+'):
            for byte in r: seq2_img.write(byte)
        else:
            for byte in r: both_img.write(byte)

    seq1_img.close()
    seq2_img.close()
    both_img.close()


# Level 19
def bin():
    import email, wave, array
    url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html'
    resp = requests.get(url)
    content = resp.text
    content = re.findall("<!--(.*?)-->", content, re.DOTALL)[-1]

    emsg = email.message_from_string(content[1:])
    filename = 'indians.wav'
    for index, part in enumerate(emsg.walk()):
        if part.get_content_maintype() == 'multipart':
            continue
        try:
            fp = open(filename, 'wb')
            fp.write(part.get_payload(decode=True))
            fp.close()
            break
        except:
            print 'error'
            # Maybe my computer is out of order. Inverse the bytes of the .wav

    w_in = wave.open(filename, 'rb')
    w_out = wave.open('inversed_' + filename, 'wb')

    w_out.setnchannels(w_in.getnchannels())
    w_out.setsampwidth(w_in.getsampwidth())
    w_out.setframerate(w_in.getframerate())
    w_out.setnframes(w_in.getnframes())

    arr = array.array('i')
    arr.fromstring(w_in.readframes(w_in.getnframes()))
    arr.byteswap()

    w_out.writeframes(arr.tostring())

    w_in.close()
    w_out.close()


# def half_slice(image_path, out_name, outdir, slice_size):
#      """slice an image into parts slice_size tall"""
#      fin = urllib.urlopen(url).read()
#      img = Image.open(StringIO.StringIO(fin))
#      width, height = img.size
#      upper = 0
#      left = 0
#      slices = int(math.ceil(width / slice_size))
#
#      count = 1
#      for slice in range(slices):
#          # if we are at the end, set the lower bound to be the bottom of the image
#          if count == slices:
#              lower = width
#          else:
#              lower = int(count * slice_size)
#
#          bbox = (upper, left, lower, height)
#          working_slice = img.crop(bbox)
#          upper += slice_size
#          # save the slice
#          working_slice.show()
#          count += 1

if __name__ == '__main__':
    # # mapthis()           # Level 1
    # # ocr()               # Level 2
    # # equality()          # Level 3
    # # linkedlist()        # Level 4
    # # peak(               # Level 5
    # # channel()           # Level 6
    # # oxygen()            # Level 7
    # # integrity()         # Level 8
    # # good()              # Level 9
    # # bull()              # Level 10
    # # oddeven()           # Level 11
    # # evil()              # Level 12
    # # disproportional()   # Level 13
    # # italy()             # Level 14
    # # uzi()               # Level 15
    # # mozart()            # Level 16
    # # romance()           # Level 17
    # # balloons()          # Level 18
    bin()  # Level 19
