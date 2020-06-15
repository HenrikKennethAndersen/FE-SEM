# --------------------------------------------- #
# Sympy code to double-check the model matrices 
# 
# Henrik Kenneth Andersen 
# 
# 15.06.2020 
# --------------------------------------------- #

# The following code just double-checks the matrix notation used in the article. 


from sympy import *


# FE-SEM ------------------------------------------------------------------

# ----- Symbols 

x1, x2, x3, y1, y2, y3, d1, d2, d3, e1, e2, e3, xi1, xi2, xi3, n1, n2, n3, a, z1, z2, z3, b = symbols('x1, x2, x3, y1, y2, y3, delta1, delta2, delta3, varepsilon1, varepsilon2, varepsilon3, xi1, xi2, xi3, eta1, eta2, eta3, alpha, zeta1, zeta2, zeta3, beta')


# ----- Matrices 

# y
y = Matrix([[y1],
            [y2],
            [y3],
            [x1],
            [x2],
            [x3]])

# Lambda_y            
Ly = Matrix([[1, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 1, 0]])

# eta
n = Matrix([[y1],
            [y2],
            [y3],
            [x1],
            [x2],
            [x3],
            [a]])

# Beta            
B = Matrix([[0, 0, 0, b, 0, 0, 1],
            [0, 0, 0, 0, b, 0, 1],
            [0, 0, 0, 0, 0, b, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]])

# zeta            
z = Matrix([[e1],
            [e2],
            [e3],
            [x1],
            [x2],
            [x3],
            [a]])
      
# Identity matrix       
I = eye(7)


# ----- Equations for y

# Normal output
print(Ly*Inverse(I - B)*z)

# Pretty latex output
# print('$' + latex(Ly*Inverse(I - B)*z) + '$')


# ----- Equations for yy'

# Normal output
print((Ly*Inverse(I - B)*z)*(Ly*Inverse(I - B)*z).T)

# Pretty latex output
# print('$' + latex((Ly*Inverse(I - B)*z)*(Ly*Inverse(I - B)*z).T) + '$')


# FE-SEM with latent variables --------------------------------------------

# ----- Symbols

x1, x2, x3, y1, y2, y3, d1, d2, d3, e1, e2, e3, xi1, xi2, xi3, n1, n2, n3, a, z1, z2, z3, b, x11, x21, x31, x12, x22, x32, x13, x23, x33, xi1, xi2, xi3, d11, d21, d31, d12, d22, d32, d13, d23, d33, l21, l31, l22, l32, l23, l33 = symbols('x1, x2, x3, y1, y2, y3, delta1, delta2, delta3, varepsilon1, varepsilon2, varepsilon3, xi1, xi2, xi3, eta1, eta2, eta3, alpha, zeta1, zeta2, zeta3, beta, x11, x21, x31, x12, x22, x32, x13, x23, x33, xi1, xi2, xi3, delta11, delta21, delta31, delta12, delta22, delta32, delta13, delta23, delta33, lambda21, lambda31, lambda22, lambda32, lambda23, lambda33')


# ----- Matrices 

# y
y = Matrix([[y1],
            [y2],
            [y3],
            [x11],
            [x21],
            [x31],
            [x12],
            [x22],
            [x32],
            [x13],
            [x23],
            [x33]])

# Lambda_y
Ly = Matrix([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]])

# eta
n = Matrix([[y1],
            [y2],
            [y3],
            [x11],
            [x21],
            [x31],
            [x12],
            [x22],
            [x32],
            [x13],
            [x23],
            [x33],
            [a],
            [xi1],
            [xi2],
            [xi3]])
     
# Beta       
B = Matrix([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, b, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, b, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, b],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, l21, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, l31, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, l22, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, l32, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, l23],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, l33],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# zeta
z = Matrix([[e1],
            [e2],
            [e3],
            [d11],
            [d21],
            [d31],
            [d12],
            [d22],
            [d32],
            [d13],
            [d23],
            [d33],
            [a],
            [xi1],
            [xi2],
            [xi3]])

# Identity matrix 
I = eye(16)


# ----- Equations for y

# Normal output 
print(Ly*Inverse(I - B)*z)

# Pretty latex output 
# print('$' + latex(Ly*Inverse(I - B)*z) + '$')



# The full model-implied covariance matrix is much too large to be of any use. 
# Instead, if one is interested, they can save the matrix as an object and 
# access individual elements. E.g.,

yy = (Ly*Inverse(I - B)*z)*(Ly*Inverse(I - B)*z).T

# for Var(y_1), use: 

expand(yy[0, 0])

# or for Cov(y_1, y_3), use:

expand(yy[0, 2])


# ----- Equations for yy'

# Normal output 
# print((Ly*Inverse(I - B)*z)*(Ly*Inverse(I - B)*z).T)

# Pretty latex output
# print('$' + latex((Ly*Inverse(I - B)*z)*(Ly*Inverse(I - B)*z).T) + '$')
