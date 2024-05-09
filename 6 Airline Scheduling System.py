#Airline Scheduling System
class AirlineSchedulingExpertSystem:
    def __init__(self):
        self.cargo_rules = {
            "small": {"domestic": ["A", "B", "C"], "international": ["X", "Y", "Z"]},
            "medium": {"domestic": ["D", "E", "F"], "international": ["W", "V", "U"]},
            "large": {"domestic": ["G", "H", "I"], "international": ["T", "S", "R"]}
        }
        self.flight_schedule = {
            "domestic": {"A": ["D1", "D2", "D3"], "B": ["E1", "E2", "E3"], "C": ["F1", "F2", "F3"]},
            "international": {"X": ["I1", "I2", "I3"], "Y": ["J1", "J2", "J3"], "Z": ["K1", "K2", "K3"],
                               "W": ["L1", "L2", "L3"], "V": ["M1", "M2", "M3"], "U": ["N1", "N2", "N3"]}
        }

    def suggest_flight(self, cargo_size, destination, is_international):
        if cargo_size in self.cargo_rules:
            if destination in self.cargo_rules[cargo_size][("international" if is_international else "domestic")]:
                return self.flight_schedule[("international" if is_international else "domestic")][destination]
        return "No suitable flights available."

# Example usage:
expert_system = AirlineSchedulingExpertSystem()

cargo_size = input("Enter cargo size (small/medium/large): ").lower()
destination = input("Enter destination (A-Z): ").upper()
is_international = input("Is it an international flight? (yes/no): ").lower() == "yes"

flight_options = expert_system.suggest_flight(cargo_size, destination, is_international)
print("\nSuggested Flight Options:")
print(flight_options)
