"""
This is Project Main Module

It is made by carrykim

linkedIn : linkedin.com/in/carrykim
github : https://github.com/gimseonjin
"""
import json

from src.robot import Robot


def main():
	"""
	Title : main
	
	This is Project Main Method!!

	made by carrykim
	"""
	with open('resource/targets.json') as f:
		targets = json.load(f)
	
	robot = Robot(targets)

	robot.run()


if __name__ == "__main__":
	main()