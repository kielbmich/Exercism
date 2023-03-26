import secrets
import string


class Robot:

    names_of_all_robots = []

    def __init__(self):
        self.reset()

    def reset(self):
        safe_name = False
        while not safe_name:
            robot_name_letters = [secrets.choice(string.ascii_uppercase) for i in range(2)]
            robot_name_numbers = [secrets.choice(string.digits) for i in range(3)]
            robot_name = "".join(robot_name_letters + robot_name_numbers)
            safe_name = robot_name not in Robot.names_of_all_robots
        Robot.names_of_all_robots.append(robot_name)
        self.name = robot_name