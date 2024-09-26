# src/navigation/inertial_navigation.py

class InertialNavigationUnit:
    def __init__(self):
        self.position = (0.0, 0.0, 0.0)
        self.velocity = (0.0, 0.0, 0.0)

    def update_position(self, delta_time):
        self.position = (
            self.position[0] + self.velocity[0] * delta_time,
            self.position[1] + self.velocity[1] * delta_time,
            self.position[2] + self.velocity[2] * delta_time,
        )
        return self.position

    def set_velocity(self, velocity):
        self.velocity = velocity
