
# coding: utf-8

# In[ ]:


import collections


# In[11]:


##char_data

char_list_unsplitted="Edelgard Bernadetta Caspar Dorothea Ferdinand Hubert Linhardt Petra Dimitri Annette Ashe Dedue Felix Ingrid Mercedes Sylvain Claude Hilda Ignatz Leonie Lorenz Lysithea Marianne Raphael Rhea Alois Catherine Cyril Flayn Gilbert Hanneman Manuela Seteth Shamir Jeralt Jeritza Byleth"
char_list = char_list_unsplitted.split()


 

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
  "You're doing great work",
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '*About hubert not liking it when they hang out*Nod',
  '*About things being different if she was born in a different house*Sigh',
  '*About being meticulous*Nod',
  '*About relaxation*Blush',
  'remember when you saved me from those bandits?Blush'],
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
  'Your ambitions',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '"Most who spend time with me..." Disagree',
  '"Lady Edelgard has taken a liking to you. she\'ll want to know all about this"Nod',
  '"While I am quite busy. this is not a waste of my time. I\'m grateful for the oppertunity to observe you."'],
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
  'Your ambitions',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  'Since I was a child. I have loved riding horses and fighting. People used to tell me to act more like a noble.Commend',
  'You often hear stories of nobles and commoners in love. I am not against such things. but rarely are things so simpleChat',
  'You have a way of making people feel comfortable. I almost cannot help telling you everything.Blush',
  'You treat everyone the same. regardless of status. Perhaps I should do that as well.Blush',
  'When I am unhappy. I try to bestow happiness upon others. Such is the way of the true noble.Nod'],
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
  'Things that bother you',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  "If I don't become a scholar. then perhaps librarian is the job for me.Praise",
  'We should explore ways to utilize the power of Relics and Crests for something other than combat.Commend',
  'Being surrounded by all these Crest-bearers makes me want to better understand Crestology.Commend',
  'You bear the legendary Crest of Flames. You simply must allow me to study it--please. Professor.Laugh',
  "Crest vs nurture. Which causes a noble's personality disorder? There's a research project. eh? Chat"],
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
  'Working together',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  "What is justice really? I'm not sure I know anymore...Chat",
  'Hey. are you getting hungry?Laugh',
  "Who was that guy? You don't know who I'm talking about? The suspicious guy who killed himself!Nod",
  "I usually don't get hung up on things. but when I do. I feel stuck!Disagree"],
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
  "You're doing great work",
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  'My mother works imperial capital...Commend',
  "Please don't eavesdrop on my singing anymoreNod",
  "It's relaxing here I should have brought my sewing kit.Nod",
  'If two people decide to be recluses together does that even still countLaugh'],
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
  'You seem different',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  'Envious at your lack of weaknessSip tea',
  'You are such an open minded personBlush',
  'Why are men so vain?Chat',
  "I'm not really a fan of hymns. I don't want to offer silly songs to the goddessChat",
  'My Ideal Partner is religous. but only just. And they have enough money to live on for all of our days.Praise'],
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
  'Fashion',
  '',
  '',
  '',
  '',
  '',
  '',
  'The ocean is far from Garreg Mach... I am feeling a bit lonely at times.Sigh',
  'If you have any worriesChat',
  'One day I am to show you the wonderful land of Brigid and its abundant natureNod',
  'If you are having problems. I am happy to be listeningChat',
  "Next I will be studying. training. researching. sparring... I'm having a lot to do!Praise",
  'You are not remembering where your homeland is? I am thinking that is strange.Chat'],
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
  'Your ambitions',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  'Day is over before I know itNod',
  'Sometimes I get clumsy/reckless training and break thingsChat',
  'Nod',
  'I cannot tell you how long it has been since I indulged in a nice. relaxing conversationSip tea',
  "When I feel down. I go out on a long ride on my own. There is no place more relaxing than a trusted steed's back.Nod"],
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
  'Your ambitions',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  'I prefer to study on my ownDisagree',
  'I am the sword and shield of His Highness. I must constantly work to improve.Commend',
  'Was there something you want to discuss?Sip tea',
  "I don't like learning in classroomsDisagree"],
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
  'Your ambitions',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  'What made you so strongChat',
  'Spending time with you is not badNod',
  'Crests. lineage... skill are the only things that matterNod',
  'Well. I appreciate all that you do for me.Nod',
  "I know it's important to take a break. but if you rest too long. your muscles wither.Nod?"],
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
  'Dining partners',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  'Everyone has their own reason to fight. At least im honest about mine.Commend',
  "Somebody gave me some candy earlier. I should've brought some with me.Nod",
  "Sometimes I'm surprised how warm the monastery is. I wish my parents treated me like this."],
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
  'Your ambitions',
  '',
  "Being here calms my nerves... Oh! But I'll leave if I'm in your way.Disagree",
  "It's warm around the monastery and the soil is rich... Honestly. I'm envious.Chat",
  'When did you start sword training?Chat',
  'as a child my father and brother used to yell at me for spending so much time with my horseLaugh',
  "I'm Already thinking of my next mealLaugh"],
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
  "You're doing great work",
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  "The cathedral is nice and quiet. It's so relaxing!Admonish",
  "I'm actually quite skilled at drawing. I wouldn't mind using you as a model!Nod",
  'I should probably write to my mother soonNod',
  'I baked a cake earlier today. Should I have brought some with me?Nod'],
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
  'Your ambitions',
  '',
  '',
  '',
  '',
  '',
  '',
  'The only way to clean is to clean with all your might.Nod',
  'Maybe I should have baked us a cake or somethingNod',
  'No effort is ever in vain... my father used to tell me that.Chat',
  "There's an equation I've been thinking about. Can you help me later?Nod",
  'I remember the first time I met you. Right away. it was like talking to an old friend.Laugh'],
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
  'Your ambitions',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  'It’s nice in here. I feel I can relaxSip tea',
  "I'm good with children. I've taken care of my younger siblings since I was a kidCommend",
  'Confident about my speedCommend',
  "Have you ever seen a ghost? Probably for the best if you haven't...Sip tea"],
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
  'Your ambitions',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  'Do you really have time for this? I know how busy you are...Sip tea',
  "You're such a mysteryDisagree",
  "You're an outsider. just like meNod",
  'I want to know more about you.Nod'],
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
  'Shareable snacks',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  'You know. I love hearing myself talk!'],
 ["Nod,Have you ever cried. Professor? It's hard to imagine you crying.Chat,You don't say much. so you're easy to talk to.Admonish,No matter what happens in this crazy world. I know I'll be safe if I stay by your side.Nod,Everyone's so serious all the time. Boooooring.Nod,"],
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
  'Your ambitions',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  "I don't care what you think of me. I just don't want to lose to youCommend",
  "Don't throw away anything that's still usuable. OK? I'll take whatever you don't need.Commend",
  "I hope you're keeping up with your training. if you're not careful. I'll surpass youCommend"],
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
  'Classes you might enjoy',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  'I have to become a knight to take care of my little sisterPraise',
  'My grandpa used to be real strong when he was younger. I obviously take after the guy!Commend',
  "I can't miss a single lecture if I want to become a proper knight!Chat"],
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
  'The view from the bridge',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  "With you and all the friends I've made. I'm glad I came herePraise",
  "I don't know what I can do. but I'm prepared to assume responsibility for my future.Praise"],
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
  'Hopes for your future',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  "Spending time with me must be boring. isn't it?Admonish",
  "I'm sorry I don't know what to say.Praise",
  "It's not like I can go home...Chat",
  "It's a waste to spend your time with me.Disagree",
  "You'll be met with misfortune if you spend to much time with me...Admonish"],
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
  'Strange fish in the pond',
  'I know I can stand to lighten up from time to timeAdmonish. Chat',
  "It's not in me to put energy into things that won't yield results. I just don't see the point.Admonish",
  "Talking to you feels worth my time. I feel there's a lot I can learn from youLaugh. Blush",
  "If I hadn't met you. I don't think I'd be who I am todayDisagree",
  'Do you believe in ghosts. Professor? Just wondering.Blush'],
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
  'The courtyard couple',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  'I desire to see the ocean again- it is difficult being so far away from it.Nod',
  'I am afraid of sleeping for fear of waking up to find my friends and family all disappeared.Praise',
  'You are an interesting person. Professor. You do not seem to know much about yourself.Disagree',
  'Lively places are my favorite. I like the monastery because there are always so many people bustling about.Nod'],
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
  'You seem well',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  "Am I that terrible a woman? So I'm a little unkempt. what of it?Admonish. Disagree",
  "There's no alcohol in here. It's better if you can sleep without it. but... all you have is tea?Admonish"],
 ['Hanneman',
  'A dinner invitation',
  'Exploring the monastery',
  "I'm counting on you",
  'The existence of crests',
  "The library's collection",
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  'The Crest of Flames shares many traits with other Crests. Yet. it also has many unique characteristics.Nod',
  '"the ashen demon. what a (something)..."Sip tea'],
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
  'Likeable allies',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  'I hear your nickname is "Ashen Demon." It\'s good. but not as good as "Thunder Catherine."Sip tea',
  "I'm always watching you. I guess this is your way of returning the favor.Disagree",
  'You know war strategy. not just how to wield a sword. Maybe I should study that too.Sip tea'],
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
  'Your ambitions',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  "I'm not much for conversation. I'll gladly leave if you're bored.Disagree",
  "The sword of the creator... It's an interesting relic.Chat"],
 ['Cyril',
  'Equipment upkeep',
  'Lady Rhea',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  'Lady Rhea sure seems to like you.Sip tea'],
 ['Alois',
  'Exploring the monastery',
  'Food in the dining hall',
  'Our first meeting',
  'Plans for the future',
  'Strange fish in the pond',
  'The last battle',
  "You're doing great work",
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  '',
  'You remind me of your fatherDisagree']]



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





class support_database:
    def __init__(self):
        #[tea,tea_dialogue,gifts,lost_items,flowers]
        
        tea_dict = collections.defaultdict(set)
        tea_dial_dict = collections.defaultdict(set)
        gifts_dict = collections.defaultdict(set)
        lost_items_dict = collections.defaultdict(set)
        flowers_dict = collections.defaultdict(set)
        
        self.char_to_obj = [tea_dict, tea_dial_dict, tea_final_question, gifts_dict ,lost_items_dict, flowers_dict]
        
        #for the reverse lookeup
        self.obj_to_char = collections.defaultdict(set)
        
        #for showing the list, pre-checking whether an item/char could be look-up, and for later adding more character if DLC
        
       
        #item_type_code
        #0-tea,1-tea_dialogue,2-gifts,3-lost_items,4-flowers
        self.item_list=[ set(), set(), set(), set(), set() ]    
        
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



 

help_message = "_"*40 +
  "\n Type either character name or item name to show corresponding list" +
  "\n Note that all nouns in items are capitalized except propsitions (and, of ,to, etc.) e.g. 'New Bottle of Perfume' (without the ' of course, similar rules applied to the commands below) "+
  "\n Type 'show_char_list' to see all possible characters"+
  "\n Type 'show_item_list_ITC' to see list of corresponding items"+
  "\n and ITC stands for item type code, which is an integer from 0 to 4, as 0-tea,1-tea_dialogue,2-gifts,3-lost_items,4-flowers"+
  "\n type 'done' to finish )"+
  "_" *40 


def lookup_items():

  item_type = input("And What kind of items are you looking up? \nInput the corresponding types: tea,tea_dialogue, gifts, lost_items, flowers :" )


def interface():

  print("_"*40 )

  print("Greetings! The support guide is ready")

  print("_"*40 )

	user_input=input("FETH support items/char look up! :")

	if user_input in FETH.char_list:		

		item_type_code = int(input("And What kind of items are you looking up? \ndInput the corresponding integer 0-tea,1-tea_dialogue,2-gifts,3-lost_items,4-flowers :" ) )

		answer = FETH.char_to_obj[item_type_code][user_input]

		line ='-' * len(str(answer))

		print (line )

		print(answer)

		print (line) 
		

		reset = input("Wanna look up something else? Type done to finish. Type anything else to look up again:")

		if reset != "done":

			print("Resetting"+"."*20)

      interface()



	if user_input == "done":

		break





