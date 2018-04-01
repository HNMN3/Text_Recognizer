# Keep coding and change the world..And do not forget anything..Not Again..
from PIL import Image
import os
import cv2


class Manipulation:
    def __init__(self):
        pass

    def change_format(self):
        i = 0
        os.chdir(r'C:\Users\HNMN3\Downloads\training\training\lower')
        for item in os.listdir('.'):
            os.chdir(item)
            for file in os.listdir('.'):
                if file.endswith('jpg') or file.startswith('Thu'):
                    continue
                f, e = os.path.splitext(file)
                img = Image.open(file)
                img = img.convert('RGB')
                img.save(f + '.jpg', 'JPEG')
                os.remove(file)
            os.chdir(os.pardir)

    def manipulate1(self):
        i = 0
        os.chdir(r'C:\Users\HNMN3\Downloads\training\training\lower')
        pre = r'H:\workspace\Projects\TextFromImage\character-database'
        fno = 36
        for item in os.listdir('.'):
            os.chdir(item)
            sno = len(os.listdir(pre + os.sep + str(fno))) + 1
            for file in os.listdir('.'):
                if file.startswith('Thu'):
                    continue
                # print file
                img = cv2.imread(file, 0)
                img = cv2.GaussianBlur(img, (5, 5), 0)
                ret, img = cv2.threshold(img, 90, 255, cv2.THRESH_BINARY_INV)
                cv2.imwrite(pre + os.sep + str(fno) + os.sep + str(sno) + '.jpg', img)
                sno += 1
            os.chdir(os.pardir)
            fno += 1

    def manipulate2(self):
        os.chdir(r'H:\workspace\personal')
        f1 = file('shayri.txt', 'r')
        data = []
        for item in f1.readlines():
            data.append(item)
        f1.close()
        f2 = file('shayri.txt', 'w')

        cnt = 1
        for line in data:
            if len(line) <= 5 or line.endswith('.)'):
                f2.write(str(cnt) + '.)\n')
                cnt += 1
            else:
                f2.write(line)

        f2.close()

    def rename_files(self, dir, startwith=0, par=os.pardir):
        os.chdir(dir)
        list = sorted([x.rjust(10, ')') for x in os.listdir(os.curdir)])
        cnt = startwith
        for item in list:
            infile = item[item.rindex(')') + 1:]
            ext = ""
            if infile.__contains__('.'):
                ext = infile[infile.rindex('.'):]
            outfile = str(cnt) + ext
            os.rename(infile, outfile)
            cnt += 1
        os.chdir(par)

        # Usage
        # os.chdir('H:\workspace\Projects\TextFromImage\character-database')
        # for item in os.listdir('.'):
        #     rename_files(item, 1)
