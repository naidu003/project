# TrafficFlowData class for CRUD operations on traffic data
class TrafficFlowData:
    _data = {}
    _id_counter = 1

    def __init__(self, volume, speed, location):
        self.id = TrafficFlowData._id_counter
        self.volume = volume
        self.speed = speed
        self.location = location
        TrafficFlowData._data[self.id] = self
        TrafficFlowData._id_counter += 1

    def update(self, volume=None, speed=None, location=None):
        if volume is not None:
            self.volume = volume
        if speed is not None:
            self.speed = speed
        if location is not None:
            self.location = location

    @staticmethod
    def create(volume, speed, location):
        """Create new traffic flow data."""
        return TrafficFlowData(volume, speed, location)

    @staticmethod
    def read(traffic_id):
        """Read traffic flow data by ID."""
        return TrafficFlowData._data.get(traffic_id)

    @staticmethod
    def delete(traffic_id):
        """Delete traffic flow data by ID."""
        if traffic_id in TrafficFlowData._data:
            del TrafficFlowData._data[traffic_id]


# TrafficManagementSolution class for CRUD operations on traffic solutions
class TrafficManagementSolution:
    _solutions = {}
    _solution_id_counter = 1

    def __init__(self, description):
        self.solution_id = TrafficManagementSolution._solution_id_counter
        self.description = description
        TrafficManagementSolution._solutions[self.solution_id] = self
        TrafficManagementSolution._solution_id_counter += 1

    def update(self, new_description):
        """Update existing traffic management solution."""
        self.description = new_description

    @staticmethod
    def create(description):
        """Create a new traffic management solution."""
        return TrafficManagementSolution(description)

    @staticmethod
    def read(solution_id):
        """Read a traffic management solution by ID."""
        return TrafficManagementSolution._solutions.get(solution_id)

    @staticmethod
    def delete(solution_id):
        """Delete a traffic management solution by ID."""
        if solution_id in TrafficManagementSolution._solutions:
            del TrafficManagementSolution._solutions[solution_id]


# Function to simulate traffic conditions based on traffic flow data
def simulate_traffic_conditions(traffic_id):
    """Simulate traffic conditions based on traffic flow data."""
    traffic = TrafficFlowData.read(traffic_id)
    if not traffic:
        return "No traffic data available."

    if traffic.volume > 1000:
        return f"High traffic at {traffic.location} with {traffic.volume} vehicles."
    elif traffic.volume > 500:
        return f"Moderate traffic at {traffic.location}."
    else:
        return f"Low traffic at {traffic.location}."


# Function to suggest traffic management solutions
def suggest_traffic_management_solutions(solution_id):
    """Suggest traffic management solutions based on a solution ID."""
    solution = TrafficManagementSolution.read(solution_id)
    if not solution:
        return "No solution available."

    return f"Suggested solution: {solution.description}"


# Unit Testing using unittest framework
import unittest

class TestTrafficFlowSimulator(unittest.TestCase):
    
    def test_traffic_flow_crud_operations(self):
        # Create
        t1 = TrafficFlowData.create(500, 35, "Location A")
        self.assertEqual(t1.volume, 500)
        
        # Read
        read_t1 = TrafficFlowData.read(t1.id)
        self.assertEqual(read_t1, t1)
        
        # Update
        t1.update(volume=600)
        self.assertEqual(t1.volume, 600)
        
        # Delete
        TrafficFlowData.delete(t1.id)
        self.assertIsNone(TrafficFlowData.read(t1.id))

    def test_traffic_management_solution_crud_operations(self):
        # Create
        s1 = TrafficManagementSolution.create("Implement traffic signals.")
        self.assertEqual(s1.description, "Implement traffic signals.")
        
        # Read
        read_s1 = TrafficManagementSolution.read(s1.solution_id)
        self.assertEqual(read_s1, s1)
        
        # Update
        s1.update("Update traffic signals timing.")
        self.assertEqual(s1.description, "Update traffic signals timing.")
        
        # Delete
        TrafficManagementSolution.delete(s1.solution_id)
        self.assertIsNone(TrafficManagementSolution.read(s1.solution_id))

    def test_simulate_traffic_conditions(self):
        t1 = TrafficFlowData.create(1200, 25, "Location B")
        result = simulate_traffic_conditions(t1.id)
        self.assertIn("High", result)

    def test_suggest_traffic_management_solutions(self):
        s1 = TrafficManagementSolution.create("Add more lanes.")
        result = suggest_traffic_management_solutions(s1.solution_id)
        self.assertIn("Add more lanes.", result)


if __name__ == '__main__':
    unittest.main()
