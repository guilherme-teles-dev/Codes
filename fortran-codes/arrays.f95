program arrays
        implicit none

        integer, dimension(10) :: array1

        integer :: array2(10)

        real, dimension(10, 10) :: array3

        real :: array4(0:9)
        real :: array5(-5:5)
        
        print *, size(array1)
        print *, size(array2)
        print *, size(array3)
        print *, size(array4)
        print *, size(array5)

end program arrays

