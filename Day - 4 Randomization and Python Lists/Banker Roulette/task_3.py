import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Short and Simple Way :-
print(random.choice(friends))

# Basic Way
random_index = random.randint(0,4)
print(friends[random_index])
