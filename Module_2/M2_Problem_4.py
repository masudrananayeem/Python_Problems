A={1,2,3,4,5}
B={4,5,6,7,8}

union = A.union(B)
print("Union of A and B is :", union)

intersection= A.intersection(B)
print("Intersection of A and B is :", intersection)

a_to_b = A.difference(B)
print("Difference of A - B is :", a_to_b)

b_to_a = B.difference(A)
print("Difference of B - A is :", b_to_a)