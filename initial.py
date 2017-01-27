import os,cv2
import numpy as np
#Keep Coding And change the world and do not forget anything... Not Again..
def func(white,i,j,l,r,fno):
    stck = {(i,j)}
    cl = white[i][j]
    pix = 0
    smpl = np.ones((l,r))
    smpl[:,:]=255
    while len(stck)>0:
        i,j = stck.pop()
        white[i][j]=-1
        smpl[i,j]=0
        pix+=1
        if i>0 and j>0 and white[i-1][j-1]==cl:
            stck.add((i-1,j-1))
        if i>0 and white[i-1][j]==cl:
            stck.add((i-1,j))
        if j>0 and white[i][j-1]==cl:
            stck.add((i,j-1))
        if i<l-1 and j>0 and white[i+1][j-1]==cl:
            stck.add((i+1,j-1))
        if i<l-1 and j<r-1 and white[i+1][j+1]==cl:
            stck.add((i+1,j+1))
        if i<l-1 and white[i+1][j]==cl:
            stck.add((i+1,j))
        if j<r-1 and white[i][j+1]==cl:
            stck.add((i,j+1))
        if i>0 and j<r-1 and white[i-1][j+1]==cl:
            stck.add((i-1,j+1))

    cv2.imwrite(str(fno)+'.jpg',smpl)
    fno+=1
    return white,fno

if __name__=="__main__":
    filename = '1.jpg'
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    l,r = img.shape[:2]
    if not os.path.exists(os.curdir + '/' + filename[:filename.rindex('.')]):
        os.mkdir(filename[:filename.rindex('.')])
    os.chdir(filename[:filename.rindex('.')])
    fno=1
    datas = [[gray[i,j] for j in range(r)] for i in range(l)]
    for i in range(l):
        for j in range(r):
            if datas[i][j] == -1:
                continue
            datas,fno = func(datas,i,j,l,r,fno)
    print fno