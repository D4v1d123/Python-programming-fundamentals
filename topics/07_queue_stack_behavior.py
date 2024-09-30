# QUEUE BEHAVIOR
client = ["Marcela", "Alejandro", "Mariana"]

process = client.pop(0)  # Extract the first item and remove it from the list.
print("Pop: ", process)

client.append("Carlos")  # Add an item to the last position.
print("Add 'Carlos': ", client)
print("\n")


# STACKS BEHAVIOR
client = ["Marcela", "Alejandro", "Mariana"]

process = client.pop()  # Extract the last item and remove it from the list.
print("Pop: ", process)

client.append("Carlos")  # Add an item to the last position.
print("Add 'Carlos': ", client)
print("\n")