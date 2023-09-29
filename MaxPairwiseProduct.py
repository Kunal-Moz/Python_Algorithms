import math

def max_pairwise1(A,n):
   result = 0
   for i in range(n):
       for j in range(i+1,n):
#           print(A[i],A[j],A[i]*A[j],result )
           if A[i]*A[j] > result:
               result = A[i]*A[j]
#               print(A[i],A[j],A[i]*A[j],result )
   return result
   
   
def max_pairwise2(A, n):
    max_index1 = -1
    for i in range(n):
        if max_index1 == -1 or A[i] > A[max_index1]:
            max_index1 = i
    
    max_index2 = -1
    for i in range(n):
        if (i != max_index1) and (max_index2 == -1 or A[i] > A[max_index2]):
            max_index2 = i
    
    return A[max_index1]*A[max_index2]
   
   


if __name__ == "__main__":
    # Get the value of N as an integer
    N = int(input("Enter the number of entries (N): "))

    # Get a single line of input containing N space-separated integers
    input_str = input(f"Enter {N} space-separated integers: ")

    # Split the input string into individual values and convert them to integers
    try:
        my_list = [int(x) for x in input_str.split()]
    
        # Check if the number of entries matches N
        if len(my_list) != N:
            print(f"Expected {N} entries, but received {len(my_list)}. Please enter exactly {N} integers.")
    except ValueError:
        print("Invalid input. Please enter space-separated integers.")
    
    
    product = max_pairwise2(my_list, N)
    print(product)
    
#    product2 = max_pairwise1(my_list, N)
#    print(product2)
