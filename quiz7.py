def std_weight(height,gender):
    if gender == "W":
        return height*height*21
    else:
        return height*height*22
height = 175
gender="M"
weight = round(std_weight(height/100,gender),2)
print("{}".format(weight))