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
		self.item_lists=[ set(), set(), set(), set(), set(),set()]    
		
		#char_list
		self.char_list=set()
		
	def person_likes_item(self,char,item_type,item):

		if char != '' and item != '':

			if char not in self.char_list:

				self.char_list.add( char )
			
			if item not in self.item_lists[item_type]:

				self.item_lists[item_type].add( item )

		
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


##########color scheme

color_reset=fg.rs+bg.rs

BE_color = fg.white + bg.red

BL_color = bg.blue+fg.white

GD_color = bg.yellow+fg.black

Neutral_color = bg.da_white+fg.black

color_scheme=[BE_color, BL_color, GD_color, Neutral_color]
 
####################


#messages
#########################

message_help = (fg.black+ bg.white + "_"*40 +
"\n Type either character name or item name to show corresponding list" +
"\n Note that all nouns in gifts/lost items are capitalized except propsitions (and, of ,to, etc.) e.g. 'New Bottle of Perfume' (without the ' of course, similar rules applied to the commands below) "+
"\n Also notice that the tea party (4 and 5) data is currently not 100% verified"+
"\n Type 'show_char_list' to see all possible characters"+
"\n Type 'show_item_list_#' to see list of corresponding items"+
"\n and # stands for item type code, which is an INTEGER from 0 to 5, as 0-tea,1-tea_dialogue,2-gifts,3-lost_items,4-flowers. 5-tea_final"+
"\n type 'done' to finish )\n"+
"_" *40 +fg.rs +bg.rs )

message_successul= fg.green + "Dingdingding! Data found" + fg.rs

message_lookup_item_loop=("You can now input another INTEGER\n"+
		bg.white+fg.black
		+"0 - tea, 1- tea_dialogue, 2 - gifts, 3 - lost_items, 4 - flowers, 5- tea_final :" +
		fg.rs+bg.rs + "to look up another type of items under the same person,\n or type names or item's name to do a new search")


message_lookup_item_greeting= ("And What kind of items are you looking up? \nInput the INTEGER corresponding types: \n"+
		bg.white+fg.black
		+"0 - tea, 1- tea_dialogue, 2 - gifts, 3 - lost_items, 4 - flowers, 5- tea_final :" +
		fg.rs+bg.rs)


message_not_found = (fg.red + "Not a valid character or item name nor a correct command, maybe check your spelling? Going back to main menu " + fg.rs)

message_return = "Going back to the main menu."

message_out_of_bound = "Parameter has to be an integer ranges from 0 to 5. Going back to main menu."

###########################################################



keywords ={"done", "help", "show_char_list", "show_item_list_0","show_item_list_1","show_item_list_2","show_item_list_3","show_item_list_4","show_item_list_5"}




#########################################################################

def print_names_colored(set_of_names):

	for name in set_of_names:

		house_color =  color_scheme[ house_dict[ name ] ]

		print( house_color + name + color_reset, end=' ')

	print(color_reset)

def output_answer(answer, answer_type,current_color=None):

	##outputing a list of items

	upper_line = '-'  *  min(len(str(answer)), 200 )

	lower_line ='_' *  min(len(str(answer)), 200 )

	if answer_type == 0:

		print(message_successul)

		print(upper_line)

		print(current_color)

		print(answer)

		print(color_reset)

		print(lower_line)

	else:

		print(message_successul)

		print(upper_line)

		print_names_colored(answer)

		print("\n"+lower_line)

	
		
	# print (upper_line)

	# print(answer)

	# print (lower_line) 




def lookup_items(name, item_type):

	legal_range={0,1,2,3,4,5}
	

	if item_type not in legal_range:

		print( message_out_of_bound )

		interface()

	else:

		answer = FETH.char_to_obj[item_type][name]

		current_color = color_scheme [ house_dict[name] ]

		output_answer(answer,0, current_color)

def lookup_people(item):

	answer = FETH.obj_to_char[item]

	output_answer(answer,1)


def output_keywords(keywords):

	if keywords == "done":

		print("Bye")

	elif keywords == "show_char_list":

		print(FETH.char_list)

		print_names_colored(FETH.char_list)

		interface()

	elif keywords[:-1] == 'show_item_list_':

			item_type_code = int(user_input[-1])

			if item_type_code not in [0,1,2,3,4,5]:

				print(message_out_of_bound)

				interface()

			else:
				print("-" *150)

				print(FETH.item_lists[item_type_code])

				print("_" *150)

				interface()


	elif keywords == "help":

		print(message_help)

		interface()


# def reset():

# 	reset_input = input("\nWanna look up something else? Check the database by\n typing 'help',\n typing 'done' to quit, or typing\n anything else to reset:")


# 	if reset_input == 'help':

# 		print(bg.white+fg.black+help_message+bg.rs+fg.rs)

# 		interface()

# 	elif reset_input == 'done':

# 		print("bye__________________________")

# 	else:
		
# 		print(fg.yellow + "Resetting"+"."*20 +fg.rs)

# 		interface()

	


def search(obj_name,obj_type):

	

	#given character name	

	if obj_type == 0:

		char_name=obj_name

		print(message_lookup_item_greeting)

		item_type = int( input())

		lookup_items(char_name,item_type)

		print(message_lookup_item_loop)
		

		while True:

			user_input = input()

			if len(user_input) == 1 and user_input.isnumeric():

				item_type = int(user_input)

				if item_type not in {0,1,2,3,4,5}:

					print(message_out_of_bound)

					interface()

				else:

					lookup_items(char_name,item_type)

					print(message_lookup_item_loop)

			else:
				break


		if user_input in keywords:

			output_keywords( user_input )

		elif user_input in FETH.char_list:

			search(user_input,0)

		elif any ( user_input in item_list for item_list in FETH.item_lists) :

			search(user_input,1)

		else:
			print(message_not_found)

			interface()


	# given item names

	else:

		lookup_people(obj_name)

		print(message_return)

		interface()







		
		


def interface():

	print("_"*40 )

	print(fg.green+"The support guide is ready"+fg.rs)

	print("_"*40 )

	user_input=input("Type item's or character' name to look up! Or type 'help' :")

	if user_input in keywords:

		output_keywords(user_input)

	elif user_input in FETH.char_list:

		search(user_input,0)

	elif any( user_input in item_list for item_list in FETH.item_lists):

		search(user_input,1)

	else:
		print(message_not_found)

		interface()
		

	



interface()