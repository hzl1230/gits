def sqrt(n):
    return n**0.5

R1 = 287
R4 = [287, 4156]
g1 = 1.4


# 3.2
c12 = 1.4*287*300
A1 = (2.8/2.4*3.66*3.66-0.4/2.4)
A2 = (1+0.2*3.66**2)
B = 1.2*3.66**2
c22 = c12*A/B
v2 = 2/2.4*(3-1./3)*sqrt(c12)
# 3.3/3.4
C = [1-0.4/2.4*sqrt(R1/R4)*(3.66-1/3.66) for R4 in R4]
p4 = [1e4*A*C[i] for i in range(len(C))]
print(p4)



# 1.7
# T = 239.2
# P = 0.38e5
# V = [217, 620]
# c = sqrt(g*R*T)
# print(c)
# for v in V:
#     T0 = T + (2.4/2.8/R)*v**2
#     p0 = P*(T0/T)**(1.4/0.4)
#     print(p0)
# 1.6
# p0 = 1e6
# pb = [0.3e5, 0.01e5]
# T0 = 800
# sigma_e = 0.1
# rho0 = p0/(R*T0)
# c0 = sqrt(g*R*T0)
# qm1 = 0.04042*p0/sqrt(T0)*sigma_e
# print(qm1)
# for p in pb :
#     p = p/p0
#     qm2 = sigma_e * rho0 * p**(1/1.4) * sqrt(2/0.4 * c0**2 * (1 - p**(0.4/1.4)))
#     print(qm2)
    # if qm2 > qm1 :
    #     qm = qm1
    # else:
    #     qm = qm2
    # print(qm)