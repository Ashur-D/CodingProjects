courses = {'prog12583':95, 'prog22567': 89, 'prog19803':85 }

codes = list(courses.keys())
codes.sort()
print(codes)

for var in codes:
    print(courses[var])
