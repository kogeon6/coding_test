def solution(park, routes):
    height = 0
    width = 0

    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                height = i
                width = j

    for route in routes:
        direction, distance = route.split()
        distance = int(distance)

        next_h = height
        next_w = width
        Flag = False

        for j in range(distance):
            if direction == "E":
                next_w += 1
            elif direction == "W":
                next_w -= 1
            elif direction == "S":
                next_h += 1
            elif direction == "N":
                next_h -= 1

            if next_h < 0 or next_h >= len(park):
                Flag = True
                break

            if next_w < 0 or next_w >= len(park[0]):
                Flag = True
                break

            if park[next_h][next_w] == "X":
                Flag = True
                break

        if Flag == False:
            height = next_h
            width = next_w

    return [height, width]