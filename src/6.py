import zipfile

with zipfile.ZipFile("../data/channel.zip") as f:
    nxt = 90052
    comments = ""
    while nxt:
        name = str(nxt) + ".txt"
        txt = f.read(name)
        comments = comments + f.getinfo(name).comment.decode("utf-8")
        try:
            nxt = int(txt.split()[-1])
        except ValueError as e:
            break
    print (comments)