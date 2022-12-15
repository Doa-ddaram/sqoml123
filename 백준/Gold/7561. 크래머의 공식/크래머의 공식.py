import sys
input = sys.stdin.readline
for _ in range(int(input())):
  a_L = [0] * 4
  b_L = [0] * 4
  c_L = [0] * 4
  B_L = [0] * 4
  for i in range(1,4):
    a_L[i], b_L[i],c_L[i], B_L[i] = map(int,input().split())
  det_a1 = B_L[1]*(b_L[2] * c_L[3] - b_L[3] * c_L[2]) - b_L[1] * (B_L[2] * c_L[3] - B_L[3] * c_L[2]) + c_L[1] * (B_L[2] * b_L[3] - B_L[3] * b_L[2])
  det_a2 = a_L[1]*(B_L[2] * c_L[3] - B_L[3] * c_L[2]) - B_L[1] * (a_L[2] * c_L[3] - a_L[3] * c_L[2]) + c_L[1] * (a_L[2] * B_L[3] - a_L[3] * B_L[2])
  det_a3 = a_L[1]*(b_L[2] * B_L[3] - b_L[3] * B_L[2]) - b_L[1] * (a_L[2] * B_L[3] - a_L[3] * B_L[2]) + B_L[1] * (a_L[2] * b_L[3] - a_L[3] * b_L[2])
  det_a = a_L[1]*(b_L[2] * c_L[3] - b_L[3] * c_L[2]) - b_L[1] * (a_L[2] * c_L[3] - a_L[3] * c_L[2]) + c_L[1] * (a_L[2] * b_L[3] - a_L[3] * b_L[2])
  print(det_a1,det_a2,det_a3, det_a)
  if det_a:
    so1,so2,so3 = det_a1/ det_a, det_a2/det_a, det_a3/det_a
    if -0.0005< so1 < 0.0005:
      so1 = 0.000
    if -0.0005< so2 < 0.0005:
      so2 = 0.000
    if -0.0005< so3 < 0.0005:
      so3 = 0.000
    print('Unique solution: %.3lf %.3lf %.3lf' %(so1,so2,so3))
  else:
    print('No unique solution')
  print('')