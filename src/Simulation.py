import cv2
import time

from src.Environment import Environment
from src.LIDARScanner import LIDARScanner
from src.FeatureExtraction import FeatureExtractor


class Simulation:
    def __init__(self, environment, scanner):
        self.environment = environment
        self.scanner = scanner
        self.LastScanTime = 0
        self.FinalImage = None
        self.FeatureExtractor = FeatureExtractor(self.environment)

    def UpdateDisplay(self):

        displayMap = self.scanner.scannerMap.copy()#self.environment.Map.copy()

        for point in self.scanner.pointCloud:
            cv2.circle(displayMap, center=point, radius=1, color=(0, 0, 255), thickness=-1)


        featureMap = FeatureExtractor.DetectAndDrawLines(self.FeatureExtractor, displayMap)
        cv2.circle(displayMap, center=self.scanner.position, radius=3, color=(0, 255, 0), thickness=-1)


        self.FinalImage = displayMap.copy()
        cv2.imshow("LIDAR Display", featureMap)


    def Run(self):

        def mouse_callback(event, x, y):
            if event == cv2.EVENT_MOUSEMOVE:
                self.scanner.UpdatePosition((x, y))

        cv2.namedWindow("LIDAR Display")
        cv2.setMouseCallback("LIDAR Display", mouse_callback)

        running = True
        while running:
            key = cv2.waitKey(1) & 0xFF
            if key == 27:
                running = False

            CurrentTime = time.time()
            ElapsedTime = CurrentTime - self.LastScanTime

            if ElapsedTime >= 1.0 / self.scanner.ScanFrequency:
                self.scanner.Scan()
                self.LastScanTime = CurrentTime

            self.UpdateDisplay()

        cv2.destroyAllWindows()