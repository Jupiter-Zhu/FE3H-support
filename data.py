import collections

##char_data

BE_char_list_unsplitted="Edelgard Bernadetta Caspar Dorothea Ferdinand Hubert Linhardt Petra" 
BL_char_list_unsplitted="Dimitri Annette Ashe Dedue Felix Ingrid Mercedes Sylvain "
GD_char_list_unsplitted="Claude Hilda Ignatz Leonie Lorenz Lysithea Marianne Raphael "
NEUTRAL_char_list_unsplitted="Rhea Alois Catherine Cyril Flayn Gilbert Hanneman Manuela Seteth Shamir Jeralt Jeritza"

char_list = [BE_char_list_unsplitted, BL_char_list_unsplitted, GD_char_list_unsplitted,NEUTRAL_char_list_unsplitted]

#house number: 0 - black eagle, 1 - blue lion, 2 - golden deer, 3 - neutral
house_dict = collections.defaultdict(int)

house_number = 0

for unsplit_list in char_list:

  temp_split = unsplit_list.split()

  for name in temp_split:

    house_dict[name] = house_number

  house_number += 1
 





tea_batch=[['Edelgard', 'Bergamot'],
 ['Ferdinand', 'Southern Fruit Blend'],
 ['Linhardt', 'Almyran Pine Needles', ' Angelica Tea'],
 ['Caspar', 'Ginger Tea'],
 ['Bernadetta', 'Albinean Berry Blend', ' Honeyed Fruit Blend'],
 ['Dorothea', 'Sweet Apple Blend'],
 ['Petra', 'Ginger Tea', ' Four Spice Blend', ' Crescent Moon Tea'],
 ['Dimitri', 'Chamomile Tea'],
 ['Dedue', 'Ginger Tea'],
 ['Felix', 'Almyran Pine Needles', ' Four Spice Blend'],
 ['Sylvain', 'Bergamot'],
 ['Ingrid', 'Mint Leaves', ' Chamomile Tea'],
 ['Mercedes', 'Crescent Moon Tea', ' Albinean Berry Blend'],
 ['Annette', 'Almond Blend', ' Sweet Apple Blend'],
 ['Ashe', 'Angelica Tea', ' Mint Leaves'],
 ['Claude', 'Almyran Pine Needles', ' Chamomile'],
 ['Hilda', 'Mint leaves', ' Albinean Berry Blend', ' Rose Petal'],
 ['Leonie', 'Angelica Tea'],
 ['Raphael', 'Ginger Tea', ' Hazelnut Tea', ' Almond Blend'],
 ['Lorenz', 'Rose Petal'],
 ['Ignatz', 'Lavender Tea'],
 ['Marianne', 'Lavender Tea'],
 ['Lysithea', 'Sweet-Apple Blend', ' Honeyed Fruit Blend', ' Crescent Moon'],
 ['Seteth', 'Angelica Tea', '  Four Spice Blend'],
 ['Flayn', 'Sweet Apple Blend', ' Crescent Moon', ' Almond Blend'],
 ['Manuela', 'Lavender Tea', ' Mint Leaves'],
 ['Hanneman', 'Bergamont'],
 ['Catherine', 'Four Spice Blend'],
 ['Shamir', 'Chamomile', ' Crescent Moon Tea']]
























##tea_dialogue

tea_dialogue_batch=[['Edelgard',
  'A new gambit',
  'A strong battalion',
  "Books you've read recently",
  'Capable comrades',
  'Cats',
  'Children at the market',
  'Classes you might enjoy',
  'Dreaming of lazy days',
  'Evaluating allies',
  'Favourite sweets',
  "Fódlan's future",
  'Gifts you would like to receive',
  "I'm counting on you",
  'Monastery rules',
  'Monastery security',
  'Our first meeting',
  'Overcoming weaknesses',
  'School uniforms',
  'The existence of crests',
  'The last battle',
  "The library's collection",
  'The view from the bridge',
  "You're doing great work"],
 ['Hubert',
  'A new gambit',
  'A strong battalion',
  'Capable comrades',
  'Close calls',
  'Equipment upkeep',
  'Evaluating allies',
  'I heard some gossip',
  'Mighty weapons',
  'Monastery mysteries',
  'Monastery rules',
  'Monastery security',
  'Someone you look up to',
  'Successful plots',
  "The library's collection",
  'Working together',
  'Your ambitions'],
 ['Ferdinand',
  'Capable comrades',
  'Equipment upkeep',
  'Evaluating allies',
  'Fashion',
  "Fódlan's future",
  'Food in the dining hall',
  'Gifts you would like to receive',
  'Heart-racing memories',
  'Hopes for your future',
  "I'm counting on you",
  'Likeable allies',
  'Mighty weapons',
  'Relaxing at the sauna',
  'School days',
  'Tell me about yourself',
  'The meaning of nobility',
  'The opera',
  'Working together',
  'Your ambitions'],
 ['Linhardt',
  'A dinner invitation',
  'A place you’d like to visit',
  'A word of advice',
  "Books you've read recently",
  'Cats',
  'Exploring the monastery',
  'Favourite sweets',
  'Gardening mishaps',
  'Gifts you would like to receive',
  'Monastery mysteries',
  'Our first meeting',
  'Past laughs',
  'Thanks for everything',
  'The art of napping',
  'The existence of crests',
  "The library's collection",
  'The view from the bridge',
  'Things that bother you'],
 ['Caspar',
  'A new gambit',
  'A place you’d like to visit',
  'A strong battalion',
  'Children at the market',
  'Close calls',
  'Equipment upkeep',
  'Hopes for your future',
  "I'm counting on you",
  'Methods for growing taller',
  'Mighty weapons',
  'Our first meeting',
  'Overcoming weaknesses',
  'Past laughs',
  'Plans for the future',
  'Potential training partners',
  'Relaxing at the sauna',
  'School days',
  'Shareable snacks',
  'Strange fish in the pond',
  'Thanks for everything',
  'The view from the bridge',
  'Things that bother you',
  'Working hours for guards',
  'Working together'],
 ['Bernadetta',
  'A place you’d like to visit',
  'Cats',
  'Children at the market',
  'Close calls',
  'Cooking mishaps',
  'Exploring the monastery',
  'Favourite sweets',
  'Food in the dining hall',
  'Gifts you would like to receive',
  "I'm counting on you",
  'Perfect recipes',
  'School uniforms',
  'Shareable Snacks',
  'Thanks for everything',
  'The courtyard couple',
  'The ideal relationship',
  'The last battle',
  "The library's collection",
  'The view from the bridge',
  'Things that bother you',
  'You seem different',
  'You seem well',
  "You're doing great work"],
 ['Dorothea',
  'A dinner invitation',
  "Books you've read recently",
  'Cute monks',
  'Dining partners',
  'Dreamy knights',
  'Fashion',
  'First crushes',
  'Gifts you would like to receive',
  'Heart-racing memories',
  'Hopes for your future',
  'I heard some gossip',
  'Likeable allies',
  'Monastery security',
  'Our first meeting',
  'Past laughs',
  'Potential training partners',
  'Relaxing at the sauna',
  'School days',
  'School uniforms',
  'Someone you look up to',
  'Tell me about yourself',
  'Thanks for everything',
  'The courtyard couple',
  'The ideal relationship',
  'The Melody of Words',
  'The opera',
  'Things you find romantic',
  'Working hours for guards',
  'Working together',
  'You seem different'],
 ['Petra',
  'A dinner invitation',
  'A new gambit',
  'A place you’d like to visit',
  'A word of advice',
  "Books you've read recently",
  'Capable comrades',
  'Cats',
  'Equipment upkeep',
  'Evaluating allies',
  'Exploring the monastery',
  "Fódlan's future",
  'Gifts you would like to receive',
  "Guessing someone's age",
  'Heart-racing memories',
  'Hopes for your future',
  "I'm counting on you",
  'Likeable allies',
  'Monastery rules',
  'Monastery security',
  'Overcoming weaknesses',
  'Plans for the future',
  'Potential training partners',
  'Relaxing at the sauna',
  'Someone you look up to',
  'Strange fish in the pond',
  'Swimming in the ocean',
  'The ideal relationship',
  "The library's collection",
  'The view from the bridge',
  'Working hours for guards',
  'Working together',
  'You seem different',
  'Tell me about yourself',
  'Thanks for everything',
  'Fashion'],
 ['Dimitri',
  'A strong battalion',
  'A word of advice',
  "Books you've read recently",
  'Equipment upkeep',
  'Evaluating allies',
  'Exploring the monastery',
  "Fódlan's future",
  "I'm counting on you",
  'Monastery rules',
  'Monastery security',
  'Potential training partners',
  'Reliable allies',
  'Someone you look up to',
  'Tell me about yourself',
  'Thanks for everything',
  'The last battle',
  'The view from the bridge',
  'Working hours for guards',
  'Your ambitions'],
 ['Dedue',
  'A dinner invitation',
  'A strong battalion',
  'Capable comrades',
  'Cooking mishaps',
  'Dimitri',
  'Equipment upkeep',
  'Exploring the monastery',
  'Favourite sweets',
  "Fódlan's future",
  'Food in the dining hall',
  'Gifts you would like to receive',
  "I'm counting on you",
  'Monastery security',
  'Overcoming weaknesses',
  'Potential training partners',
  'Reliable allies',
  'Shareable snacks',
  'Someone you look up to',
  'Thanks for everything',
  'The last battle',
  'Working hours for guards',
  'Working together',
  'Your ambitions'],
 ['Felix',
  'A new gambit',
  'A new sword technique',
  'A strong battalion',
  'Cats',
  'Children at the market',
  'Evaluating allies',
  "I'm counting on you",
  'Overcoming weaknesses',
  'Plans for the future',
  'Potential training partners',
  'Reliable Allies',
  'Shareable snacks',
  'Someone you look up to',
  'Your ambitions'],
 ['Sylvain',
  'A dinner invitation',
  'Close calls',
  'Cooking mishaps',
  'Dating escapades',
  "Guessing someone's age",
  'Hopes for your future',
  'Relaxing at the sauna',
  'The view from the bridge',
  'Things you find romantic',
  'You seem different',
  "You're doing great work",
  'Overcoming weaknesses',
  'Dining partners'],
 ['Ingrid',
  'A dinner invitation',
  'A new gambit',
  'A strong battalion',
  'A word of advice',
  "Books you've read recently",
  'Classes you might enjoy',
  'Cooking mishaps',
  'Dreamy knights',
  'Equipment upkeep',
  'Evaluating allies',
  'Exploring the monastery',
  'Favourite sweets',
  "Fódlan's future",
  'Food for life',
  'Food in the dining hall',
  "I'm counting on you",
  'Mighty weapons',
  'Monastery rules',
  'Monastery security',
  'Our first meeting',
  'Overcoming weaknesses',
  'Past laughs',
  'Perfect recipes',
  'Plans for the future',
  'Potential training partners',
  'Reliable Allies',
  'School days',
  'Shareable snacks',
  'Someone you look up to',
  'Strange fish in the pond',
  'Thanks for everything',
  'The existence of crests',
  'The ideal professor',
  'The last battle',
  "The library's collection",
  'The view from the bridge',
  'Working hours for guards',
  'You seem well',
  "You're doing great work",
  'Your ambitions'],
 ['Mercedes',
  'A dinner invitation',
  "Books you've read recently",
  'Cats',
  "Books you've read recently",
  'Cooking mishaps',
  'Cute monks',
  'Dining partners',
  'Dreamy knights',
  'Exploring the monastery',
  'Fashion',
  'Favourite sweets',
  'Gardening mishaps',
  'Gifts you would like to receive',
  'I heard some gossip',
  "I'm counting on you",
  'Likeable allies',
  'Perfect recipes',
  'Relaxing at the sauna',
  'School days',
  'School uniforms',
  'Shareable snacks',
  'Tell me about yourself',
  'The courtyard couple',
  'The ideal relationship',
  'The opera',
  "You're doing great work"],
 ['Annette',
  'A dinner invitation',
  'A new gambit',
  'A word of advice',
  'Cooking mishaps',
  'Dining partners',
  'Evaluating allies',
  'Exploring the monastery',
  'Gardening mishaps',
  'Gardening mishaps',
  'Gifts you would like to receive',
  "Guessing someone's age",
  'Hopes for your future',
  'Kitchen catastrophe',
  'Our first meeting',
  'Overcoming weaknesses',
  'Past laughs',
  'Perfect recipes',
  'Plans for the future',
  'Relaxing at the sauna',
  'School days',
  'Shareable snacks',
  'Someone you look up to',
  'Tell me about yourself',
  'Thanks for everything',
  'The courtyard couple',
  'The ideal professor',
  'The last battle',
  "The library's collection",
  'The opera',
  'Things that bother you',
  'Working together',
  'You seem different',
  'You seem well',
  "You're doing great work",
  'Your ambitions'],
 ['Ashe',
  'A dinner invitation',
  'A place you’d like to visit',
  'A word of advice',
  'Being the perfect knight',
  "Books you've read recently",
  'Cats',
  'Children at the market',
  'Dreamy knights',
  'Equipment upkeep',
  'Favourite sweets',
  'Gifts you would like to receive',
  "I'm counting on you",
  'Past laughs',
  'Shareable snacks',
  'Strange fish in the pond',
  'Tell me about yourself',
  'Thanks for everything',
  'The last battle',
  "The library's collection",
  'Things that bother you',
  'Working hours for guards',
  'Working together',
  'You seem well',
  'Your ambitions'],
 ['Claude',
  'A new Gambit',
  'A place you’d like to visit',
  'A word of advice',
  "Books you've read recently",
  'Capable comrades',
  'Children at the market',
  'Equipment upkeep',
  'Evaluating allies',
  "Fódlan's future",
  'Food in the dining hall',
  "Guessing someone's age",
  'Hopes for your future',
  'I heard some gossip',
  "I'm counting on you",
  'Mighty weapons',
  'Monastery mysteries',
  'Monastery security',
  'Our first meeting',
  'Overcoming weaknesses',
  'Perfect recipes',
  'Strange fish in the pond',
  'Tell me about yourself',
  'Thanks for everything',
  'The existence of crests',
  'The last battle',
  'Things that bother you',
  'Working together',
  'Your ambitions'],
 ['Hilda',
  'A dinner invitation',
  'A place you’d like to visit',
  'Classes you might enjoy',
  'Cute accessories',
  'Cute monks',
  'Dining partners',
  'Dreamy knights',
  'Fashion',
  'Favourite sweets',
  'First crushes',
  'Gifts you would like to receive',
  'Gossip',
  "Guessing someone's age",
  'Heart-racing memories',
  'I heard some gossip',
  'Likeable allies',
  'Past laughs',
  'Relaxing at the sauna',
  'Reliable Allies',
  'School days',
  'School uniforms',
  'Tell me about yourself',
  'Thanks for everything',
  'The courtyard couple',
  'The ideal relationship',
  'The opera',
  'Things that bother you',
  'Things you find romantic',
  'You seem different',
  "You're doing great work",
  'Shareable snacks'],
 ['Leonie',
  'A dinner invitation',
  'A new gambit',
  'A strong battalion',
  'A word of advice',
  'Capable comrades',
  'Classes you might enjoy',
  'Close calls',
  'Equipment upkeep',
  'Evaluating allies',
  'Exploring the monastery',
  'Hopes for your future',
  "I'm counting on you",
  'Jeralt',
  'Mighty weapons',
  'Monastery mysteries',
  'Monastery security',
  'Overcoming weaknesses',
  'Plans for the future',
  'Reliable Allies',
  'The last battle',
  'The view from the bridge',
  'Things that bother you',
  'Working together',
  'Your ambitions'],
 ['Raphael',
  'Food in the dining hall',
  'Overcoming weaknesses',
  'School days',
  'Shareable snacks',
  'The last battle',
  'Muscle growth',
  'Favourite sweets',
  'A dinner invitation',
  'Perfect recipes',
  'Cooking mishaps',
  'Working together',
  'Classes you might enjoy'],
 ['Lorenz',
  'Dining partners',
  'Plans for the future',
  'The ideal relationship'],
 ['Ignatz',
  'A place you’d like to visit',
  'Cats',
  'Exploring the monastery',
  'I heard some gossip',
  'Mixing Pigments',
  'Monastery mysteries',
  'Plans for the future',
  'Someone you look up to',
  'Tell me about yourself',
  'The courtyard couple',
  'The view from the bridge'],
 ['Marianne',
  'Cats',
  'children at the market',
  'Exploring the monastery',
  "Fódlan's future",
  'Gardening mishaps',
  'Good books',
  'Likeable Allies',
  'Monastery mysteries',
  'Overcoming weaknesses',
  'School days',
  'Strange fish in the pond',
  'the existence of crests',
  "The library's collection",
  'The view from the bridge',
  'A dinner invitation',
  "Books you've read recently",
  'Our first meeting',
  'Tell me about yourself',
  'You seem different',
  'Hopes for your future'],
 ['Lysithea',
  'A dinner invitation',
  'A place you’d like to visit',
  "Books you've read recently",
  'Capable comrades',
  'Cats',
  'Classes you might enjoy',
  'Close calls',
  'Cooking mishaps',
  'Evaluating Allies',
  'Favourite sweets',
  'Fashion',
  'Food in the Dining Hall',
  'Gifts you would like to receive',
  'Hopes for your future',
  'I heard some gossip',
  "I'm counting on you",
  'Likeable allies',
  'Monastery mysteries',
  'Monastery rules',
  'Perfect recipes',
  'Our First Meeting',
  'Overcoming weaknesses',
  'Past Laughs',
  'The last battle',
  'Plans for the Future',
  'Relaxing at the sauna',
  'School Uniforms',
  'Shareable snacks',
  'Someone you look up to',
  'Thanks for everything',
  'The existence of crests',
  'The ideal professor',
  "The library's collection",
  'The thrill of sweets',
  'Working together',
  'You seem different',
  'Your ambitions',
  'School days',
  'Tell me about yourself',
  "Fódlan's future",
  'Strange fish in the pond'],
 ['Flayn',
  "Books you've read recently",
  'Cats',
  'Children at the market',
  'Cooking mishaps',
  'Dining partners',
  'Favourite sweets',
  "Guessing someone's age",
  'Heart-racing memories',
  'Hopes for your future',
  "I'm counting on you",
  'Past laughs',
  'School days',
  'Strange fish in the pond',
  'The ideal professor',
  'The ideal relationship',
  'Working together',
  "You're doing great work",
  'First crushes',
  'The courtyard couple'],
 ['Manuela',
  'A dinner invitation',
  'A word of advice',
  'Best performance venues',
  'Classes you might enjoy',
  'Cooking mishaps',
  'Dining partners',
  'Dreamy knights',
  'Exploring the monastery',
  'Fashion',
  'Favourite sweets',
  'First crushes',
  'Gifts you would like to receive',
  'Gossip',
  "Guessing someone's age",
  'Heart-racing memories',
  'I heard some gossip',
  'Monastery security',
  'Our first meeting',
  'Overcoming weaknesses',
  'Past laughs',
  'Plans for the future',
  'Relaxing at the sauna',
  'Shareable snacks',
  'Tell me about yourself',
  'The ideal professor',
  'The ideal relationship',
  'The opera',
  'Things you find romantic',
  'You seem well'],
 ['Hanneman',
  'A dinner invitation',
  'Exploring the monastery',
  "I'm counting on you",
  'The existence of crests',
  "The library's collection"],
 ['Catherine',
  'A new gambit',
  'Academy memories',
  'Capable comrades',
  'Close calls',
  'Cooking mishaps',
  'Exploring the monastery',
  'Food in the dining hall',
  'Gardening mishaps',
  "I'm counting on you",
  'Mighty weapons',
  'Monastery security',
  'Our first meeting',
  'Past laughs',
  'Potential training partners',
  'Tell me about yourself',
  'Thanks for everything',
  'The existence of crests',
  'Working for hours on end',
  'Working together',
  "You're doing great work",
  'Your ambitions',
  'The last battle',
  'Likeable allies'],
 ['Shamir',
  'A new gambit',
  'Better Weapons',
  'Close calls',
  'Equipment upkeep',
  'Hopes for your future',
  'Overcoming weaknesses',
  'Talk about the Church',
  'The last battle',
  "You're doing great work",
  'Your ambitions'],
 ['Cyril', 'Equipment upkeep', 'Lady Rhea'],
 ['Alois',
  'Exploring the monastery',
  'Food in the dining hall',
  'Our first meeting',
  'Plans for the future',
  'Strange fish in the pond',
  'The last battle',
  "You're doing great work"]]


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
  'Tasty Baked Treat',
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



##tea_final

tea_final_batch=[['Edelgard',
  '*About hubert not liking it when they hang out*Nod',
  '*About things being different if she was born in a different house*Sigh',
  '*About being meticulous*Nod',
  '*About relaxation*Blush',
  'remember when you saved me from those bandits?Blush'],
 ['Hubert',
  '"Most who spend time with me..." Disagree',
  '"Lady Edelgard has taken a liking to you. she\'ll want to know all about this"Nod',
  '"While I am quite busy. this is not a waste of my time. I\'m grateful for the oppertunity to observe you."'],
 ['Ferdinand',
  'Since I was a child. I have loved riding horses and fighting. People used to tell me to act more like a noble.Commend',
  'You often hear stories of nobles and commoners in love. I am not against such things. but rarely are things so simpleChat',
  'You have a way of making people feel comfortable. I almost cannot help telling you everything.Blush',
  'You treat everyone the same. regardless of status. Perhaps I should do that as well.Blush',
  'When I am unhappy. I try to bestow happiness upon others. Such is the way of the true noble.Nod'],
 ['Linhardt',
  "If I don't become a scholar. then perhaps librarian is the job for me.Praise",
  'We should explore ways to utilize the power of Relics and Crests for something other than combat.Commend',
  'Being surrounded by all these Crest-bearers makes me want to better understand Crestology.Commend',
  'You bear the legendary Crest of Flames. You simply must allow me to study it--please. Professor.Laugh',
  "Crest vs nurture. Which causes a noble's personality disorder? There's a research project. eh? Chat"],
 ['Caspar',
  "What is justice really? I'm not sure I know anymore...Chat",
  'Hey. are you getting hungry?Laugh',
  "Who was that guy? You don't know who I'm talking about? The suspicious guy who killed himself!Nod",
  "I usually don't get hung up on things. but when I do. I feel stuck!Disagree"],
 ['Bernadetta',
  'My mother works imperial capital...Commend',
  "Please don't eavesdrop on my singing anymoreNod",
  "It's relaxing here I should have brought my sewing kit.Nod",
  'If two people decide to be recluses together does that even still countLaugh'],
 ['Dorothea',
  'Envious at your lack of weaknessSip tea',
  'You are such an open minded personBlush',
  'Why are men so vain?Chat',
  "I'm not really a fan of hymns. I don't want to offer silly songs to the goddessChat",
  'My Ideal Partner is religous. but only just. And they have enough money to live on for all of our days.Praise'],
 ['Petra',
  'The ocean is far from Garreg Mach... I am feeling a bit lonely at times.Sigh',
  'If you have any worriesChat',
  'One day I am to show you the wonderful land of Brigid and its abundant natureNod',
  'If you are having problems. I am happy to be listeningChat',
  "Next I will be studying. training. researching. sparring... I'm having a lot to do!Praise",
  'You are not remembering where your homeland is? I am thinking that is strange.Chat'],
 ['Dimitri',
  'Day is over before I know itNod',
  'Sometimes I get clumsy/reckless training and break thingsChat',
  'Nod',
  'I cannot tell you how long it has been since I indulged in a nice. relaxing conversationSip tea',
  "When I feel down. I go out on a long ride on my own. There is no place more relaxing than a trusted steed's back.Nod"],
 ['Dedue',
  'I prefer to study on my ownDisagree',
  'I am the sword and shield of His Highness. I must constantly work to improve.Commend',
  'Was there something you want to discuss?Sip tea',
  "I don't like learning in classroomsDisagree"],
 ['Felix',
  'What made you so strongChat',
  'Spending time with you is not badNod',
  'Crests. lineage... skill are the only things that matterNod',
  'Well. I appreciate all that you do for me.Nod',
  "I know it's important to take a break. but if you rest too long. your muscles wither.Nod?"],
 ['Sylvain',
  'Everyone has their own reason to fight. At least im honest about mine.Commend',
  "Somebody gave me some candy earlier. I should've brought some with me.Nod",
  "Sometimes I'm surprised how warm the monastery is. I wish my parents treated me like this."],
 ['Ingrid',
  "Being here calms my nerves... Oh! But I'll leave if I'm in your way.Disagree",
  "It's warm around the monastery and the soil is rich... Honestly. I'm envious.Chat",
  'When did you start sword training?Chat',
  'as a child my father and brother used to yell at me for spending so much time with my horseLaugh',
  "I'm Already thinking of my next mealLaugh"],
 ['Mercedes',
  "The cathedral is nice and quiet. It's so relaxing!Admonish",
  "I'm actually quite skilled at drawing. I wouldn't mind using you as a model!Nod",
  'I should probably write to my mother soonNod',
  'I baked a cake earlier today. Should I have brought some with me?Nod'],
 ['Annette',
  'The only way to clean is to clean with all your might.Nod',
  'Maybe I should have baked us a cake or somethingNod',
  'No effort is ever in vain... my father used to tell me that.Chat',
  "There's an equation I've been thinking about. Can you help me later?Nod",
  'I remember the first time I met you. Right away. it was like talking to an old friend.Laugh'],
 ['Ashe',
  'It’s nice in here. I feel I can relaxSip tea',
  "I'm good with children. I've taken care of my younger siblings since I was a kidCommend",
  'Confident about my speedCommend',
  "Have you ever seen a ghost? Probably for the best if you haven't...Sip tea"],
 ['Claude',
  'Do you really have time for this? I know how busy you are...Sip tea',
  "You're such a mysteryDisagree",
  "You're an outsider. just like meNod",
  'I want to know more about you.Nod'],
 ['Hilda', 'You know. I love hearing myself talk!'],
 ["Nod,Have you ever cried. Professor? It's hard to imagine you crying.Chat,You don't say much. so you're easy to talk to.Admonish,No matter what happens in this crazy world. I know I'll be safe if I stay by your side.Nod,Everyone's so serious all the time. Boooooring.Nod,"],
 ['Leonie',
  "I don't care what you think of me. I just don't want to lose to youCommend",
  "Don't throw away anything that's still usuable. OK? I'll take whatever you don't need.Commend",
  "I hope you're keeping up with your training. if you're not careful. I'll surpass youCommend"],
 ['Raphael',
  'I have to become a knight to take care of my little sisterPraise',
  'My grandpa used to be real strong when he was younger. I obviously take after the guy!Commend',
  "I can't miss a single lecture if I want to become a proper knight!Chat"],
 ['Ignatz',
  "With you and all the friends I've made. I'm glad I came herePraise",
  "I don't know what I can do. but I'm prepared to assume responsibility for my future.Praise"],
 ['Marianne',
  "Spending time with me must be boring. isn't it?Admonish",
  "I'm sorry I don't know what to say.Praise",
  "It's not like I can go home...Chat",
  "It's a waste to spend your time with me.Disagree",
  "You'll be met with misfortune if you spend to much time with me...Admonish"],
 ['Lysithea',
  'I know I can stand to lighten up from time to timeAdmonish. Chat',
  "It's not in me to put energy into things that won't yield results. I just don't see the point.Admonish",
  "Talking to you feels worth my time. I feel there's a lot I can learn from youLaugh. Blush",
  "If I hadn't met you. I don't think I'd be who I am todayDisagree",
  'Do you believe in ghosts. Professor? Just wondering.Blush'],
 ['Flayn',
  'I desire to see the ocean again- it is difficult being so far away from it.Nod',
  'I am afraid of sleeping for fear of waking up to find my friends and family all disappeared.Praise',
  'You are an interesting person. Professor. You do not seem to know much about yourself.Disagree',
  'Lively places are my favorite. I like the monastery because there are always so many people bustling about.Nod'],
 ['Manuela',
  "Am I that terrible a woman? So I'm a little unkempt. what of it?Admonish. Disagree",
  "There's no alcohol in here. It's better if you can sleep without it. but... all you have is tea?Admonish"],
 ['Hanneman',
  'The Crest of Flames shares many traits with other Crests. Yet. it also has many unique characteristics.Nod',
  '"the ashen demon. what a (something)..."Sip tea'],
 ['Catherine',
  'I hear your nickname is "Ashen Demon." It\'s good. but not as good as "Thunder Catherine."Sip tea',
  "I'm always watching you. I guess this is your way of returning the favor.Disagree",
  'You know war strategy. not just how to wield a sword. Maybe I should study that too.Sip tea'],
 ['Shamir',
  "I'm not much for conversation. I'll gladly leave if you're bored.Disagree",
  "The sword of the creator... It's an interesting relic.Chat"],
 ['Cyril', 'Lady Rhea sure seems to like you.Sip tea'],
 ['Alois', 'You remind me of your fatherDisagree']]