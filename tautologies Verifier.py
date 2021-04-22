from itertools import product

# tautologies to solve
# (~B => ~A) => (A => B) (reverse of contraposition)
# ((A => B) => A) => A   (Peirce's law)
# (~A => A) =>  A        (consequentia mirabilis)
# (A => ~B) => (B => ~A) (contraposition with negated consequent)

V = 'âˆ€'
E = 'âˆƒ'


def tt(f, n):
    xss = product((0, 1), repeat=n)
    print('function:', f.__name__)
    for xs in xss: print(*xs, ':', int(f(*xs)))
    print('')


def f(p, q, r):
    return \
        p and q and not r or \
        not p and q and r or \
        p and not q and r


# tt(f,3)

def deMorgan1(a, b):
    x = not (a and b)
    y = not a or not b
    return x == y


def deMorgan2(a, b):
    x = not (a or b)
    y = not a and not b
    return x == y


# tt(deMorgan1,2)

# tt(deMorgan2,2)

# tt(lambda x,y: not (x and y),2)

def implication(c, t):
    # return c and t or not c
    return not c or t


def xor(x, y):
    return x != y


# tt(implication,2)

def ite(c, t, e):
    return c and t or not c and e



# (~B => ~A) => (A => B)
print("(~B => ~A) => (A => B)")


def Prob1(p, q):
    x = implication(not p, not q)
    y = implication(p, q)
    return implication(x, y)

tt(Prob1, 2)

# ((A => B) => A) => A
print("(A => B) => A) => A")


def Prob2(p, q):
    x = implication((p, q), p)
    y = p
    return implication(x, y)

tt(Prob2, 2)
# (~A => A) => A
print("(~A => A) => A")


def Prob3(p, q):
    x = implication(not p, q)
    y = p
    return implication(x, y)

tt(Prob3, 2)

# (A => ~B) = (B => ~A)
print("(A => ~B) = (B => ~A)")


def Prob4(p, q):
    x = implication(p, not q)
    y = implication(q, not p)
    return x == y

tt(Prob4, 2)
