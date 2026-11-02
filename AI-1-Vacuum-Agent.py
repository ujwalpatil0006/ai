# Simple Reflex Agent for Vacuum Cleaner World

def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    else:
        return "Left"


# Environment
environment = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"

# Run the agent
for i in range(5):
    print("Location:", location)
    print("Status:", environment[location])

    action = vacuum_agent(location, environment[location])
    print("Action:", action)

    if action == "Suck":
        environment[location] = "Clean"
    elif action == "Right":
        location = "B"
    elif action == "Left":
        location = "A"

    print()
