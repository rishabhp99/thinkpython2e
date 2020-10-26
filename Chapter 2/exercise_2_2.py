# Assume that we execute the following assignment statements:
# width = 17
# height = 12.0
# delimiter = '.'
# For each of the following expressions, write the value of the expression and the type (of the value of
# the expression).
# 1. width/2
# 2. width/2.0
# 3. height/3
# 4. 1 + 2 * 5
# 5. delimiter * 5

width = 17
height = 12.0
delimiter = '.'

print(width/2, "type: ", type(width/2))

print(width/2.0, "type: ", type(width/2.0))

print(height/3, "type: ", type(height/3))

print(1 + 2 * 5, "type: ", type(1 + 2 * 5))

print(delimiter * 5, "type: ", type(delimiter*5))