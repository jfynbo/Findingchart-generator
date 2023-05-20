# Findingchart-generator
A simple python tool to generate finding charts for a list of targets 

This is a simple script to generate finding charts for a list of targets. I use this for a summerschool I teach to help the students make finding charts for their targets. The scripts fetches images from the Digital Sky Survey. It is hardwired to show a field of 8x8 arcmin^2. Information that should go into the finding charts is given in a configuration file. The configuration file looks like this (example):

first row: number of FCs to make
2nd row: Field of view (in arcmin). If larger than 8 arcmin it will not be shown.
3rd row: run name
4th row: PI
In the rows below "Target" provide: Targetname RA(hr:min:sec) Dec(deg:min:sec).
Coordinates are assumed J2000.0.
----------------------------------------------------------------------------------
5

6.7

68-802

IDA Summerschool 2023


Targets:

UGC12423    23:13:13.18    06:25:49.1

Comet       16:23:00      -11:57:25

AT2022nxe   18:43:11.13    60:39:15.7

AT2022ouu   00:42:39.28    41:15:16.9

AT2022fpx   15:31:03.70    53:24:19.26


The script uses numpy, matplotlib, astropy, and astroquery.skyview.
