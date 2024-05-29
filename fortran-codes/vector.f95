program coordinate_example
    implicit none
    
    ! Declare variables
    integer :: i
    real :: coordinates(3)! Arrays for x, y, and z coordinates
    
    
    do i = 1, 3
        read(,*,)
    end do
    ! Initialize coordinates
    x = [1.0, 2.0, 3.0]
    y = [4.0, 5.0, 6.0]
    z = [7.0, 8.0, 9.0]
    
    ! Print coordinates
    print *, "Coordinates:"
    do i = 1, 3
        print *, "Point ", i, ": (", x(i), ", ", y(i), ", ", z(i), ")"
    end do
    
    ! Calculate distances between points
    print *, "Distances between points:"
    print *, "Distance between Point 1 and 2:", distance(x(1), y(1), z(1), x(2), y(2), z(2))
    print *, "Distance between Point 2 and 3:", distance(x(2), y(2), z(2), x(3), y(3), z(3))
    print *, "Distance between Point 3 and 1:", distance(x(3), y(3), z(3), x(1), y(1), z(1))
    
contains ! What's this?

    ! Function to calculate distance between two points
    real function distance(x1, y1, z1, x2, y2, z2)
        real, intent(in) :: x1, y1, z1, x2, y2, z2 !What's intent?
        distance = sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    end function distance

end program coordinate_example
