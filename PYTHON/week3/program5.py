# 9/17/2025
# demonstarting runtime errors

score1 = 112
score2 = 82
score3 = 136
avg = (score1 + score2 + score3) / 0 # apply order of operations
print("The average score is", avg, end='\n') # go to next line
print("The average score", avg, sep=' = ')