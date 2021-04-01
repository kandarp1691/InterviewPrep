def canAttendMeeting(intervals):
    intervals = sorted(intervals, key=lambda x:x[0])
    for i in range(1, len(intervals)):
        if intervals[i-1][0] > intervals[i][1] :
            return False
    return True

print canAttendMeeting([[7,10],[2,4]])
