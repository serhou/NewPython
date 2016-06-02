#!/usr/bin/python python3
# -*- coding: utf-8 -*-
"""
	哈哈哈哈
"""
import os
import subprocess

javadirs = []

def my_test():
	for path, dirs, files in os.walk('.'):
		for file in files:
			if file.endswith(".java"):
				javadirs.append(path)
				break
	print(javadirs)	
	# print(os.getcwd())
	# os.system('java -version')
	# os.system('python --version')
	command = input('input system command:')
	# subprocess.Popen(command, shell=True)	
	info = os.system(command)

	
			
def main():
	my_test()
			
			

if __name__ == '__main__':
	main()