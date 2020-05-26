
from __future__ import division
# Phi/Psi corrections in Angstrom and Radials
mean_devs = {
  (-170, -180) : (0.039100, -1.177605), # 20
  (-170, -170) : (0.035297, -1.183224), # 12
  (-170, 140) : (0.010351, -0.992488), # 39
  (-170, 150) : (0.019600, 0.905143), # 84
  (-170, 160) : (0.039774, 0.475851), # 72
  (-170, 170) : (0.039804, 0.537838), # 32
  (-170, 180) : (0.034055, 0.228127), # 22
  (-160, -180) : (0.055875, -1.071045), # 71
  (-160, -170) : (0.066824, -0.922656), # 61
  (-160, -160) : (0.069252, -0.904102), # 14
  (-160, 130) : (0.018519, -1.690495), # 48
  (-160, 140) : (0.035125, -1.193746), # 212
  (-160, 150) : (0.027591, -0.348835), # 538
  (-160, 160) : (0.028775, -0.078730), # 329
  (-160, 170) : (0.030259, -0.494728), # 125
  (-160, 180) : (0.045031, -0.859731), # 72
  (-150, -180) : (0.053651, -1.126372), # 92
  (-150, -170) : (0.085264, -1.234147), # 142
  (-150, -160) : (0.090567, -1.113362), # 31
  (-150, 100) : (0.038911, 1.637471), # 13
  (-150, 110) : (0.039372, 1.041075), # 23
  (-150, 120) : (0.003001, -1.219585), # 54
  (-150, 130) : (0.020729, -1.128077), # 259
  (-150, 140) : (0.029106, -0.956691), # 863
  (-150, 150) : (0.029243, -0.810366), # 937
  (-150, 160) : (0.018249, 0.916283), # 601
  (-150, 170) : (0.020163, 1.255210), # 388
  (-150, 180) : (0.020676, -0.853797), # 134
  (-140, -180) : (0.018951, 0.298835), # 141
  (-140, -170) : (0.040871, -1.080730), # 117
  (-140, -160) : (0.104336, -1.239540), # 32
  (-140, -150) : (0.118324, -1.314583), # 10
  (-140, -60) : (0.033567, -1.726091), # 10
  (-140, -50) : (0.004572, 2.864564), # 12
  (-140, -40) : (0.048146, -2.037771), # 10
  (-140, -30) : (0.035968, -2.056307), # 25
  (-140, -20) : (0.044028, -2.459679), # 19
  (-140, -10) : (0.028699, 2.496739), # 40
  (-140, 0) : (0.012065, 3.128299), # 42
  (-140, 10) : (0.005250, 2.917852), # 32
  (-140, 20) : (0.003626, -2.880002), # 46
  (-140, 30) : (0.038224, -1.292172), # 24
  (-140, 40) : (0.039848, -1.458059), # 26
  (-140, 50) : (0.045414, -1.691334), # 23
  (-140, 60) : (0.028321, -1.383843), # 31
  (-140, 70) : (0.020617, -0.776091), # 52
  (-140, 80) : (0.019672, -0.966172), # 49
  (-140, 90) : (0.027733, 0.451979), # 60
  (-140, 100) : (0.031654, 1.119220), # 95
  (-140, 110) : (0.031791, 1.263151), # 216
  (-140, 120) : (0.033046, 1.348114), # 742
  (-140, 130) : (0.031191, 1.116316), # 1970
  (-140, 140) : (0.020804, 0.392644), # 2293
  (-140, 150) : (0.002702, 0.908554), # 1826
  (-140, 160) : (0.025906, 1.927208), # 2502
  (-140, 170) : (0.035307, 1.559917), # 1439
  (-140, 180) : (0.028871, 1.357359), # 303
  (-130, -180) : (0.011292, -0.022455), # 178
  (-130, -170) : (0.025431, -0.841925), # 121
  (-130, -160) : (0.092040, -1.256506), # 36
  (-130, -100) : (0.083186, -1.702218), # 15
  (-130, -90) : (0.086638, -1.547633), # 24
  (-130, -80) : (0.061876, -1.617552), # 23
  (-130, -70) : (0.042582, -1.329022), # 22
  (-130, -60) : (0.032320, -1.638576), # 72
  (-130, -50) : (0.032905, -1.463480), # 62
  (-130, -40) : (0.038181, -1.928063), # 54
  (-130, -30) : (0.042138, -2.388421), # 93
  (-130, -20) : (0.032274, -2.650007), # 252
  (-130, -10) : (0.025416, -2.690438), # 293
  (-130, 0) : (0.031060, -2.265391), # 279
  (-130, 10) : (0.026805, -2.026934), # 266
  (-130, 20) : (0.033225, -1.752752), # 231
  (-130, 30) : (0.043239, -1.663039), # 154
  (-130, 40) : (0.049720, -1.673735), # 97
  (-130, 50) : (0.061324, -1.606206), # 60
  (-130, 60) : (0.054534, -1.520821), # 109
  (-130, 70) : (0.031602, -0.951458), # 149
  (-130, 80) : (0.021598, -0.828470), # 177
  (-130, 90) : (0.015097, -0.291520), # 220
  (-130, 100) : (0.020191, 0.558579), # 375
  (-130, 110) : (0.020975, 0.723288), # 1076
  (-130, 120) : (0.024324, 1.009148), # 3515
  (-130, 130) : (0.027783, 0.887899), # 6274
  (-130, 140) : (0.024640, 0.511681), # 3901
  (-130, 150) : (0.013799, -2.199653), # 2879
  (-130, 160) : (0.009897, 3.135324), # 3748
  (-130, 170) : (0.015384, 1.493375), # 1917
  (-130, 180) : (0.016643, 1.145796), # 373
  (-120, -180) : (0.015445, -0.152133), # 105
  (-120, -170) : (0.039681, -1.175070), # 70
  (-120, -160) : (0.067194, -1.325840), # 11
  (-120, -150) : (0.087968, -1.366773), # 11
  (-120, -140) : (0.152628, -1.450107), # 10
  (-120, -100) : (0.129841, -1.541614), # 14
  (-120, -90) : (0.082933, -1.369499), # 31
  (-120, -80) : (0.073783, -1.548882), # 40
  (-120, -70) : (0.064228, -1.505918), # 65
  (-120, -60) : (0.044445, -1.590806), # 186
  (-120, -50) : (0.035180, -1.270478), # 210
  (-120, -40) : (0.027087, -1.166147), # 128
  (-120, -30) : (0.047747, -2.124127), # 203
  (-120, -20) : (0.037015, -2.374941), # 556
  (-120, -10) : (0.042211, -2.195318), # 773
  (-120, 0) : (0.037122, -2.030320), # 677
  (-120, 10) : (0.042402, -1.921795), # 608
  (-120, 20) : (0.051830, -1.797003), # 527
  (-120, 30) : (0.065015, -1.717984), # 217
  (-120, 40) : (0.069011, -1.610637), # 65
  (-120, 60) : (0.033718, -1.615376), # 14
  (-120, 70) : (0.040346, -1.353159), # 37
  (-120, 80) : (0.025695, -0.647170), # 99
  (-120, 90) : (0.023101, -0.187190), # 203
  (-120, 100) : (0.022700, 0.113396), # 588
  (-120, 110) : (0.018771, 0.369761), # 1808
  (-120, 120) : (0.024071, 0.664790), # 5812
  (-120, 130) : (0.028615, 0.635577), # 7908
  (-120, 140) : (0.025823, 0.295269), # 3286
  (-120, 150) : (0.023733, -1.918635), # 1811
  (-120, 160) : (0.013737, -2.271646), # 1917
  (-120, 170) : (0.006331, 1.333296), # 909
  (-120, 180) : (0.017084, 1.021596), # 205
  (-110, -180) : (0.020220, -0.834912), # 68
  (-110, -170) : (0.020710, -0.422097), # 53
  (-110, -160) : (0.072020, -1.362856), # 12
  (-110, -100) : (0.095726, -1.431237), # 11
  (-110, -90) : (0.114713, -1.551160), # 23
  (-110, -80) : (0.082703, -1.425735), # 29
  (-110, -70) : (0.066952, -1.566962), # 51
  (-110, -60) : (0.044522, -1.501933), # 169
  (-110, -50) : (0.026507, -1.183272), # 312
  (-110, -40) : (0.031472, -1.295729), # 251
  (-110, -30) : (0.041576, -1.867514), # 258
  (-110, -20) : (0.036150, -2.202371), # 745
  (-110, -10) : (0.040648, -2.027974), # 873
  (-110, 0) : (0.038531, -2.025919), # 819
  (-110, 10) : (0.050562, -1.896469), # 764
  (-110, 20) : (0.072009, -1.783872), # 476
  (-110, 30) : (0.065275, -1.779605), # 141
  (-110, 40) : (0.048289, -1.438638), # 17
  (-110, 50) : (0.102641, -1.754653), # 12
  (-110, 80) : (0.038746, -0.872601), # 18
  (-110, 90) : (0.026924, -0.488421), # 102
  (-110, 100) : (0.027291, -0.062153), # 572
  (-110, 110) : (0.022013, 0.217559), # 2044
  (-110, 120) : (0.025312, 0.529715), # 5518
  (-110, 130) : (0.029844, 0.528276), # 6161
  (-110, 140) : (0.026977, 0.182348), # 2112
  (-110, 150) : (0.023594, -1.845726), # 853
  (-110, 160) : (0.005900, -2.088980), # 907
  (-110, 170) : (0.018649, 1.201660), # 517
  (-110, 180) : (0.015396, 1.027305), # 120
  (-100, -180) : (0.020408, 0.185498), # 46
  (-100, -170) : (0.026144, -0.757265), # 48
  (-100, -160) : (0.090657, -1.046887), # 13
  (-100, -90) : (0.102330, -1.521455), # 14
  (-100, -80) : (0.072720, -1.310019), # 16
  (-100, -70) : (0.062296, -1.319038), # 39
  (-100, -60) : (0.046745, -1.544039), # 160
  (-100, -50) : (0.025759, -1.110632), # 443
  (-100, -40) : (0.026827, -0.896894), # 412
  (-100, -30) : (0.034651, -1.838309), # 318
  (-100, -20) : (0.031750, -2.194610), # 690
  (-100, -10) : (0.034680, -2.197765), # 840
  (-100, 0) : (0.038343, -2.030933), # 998
  (-100, 10) : (0.049948, -1.890953), # 738
  (-100, 20) : (0.062976, -1.829923), # 258
  (-100, 30) : (0.071842, -1.682743), # 42
  (-100, 40) : (0.096815, -1.623131), # 11
  (-100, 60) : (0.049525, -1.335983), # 10
  (-100, 70) : (0.041289, -0.772956), # 16
  (-100, 80) : (0.034276, -0.976998), # 30
  (-100, 90) : (0.037794, -0.713208), # 90
  (-100, 100) : (0.024078, -0.209898), # 444
  (-100, 110) : (0.023245, 0.140584), # 1782
  (-100, 120) : (0.025831, 0.393736), # 3931
  (-100, 130) : (0.029760, 0.479753), # 3940
  (-100, 140) : (0.030358, 0.169726), # 1295
  (-100, 150) : (0.021572, -1.575677), # 492
  (-100, 160) : (0.003847, 2.058461), # 578
  (-100, 170) : (0.024890, 1.159575), # 430
  (-100, 180) : (0.020909, 1.053170), # 102
  (-90, -180) : (0.025057, 0.627467), # 45
  (-90, -170) : (0.036556, -1.208946), # 22
  (-90, -160) : (0.032532, -0.693381), # 11
  (-90, -70) : (0.075865, -1.576000), # 35
  (-90, -60) : (0.046183, -1.550310), # 141
  (-90, -50) : (0.024688, -1.053965), # 606
  (-90, -40) : (0.030710, -1.008599), # 589
  (-90, -30) : (0.039961, -1.689632), # 416
  (-90, -20) : (0.031583, -2.157844), # 792
  (-90, -10) : (0.033368, -2.227301), # 1074
  (-90, 0) : (0.035012, -2.095990), # 1028
  (-90, 10) : (0.044279, -1.880319), # 394
  (-90, 20) : (0.051895, -1.832240), # 44
  (-90, 40) : (0.064170, -1.647912), # 10
  (-90, 50) : (0.042887, -1.243863), # 12
  (-90, 60) : (0.051084, -1.355028), # 23
  (-90, 70) : (0.078866, -1.421970), # 45
  (-90, 80) : (0.050852, -1.155882), # 125
  (-90, 90) : (0.039571, -0.971753), # 179
  (-90, 100) : (0.025085, -0.450660), # 433
  (-90, 110) : (0.021645, -0.071709), # 1360
  (-90, 120) : (0.023916, 0.239667), # 2775
  (-90, 130) : (0.029990, 0.297050), # 2804
  (-90, 140) : (0.033344, 0.135823), # 998
  (-90, 150) : (0.016757, -1.104586), # 379
  (-90, 160) : (0.014991, 1.466174), # 666
  (-90, 170) : (0.039526, 1.252086), # 533
  (-90, 180) : (0.024542, 0.954524), # 94
  (-80, -180) : (0.038022, 0.986759), # 40
  (-80, -170) : (0.038421, 1.010631), # 28
  (-80, -60) : (0.047030, -1.550948), # 156
  (-80, -50) : (0.031225, -1.211185), # 1091
  (-80, -40) : (0.038368, -1.151238), # 1342
  (-80, -30) : (0.060821, -1.728169), # 809
  (-80, -20) : (0.048417, -2.095827), # 1019
  (-80, -10) : (0.043192, -2.206976), # 1178
  (-80, 0) : (0.054472, -1.953496), # 474
  (-80, 10) : (0.048692, -1.811687), # 82
  (-80, 60) : (0.088120, -1.489534), # 18
  (-80, 70) : (0.051681, -1.155341), # 26
  (-80, 80) : (0.063863, -1.322189), # 67
  (-80, 90) : (0.048564, -1.152976), # 82
  (-80, 100) : (0.028063, -0.843964), # 224
  (-80, 110) : (0.020497, -0.449375), # 775
  (-80, 120) : (0.021419, 0.102185), # 2273
  (-80, 130) : (0.026538, 0.122153), # 2638
  (-80, 140) : (0.035253, -0.015866), # 1079
  (-80, 150) : (0.015586, -1.340575), # 487
  (-80, 160) : (0.016404, 1.651580), # 935
  (-80, 170) : (0.041047, 1.269616), # 818
  (-80, 180) : (0.039924, 1.268462), # 109
  (-70, -60) : (0.059024, -1.616031), # 229
  (-70, -50) : (0.038942, -1.251738), # 6470
  (-70, -40) : (0.050463, -1.321426), # 13825
  (-70, -30) : (0.083713, -1.767829), # 3619
  (-70, -20) : (0.065105, -1.977661), # 2028
  (-70, -10) : (0.064499, -2.065330), # 1160
  (-70, 0) : (0.069219, -1.966177), # 157
  (-70, 100) : (0.023202, -0.341432), # 24
  (-70, 110) : (0.022787, -0.805295), # 176
  (-70, 120) : (0.018220, -0.282864), # 1247
  (-70, 130) : (0.025526, -0.117578), # 2656
  (-70, 140) : (0.031534, -0.272924), # 1353
  (-70, 150) : (0.019928, -1.494329), # 766
  (-70, 160) : (0.009805, 1.790617), # 1090
  (-70, 170) : (0.033224, 1.206697), # 492
  (-70, 180) : (0.015042, 0.333699), # 32
  (-60, -60) : (0.068141, -1.649754), # 330
  (-60, -50) : (0.039577, -1.281559), # 19101
  (-60, -40) : (0.047504, -1.289895), # 19952
  (-60, -30) : (0.070756, -1.644570), # 3416
  (-60, -20) : (0.063359, -1.873275), # 1241
  (-60, -10) : (0.077656, -2.023494), # 124
  (-60, 110) : (0.016187, -0.490848), # 19
  (-60, 120) : (0.020170, -0.302879), # 463
  (-60, 130) : (0.025008, -0.380850), # 1938
  (-60, 140) : (0.030405, -0.621625), # 1316
  (-60, 150) : (0.025029, -1.592350), # 522
  (-60, 160) : (0.003992, 2.751709), # 224
  (-60, 170) : (0.020786, 0.485073), # 38
  (-50, -60) : (0.075194, -1.706880), # 129
  (-50, -50) : (0.046158, -1.449030), # 2092
  (-50, -40) : (0.057016, -1.443656), # 1517
  (-50, -30) : (0.068207, -1.601243), # 325
  (-50, -20) : (0.047212, -1.586467), # 23
  (-50, 120) : (0.019259, -0.337252), # 147
  (-50, 130) : (0.026765, -0.385795), # 648
  (-50, 140) : (0.035590, -0.750828), # 314
  (-50, 150) : (0.027311, -1.520417), # 43
  (-40, -60) : (0.070546, -1.619691), # 25
  (-40, -50) : (0.054911, -1.512325), # 65
  (-40, -40) : (0.041599, -1.153152), # 20
  (-40, 120) : (0.017717, 0.142113), # 21
  (-40, 130) : (0.022994, -0.572740), # 36
  (40, 40) : (0.199025, -1.892311), # 13
  (40, 50) : (0.129214, -1.808620), # 20
  (40, 60) : (0.109516, -1.887967), # 17
  (50, 40) : (0.150394, -1.777165), # 25
  (50, 50) : (0.102268, -1.849139), # 29
  (50, 60) : (0.078204, -1.638902), # 21
  (60, 40) : (0.099065, -1.771405), # 17
  (60, 50) : (0.078828, -1.817775), # 16
  (60, 60) : (0.113703, -1.792203), # 22
  (60, 70) : (0.112526, -1.761346), # 10
  (70, -60) : (0.118713, -2.020618), # 29
  (70, -50) : (0.097268, -2.024971), # 23
  (70, 0) : (0.141350, -2.247120), # 12
  (70, 160) : (0.128734, -2.394952), # 13
  (70, 170) : (0.081413, -2.838786), # 14
  (80, -10) : (0.173921, -2.422485), # 20
  (80, 0) : (0.186558, -2.434710), # 19
}

if __name__ == '__main__':
  for phi_psi in [(0,0), (-60,-60)]:
    print(phi_psi, mean_devs.get(phi_psi, None))
