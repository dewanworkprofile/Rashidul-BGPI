import numpy as np
# week = np.array([12, 23, 12, 33, 44, 2, 34, 244, 24, 42, 2, 231, 234, 4, 234, 45, 23, 24])
# week_seals=week.reshape(3,6)
# print(week_seals.shape)
# print(*week.shape)
# print(week.dtype)
# print(week_seals.ndim)
# print(week_seals)

brance=np.array(['Dhaka','Chatagram','khulna','Barishal'],dtype='U')
week_days=np.array([1,2,3,4,5,6,7],dtype='i8')
# for i in week_days:
#     print(i)
# print(week_days.astype('F'))
# days=np.array(['sat','sun','mon','tue','wed','thu','fri'])
# print(days.astype('U'))
# arr3=week_days.copy()
# arr4=week_days.view()
# arr4[2]=9
# print(f"copied:{arr3},{arr3.dtype}")
# print(f"viewed:{arr4},{arr4.dtype}")
copied=week_days.copy()
slice=week_days[0:4]
slice_reverse=week_days[5:3:-1]
print(f"sliced:{slice}")
print(f"sliced reverse:{slice_reverse}")
print(week_days[::2])
print(week_days[1::2])
