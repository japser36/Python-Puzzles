from string import maketrans

inputStr = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
input2 = "http://www.pythonchallenge.com/pc/def/map.html"
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet2 = "cdefghijklmnopqrstuvwxyzab"

print input2.translate(maketrans(alphabet, alphabet2))
