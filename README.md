# SimuLIDAR

## Overview

SimuLIDAR is a LIDAR scanner simulation tool developed with OpenCV. It allows users to simulate the operation of a LIDAR scanner on a 2D black-and-white map (e.g., a floor plan). The project is designed to mimic the behavior of a real LIDAR scanner, including the addition of noise to the measurements. The simulated LIDAR data is then processed to extract the structural features of the environment, producing a detailed map using computer vision techniques like Canny edge detection and the Probabilistic Hough Line Transform.

## Example

Below is an example of the process:

1. **Input Map:**

   <img src="/maps/FloorPlan2.png" alt="Input Map" width="450"/>

2. **Generated Point Cloud:**

   <img src="/recordings/LIDARDisplay2024-08-1719-55-18-ezgif.com-video-to-gif-converter.gif" alt="Point Cloud" width="450"/>

3. **Edges Detected on Point Cloud:**

   <img src="/recordings/LIDARDisplay2024-08-1719-58-30-ezgif.com-video-to-gif-converter.gif" alt="Edges" width="450"/>

4. **Reconstructed Environment:**

   <img src="/recordings/LIDARDisplay2024-08-1720-00-04-ezgif.com-video-to-gif-converter.gif" alt="Reconstructed Map" width="450"/>

## Features

- **LIDAR Simulation:** Simulates a 2D LIDAR scanner with added noise to represent real-world imperfections.
- **Point Cloud Generation:** Produces a point cloud from the simulated LIDAR measurements.
- **Edge Detection:** Utilizes the Canny edge detection algorithm to identify edges in the point cloud.
- **Line Feature Extraction:** Applies the Probabilistic Hough Line Transform to extract and represent the main structural features of the environment.
- **Map Reconstruction:** Generates a final map of the environment based on the extracted features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
