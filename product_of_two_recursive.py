def product_of_two_recursive(x,y):
    if y == 0:
        return 0
    if x < y:
        return product_of_two_recursive(y,x) #stops reaching recursive depth with large numbers
    return x + product_of_two_recursive(x, y-1)

print(product_of_two_recursive(9,3))