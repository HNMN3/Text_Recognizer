#Keep Coding And change the world and do not forget anything... Not Again..
try:
    import cv2,os,sys
    from Tkinter import Tk,IntVar,Label,StringVar,SUNKEN,W
    from tkFileDialog import askopenfilename
    from tkMessageBox import showerror,showinfo
    import tkSimpleDialog as tsd
    from connectedComponents import connected_components as cmp
    import pyocr
    import pyocr.builders
    from PIL import Image
except Exception as e:
    Tk().withdraw()
    showerror('Text Taker Program','Import Error : ' + str(e) + "\n Please install it")
    quit()
Tk().withdraw()
filename=None
NextFile = "yo/OCR/RawInfoHandler"
try:
    filename = askopenfilename(title="Text Taker Program",initialdir=".",filetypes=[("JPEG Files","*.jpg"),("PNG Files","*.png")])
except Exception:
    showerror('Error','File not choosen correctly..')
    quit()
if filename is None or len(filename)==0:
    showerror('Error','File not choosen correctly..')
    quit()

try:
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        showerror('Error','No OCR tool Found')
        quit()
    tool = tools[0]
    langs = tool.get_available_languages()
    lang = None
    for item in langs:
        if item.__contains__('eng'):
            lang = item
    if lang == None:
        print "No english lang found"
        quit()
    print "Opening Image.."
    image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    orignal = cv2.imread(filename)
    dir = filename[:filename.rindex('.')]
    if not os.path.exists(dir):
        os.mkdir(dir)
    os.chdir(dir)
    l,r = image.shape[:2]
    h=2
    w=int(r/64)
    Tmin = 50
    TFixed = 0
    cv2.imwrite('original.jpg',orignal)
    print "Extracting Foreground.."
    for i in range(0,l-h,2):
        for j in range(0,r-w,w):
            img = image[i:i+h,j:j+w]
            hist = cv2.calcHist([img],[0],None,[256],[0,256])
            flag=0
            for item in hist:
                if item[0]>0:
                    break
                flag+=1
            if flag>Tmin:
                var = cv2.meanStdDev(img)
                var = int(var[1][0][0]**2)
                dthres = (((flag-Tmin) - min(TFixed,flag-Tmin))*2)
                if var<dthres:
                    image[i:i+h,j:j+w] = 255
                else:
                    image[i:i+h,j:j+w] = 0
            else:
                image[i:i+h,j:j+w] = 0

    cv2.imwrite('binary.jpg',image)
    print "Finding Connected Components.."
    def func(white,i,j,l,r):
        skew = set()
        stck = {(i,j)}
        mini,minj,maxi,maxj = i,j,i,j
        while len(stck)>0:
            i,j = stck.pop()
            if white[i,j]==255:
                continue
            if j<minj:
                minj = j
            if j>maxj:
                maxj = j
            if i<mini:
                mini = i
            if i>maxi:
                maxi = i
            white[i,j]=255
            #if i>0 and j>0 and white[i-1][j-1]==0:
             #   stck.add((i-1,j-1))
            if i>0 and white[i-1][j]==0:
                stck.add((i-1,j))
            if j>0 and white[i][j-1]==0:
                stck.add((i,j-1))
            #if i<l-1 and j>0 and white[i+1][j-1]==0:
             #   stck.add((i+1,j-1))
            #if i<l-1 and j<r-1 and white[i+1][j+1]==0:
             #   stck.add((i+1,j+1))
            if i<l-1 and white[i+1][j]==0:
                stck.add((i+1,j))
            if j<r-1 and white[i][j+1]==0:
                stck.add((i,j+1))
            #if i>0 and j<r-1 and white[i-1][j+1]==0:
             #   stck.add((i-1,j+1))
        flag = (True if len(skew)>100 else False)
        return white,mini,minj,maxi,maxj
    txfile ="gotInfo.txt"
    ffinal = open(txfile,'w')
    fno=1

    for i in range(l):
        for j in range(r):
            if image[i,j]==0:
                image,a,b,c,d = func(image,i,j,l,r)
                if c-a > int(0.75*l) or d-b > (0.75*r) or c-a <int(0.009*l) or d-b<int(0.09*r) :
                    continue
                if a>2:
                    a-=2
                if b>2:
                    b-=2
                if c<l-3:
                    c+=2
                if d<r-3:
                    d+=2
                #cv2.rectangle(orignal,(b,a),(d,c),(255,0,255),2)
                sample = orignal[a:c,b:d]
                cv2.imwrite('ttmp.jpg',sample)
                #cmp(sample,'sample'+str(fno))
                #os.chdir(dir)
                fno+=1
                txt = tool.image_to_string(
                Image.open('ttmp.jpg'),
                lang=lang,
                builder=pyocr.builders.TextBuilder()
                )
                try:
                    ffinal.write(txt + "\n")
                except Exception:
                    continue
    print "All Done Successfully.."
    ffinal.close()
    #cv2.imwrite('rectangle.jpg',orignal)
    #if os.path.exists(os.curdir + "/ttmp.jpg"):
        #os.remove('ttmp.jpg')


    #Identifying Values
    #print("Running " + "javac -cp " + os.path.abspath(os.curdir) +" "+ NextFile + ".java")
    #os.system("javac -cp " + os.path.abspath(os.curdir) +" "+ NextFile + ".java")
    #print("Running " + "java  -cp " + os.path.abspath(os.curdir) +" "+ NextFile.replace('/','.'))
    #os.system("java  -cp " + os.path.abspath(os.curdir) +" "+ NextFile.replace('/','.'))
    #showinfo('Text Taker Program',"Text Saved in "+txfile)
except Exception as e:
    showerror('Text Taker Program','Error occured : ' + str(e))
    #ffinal.close()
if os.path.exists(os.curdir + "/ttmp.jpg"):
    os.remove('ttmp.jpg')