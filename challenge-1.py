
def array_left_rotation(array, n, rotations):
    for _ in range(0, rotations):
        array = [*array[1:], array[0]]
    return array

n, k = map(int, input().strip().split(' '))
array = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(array, n, k);
print(*answer, sep=' ')