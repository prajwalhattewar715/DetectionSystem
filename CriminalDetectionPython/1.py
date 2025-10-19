import numpy as np
from keras.utils import to_categorical
### Categorical data to be converted to numeric data
#colors = ["BELL HOWARD", "Dawood Ibrahim Kaskar", "GARVIN RAYMOND", "Ilyas Kashmiri", "Masood Azhar","MCCUTCHEON JOHN"]

### Universal list of colors
#total_colors = ["BELL HOWARD", "Dawood Ibrahim Kaskar", "GARVIN RAYMOND", "Ilyas Kashmiri", "Masood Azhar","MCCUTCHEON JOHN"]
colors =  ["BELL HOWARD","Dawood Ibrahim Kaskar","GARVIN RAYMOND","Ilyas Kashmiri","Masood Azhar","MCCUTCHEON JOHN","Sajid Mir","Syed Salahuddin","TIPTON DARNELL"]
total_colors = ["BELL HOWARD","Dawood Ibrahim Kaskar","GARVIN RAYMOND","MCCUTCHEON JOHN","Ilyas Kashmiri","Masood Azhar","Sajid Mir","Syed Salahuddin","TIPTON DARNELL"]









### map each color to an integer
predicted_label = sorted(total_colors)
print(predicted_label)
mapping = {}
for x in range(len(total_colors)):
  mapping[total_colors[x]] = x
  print(total_colors[x])

# integer representation
for x in range(len(colors)):
  colors[x] = mapping[colors[x]]
  print(colors[x])

print(colors)
colors=[1,2,3,4,5,6,10,11,12,7,8,9]
one_hot_encode = to_categorical(colors)
print(one_hot_encode)