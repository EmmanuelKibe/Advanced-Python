def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

numbers = count_up_to(5)
for number in numbers:
    print(number)

#Normal function
def normal_count_up_to(n):
    result = []
    count = 1
    while count <= n:
        result.append(count)
        count += 1
    return result
print(normal_count_up_to(5))