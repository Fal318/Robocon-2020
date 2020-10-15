import time

from pandas._libs import interval
import pandas as pd
import numpy as np
import cv2

BPM = 105
DELAY = 30/(BPM*4)


def hstacks(img: list):
    return np.hstack((np.hstack((img[3], img[2])), np.hstack((img[1], img[0]))))


def vstacks(img: list):
    image = [np.vstack((np.vstack((img[0], img[1])), np.vstack((img[2], img[3])))),
             np.vstack((np.vstack((img[4], img[5])),
                        np.vstack((img[6], img[7]))))
             ]
    return np.vstack((image[0], image[1]))


def main() -> list:
    use_timing = [[] for _ in range(4)]
    count = 0
    df = pd.read_csv("../data/fixed/365.csv")
    for string, fret in zip(df["STRING"], zip(df["FRET1"], df["FRET2"], df["FRET3"], df["FRET4"])):
        start_time = time.time()
        height, width = 100, 150
        images = [[np.zeros((height, width, 3), np.uint8)
                   for _ in range(4)] for _ in range(8)]

        for i, f in enumerate(fret):
            if string == i+1 and f:
                images[int(f)-1][string-1] = np.tile(
                    np.uint8([84, 255, 159]), (height, width, 1))
                use_timing[string-1].append(count)

        image = vstacks([hstacks(images[i]) for i in range(8)])
        cv2.imshow("bow", image)
        if cv2.waitKey(int((time.time()+DELAY-start_time)*1000)) & 0xFF == (ord("q") and ord("e")):
            break

        count += 1

    cv2.destroyAllWindows()
    return use_timing


if __name__ == "__main__":

    use_timing = main()
    interval = []
    for timing in use_timing:
        for i in range(1, len(timing)):
            interval.append(timing[i] - timing[i-1])
    print(min(interval))
