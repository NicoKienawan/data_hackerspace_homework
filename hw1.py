#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np
import math

def histogram_times(filename):
    with open(filename) as input:
    	read = csv.reader(input)
    	data = list(read)
    L = [0] * 24
    for incident in data[1:]:
    	if incident[1]:
    		check = incident[1].split(':')[0]
    		if check.isdigit():
    			hour = int(check)
    			if (hour < 25 and hour > -1):
    				L[hour] += 1
    return L

def weigh_pokemons(filename, weight):
	with open(filename) as input:
		read = json.load(input)
	L = []
	for pokemon in read["pokemon"]:
		check = pokemon["weight"].split(' ')[0]
		if float(check) == weight:
			L.append(pokemon["name"])
	return L

def single_type_candy_count(filename):
    with open(filename) as input:
    	read = json.load(input)
    count = 0;
    for pokemon in read["pokemon"]:
    	if "candy_count" in pokemon.keys():
    		if len(pokemon["type"]) == 1:
    			count += pokemon["candy_count"]
    return count

def reflections_and_projections(points):
	index = 0
	for y in points[1]:
		points[1][index] += 2*(1-y)
		index += 1

	A = np.array([[0, -1], [1,0]])
	points = A.dot(points)

	B = np.array([[1, 3], [3, 9]])
	points = B.dot(points)

	points /= 10
	return points

def normalize(image):
	max = image.max()
	min = image.min()

	for x in range(0,32):
		for y in range(0,32):
			image[x][y] = 255 / (max - min) * (image[x][y] - min)

	return image

def sigmoid_normalize(image, a):
	for x in range(0,32):
		for y in range(0,32):
			image[x][y] = 255 / (1 + math.exp(-1 / a * (image[x][y] - 128)))

	return image