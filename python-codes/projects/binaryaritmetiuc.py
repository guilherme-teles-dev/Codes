#Function for binary operations
def bitops(operation, fromright, bit1, bit2):
    #Output variables declarations
    bf = 0 #Final Bit
    gr = 0 #Go to right bit
    gl = 0 #Go from left bit
    #Input processing
    if operation == "+": #Sum conditional
        #Start a ocnditional 
        if (fromright+bit1+bit2)%2==1: #Check if the sum can be 3 or 1
            bf = 1
            if(fromright+bit1+bit2) == 3: #If 3 give 1 to other number
                gl = 1 #Send a bit to the next operation
        else: #The number only can be 2 or 0
            bf = 0
            if(fromright+bit1+bit2) == 2: #If be 2 give 1 to other number
                gl = 1 #Sendo a bit to the next operation
                
    else: #Subtraction conditional
        #Start a conditional block to check the relation between the binarys numbers
        if bit1+fromright != bit2: #If both numbers are the same, the output will ever be the same
            bf = 1
            if bit1+fromright < bit2:
                gr = -1
        else:
            bf = 0
    return (bf, gr, gl)

#Input the process material data
operation = input("[Sum/Sub]: ")
bin1 = input("Binary 1: ")
bin2 = input("Binary 2: ")
#Input corretion data
aux = ''
if(len(bin1) != len(bin2)):
    if len(bin1) > len(bin2):
        for c in range(len(bin1)-len(bin2)):
            aux = '0'+aux
        bin2 = aux+bin2
    else:
        for c in range(len(bin2)-len(bin1)):
            aux = '0'+aux
        bin1 = aux+bin1

#Declaration of auxiliar variables
lenbin = len(bin1)-1
momentoperation = (0, 0, 0)
#Set the output format
finalbin = ''
print("Final Bin = ", end="")
#Processing
if(operation == "Sum"): #Start a conditional block to check the type of operation
    while lenbin > -1: #Start a looping to run the binary inputed array
        momentoperation = bitops("+" , momentoperation[2], int(bin1[lenbin]), int(bin2[lenbin])) #Core process bitops(operationtype, fromrightnumber, operedbit, operingbit)
        finalbin = str(momentoperation[0])+finalbin #Output construction
        lenbin -= 1 #Reverse count
else:
    while lenbin > -1: #Start a looping to run the binary inputed array
        momentoperation = bitops("-",momentoperation[1], int(bin1[lenbin]), int(bin2[lenbin]))
        finalbin = str(momentoperation[0])+finalbin
        lenbin -= 1
print(finalbin) #Output