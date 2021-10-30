# ClutchMomentsFootball Analysis: 
An ongoing project to identify and analyse decisive goals and plays made in high-pressure moments of a football match.

This is a personal project to gain exposure to data-driven analysis, sports related data science and gain hands-on experience working in a data science project.

The data used is from Statsbomb's Open Data, found here: https://github.com/statsbomb/open-data

The goal of the project is to create a program that:
  1. Accepts a list of .json files from Statsbomb's Open Data source, containing event data for each match.
  2. Finds and filters out shots made in the 80+ minute, high Expected Goal (xG) Blocks, one-on-one opportunities, etc.
  3. Analyse whether/ how the match was decided in the 80+ minutes.
  4. Return the information on the event(s) that decided the outcome of the match.

Documentation of code:
  1. Shot_Seeker.py : To open a file, find the positions of all the shots within the file, and return a list with those values, to be used in subsequent analysis.
  2. Shot_Filter.py : to open a .json database and filter out the shots after the 80th minute.
