# copy this method into your adidas script and call the function right before making your atc request

def updateCookies(session):

    while True:
        try:
            file1=open("result.txt","r")
            fn = file1.readlines()[0].split("[")[0]
            break
        except:
            continue
        
    file1=open(fn,"r")
    lines=file1.readlines()

    for x in range (4, len(lines)):
        name = lines[x].split()[5])
        value = lines[x].split()[6])
        session.headers.update({name : value}

    
