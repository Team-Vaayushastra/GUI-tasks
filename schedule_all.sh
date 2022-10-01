#!/bin/bash


wget -q https://www.celestrak.com/NORAD/elements/weather.txt -O /home/pi/Desktop/Weather_satt/predict/weather.txt
grep "NOAA 15" /home/pi/Desktop/Weather_satt/predict/weather.txt -A 2 >> /home/pi/Desktop/Weather_satt/predict/weather.tle
grep "NOAA 18" /home/pi/Desktop/Weather_satt/predict/weather.txt -A 2 >> /home/pi/Desktop/Weather_satt/predict/weather.tle
grep "NOAA 19" /home/pi/Desktop/Weather_satt/predict/weather.txt -A 2 >> /home/pi/Desktop/Weather_satt/predict/weather.tle
grep "METEOR-M 2" /home/pi/Desktop/Weather_satt/predict/weather.txt -A 2 >> /home/pi/Desktop/Weather_satt/predict/weather.tle

for i in `atq | awk '{print $1}'`;do atrm $i;done

/home/pi/Desktop/Weather_satt/predict/schedule_satellite.sh "NOAA 19" 137.1000
/home/pi/Desktop/Weather_satt/predict/schedule_satellite.sh "NOAA 18" 137.9125
/home/pi/Desktop/Weather_satt/predict/schedule_satellite.sh "NOAA 15" 137.6200
/home/pi/Desktop/Weather_satt/predict/schedule_satellite.sh "METEOR-M 2" 137.1000