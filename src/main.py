# src/main.py

from navigation.motion_planning import MotionPlanning
from control.control_system import ControlSystem
from vision.crack_detection import CrackDetection
from communication.data_transmission import DataTransmission
from utilities.config import Config

def main():
    # Load configuration
    config = Config().load_config()
    
    # Initialize modules
    motion_planning = MotionPlanning(config['navigation'])
    control_system = ControlSystem(config['control'])
    crack_detection = CrackDetection(config['vision'])
    data_transmission = DataTransmission(config['communication'])
    
    # Perform navigation and inspection
    path = motion_planning.calculate_optimal_path()
    control_system.follow_path(path)
    
    # Conduct inspections and detect cracks
    cracks = crack_detection.detect_cracks()
    
    # Process the collected data
    processed_data = data_transmission.process_data(cracks)
    
    # Send the data for storage or further processing
    data_transmission.send_data(processed_data)

if __name__ == "__main__":
    main()
