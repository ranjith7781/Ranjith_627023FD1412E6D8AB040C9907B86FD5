def LinearSearchProduct(products, targetproduct):  
    indices = [] 
    for i,product in enumerate(products):
        if product == targetproduct:
            indices.append(i)  
    return indices
product = ["shoes","bags","shop","shoes","watch","shoes" ]
target = "shoes"
target2 = 'apple'
result = LinearSearchProduct(product,target)
print (result)
L1 = ['cars','labtop']