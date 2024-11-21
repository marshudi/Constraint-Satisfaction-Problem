# Names:
# Mohammed Amour Al-Marshudi ~ 16S194   
# Maram Abdullah Al-Nuaimi   ~ 16S1967


#################################
print("Please pick a valid number!")
print("1. Show 12 countries using CSP Backtracking")
print("2. Show Oman (11) States using CSP Backtracking")
print("3. Show Australia (7) States using CSP Backtracking")
num=int(input("Enter: "))

#####################################################################################################################################
if(num==1):
    print("Please pick a Number!")
    print("1. Show results using 4 colors")
    print("2. Show results using 2 colors")
    nums=int(input("Enter: "))    
    if(nums==1):
        print("#############################")
        #domain
        colors=['Red','Green','Blue','Yellow']  #minimum color for these state=4
        #variables
        states=['Oman','UAE','Yemen','KSA','Qatar','Bahrain','Kuwait','Iraq','Syria','Lebanon','Jordan','Palestine'] #12 countries 


        neighbors= {}
        # connection between the border
        #constraints 
        #adjacent regions must have different colors
                #adjacents      #regions 
        neighbors['Oman']=['UAE','KSA','Yemen'] 
        neighbors['UAE']=['Oman','KSA']         
        neighbors['Yemen']=['Oman','KSA']
        neighbors['KSA']=['Yemen','Oman','UAE','Qatar','Kuwait','Iraq','Jordan']
        neighbors['Qatar']=['KSA']
        neighbors['Bahrain']=[]
        neighbors['Kuwait']=['Iraq','KSA']
        neighbors['Iraq']=['Kuwait','KSA','Syria','Jordan']
        neighbors['Syria']=['Palestine','Lebanon','Jordan','Iraq']
        neighbors['Lebanon']=['Palestine','Syria']
        neighbors['Jordan']=['Palestine','KSA','Syria','Iraq']
        neighbors['Palestine']=['Jordan','Syria','Lebanon']


        colors_of_states={}   #Empty Dictionary to store the output and print it 


        def promising(state,color):
            for neighbor in neighbors.get(state):
                colors_of_neighbor= colors_of_states.get(neighbor)
                if colors_of_neighbor== color:
                    return False                # if the neigbhor color and the state color are the same it will return False 
            return True                         # if the neigbhor color and the state color are diffrent it will return True


        def get_color_for_state(state):
            for color in colors:
                if promising(state, color):     #if promising which color will be allowed to the state // it takes us to def promising for checking wether the neigbhor 
                    return color                                                                        # is having the same color of the state
                    

    # here we are assigning the color for the state(variable)
        def main():
            for state in states:
                colors_of_states[state]=get_color_for_state(state)
            print(colors_of_states)
        main()
        print("#############################")

################################################################
    
    elif(nums==2):
        print("#############################")
        #domain
        colors=['Red','Green']  #minimum color for these state=4
        #variables
        states=['Oman','UAE','Yemen','KSA','Qatar','Bahrain','Kuwait','Iraq','Syria','Lebanon','Jordan','Palestine'] #12 countries 


        neighbors= {}
        # connection between the border
        #constraints 
        #adjacent regions must have different colors
                #adjacents      #regions 
        neighbors['Oman']=['UAE','KSA','Yemen'] 
        neighbors['UAE']=['Oman','KSA']         
        neighbors['Yemen']=['Oman','KSA']
        neighbors['KSA']=['Yemen','Oman','UAE','Qatar','Kuwait','Iraq','Jordan']
        neighbors['Qatar']=['KSA']
        neighbors['Bahrain']=[]
        neighbors['Kuwait']=['Iraq','KSA']
        neighbors['Iraq']=['Kuwait','KSA','Syria','Jordan']
        neighbors['Syria']=['Palestine','Lebanon','Jordan','Iraq']
        neighbors['Lebanon']=['Palestine','Syria']
        neighbors['Jordan']=['Palestine','KSA','Syria','Iraq']
        neighbors['Palestine']=['Jordan','Syria','Lebanon']


        colors_of_states={}   #Empty Dictionary to store the output and print it 


        def promising(state,color):
            for neighbor in neighbors.get(state):
                colors_of_neighbor= colors_of_states.get(neighbor)
                if colors_of_neighbor== color:
                    return False                # if the neigbhor color and the state color are the same it will return False 
            return True                         # if the neigbhor color and the state color are diffrent it will return True


        def get_color_for_state(state):
            for color in colors:
                if promising(state, color):     #if promising which color will be allowed to the state // it takes us to def promising for checking wether the neigbhor 
                    return color                                                                        # is having the same color of the state
                    

    # here we are assigning the color for the state(variable)
        def main():
            for state in states:
                colors_of_states[state]=get_color_for_state(state)
            print(colors_of_states)
        main()
        print("#############################")
        print("Here You will see the [ None ] values becuase minimum color is = 4 ")
        print("Constraint is not Satified ")
        print("#############################")
    else:
        print("#############################")
        print("please Enter a Valid Number!")
        print("#############################")
##################################################################################################################################
elif(num==2):
    print("#############################")
    #domain
    colors=['Red','Green','Blue','Yellow']  #minimum color for these state=4
    #variables
    states=['Muscat','Ash Sharqiyah South','Ash Sharqiyah North','Ad Dakhiliyah','Al Batinah South','Al Batinah North','Ad Dhahirah','Al Buraimi','Musandam','Al Wusta','Dhofar'] #11 states 


    neighbors= {}
    # connection between the border
    neighbors['Muscat']=['Ash Sharqiyah South','Ash Sharqiyah North','Ad Dakhiliyah','Al Batinah South']
    neighbors['Ash Sharqiyah South']=['Muscat','Ash Sharqiyah North','Al Wusta']
    neighbors['Ash Sharqiyah North']=['Muscat','Ash Sharqiyah South','Al Wusta','Ad Dakhiliyah']
    neighbors['Ad Dakhiliyah']=['Muscat','Ash Sharqiyah North','Al Wusta','Ad Dhahirah','Al Batinah South']
    neighbors['Al Batinah South']=['Muscat','Ad Dakhiliyah','Al Wusta','Ad Dhahirah','Al Batinah North']
    neighbors['Al Batinah North']=['Al Buraimi','Ad Dhahirah','Al Batinah South']
    neighbors['Ad Dhahirah']=['Al Buraimi','Al Batinah North','Al Batinah South','Ad Dakhiliyah','Al Wusta']
    neighbors['Al Buraimi']=['Al Batinah North','Ad Dhahirah']
    neighbors['Musandam']=[]
    neighbors['Al Wusta']=['Ash Sharqiyah South','Ash Sharqiyah North','Ad Dhahirah','Ad Dakhiliyah','Dhofar']
    neighbors['Dhofar']=['Al Wusta']



    colors_of_states={}  

    def promising(state,color):
        for neighbor in neighbors.get(state):
            colors_of_neighbor= colors_of_states.get(neighbor)
            if colors_of_neighbor== color:
                return False
        return True
    def get_color_for_state(state):
        for color in colors:
            if promising(state, color):
                return color

    def main():
        for state in states:
            colors_of_states[state]=get_color_for_state(state)
        print(colors_of_states)
    main()
    print("#############################")
#####################################################################################################
elif(num==3):
    print("#############################")
    #domain
    colors=['Red','Green','Blue',]  #minimum color for these state=3
    #variables
    states=['Western Australia','Northern Territory','South Australia','Queensland','New South Wales','Victoria','Tasmania'] #7 states 


    neighbors= {}
    # connection between the border
    neighbors['Western Australia']=['Northern Territory','South Australia']
    neighbors['Northern Territory']=['Western Australia','South Australia','Queensland']
    neighbors['South Australia']=['Western Australia','Northern Territory','Queensland','New South Wales']
    neighbors['Queensland']=['Northern Territory','South Australia','New South Wales']
    neighbors['New South Wales']=['Queensland','South Australia','Victoria']
    neighbors['Victoria']=['New South Wales','South Australia']
    neighbors['Tasmania']=[]
    


    colors_of_states={}

    def promising(state,color):
        for neighbor in neighbors.get(state):
            colors_of_neighbor= colors_of_states.get(neighbor)
            if colors_of_neighbor== color:
                return False
        return True
    
    def get_color_for_state(state):
        for color in colors:
            if promising(state, color):
                return color

    def main():
        for state in states:
            colors_of_states[state]=get_color_for_state(state)
        print(colors_of_states)
    main()
    print("#############################")
#####################################################################################################


else:
    print("#############################")
    print("please Enter a Valid Number!")
    print("#############################")