# Practice Exercise 5: Traffic Simulator
import time

def traffic_lights_simulator():
    # Define the intervals for each light in seconds
    green_duration = 30
    yellow_duration = 5
    red_duration = 20
    
    while True:  # Run indefinitely
        print("Green light - Go!")
        time.sleep(green_duration)
        
        print("Yellow light - Prepare to stop!")
        time.sleep(yellow_duration)
        
        print("Red light - Stop!")
        time.sleep(red_duration)
        
        # Ask the user if they want to continue or stop the simulation
        user_input = input("Do you want to continue the simulation? (yes/no): ").lower()
        if user_input != 'yes':
            break

# Call the function to start the traffic lights simulation
traffic_lights_simulator()
