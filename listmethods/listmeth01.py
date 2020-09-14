#!/usr/bin/env python3

proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

# print the current proto list
print(proto)

# Counts the number times 'http' appears in the list
proto.count("http")

# Inserts 'http' after the second item in the proto list
proto.insert(1, "http")

# Count the number of time 'http' appears in the list and then prints the list
proto.count("http")
print(proto)

