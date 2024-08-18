import numpy as np
import cv2
from scipy.spatial import KDTree

class LIDARScanner:
    def __init__(self, startPosition, environment, Range, DistanceNoise, AngleNoise, ScanFrequency, NumAngles=30, ProximityThreshold=10):
        self.position = startPosition
        self.environment = environment
        self.Range = Range
        self.DistanceNoise = DistanceNoise
        self.AngleNoise = AngleNoise
        self.NumAngles = NumAngles
        self.ScanFrequency = ScanFrequency
        self.ProximityThreshold = ProximityThreshold

        self.scannerMap = np.zeros((self.environment.Height, self.environment.Width, 3), dtype=np.uint8)
        self.pointCloud = []
        self.kdtree = None

    def GetPointCloud(self):
        return self.pointCloud.copy()

    def UpdatePosition(self, newPosition):
        self.position = newPosition

    def Scan(self):
        angles = np.linspace(0, 2 * np.pi, self.NumAngles, endpoint=False)
        measurements = []

        for angle in angles:
            dx = np.cos(angle)
            dy = np.sin(angle)

            for dist in range(self.Range):
                x = int(self.position[0] + dx * dist)
                y = int(self.position[1] + dy * dist)

                if x < 0 or x >= self.environment.Width or y < 0 or y >= self.environment.Height:
                    break

                if np.all(self.environment.Map[y, x] == [0, 0, 0]):
                    measurements.append(self.AddNoise((dist, angle)))
                    break

        for m in measurements:
            point = self.Measurement2Point(m)
            if not self.isPointTooClose(point):
                self.pointCloud.append(point)
                self.updateKDTree()

    def isPointTooClose(self, point):
        if self.kdtree is None or len(self.pointCloud) == 0:
            return False

        dist, _ = self.kdtree.query(point)
        return dist < self.ProximityThreshold

    def updateKDTree(self):
        if len(self.pointCloud) > 0:
            self.kdtree = KDTree(self.pointCloud)

    def AddNoise(self, measurement):
        distance, angle = measurement
        noisy_distance = distance + np.random.normal(0, self.DistanceNoise)
        noisy_angle = angle + np.random.normal(0, self.AngleNoise)

        return (noisy_distance, noisy_angle)

    def Measurement2Point(self, measurement):
        distance, angle = measurement
        x = int(self.position[0] + distance * np.cos(angle))
        y = int(self.position[1] + distance * np.sin(angle))

        return (x, y)