import pandas as pd
import numpy as np
import cv2

DELAY = 100


def hstacks(img: list):
    return np.hstack((np.hstack((img[0], img[1])), np.hstack((img[2], img[3]))))


def vstacks(img: list):
    image = [np.vstack((np.vstack((img[0], img[1])), np.vstack((img[2], img[3])))),
             np.vstack((np.vstack((img[4], img[5])),
                        np.vstack((img[6], img[7]))))
             ]
    return np.vstack((image[0], image[1]))


def main():
    df = pd.read_csv("../data/fixed/365.csv")
    for fret in zip(df["FRET1"], df["FRET2"], df["FRET3"], df["FRET4"]):
        # for _ in range(100):
        height, width = 100, 200
        images = [[np.zeros((height, width, 3), np.uint8)
                   for _ in range(4)] for _ in range(8)]
        for i, f in enumerate(fret):
            if f == 1:
                for img in images:
                    img[i] = np.tile(
                        np.uint8([84, 255, 159]), (height, width, 1))
        image = vstacks([hstacks(images[i])for i in range(8)])
        cv2.imshow("bow", image)
        if cv2.waitKey(DELAY) & 0xFF == (ord("q") and ord("e")):
            return


if __name__ == "__main__":
    main()
