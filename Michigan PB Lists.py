#Write a program that extracts the last three items in the list sports and assigns it to the variable last.
#Make sure to write your code so that it works no matter how many items are in the list.

sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
last = sports[len(sports)-3:len(sports)]
print(last)

#Write code that combines the following variables so that the sentence “You are doing a great job, keep it up!”
#is assigned to the variable message. Do not edit the values assigned to by, az, io, or qy.

by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"
message = by + " " + az + io + ", " + qy                 #another form of doing it is: " ".join([by, az, io, qy])
print(message)