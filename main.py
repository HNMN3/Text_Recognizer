# Keep Coding And change the world and do not forget anything... Not Again..
from collections import defaultdict
from DynamicThresh import dynamic_threshing
from ConnectedComponents import connected_components
from BoundingRect import bounding_rect
from Classifiy import Classifier
import cv2
import argparse


def detect_and_split_characters(input_filename, output_filename):
    # original image
    org = cv2.imread(input_filename)
    l, r = org.shape[:2]

    # Normalization
    m = 1000
    n = m * l / r
    l, r = n, m
    org = cv2.resize(org, (r, l))

    # Convert image in grayscale
    gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)

    # Thresholding
    img = dynamic_threshing(gray)

    # initializing variable
    data_list = map(list, img)

    # Initialize the classifier
    clf = Classifier()

    out_file = open(output_filename, 'w')

    # splitting image and getting connected components
    for i in range(l):
        for j in range(r):
            if data_list[i][j] != 0:
                continue
            data_list, a, b, c, d = bounding_rect(data_list, i, j, l, r)

            # Removing unnecesary Blocks..
            if c - a > int(0.65 * l) or d - b > 900 or c - a < int(0.03 * l) or d - b < 50:
                continue

            a = max(1, a - 1)
            b = max(1, b - 1)
            c = min(c + 1, l - 1)
            d = min(d + 1, r - 1)

            # Temporarily saving image of block..
            cv2.imwrite('/tmp/block.jpg', org[a:c, b:d])

            # Finding the connected components..
            smt = connected_components(cv2.imread('/tmp/block.jpg'))
            smt_data = defaultdict(list)
            for item in smt:
                smt_data[item[1]].append((item[0], item[2]))

            for key in sorted(smt_data.keys()):
                smt_data[key] = sorted(smt_data[key], key=lambda x: x[0])
                out = ""
                prev_pos = max(smt_data[key], key=lambda x: x[0])[0]
                ch_size = 0
                for pos, img in smt_data[key]:
                    if pos - prev_pos > 1.8 * ch_size:
                        out += " "
                    prev_pos = pos
                    height, ch_size = img.shape
                    if height < 6:
                        out += " "
                        continue
                    out += clf.predict(img)
                out_file.write(out + '\n')

    out_file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_path',
                        help="Path of an Image")
    parser.add_argument("--output_file",
                        help="Name of output file",
                        default="output.txt")

    args = parser.parse_args()

    detect_and_split_characters(args.image_path, args.output_file)
    print("Successfully Executed!! Output stored in {}".format(args.output_file))
