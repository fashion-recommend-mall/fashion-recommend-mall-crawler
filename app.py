import json

from src.robot import Robot


def main():
	with open('resource/targets.json') as f:
		targets = json.load(f)
	
	robot = Robot(targets)

	robot.run()


if __name__ == "__main__":
	main()