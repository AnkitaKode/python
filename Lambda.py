# def reciprocal( num ):  
#     return 1 / num  
   
# lambda_reciprocal = lambda num: 1 / num  
   
# # to defined by def keyword  
# print( "Def keyword: ", reciprocal(6) )  
   
# # to defined by lambda keyword  
# print( "Lambda keyword: ", lambda_reciprocal(6) )  


numbers_list = [2, 4, 5, 1, 3, 7, 8, 9, 10]      
squared_list = list(map( lambda num: num ** 2 , numbers_list ))      
print( 'Square of each number in the given list:' ,squared_list )   