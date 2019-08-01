
# coding: utf-8

# In[ ]:


import collections


# In[11]:


##char_data

char_list_unsplitted="Edelgard Bernadetta Caspar Dorothea Ferdinand Hubert Linhardt Petra Dimitri Annette Ashe Dedue Felix Ingrid Mercedes Sylvain Claude Hilda Ignatz Leonie Lorenz Lysithea Marianne Raphael Rhea Alois Catherine Cyril Flayn Gilbert Hanneman Manuela Seteth Shamir Jeralt Jeritza Byleth"
char_list = char_list_unsplitted.split()


# In[52]:


##lost_item
#[name,items]

lost_items_batch=[['Edelgard', 'White Glove', 'Time worn Quill Pen', 'Eastern Porcelain'],
 ['Dimitri', 'Dulled Longsword', 'Black Leather Gloves', 'Training Logbook'],
 ['Claude', 'Leather Bow Sheath', 'Mild Stomach Poison', 'Board Game Piece'],
 ['Hubert', 'Hresvelg Treatise', 'Noxious Handkerchief', 'Folding Razor'],
 ['Ferdinand', 'Maintenance Oil', 'Agricultural Survey', 'Bag of Tea Leaves'],
 ['Linhardt', 'The Saints Revealed', 'Feather Pillow', 'Animated Bait'],
 ['Caspar', 'Thunderbrand Replica', 'Tattered Overcoat', 'Grounding Charm'],
 ['Bernadetta', 'Needle and Thread', 'Still-Life Picture', 'Hedgehog Case'],
 ['Dorothea', 'Silver Brooch', 'Songstress Poster', 'Lovely Comb'],
 ['Petra', 'Exotic Flower', 'Small Tanned Hide', 'Annotated Dictionary'],
 ['Dedue', 'Gold Earring', 'Gardening Sheers', 'Iron Cooking Pot'],
 ['Felix', 'Black Iron Spur', 'Sword Belt Fragment', 'Toothed Dagger'],
 ['Ashe', "Moon Knight's Tale", 'Evil-Repelling Amulet', 'Bundle of Herbs'],
 ['Sylvain',
  'Unused Lipstick',
  'Crumpled Love Letter',
  'The History of Sreng'],
 ['Mercedes',
  'Book of Ghost Stories',
  'Fruit Preserves',
  'How to Bake Sweets'],
 ['Annette', 'Unfinished Score', 'School of Sorcery Book', 'Wax Diptych'],
 ['Ingrid', 'Pegasus Horseshoes', 'Jousting Almanac', 'Curry Comb'],
 ['Lorenz',
  'Artificial Flower',
  'A Treatise on Etiquette',
  'Silk Handkerchief'],
 ['Raphael', 'Wooden Button', 'Burlap Sack of Rocks', 'Big Spoon'],
 ['Ignatz', 'Blue Stone', 'Art Book', 'Letter to the Goddess'],
 ['Lysithea',
  'Encyclopedia of Sweets',
  'Princess Doll',
  'New Bottle of Perfume'],
 ['Marianne', 'Bag of Seeds', 'How to be Tidy', 'Confessional Letter'],
 ['Hilda', 'Handmade Hair Clip', 'Spotless Bandage', 'Used Bottle of Perfume'],
 ['Leonie', 'Hand Drawn Map', 'Crude Arrowheads', 'Fur Scarf'],
 ['Seteth', 'Unfinished Fable', 'Old Fishing Rod', 'Snapped Writing Quill'],
 ['Flayn', 'Antique Clasp', 'Old Map of Enbarr', 'Dusty Book of Fables'],
 ['Hanneman', 'Lens Cloth', 'Hammer and Chisel', 'Sketch of a Sigil'],
 ['Manuela', 'Wellness Herbs', 'Clean Dusting Cloth', 'Light Purple Veil'],
 ['Gilbert', 'Noseless Puppet', 'Carving Hammer', 'Silver Necklace'],
 ['Alois',
  'Introduction to Magic',
  'Foreign Gold Coin',
  'Mysterious Notebook'],
 ['Catherine', 'Weathered Cloak', 'Letter to Rhea', 'Badge of Graduation'],
 ['Shamir', 'Bundle of Dry Hemp', 'Centipede Picture', 'Animal Bone Dice'],
 ['Cyril', 'Well-Used Hatchet', 'Portrait of Rhea', 'Old Cleaning Cloth'],
 ['Jeralt', 'Wooden Flask']]



# In[53]:


##gifts
#[name, gifts]
gifts_batch=[['Edelgard', 'Armored Bear Stuffy', 'Monarch Studies Book', 'Board Game'],
 ['Dimitri',
  'Training Weight',
  'Whetstone',
  'Riding Boots',
  'Ceremonial Sword'],
 ['Claude',
  'Riding Boots',
  'Book of Crest Designs',
  'Exotic Spices',
  'Board Game'],
 ['Hubert', 'Coffee Beans', 'Board Game', 'The History of Fodlan'],
 ['Ferdinand', 'Riding Boots', 'Whetstone', 'Tea Leaves'],
 ['Linhardt', 'Tasty Baked Treat', 'Book of Crest Designs', 'Fishing Float'],
 ['Caspar', 'Training Weight', 'Whetstone', 'Hunting Dagger', 'Smoked Meat'],
 ['Bernadetta',
  'Armored Bear Stuffy',
  'Book of Sheet Music',
  'Watering Can',
  'Landscape Painting',
  'Dapper Handkerchief'],
 ['Dorothea', 'Book of Sheet Music', 'Gemstone Beads', 'Stylish Hair Clip'],
 ['Petra', 'Hunting Dagger', 'Exotic Spices', 'Smoked Meat'],
 ['Dedue', 'Exotic Spices', 'Floral Adornment', 'Watering Can'],
 ['Felix',
  'Smoked Meat',
  'Hunting Dagger',
  'Training Weight',
  'Ceremonial Sword'],
 ['Ashe',
  'Legends of Chivalry',
  'Exotic Spices',
  'Tasty Baked Treat',
  'Ancient Coin'],
 ['Sylvain', 'Landscape Painting', 'Dapper Handkerchief', 'Board Game'],
 ['Mercedes',
  'Tasty Bake Treat',
  'Goddess Statuette',
  'Armored Bear Stuffy',
  'Gemstone Beads'],
 ['Annette',
  'Book of Sheet Music',
  'Stylish Hair Clip',
  'Arithmetic Textbook'],
 ['Ingrid', 'Riding Boots', 'Smoked Meat', 'Legends of Chivalry'],
 ['Lorenz', 'Floral Adornment', 'Tea Leaves', 'Book of Sheet Music'],
 ['Raphael',
  'Smoked Meat',
  'Training Weight',
  'Tasty Baked Treat',
  'Blue Cheese'],
 ['Ignatz',
  'Ancient Coin',
  'Landscape Painting',
  'Goddess Statuette',
  'Ceremonial Sword'],
 ['Lysithea',
  'Armored Bear Stuffy',
  'Arithmetic Textbook',
  'Tasty Baked',
  'Treat Book of Crest Designs'],
 ['Marianne',
  'Dapper Handkerchief',
  'Floral Adornment',
  'Armored Bear Stuffy'],
 ['Hilda',
  'Gemstone Beads',
  'Dapper Handkerchief',
  'Book of Sheet Music',
  'Stylish Hair Clip',
  'Armored Bear Stuffy'],
 ['Leonie', 'Hunting Dagger', 'Training Weight', 'Fishing Float'],
 ['Seteth', 'The History of Fodlan', 'Fishing Float', 'Dapper Handkerchief'],
 ['Flayn',
  'Tasty Baked Treat',
  'Armored Bear Stuffy',
  'Stylish Hair Clip',
  'Dapper Handkerchief'],
 ['Hanneman',
  'Arithmetic Textbook',
  'Tea Leaves',
  'Book of Crest Designs',
  'Dapper Handkerchief'],
 ['Manuela',
  'Book of Sheet Music',
  'Gemstone Beads',
  'Blue Cheese',
  'Goddess Statuette'],
 ['Gilbert', 'Goddess Statuette', 'Fishing Float', 'Ceremonial Sword'],
 ['Alois', 'Ancient Coin', 'Fishing Float', 'Floral Adornment'],
 ['Catherine',
  'Training Weight',
  'Whetstone',
  'Legends of Chivalry',
  'Blue Cheese'],
 ['Shamir',
  'Ancient Coin',
  'Exotic Spices',
  'Coffee Beans',
  'Hunting Dagger',
  'Book of Sheet Music'],
 ['Cyril', 'Smoked Meat', 'Hunting Dagger', 'Watering Can'],
 ['Rhea', 'Landscape Painting', 'Goddess Statuette', 'Ancient Coin']]


# In[54]:


##flowers
#[name, flowers]
flowers_batch=[['Edelgard', 'Carnation'],
 ['Bernadetta', 'Pitcher Plant'],
 ['Petra', 'Sunflower'],
 ['Ashe', 'Violet'],
 ['Mercedes', 'Lavender'],
 ['Lorenz', 'Rose'],
 ['Ignatz', 'Forget-me-nots'],
 ['Lysithea', 'Lily'],
 ['Marianne', 'Lily of the Valley'],
 ['Hilda', 'Anemone'],
 ['Flayn', 'Forget-me-nots'],
 ['Alois', 'Sunflower'],
 ['Cyril', "Baby's Breath"]]


# In[55]:


class support_database:
    def __init__(self):
        #[tea,tea_dialogue,gifts,lost_items,flowers]
        
        tea_dict = collections.defaultdict(set)
        tea_dial_dict = collections.defaultdict(set)
        gifts_dict = collections.defaultdict(set)
        lost_items_dict = collections.defaultdict(set)
        flowers_dict = collections.defaultdict(set)
        
        self.char_to_obj = [tea_dict, tea_dial_dict, gifts_dict ,lost_items_dict, flowers_dict]
        
        #for the reverse lookeup
        self.obj_to_char = collections.defaultdict(set)
        
        #for showing the list, pre-checking whether an item/char could be look-up, and for later adding more character if DLC
        
       
        #item_type_code
        #0-tea,1-tea_dialogue,2-gifts,3-lost_items,4-flowers
        self.item_list=[set(),set(),set(),set(),set()]    
        
        #char_list
        self.char_list=set()
        
    def person_likes_item(self,char,item_type,item):
        if char not in self.char_list:
            self.char_list.add( char )
            
        if item not in self.item_list[item_type]:
            self.item_list[item_type].add( item )
        
        #update the dict
        self.char_to_obj[item_type][char].add(item)
        self.obj_to_char[item].add(char)
        
        


# In[59]:


FETH=support_database()
batch_data=[gifts_batch,lost_items_batch,flowers_batch]
data_type_counter=2
for data in batch_data:
    for row in data:
        for item in row[1:]:
            FETH.person_likes_item(row[0],data_type_counter,item)
        
    data_type_counter += 1

# FETH.person_likes_item("Marianne",1, "Lavender Tea")
# FETH.person_likes_item("Annette",1, "Almond Tea")
# FETH.person_likes_item("Flayn",1, "Sweet Apple Tea")
# FETH.person_likes_item("Lysithea",1, "Sweet Apple Tea")
# FETH.person_likes_item("Lysithea",1, "Crescent Moon Tea")
# FETH.person_likes_item("Felix",1, "Four Spice Blend")
# FETH.person_likes_item("Edelgard",1, "Bergamot")
# FETH.person_likes_item("Claude",1, "Almyran Pine Needles")
# FETH.person_likes_item("Petra",1, "Ginger Tea")
# FETH.person_likes_item("Petra",1, "Crescent Moon Tea")



running = True

while running:
	print("_"*40)
	print("Type either character name or item name to show corresponding list")
	print("Note that all nouns in items are capitalized except propsitions (and, of ,to, etc.) e.g. 'New Bottle of Perfume' (without the ' of course, similar rules applied to the commands below) ")
	print("Type 'show_char_list' to see all possible characters")
	print("Type 'show_item_list_ITC' to see list of corresponding items")
	print("and ITC stands for item type code, which is an integer from 0 to 4, as 0-tea,1-tea_dialogue,2-gifts,3-lost_items,4-flowers ")
	print("type 'done' to finish ")

	user_input=input("FETH support items/char look up! :")

	if user_input in FETH.char_list:		

		item_type_code = int(input("And What kind of items are you looking up? \ndInput the corresponding integer 0-tea,1-tea_dialogue,2-gifts,3-lost_items,4-flowers :" ) )

		answer = FETH.char_to_obj[item_type_code][user_input]

		line ='-' * len(str(answer))

		print (line )

		print(answer)

		print (line) 
		

		reset = input("Wanna look up something else? Type done to finish. Type anything else to look up again:")

		if reset == "done":
			break
		else:
			print("Reset!")



	if user_input == "done":

		break





