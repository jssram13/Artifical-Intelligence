class multifun:
    def OddEven():
        even = int(input("Enter a number: "))
        if even % 2 == 0:
            print(even, "is Even number")
        else:
            print(even, "is Odd number")

    def Subfields():
        fld1 = [
            "Machine Learning",
            "Neural Networks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing"
        ]
        print("Sub-fields in AI are:")
        for fld in (fld1):
            print (fld)

    def Elegible():
        gender=input ("Your Gender:")
        age =int(input("Your Age:"))
        if gender == "male":
            if age >= 21 :
                print ("ELIGIBLE")
            else :
                print ("Not ELIGIBLE")
        elif gender == "female":
            if age >= 18 :
                print ("ELIGIBLE")
            else :
                print ("Not ELIGIBLE")


    def percentage():
        sub1=int(input("subject1:"))
        sub2=int(input("subject2:"))
        sub3=int(input("subject3:"))
        sub4=int(input("subject4:"))
        sub5=int(input("subject5:"))
        Total = sub1+sub2+sub3+sub4+sub5
        print ("Total : ", Total)
        percent = (Total / 500) * 100
        print("Percentage :" ,percent)


    def triangle():
        # Calculate area
        height=float(input("Height:"))
        breadth=float(input("Breadth:"))
        area=(height*breadth)/2
        print("Area of Triangle:",area)
        
        # Calculate perimeter
        height=float(input("Height1:"))
        height2=float(input("Height2:"))
        breadth=float(input("Breadth:"))
        Perimeter = height+height2+breadth
        print("Perimeter of Triangle:",Perimeter)