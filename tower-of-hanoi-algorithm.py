def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]

    moves = []

    def record():
        moves.append(f"{rods[0]} {rods[1]} {rods[2]}")

    def move_disks(count, source, target, auxiliary):
        if count == 0:
            return
        
        move_disks(count -1, source, auxiliary, target)

        disk = rods[source].pop()
        rods[target].append(disk)
        record()

        move_disks(count -1, auxiliary, target, source)

    record()

    move_disks(n, 0, 2, 1)

    return "\n".join(moves)
