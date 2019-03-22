def getBribes(q):
    final_state_map = {}
    initial_state_map = {}
    total_bribes = 0
    ini_q = sorted(q)

    for i in range(0,len(q)):
        initial_state_map[i+1] = i

    for i in range(0,len(q)):
        final_state_map[q[i]] = i

    for i in range(1, len(q)):
        if q[i-1] - ini_q[i-1] > 0:
            bribes = abs(final_state_map[q[i-1]] - initial_state_map[q[i-1]])
            if bribes > 2:
                return 'Too chaotic'
            else:
                total_bribes = bribes + total_bribes
        if q[i-1] > q[i] and final_state_map[q[i-1]] - initial_state_map[q[i-1]] > 0:
            bribes = abs(final_state_map[q[i-1]] - initial_state_map[q[i-1]])
            total_bribes = bribes + total_bribes

    return total_bribes
print getBribes([1,2,5,3,7,8,6,4])