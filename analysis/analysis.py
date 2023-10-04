import pandas as pd
import matplotlib.pyplot as plt


moving_good_df = pd.read_csv (r'/home/basilreji/catkin_ws/src/lab2/good_moving.csv')

plt.title("Moving RTK GPS Plot (Open Area)")
plt.xlabel("UTM Easting (m)")
plt.ylabel("UTM Northing (m)")

easting1, northing1 = moving_good_df[".UTM_easting"], moving_good_df[".UTM_northing"] 
plt.scatter(easting1, northing1, color = 'r')
plt.show()

moving_bad_df = pd.read_csv (r'/home/basilreji/catkin_ws/src/lab2/bad_moving.csv')
plt.title("Moving RTK GPS Plot (Secluded Area)")
plt.xlabel("UTM Easting (m)")
plt.ylabel("UTM Northing (m)")

easting2, northing2 = moving_bad_df[".UTM_easting"], moving_bad_df[".UTM_northing"] 
plt.scatter(easting2, northing2, color = 'g')
plt.show()

static_good_df = pd.read_csv (r'/home/basilreji/catkin_ws/src/lab2/good_static.csv')
plt.title("Moving RTK GPS Plot (Open Area)")
plt.xlabel("UTM Easting (m)")
plt.ylabel("UTM Northing (m)")

easting3, northing3 = static_good_df[".UTM_easting"], static_good_df[".UTM_northing"] 
plt.scatter(easting3, northing3, color = 'b')
plt.show()

static_bad_df = pd.read_csv (r'/home/basilreji/catkin_ws/src/lab2/bad_static.csv')
plt.title("Moving RTK GPS Plot (Secluded Area)")
plt.xlabel("UTM Easting (m)")
plt.ylabel("UTM Northing (m)")

easting4, northing4 = static_bad_df[".UTM_easting"], static_bad_df[".UTM_northing"] 
plt.scatter(easting4, northing4, color = 'y')
plt.show()

