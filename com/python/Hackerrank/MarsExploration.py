#This solution is timing about, the commented one in Java works fine
def find_altered_characters(S):
    counter = 0
    for i in range(0, len(S)):
        if S[i] != 'S' and S[i] != 'O':
            counter += 1

    return counter


S = 'SOSSPSSQSSOR'
print find_altered_characters(S)


'''
public static int countChanges(String message) {
        String sos = "SOS";
        int count = 0;
        for (int i = 0; i < message.length(); i++) {
            if (message.charAt(i) != sos.charAt(i % 3)) count++;
        }
        return count;
    }
'''

