source = 'abcdefghijklmnopqrstuvwxyz'
target = source[2:] + source[:2]

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

trans = ''
for c in text:
    idx = source.find(c)
    if idx >= 0:
        trans = trans + target[idx]
    else:
        trans = trans + c

print trans
        
        
