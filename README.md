# HydroVigil-1-AUV-
**HydroVigil-1: Indigenous Autonomous Underwater Vehicle (AUV) Development for Underwater Inspection**

![SUV3](https://github.com/user-attachments/assets/e7fd2e5d-c78b-4eae-a38e-d5c5dc5d3cf5)
![SUV2](https://github.com/user-attachments/assets/f55bfb68-e2c2-48b3-a50c-c66ed55a4456)



**Project Description**
HydroVigil-1 is an indigenous Autonomous Underwater Vehicle (AUV) designed specifically for underwater inspection tasks, such as ship hull crack identification and marine infrastructure assessments. HydroVigil-1 is engineered to operate at depths of up to 50 meters with a range of around 500 meters, providing a versatile solution for underwater inspection in various marine environments. The project is currently in the prototype phase, with ongoing testing to optimize performance and functionality.

**System Overview**
HydroVigil-1 is developed as a robust platform for underwater inspection, capable of navigating autonomously in challenging underwater conditions. It integrates a variety of sensors, including locally sourced and R&D-based sensors available in the market, such as GPS for surface localization, an Inertial Navigation Unit (INU) for precise underwater positioning, depth sensors, and acoustic sensors for environment mapping and obstacle avoidance.

**Functions and Features**

**Autonomous Navigation:** HydroVigil-1 utilizes advanced control algorithms to autonomously navigate through predefined paths or dynamically adjust its route based on real-time sensor data.
**Ship Hull Crack Identification:** The integration of computer vision and machine learning algorithms enables HydroVigil-1 to detect and assess cracks and structural integrity of ship hulls and underwater pipelines effectively.
**Data Collection and Analysis:** The vehicle collects visual and acoustic data, which can be processed onboard using embedded AI models for immediate analysis or uploaded to a remote server for further processing.
**Real-time Communication:** HydroVigil-1 supports underwater acoustic communication for real-time data transmission and remote control capabilities within a 500-meter operational range.

**Modules and Components**

**Mechanical Design:** HydroVigil-1 features a streamlined torpedo-shaped hull for minimal hydrodynamic drag. The main structural frame is constructed from marine-grade aluminum to ensure durability and corrosion resistance. Enclosures for electronics and batteries are sealed to IP68 standards using O-rings and marine-grade epoxy to prevent water ingress.

**Electrical Systems:** HydroVigil-1 is powered by high-capacity Lithium Polymer batteries from OEMs like Panasonic and LG Chem. A custom-designed Power Distribution Board (PDB) manages power flow, utilizing buck and boost converters to meet the varying voltage requirements of onboard components. The electrical system is controlled by a PIC microcontroller as the main controller, with an Arduino Mega serving as a slave controller for motor driver management.

**Sensor Suite:** The sensor suite includes a U-Blox GPS module for surface-level positioning, a Honeywell HG4930 Inertial Navigation Unit (INU) for underwater navigation, TE Connectivity depth sensors to monitor submersion, and a Sony IMX323 high-resolution camera for visual inspection. Additionally, locally sourced acoustic sensors are installed for sonar-based mapping and object detection, while specialized R&D sensors provide enhanced data collection capabilities.

**Specifications**

**Operational Depth:** Up to 50 meters
**Range:** Around 500 meters
**Propulsion:** Electrically driven thrusters capable of omnidirectional movement with 5 degrees of freedom
**Battery Life:** Up to 4 hours on a single charge, depending on operational load and conditions
**Communication:** Underwater acoustic modem for data transmission and remote control; RF communication for surface operations
**Processing Unit:** Onboard computer with a ROS (Robot Operating System) framework for modular control and data processing, integrated with computer vision and machine learning models for real-time analysis.

**Power Methodology**

HydroVigil-1 is powered by Lithium Polymer batteries, chosen for their high energy density and lightweight properties. The batteries are housed in a pressure-sealed compartment to prevent water ingress and are designed to provide sufficient power for extended underwater missions. The power management system ensures efficient distribution to all subsystems, with built-in safety features to prevent overcharging and overheating.

**System Configuration and Stack**

The software architecture is based on the Robot Operating System (ROS), which provides a flexible framework for developing and integrating various modules. The system is divided into several key components:

**Motion Planning Module:** Calculates optimal paths for HydroVigil-1 to follow based on mission objectives and real-time sensor input.
**Control Module:** Ensures precise maneuverability and stability of HydroVigil-1, maintaining desired speed and orientation.
**Navigation Module:** Integrates data from GPS, INU, and depth sensors to provide accurate positioning and trajectory updates.
**Vision and ML Module:** Utilizes computer vision and machine learning algorithms to detect cracks, identify objects, and assess structural integrity.

**Current Status and Future Work**

HydroVigil-1 is currently in the prototype phase, with extensive testing being conducted in controlled environments to validate the design and functionality. Future work includes enhancing the software stack for improved autonomy, integrating advanced AI algorithms for real-time decision-making, and expanding the sensor suite for more comprehensive underwater inspections.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/HydroVigil-1.git
   cd HydroVigil-1
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Configuration
Create a config.json file with navigation, control, vision, and communication settings:
json
Copy code
{
    "navigation": {
        "goal": [10, 10]
    },
    "control": {
        "speed": 2.0,
        "stability_control": true
    },
    "vision": {
        "model_path": "path/to/model"
    },
    "communication": {
        "acoustic_modem": true
    }
}
Usage
Run the main program:

bash
Copy code
python src/main.py
Testing
To run tests, use:

bash
Copy code
python -m unittest discover -s tests
python
Copy code

### Testing Enhancements
Add realistic assertions to the tests based on actual functionality.

#### Example: `test_crack_detection.py`
```python
# tests/test_crack_detection.py

import unittest
from vision.crack_detection import CrackDetection

class TestCrackDetection(unittest.TestCase):
    def test_detect_cracks(self):
        crack_detection = CrackDetection({'model_path': 'dummy/path'})
        cracks = crack_detection.detect_cracks()
        self.assertIsInstance(cracks, list)
        self.assertGreater(len(cracks), 0)
        for crack in cracks:
            self.assertIsInstance(crack, tuple)  # Each crack should be a tuple (x, y)

if __name__

