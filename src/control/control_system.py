# src/control/control_system.py

class ControlSystem:
    def __init__(self, config):
        self.speed = config['speed']
        self.stability_control_enabled = config['stability_control']

    def follow_path(self, path):
        for point in path:
            self.move_to(point)

    def move_to(self, point):
        print(f"Controlling AUV to position: {point} at speed {self.speed}")
        if self.stability_control_enabled:
            self.stabilize()
    
    def stabilize(self):
        print("Stabilizing AUV...")
