# fabric = 1000 in^2
# fabric divided into rectangles
    # they overlap
#question: how many square inches of fabric overlap?

# xxxx in the example is defined as
# @3,3: 2x2

# which can be deduced by:
# id; Y,X: WxH
# 1 @ 1,3: 4x4
# 2 @ 3,1: 4x4
# 3 @ 5,5: 2x2

# overlap =
#   @ 3,3: 2x2


#Solution (sketch):
    # Given: Top left coordinates, and height and width of all squares
    """
        Format given input as a list of objects, with keys identifying each attribute (Y,X,W,H).

        Loop through the list, similar to Day 2, comparing the first member (hereinafter, 'specimen') to each following member (hereinafter, 'test case').  When there are

        For each comparison, check for an overlap:
        => if |Ya - Yb| < Hb && |Xa-Xb| < Wb
            (where Ya is the Y coordinate of the specimen, Yb is the Y coordinate of the test case, and so on with x coordinate, height, and width.)

        If there is an overlap, generate the coordinates for the bottom right corner of each rectangle:
            (Ya+Ha,Xa+Wa)
            (Yb+Hb,Xb+Wb)

        This gives us opposing coordinate pairs for the two rectangles in question:
            Ra: (Ya, Xa),(Ya+Ha,Xa+Wa)
            Rb: (Yb, Xb),(Yb+Hb,Xb+Wb)

        Now generate the same opposing coordinate pairs for the overlap region:
            Yo = max(Ya,Yb)
            Xo = max(Xa,Xb)
            Yo' = min((Ya+Ha),(Yb+Hb))
            Xo' = min((Xa+Wa),(Xb+Wb))

            # Ro: [(Yo,Xo),(Yo',Xo')]

        Now calculate the height and width of the overlap region:
            Ho = Yo'-Yo
            Wo = Xo'-Xo

        Now proceed below to generate the coordinates for all top left corners of 1X1 squares within the overlapping area, and add these to a global list.

    """

    c_init = [Yo,Xo] #this is the top left corner of the overlapping area
    w = Wo #this is the width of the overlapping area
    h = Ho #this is the height of the overlapping area
    c_final = []

    # A) this generates the coordinates for all top left corners of 1X1 squares within the overlapping area:
    for x in range(w): # increment the x
        for y in range(h): #increment the y for each x
            c_next = [(Yo + y),(Xo + x)]
            c_final.append(c_next)

    print(c_final)

    # B) generate the coordinates using the logic in (A) for each overlapping area.  Once the coordinates are generated, remove the current specimen from the beginning of the array.

    # C) After the program has iterated through the entire input and generated coordinates for all overlapping areas divided into 1X1 squares, eliminate duplicate coordinates.

    # D) count the members of the list -- this is the total overlapping area among all squares.

# Brainstorming work:

    if |Ya - Yb| < Hb && |Xa-Xb| < Wb
    # then it's an overlap condition

    dimensions of rectangle a:
        (Ya, Xa),(Ya, Xa+Wa),(Ya+Ha,Xa+Wa),(Ya+Ha,Xa)
        (2,3),(2,6),(8,6),(8,3)
    dimensions of rectangle b:
        (Yb, Xb),(Yb, Xb+Wb),(Yb+Hb,Xb+Wb),(Yb+Hb,Xb)
        (3,5),(3,8),(9,8),(9,5)
    dimensions of overlap:
        (3,5),(3,6),(8,6),(8,5)
        (max,max),(max,min),(min,min),(min,max)
    dimensions of rectangle a:
        (2,3),(2,6),(8,6),(8,3)
    dimensions of rectangle b:
        (6,4),(6,6),(11,6),(11,4)
    dimensions of overlap:
        (6,4),(6,6),(8,6),(8,4)
        (max,max),(max,min),(min,min),(min,max)

    dimensions of rectangle a:
        (6,4),(6,6),(11,6),(11,4)
    dimensions of rectangle b:
        (3,5),(3,8),(9,8),(9,5)
    dimensions of overlap:
        (6,5),(6,6),(9,6),(9,5)
        (max,max),(max,min),(min,min),(min,max)



# figure out how to generate the 1 in^2 squares programmatically - eliminate all but the top left corners - then eliminate duplicates and count the remaining members for the total area.
    Overlap 1
        (3,5),(3,6),(8,6),(8,5) ==> equivalent to:

        (3,5),(3,6),(4,6),(4,5)
        (4,5),(4,6),(5,6),(5,5)
        (5,5),(5,6),(6,6),(6,5)
        (6,5),(6,6),(7,6),(7,5)
        (7,5),(7,6),(8,6),(8,5)

        area defined by (3,5)=>(8,6)
            8-3=5
            6-5=1
        3,5
        4,5
        5,5
        6,5
        7,5

    Overlap 2
        (6,4),(6,6),(8,6),(8,4) ==> equivalent to:


        Area defined by (6,4)=>(8,6) =
        8-6=2
        6-4=2
            =>2X2

        6,4  6,5
        7,4  7,5

        create coordinates by...
        looping over the width
        looping over the height

        (6,4),(6,5),(7,5),(7,4)
        (6,5),(6,6),(7,6),(7,5)
        (7,5),(7,6),(8,6),(8,5)
        (7,4),(7,5),(8,5),(8,4)

    Overlap 3

        (6,4),(6,6),(8,6),(8,4)
        (6,5),(6,6),(9,6),(9,5)

        6,5 6,6 8,6 8,5

    # top left coordinates of overlap area:
        (|Ya-Yb| + min(Ya,Yb)),(|Xa-Xb| + min(Xa,Xb))
        (|Ya-Yb| + max(Ya,Yb)),(|Xa-Xb| + max(Xa,Xb))
        3,5
    # bottom right coordinates of overlap area:
        # (|Ya-Yb| + max(Ya,Yb)),(|Xa-Xb| + max(Xa,Xb))


        min(Y1, Y2) + max(H1, H2), min(Y1, Y2) + H1
        2 + 6 = 8


        need to get the extent of the overlap.
        Calculate the height and width of the overlap:

        Height_overlap: max(Ha,Hb) - |ΔY|
                            5-4 = 1
                            6-4=2
                            6-1=5
                            4-
        Width_overlap: max(Wa,Wb) - |ΔX|
                            3-2= 1
                            3-1=2
                            3-2=1
                            4-2=2

                        min(W) - |ΔX|
