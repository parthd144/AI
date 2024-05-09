class HelpDeskExpertSystem:
    def __init__(self):
        self.rules = {
            "printer_not_working": "Please check if the printer is properly connected and powered on.",
            "slow_internet_connection": "Try restarting your router or contacting your internet service provider.",
            "software_not_installing": "Make sure you have sufficient disk space and administrative privileges.",
            "forgot_password": "You can reset your password using the 'Forgot Password' option on the login screen.",
            "email_not_sending": "Check your internet connection and email server settings."
        }

    def get_solution(self, problem):
        if problem in self.rules:
            return self.rules[problem]
        else:
            return "Sorry, I couldn't find a solution for that problem. Please contact your IT support."

# Example usage:
help_desk = HelpDeskExpertSystem()

print("Welcome to the Help Desk Expert System!")
print("Available problems: printer_not_working, slow_internet_connection, software_not_installing, forgot_password, email_not_sending")

while True:
    problem = input("Enter the problem you're facing (or type 'exit' to quit): ").strip().lower()
    if problem == 'exit':
        print("Goodbye!")
        break
    else:
        solution = help_desk.get_solution(problem)
        print("Solution:", solution)
