import time  

# Ask the user how many seconds to count down from
seconds = int(input("Enter the number of seconds: "))

# Use a loop to count down
while seconds > 0:
    print("Time left:", seconds, "seconds")
    time.sleep(1)  # Wait for 1 second
    seconds = seconds - 1  # Subtract 1 from the seconds

# When the loop ends, print this
print("Time's up!")
