import json

from src.robot import Robot


def main():
	with open('targets.json') as f:
		targets = json.load(f)
	
	robot = Robot(targets)

	#robot.run()
	robot.test()


if __name__ == "__main__":
	main()