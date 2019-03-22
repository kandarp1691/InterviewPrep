def maximumPeople(p, x, y, r):
    # Return the maximum number of people that will be in a sunny town after removing exactly one cloud.
    total_population = sum(p)
    print total_population
    location_to_pop = {}
    cloud_range = {}
    for i in range(0, len(p)):
        location_to_pop[x[i]] = p[i]

    # location and range of clouds
    for i in range(0, len(y)):
        cloud_range[y[i]] = (y[i] - r[i], y[i] + r[i])

    affected = {}
    for k, v in cloud_range.iteritems():
        for i in range(0, len(x)):
            if v[0] <= x[i] <= v[1]:
                affected[x[i]] = location_to_pop[x[i]]
    print affected

    total_affected = sum(affected.values())
    total_unaffected = total_population - total_affected
    max_pop_affected_by_cloud = max(affected.iteritems(), key=lambda x: x[1])[1]

    max_people_saved = total_unaffected + max_pop_affected_by_cloud

    return max_people_saved
