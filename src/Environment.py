import cv2


class Environment:
    def __init__(self, MapPath):
        self.Map = cv2.imread(MapPath)

        if self.Map is None:
            raise ValueError(f"Failed to load the map from the path: {MapPath}")

        self.Height, self.Width, _ = self.Map.shape

    def DisplayMap(self):
        cv2.imshow("Map", self.Map)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


