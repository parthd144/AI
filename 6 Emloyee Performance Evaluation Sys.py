#Emloyee Performance Evaluation System
class PerformanceEvaluationExpertSystem:
    def __init__(self):
        self.rules = {
            "productivity": {
                "Excellent": lambda productivity: productivity >= 90,
                "Good": lambda productivity: 80 <= productivity < 90,
                "Fair": lambda productivity: 70 <= productivity < 80,
                "Poor": lambda productivity: productivity < 70
            },
            "attendance": {
                "Excellent": lambda attendance: attendance >= 95,
                "Good": lambda attendance: 90 <= attendance < 95,
                "Fair": lambda attendance: 80 <= attendance < 90,
                "Poor": lambda attendance: attendance < 80
            },
            "attitude": {
                "Excellent": lambda attitude: attitude >= 9,
                "Good": lambda attitude: 7 <= attitude < 9,
                "Fair": lambda attitude: 5 <= attitude < 7,
                "Poor": lambda attitude: attitude < 5
            }
        }

    def evaluate_performance(self, productivity, attendance, attitude):
        evaluation = {}
        for criterion, criterion_rules in self.rules.items():
            for category, rule in criterion_rules.items():
                if rule(eval(criterion)):
                    evaluation[criterion] = category
                    break
        return evaluation

# Example usage:
evaluation_system = PerformanceEvaluationExpertSystem()

productivity = int(input("Enter productivity score (0-100): "))
attendance = int(input("Enter attendance percentage (0-100): "))
attitude = int(input("Enter attitude score (0-10): "))

evaluation = evaluation_system.evaluate_performance(productivity, attendance, attitude)

print("\nPerformance Evaluation:")
for criterion, category in evaluation.items():
    print(f"{criterion.capitalize()}: {category}")
