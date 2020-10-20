from pandas._libs import interval
import pandas as pd
import numpy as np
import cv2

BPM = 1200
DELAY = 60/(BPM*4)
height, width = 120, 200
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 1/DELAY, (600, 800))

KEYNAME = ["CS", "D", "DS", "E", "F", "FS", "G", "GS",
           "A", "AS", "B", "C2", "CS2", "D2", "DS2", "E2", "F2"]
SINGLE_SOUND = {
    "CS": [[1, 3]],
    "D": [[2, 3]],
    "DS": [[3, 3]],
    "E": [[4, 3]],
    "F": [[1, 2], [5, 3]],
    "FS": [[2, 2], [6, 3]],
    "G": [[3, 2], [7, 3]],
    "GS": [[1, 4],  [4, 2], [8, 3]],
    "A": [[2, 4], [5, 2]],
    "AS": [[3, 4], [6, 2], [1, 1]],
    "B": [[4, 4], [7, 2], [2, 1]],
    "C2": [[5, 4], [8, 2], [3, 1]],
    "CS2": [[6, 4], [4, 1]],
    "D2": [[7, 4], [5, 1]],
    "DS2": [[8, 4], [6, 1]],
    "E2": [[7, 1]],
    "F2": [[8, 1]],
}


def hstacks(img: list):
    return np.hstack((np.hstack((img[0], img[1])), np.hstack((img[2], img[3]))))


def vstacks(img: list):
    image = [np.vstack((np.vstack((img[0], img[1])), np.vstack((img[2], img[3])))),
             np.vstack((np.vstack((img[4], img[5])),
                        np.vstack((img[6], img[7]))))
             ]
    return np.vstack((image[0], image[1]))


def main() -> list:
    images = [[np.zeros((height, width, 3), np.uint8)
               for _ in range(4)] for _ in range(8)]

    use_timing = [[] for _ in range(4)]
    count = 0
    df = pd.read_csv("../data/fixed/365.csv")
    for string, fret in zip(df["STRING"], zip(df["FRET1"], df["FRET2"], df["FRET3"], df["FRET4"])):

        images = [[np.zeros((height, width, 3), np.uint8)
                   for _ in range(4)] for _ in range(8)]

        for i, f in enumerate(fret):
            if string == i+1 and f:
                images[int(f) - 1][4-string] = np.tile(
                        np.uint8([0, 205, 0]), (height, width, 1))
                """
                if string % 2:
                    images[int(f) - 1][4-string] = np.tile(
                        np.uint8([0, 0, 205]), (height, width, 1))
                else:
                    images[int(f) - 1][4-string] = np.tile(
                        np.uint8([0, 205, 0]), (height, width, 1))
                """
                use_timing[string-1].append(count)

        for name in KEYNAME:
            for place in SINGLE_SOUND[name]:
                for i in range(len(images)):
                    for j in range(len(images[i])):

                        if place[0]-1 == i and 4-place[1] == j:
                            cv2.putText(
                                images[i][j],
                                name,
                                (0, height - int(height/4)),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                3,
                                (0, 0, 0),
                                3,
                            )
        image = vstacks([hstacks(images[i]) for i in range(8)])
        out.write(image)
        cv2.imshow("bow", image)
        if cv2.waitKey(int(DELAY*1000)) & 0xFF == ord("e"):
            break

        count += 1
    out.release()
    cv2.destroyAllWindows()
    return use_timing


if __name__ == "__main__":

    use_timing = main()
    interval = []
    for timing in use_timing:
        for i in range(1, len(timing)):
            interval.append(timing[i] - timing[i-1])
    print(min(interval))
