import numpy as np
import csv

# import file
f = open('D:/Study/Dataquest/Data sets/nyc_taxis.csv', 'r')
file = list(csv.reader(f))
print(file[0:5])
# header
header = file[0]
taxi_data = file[1:]
# numpy array
converted_taxi_list = []
for t in taxi_data:
    converted_row = []
    for i in t:
        converted_row.append(float(i))
    converted_taxi_list.append(converted_row)

taxi = np.array(converted_taxi_list)

# finding the size of the ndarray
taxi_shape = taxi.shape
print(taxi_shape)
# getting the subset of data using indexing. Since our array is 2d we are passing 2 vector for that.
rows_391_to_500 = taxi[391:501]
row_21_column_5 = taxi[21, 5]

# getting multiple column of data at once
col = [1, 4, 7]
columns_1_4_7 = taxi[:, col]

trip_distance_miles = taxi[:,7]
trip_length_seconds = taxi[:,8]

trip_length_hours = trip_length_seconds / 3600 # 3600 seconds is one hour
trip_mph = trip_distance_miles / trip_length_hours

mph_min = trip_mph.min()
mph_max = trip_mph.max()
mph_mean = trip_mph.mean()

# we'll compare against the first 5 rows only
taxi_first_five = taxi[:5]
# select these columns: fare_amount, fees_amount, tolls_amount, tip_amount
fare_components = taxi_first_five[:,9:13]
# sum the component columns
fare_sums = fare_components.sum(axis=1)

# select the total_amount column
fare_totals = taxi_first_five[:,13]

# compare the summed columns to the fare_totals
print(fare_totals)
print(fare_sums)


# we can also read file like this
taxi1 = np.genfromtxt('D:/Study/Dataquest/Data sets/nyc_taxis.csv', delimiter=',', skip_header=1)

# boolean indexing
a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])
a_bool = a < 3
b_bool = b == "blue"
c_bool = c > 100

pickup_month = taxi[:,1]

january_bool = pickup_month == 1
january = pickup_month[january_bool]
january_rides = january.shape[0]
february_bool = pickup_month == 2
february = pickup_month[february_bool]
february_rides = february.shape[0]

# this creates a copy of our taxi ndarray
taxi_modified = taxi.copy()
taxi_modified[28214, 5] = 1
taxi_modified[:, 0] = 16#(taxi_modified[:, 0] % 1000) # since year in the data in 2106, we can replace it with 16
# data for trip distace at index 1800 and 1801 is wrong so replace it with the mean value
taxi_modified[1800:1802, 7] = taxi_modified[:, 7].mean()
# since amount can't bbe negative so replace it with 0
total_amount = taxi_copy[:,13]
total_amount[total_amount < 0] = 0

# create a new column filled with `0`.
zeros = np.zeros([taxi.shape[0], 1])
taxi_modified = np.concatenate([taxi, zeros], axis=1)
print(taxi_modified)
taxi_modified[taxi_modified[:, 5] == 2, 15] = 1
taxi_modified[taxi_modified[:, 5] == 3, 15] = 1
taxi_modified[taxi_modified[:, 5] == 5, 15] = 1

trip_mph = taxi[:,7] / (taxi[:,8] / 3600)
cleaned_taxi = taxi[trip_mph < 100]

mean_distance = cleaned_taxi[:,7].mean()
mean_length = cleaned_taxi[:,8].mean()
mean_total_amount = cleaned_taxi[:,13].mean()
