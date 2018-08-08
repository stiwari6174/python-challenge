from PIL import Image
from functools import reduce
import re

img = Image.open("../data/oxygen.png")

# get each pixel along the horizontal central axis of the image
pixels = [img.getpixel((h, img.height/2)) for h in range(img.width)]

# information is encoded in pixels that have the same r,g,b values
encodedInfo = [r for r, g, b, x in pixels if r == g == b]

# convert each pixel value to its equivalent character
strWithDupes = ''.join(map(chr, encodedInfo))

# there are repetions; take every 7th character
every7th = strWithDupes[::7]

# we are looking for a list of ascii values; extract this list and convert to chr again
match = re.search("\[.+\]", every7th)
answer = ''.join(map(chr, eval(match.group(0))))
print (answer)