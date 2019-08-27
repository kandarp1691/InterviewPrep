def subdomainVisits(cpdomains):
    """
    :type cpdomains: List[str]
    :rtype: List[str]
    """
    dict = {}
    for each in range(0, len(cpdomains)):
        arr = cpdomains[each].split(" ")
        visits = arr[0]
        domains = arr[1]
        dict[domains] = int(visits)
        arr = domains.split(".")
        last_val = arr[-1]
        if last_val in dict:
            dict[last_val] = dict[last_val]+int(visits)
        else:
            dict[last_val] = int(visits)
        if len(arr) == 3:
            second_last = arr[-2] +"." + arr[-1]
            if second_last in dict:
                dict[second_last] = dict[second_last] + int(visits)
            else:
                dict[second_last] = int(visits)
    result = []
    for k, v in dict.iteritems():
        result.append(str(v) + " " + str(k))
    return result

input = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

print subdomainVisits(input)


