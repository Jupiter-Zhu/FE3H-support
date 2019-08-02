import collections
from data import house_dict, tea_batch, tea_dialogue_batch, lost_items_batch, gifts_batch, flowers_batch, tea_final_batch
from sty import fg, bg, ef, rs, RgbFg





class support_database:
    def __init__(self):
        #[tea,tea_dialogue,gifts,lost_items,flowers]
        
        tea_dict = collections.defaultdict(set)
        tea_dial_dict = collections.defaultdict(set)
        gifts_dict = collections.defaultdict(set)
        lost_items_dict = collections.defaultdict(set)
        flowers_dict = collections.defaultdict(set)
        tea_final_dict = collections.defaultdict(set)
        
        self.char_to_obj = [tea_dict, tea_dial_dict, gifts_dict ,lost_items_dict, flowers_dict, tea_final_dict]
        
        #for the reverse lookeup
        self.obj_to_char = collections.defaultdict(set)
        
        #for showing the list, pre-checking whether an item/char could be look-up, and for later adding more character if DLC
        
       
        #item_type_code
        #0-tea,1-tea_dialogue,2-gifts,3-lost_items,4-flowers, 5- tea_final
        self.item_list=[ set(), set(), set(), set(), set(),set()]    
        
        #char_list
        self.char_list=set()
        
    def person_likes_item(self,char,item_type,item):

        if char != '' and item != '':

            if char not in self.char_list:

                self.char_list.add( char )
            
            if item not in self.item_list[item_type]:

                self.item_list[item_type].add( item )

        
        #update the dict
            self.char_to_obj[item_type][char].add(item)
            self.obj_to_char[item].add(char)
        
        


# In[59]:


FETH=support_database()

batch_data=[tea_batch, tea_dialogue_batch, gifts_batch, lost_items_batch, flowers_batch, tea_final_batch]

data_type_counter = 0

for data in batch_data:

    for row in data:

        for item in row[1:]:

            FETH.person_likes_item(row[0],data_type_counter,item)
        
    data_type_counter += 1


##color scheme

color_reset=fg.rs+bg.rs

BE_color = fg.white + bg.red

BL_color = bg.blue+fg.white

GD_color = bg.yellow+fg.black

Neutral_color = bg.da_white+fg.black

color_scheme=[BE_color, BL_color, GD_color, Neutral_color]
 
####################

help_message = ("_"*40 +
"\n Type either character name or item name to show corresponding list" +
"\n Note that all nouns in items are capitalized except propsitions (and, of ,to, etc.) e.g. 'New Bottle of Perfume' (without the ' of course, similar rules applied to the commands below) "+
"\n Type 'show_char_list' to see all possible characters"+
"\n Type 'show_item_list_#' to see list of corresponding items"+
"\n and # stands for item type code, which is an INTEGER from 0 to 4, as 0-tea,1-tea_dialogue,2-gifts,3-lost_items,4-flowers"+
"\n type 'done' to finish )\n"+
"_" *40 )

successul_message= fg.green + "Dingdingding! Data found" + fg.rs


def output_answer(answer):

    upper_line = '-'  *  min(len(str(answer)), 200 )

    lower_line ='_' *  min(len(str(answer)), 200 )
        
    print (upper_line)

    print(answer)

    print (lower_line) 




def lookup_items(name):

    print("And What kind of items are you looking up? \nInput the INTEGER corresponding types: \n"+
        bg.white+fg.black
        +"0 - tea, 1- tea_dialogue, 2 - gifts, 3 - lost_items, 4 - flowers, 5- tea_final :" +
        fg.rs+bg.rs)
    item_type = int( input())
    legal_range={0,1,2,3,4,5}

    if item_type not in legal_range:

        print( "Not a valid input type" )

    else:

        answer = FETH.char_to_obj[item_type][name]

        print(successul_message)

        print(color_scheme[ house_dict[ name ] ])

        output_answer(answer)

        print(color_reset)


def lookup_people(item):
	answer = FETH.obj_to_char[item]
	print(successul_message)
	print("-"*100)

	for name in answer:

		house_color =  color_scheme[ house_dict[ name ] ]

		print( house_color + name + color_reset, end=' ' )

	print("\n")
	print("_"*100)


def reset():

    reset_input = input("\nWanna look up something else? Check the database by\n typing 'help',\n typing 'done' to quit, or typing\n anything else to reset:")


    if reset_input == 'help':

        print(bg.white+fg.black+help_message+bg.rs+fg.rs)

        interface()

    elif reset_input == 'done':

    	print("bye__________________________")

    else:
    	
        print(fg.yellow + "Resetting"+"."*20 +fg.rs)

        interface()

    



  	    


def interface():

    print("_"*40 )

    print(fg.green+"Greetings! The support guide is ready"+fg.rs)

    print("_"*40 )

    user_input=input("Type item's or character' name to look up! Or type 'help' :")

    if user_input == "done":

        print("Bye")

    else:

        if user_input == 'show_char_list':

            print("-" *150)

            print(FETH.char_list)

            print("_" *150)

            reset()

        elif user_input[:-1] == 'show_item_list_':

            item_type_code = int(user_input[-1])

            if item_type_code not in [0,1,2,3,4]:

                print("item code out of bound")

            else:
                print("-" *150)

                print(FETH.item_list[item_type_code])

                print("_" *150)

                reset()

        elif user_input == 'help':
            
            print(bg.white+fg.black+help_message+bg.rs+fg.rs)

            reset()

        elif user_input in FETH.char_list:

            lookup_items(user_input)


            reset()  	    
    
       
        elif  any( user_input in items for items in FETH.item_list):

            lookup_people(user_input)
                
            reset()

        

        else:

            print("_"*60)

            print(fg.red + "Not a valid character or item name nor a correct command, maybe check your spelling? " + fg.rs)

            reset()

        

    





interface()

