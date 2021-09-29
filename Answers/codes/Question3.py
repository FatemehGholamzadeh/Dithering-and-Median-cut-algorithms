from matplotlib import pyplot as plt
import  cv2
import numpy as np
import math

###################################################################################

# reading image
pic = cv2.imread("2.jpg")
rows_size, columns_size, channels = pic.shape
pixel_num = rows_size*columns_size
red_palette = []
green_palette = []
blue_palette = []
index_median = []
hist_median = []


##############################################################################


#defining a function to get color
def getColor(channel_palette, color_value):
    diff = [math.fabs(x - color_value) for x in channel_palette]
    min_diff = 256
    index = 0
    for i in range(len(diff)):
        if diff[i] < min_diff:
            min_diff = diff[i]
            index = i
        i += 1
    return index



##########################################################################

# histogram for red channel

sum_pixels = 0
j = 0
k = 0

R_histo = cv2.calcHist([pic], [0], None, [255], [0, 255])
plt.plot(R_histo,color="red")

for i in range(1, 8):
    hist_median.append((i*pixel_num)/8)

for i in range(0,len(R_histo)) :
    sum_pixels += R_histo[i]
    try:
         if sum_pixels >= (hist_median[j]):
            index_median.append(i)
            j += 1
    except :
        break


for i in range(0,len(index_median)):
    mean = 0
    for j in range(k, index_median[i]+1):
        mean += j
    k = i
    red_palette.append(np.round(mean/(index_median[i]-k+1)))

for j in range(k, 256):
    mean += j
red_palette.append(np.round(mean/(256 - k)))

index_median.clear()

#####################################################################################################
# histogram for green channel

sum_pixels = 0
j = 0
k = 0

G_histo = cv2.calcHist([pic], [1], None, [255], [0, 255])
plt.plot(G_histo, color="green")

for i in range(0, len(G_histo)) :
    sum_pixels += G_histo[i]
    try:
        if sum_pixels >= (hist_median[j]):
            index_median.append(i)
            j += 1
    except :
        break

for i in range(0, len(index_median)):
    mean = 0
    for j in range(k, index_median[i]+1):
        mean += j
    k = i
    green_palette.append(np.round(mean / (index_median[i] - k + 1)))

for j in range(k, 256):
    mean += j
green_palette.append(np.round(mean / (256 - k)))

index_median.clear()
hist_median.clear()

###############################################################################################
# histogram for blue channel

sum_pixels = 0
j = 0
k = 0

B_histo=cv2.calcHist([pic], [2], None, [255], [0, 255])
plt.plot(B_histo,color="blue")

for i in range(1, 4):
    hist_median.append((i * pixel_num) / 8)

for i in range(0, 256):
    sum_pixels += B_histo[i]
    try:
      if sum_pixels >= (hist_median[j]):
            index_median.append(i)
            j += 1
    except:
        break

for i in range(0, len(index_median)):
    mean = 0
    for j in range(k, index_median[i
    ]+1):
        mean += j
    k = i
    blue_palette.append(np.round(mean / (index_median[i ] - k + 1)))

for j in range(k, 256):
        mean += j
blue_palette.append(np.round(mean / ( 256 - index_median[k])))


#############################################################################
#medin cut

for x in range(rows_size):
    for y in range(columns_size):
        red, green, blue = pic[x,y]
        alt_red = red_palette[getColor(red_palette, red)]
        alt_green = red_palette[getColor(green_palette, green)]
        alt_blue = red_palette[getColor(blue_palette, blue)]
        pic[x, y] = (alt_red, alt_green, alt_blue)


##############################################################
#howing the result

cv2.imwrite("Median.jpg",pic)
cv2.imshow("Median Result ",pic)
cv2.waitKey()
plt.show()



