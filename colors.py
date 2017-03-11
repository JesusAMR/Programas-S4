#! /usr/bin/python
#Write a Python program to display the first and last colors from the following list.

color_list = ["Red", "Green", "White", "Black"]
dic_colores = {"Red": "\033[31m", "Green": "\033[32m", "White": "\033[37m", "Black": "\033[30m"}
limpiarstr = "\033[0m"

print dic_colores[color_list[0]] + color_list[0] + " " + dic_colores[color_list[-1]] + color_list[-1] + limpiarstr

