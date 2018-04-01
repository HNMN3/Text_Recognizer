import os,numpy as np,copy,cv2

dict = {0:lambda a,b:(a,b+1),1:lambda a,b:(a,b+1),2:lambda a,b:(a+1,b),3:lambda a,b:(a+1,b),4:lambda a,b:(a,b-1),5:lambda a,b:(a,b-1),6:lambda a,b:(a-1,b),7:lambda a,b:(a-1,b),8:lambda a,b:(a-1,b)}
def moore(start,arr,cl):
    global dict
    cnt=0
    l,r  = arr.shape[:2]
    smpl=np.zeros((l+4,r+4))
    for i in range(l):
        for j in range(r):
            smpl[i+2,j+2]=arr[i,j]

    arr = smpl
    start = [start[0]+2,start[1]+2]
    prev=copy.copy(start)
    pix=8
    #print start,pix
    path=""
    nxt = dict[pix](start[0],start[1])
    pix=1
    while nxt[0]!=start[0] or nxt[1]!=start[1]:
        prev=copy.copy(nxt)
        nxt = dict[pix](nxt[0], nxt[1])
        #print nxt,pix
        #raw_input()
        if nxt[0]==start[0] and nxt[1]==start[1]:
            break
        if(arr[nxt[0],nxt[1]]!=cl):
            pix+=1
            pix%=8
            cnt+=1
        else:
            cnt=0
            path += str((pix+1)%8)
            pix-=pix%2
            pix = (pix+7)%8
            nxt=prev
        if cnt>=8:
            return path

    return path


if __name__=="__main__":
    arr = cv2.imread('./character-database/28/121.jpg',0)#np.array([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,1,0,0,0,0],[0,1,0,0,0,0],[0,1,1,1,1,0],[0,0,0,0,0,0]])
    ret,arr = cv2.threshold(arr,0,255,cv2.THRESH_OTSU)
    cv2.imshow('l', arr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    l,r = arr.shape[:2]
    for i in range(l):
        for j in range(r):
            if arr[i,j]==0:
                print i,j,
                print moore((i,j),arr,1)
                quit()
