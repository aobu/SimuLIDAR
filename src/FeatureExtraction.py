import numpy as np
import cv2


class FeatureExtractor:
    def __init__(self, environment):
        self.environment = environment
        self.FeatureMap = np.zeros((self.environment.Height, self.environment.Width, 3), dtype=np.uint8)

    def ScanImage2GreyScale(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def DisplayImage(self, img):
        cv2.imshow('Image', img)
        cv2.waitKey(0)

    def DetectAndDrawLines(self, img):
        gray = self.ScanImage2GreyScale(img)

        edges = cv2.Canny(gray, 50, 200, apertureSize=3)
        lines = cv2.HoughLinesP(edges, 2, np.pi / 360, threshold=30, minLineLength=25, maxLineGap=10)

        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv2.line(self.FeatureMap, (x1, y1), (x2, y2), (255, 0, 0), 1)  # Blue color (BGR format)

        return self.FeatureMap