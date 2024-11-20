# Robot Navigation System

This project is a modular Python system for real-time robot navigation using video streaming, color detection, and A* pathfinding. The system detects obstacles and the robot's position using color segmentation and generates a path to a goal using a simplified grid map.

The project was created during the Hackathon `Hack-a-Signal` in Cracow, Poland on November 16-17, 2024, and it may have some issues.

---

## File Structure
- **`main.py`**: The main script that integrates video streaming, color detection, and pathfinding.
- **`stm_Connection.py`**: Contains the `STMconnect` function for communication with an ESP32.
- **`color_Detection.py`**: Contains the `colorDetection` function to detect and highlight specified colors in an image.
- **`path_Finding.py`**: Implements A* pathfinding logic.

---

## Setup and Dependencies
### Prerequisites
Ensure Python 3.6+ is installed. Install the following libraries:
```bash
pip install requests numpy opencv-python opencv-contrib-python imutils matplotlib
```

---

## Usage
1. Clone the repository or copy the scripts into a directory.
2. Update the IP address of the video stream in main.py:
```python
url = "http://<your_camera_ip>/shot.jpg"
```
3. Run the main script:
```bash
python main.py
```

---
## Function Overview:
### STMconnect (in `stm_connection.py`)
Sends binary data to an ESP32 using HTTP POST.
*Usage:*
```python
from stm_connection import STMconnect
STMconnect(esp32IP="192.168.0.1", data=b"your_binary_data")
```
### colorDetection (in `color_detection.py`)
Detects specified colors in an image and highlights them.
*Usage:*
```python
from color_detection import colorDetection
colorDetection("image.jpg", np.array([B, G, R]), tolerance=50)
```
### a_star (in `pathfinding.py`)
Computes the optimal path on a grid using A* algorithm.
*Usage:*
```python
from pathfinding import a_star
path = a_star(grid, start=(0, 0), goal=(10, 10))
```

---

## Example Workflow
1. The robot's camera streams video to a specified IP address.
2. main.py processes each frame:
    - Detects the robot and obstacles using color segmentation.
    - Maps the positions to a 128x128 grid.
    - Computes the shortest path to the goal using A*.
3. The path is visualized in a simplified map and displayed alongside the video feed.

---

## Features
1. *Color-Based Object Detection:* Configurable color ranges for car and obstacle detection.
2. *Real-Time Pathfinding:* Dynamically calculates the shortest path to the goal.
3. *ESP32 Communication:* Supports binary data transfer for integration with hardware.
4. *Keyboard Controls:* press `q` to Exit the application.

---

## Notes
- Ensure the IP camera stream is accessible and matches the URL in main.py.
- Tune color ranges (blueLow, blueUp, greenLow, greenUp) in main.py for optimal detection in your environment.
