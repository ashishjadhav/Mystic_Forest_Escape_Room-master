from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

 
print("1")
look_descriptions = {
    "tree": """ETHAN: Now look into the tree trunk 🌴. Inside, you'll find a survival tool 1.
               To grab it, you have to solve question 1:
               A) Everyone has me but nobody can lose me. Who am I?
                  Options:
                  1. Shadow
                  2. Energy
                  3. Memory
                  4. Time
                  """,
    "trees": """ETHAN: Now look into the tree trunk. Inside, you'll find a survival tool 1.
               To grab it, you have to solve question 1:
               A) Everyone has me but nobody can lose me. Who am I?
                  Options:
                  1. Shadow
                  2. Energy
                  3. Memory
                  4. Time
                  """,

    "forest": """You find yourself in a dense, mystical wilderness filled with trees 🌴, rocks 🪨 , and caves 🗿. 
                 Take a close look at each object around you.
                 """,

    "cave": "You enter a dark and mysterious chamber. The path ahead leads to unknown worlds. But you need some tool to travel through cave. Try looking at your surroundings.",
    "caves": "You enter a dark and mysterious chamber. The path ahead leads to unknown worlds. But you need some tool to travel through cave. Try looking at your surroundings.",

    "burrow": "You discover a hole in the ground, resembling a nest made by wild rabbits. Keep looking at the other available objects around you in the forest.",
    "burrows": "You discover a hole in the ground, resembling a nest made by wild rabbits. Keep looking at the other available objects around you in the forest.",

    "rock": """Sturdy and rugged, it may serve as a stepping stone or hide a hidden passage. 
                There is a survival tool 2 inside it. To grab it, you have to solve question 2:
                Here's a puzzle for you:
                Large as a mountain, small as a pea, 
                Endlessly swimming in a waterless sea. Who am I? 
                   Options: 
                   1. Fish
                   2. Desert
                   3. Asteroid
                   4. Star
                   """,
    "rocks": """Sturdy and rugged, it may serve as a stepping stone or hide a hidden passage. 
                There is a survival tool 2 inside it. To grab it, you have to solve question 2:
                Here's a puzzle for you:
                Large as a mountain, small as a pea, 
                Endlessly swimming in a waterless sea. Who am I? 
                   Options: 
                   1. Fish
                   2. Desert
                   3. Asteroid  
                   4. Star
                   """,

    "chockstone": "Chockstone is large rock wedged in cracks or narrow spaces on a mountain. Keep looking at the other available objects around mountains.",
    "chockstones": "Chockstone is large rock wedged in cracks or narrow spaces on a mountain. Keep looking at the other available objects around mountains.",

    "mountain": """The tallest mountain with lots of big rocks and chockstone is ahead of you.
                   Take a close look at each objects around you.  And you need some tool to climb the mountain.
                   """,
    "mountains": """The tallest mountain with lots of big rocks and chockstone is ahead of you.
                   Take a close look at each objects around you.
                   """,

    "river": """The deepest river with deadly predators in it and on the banks of river there is sand and shells on it. 
                Fortunately there is bridge on it but it is locked, Take a close look at each object around you.
                """,

    "bridge": "The bridge is locked. You cant cross it. Take a close look at each objects around you.",
    "locked bridge": "The bridge is locked. You cant cross it. Take a close look at each objects around you.",

    "shell": """Shells are the hard external coverings of marine mollusks.
                Here's a puzzle3 for you: 
                The moon is my father. The sea is my mother. I have a million brothers. 
                I die when I reach land. who am i? 
                Options: 
                1. Pearl 
                2. Dewdrop 
                3. Foam 
                4. Waves
                
                """,
    "shells": """Shells are the hard external coverings of marine mollusks.
                Here's a puzzle3 for you: 
                The moon is my father. The sea is my mother. I have a million brothers. 
                I die when I reach land. who am i? 
                Options: 
                1. Pearl 
                2. Dewdrop 
                3. Foam 
                4. Waves

                """,

    "sand": """the wet and smooth soil and there is a shell lying on it.
                There is a survival tool 3 inside it.To grab it, you have to solve question 3
                Take a close look at each objects around you.
                """,


}

print("2")


class ActionLook(Action):
    def name(self) -> Text:
        return "action_look"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        spoken = False

        for blob in tracker.latest_message['entities']:
            if blob['entity'] == 'object':
                try:
                    description = look_descriptions[blob['value']]
                    dispatcher.utter_message(text=description)
                    spoken = True
                    print("3")
                except KeyError:
                    dispatcher.utter_message(text="Sorry, there is no description available for that object.")
                    spoken = True
                    print("4")
        if not spoken:
            dispatcher.utter_message(text="Could you repeat what you're trying to look at?")
            print("5")
        return []

print("6")

# class AnswerCheckAction(Action):
#     def name(self) -> Text:
#         return "action_check_answer"
#
#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Retrieve user's answer for question 1 and question 2
#         answer1 = tracker.latest_message.get('text')
#         answer2 = tracker.latest_message.get('text')
#         answer3 = tracker.latest_message.get('text')
#         # Retrieve the correct answers for question 1 and question 2
#         correct_answer1 = "Shadow"
#         correct_answer2 = "asteroid"
#         correct_answer3 = "waves"
#
#         # Check if the user provided an answer for question 1
#         if answer1:
#             if answer1.lower() == correct_answer1.lower():
#                 dispatcher.utter_message(text="Correct! You have unlocked a survival tool 1 torch. Now  pick the "
#                                                "torch to put  into your bag.")
#             else:
#                 dispatcher.utter_message(text="Wrong answer! Please try again.")
#             return []
#
#         # Check if the user provided an answer for question 2
#         if answer2:
#             if answer2.lower() == correct_answer2.lower():
#                 dispatcher.utter_message(text="Correct! You have unlocked a survival tool 2 rope. Now u pick the"
#                                               "rope to put  into your bag")
#             else:
#                 dispatcher.utter_message(text="Incorrect answer. Please try again.")
#             return []
#
#         if answer3:
#             if answer3.lower() == correct_answer3.lower():
#                 dispatcher.utter_message(text="Correct! You have unlocked a survival tool 3 key. Now u pick the "
#                                                           "key to put  into your bag.")
#             else:
#                 dispatcher.utter_message(text="Incorrect answer. Please try again.")
#             return []
#
#
#         # If no answer provided, prompt the user to choose an option
#         dispatcher.utter_message(text="Please choose one of the 4  options.")
#
#         return []


class AnswerCheckAction(Action):
    def name(self) -> Text:
        return "action_check_answer"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Retrieve user's answer for question 1
        answer1 = tracker.latest_message.get('text')

        # Retrieve the correct answers for question 1
        correct_answer1 = "Shadow"
        correct_answer2 = "asteroid"
        correct_answer3 = "waves"
        correct_answer4 = "wave"


        # Check if the user provided an answer for question 1
        if answer1:
            if answer1.lower() == correct_answer1.lower():
                dispatcher.utter_message(
                    text="Correct! You have unlocked a survival tool 1 'TORCH'. Now pick the torch to put into your bag.")
            elif answer1.lower() == correct_answer2.lower():
                dispatcher.utter_message(
                    text="Correct! You have unlocked a survival tool 2 'ROPE'. Now collect the rope to put into your bag.")
            elif answer1.lower() == correct_answer3.lower():
                dispatcher.utter_message(
                    text="Correct! You have unlocked a survival tool 3 'KEY'. Now grab the key to put into your bag.")
            elif answer1.lower() == correct_answer4.lower():
                dispatcher.utter_message(
                    text="Correct! You have unlocked a survival tool 3 'KEY'. Now pick the key to put into your bag.")
            else:
                dispatcher.utter_message(text="Wrong answer! Please try again.")

            return []


able_to_pick_up = ["torch", "rope", "key", "sword"]


class ActionPickUp(Action):
    def name(self) -> Text:
        return "action_pickup"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        items_to_add = []
        # We need to check what objects the user wants to pick up. We cannot pick up
        # all objects, and we need to check if the object is already in your inventory.
        for blob in tracker.latest_message['entities']:
            if blob['entity'] == 'object':
                item = blob['value']
                if item not in able_to_pick_up:
                    dispatcher.utter_message(text=f"You can't pick up {item}.")
                else:
                    item_in_inventory = tracker.get_slot(item)
                    if item_in_inventory:
                        dispatcher.utter_message(text=f"You already have {item} in your inventory.")
                    else:
                        items_to_add.append(SlotSet(item, True))
                        dispatcher.utter_message(text=f"You've picked up the {item} and it is in your inventory. Now try to combine it with other required objects around you to find the hidden route for the next level.")

        # We could add multiple items here.
        if len(items_to_add) > 0:
            return items_to_add
        dispatcher.utter_message(text="Are you sure you spelled the item you wanted to pick up correctly?")
        return []


class ActionInventory(Action):
    def name(self) -> Text:
        return "action_inventory"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        items_in_inventory = [item for item in able_to_pick_up if tracker.get_slot(item)]
        if len(items_in_inventory) == 0:
            dispatcher.utter_message(text="There are no items in your inventory.")
            return []
        dispatcher.utter_message(text="These are the items in your inventory:")
        for item in items_in_inventory:
            dispatcher.utter_message(text=f"- {item}")
        return []

combinations = {
    ('torch', 'cave'): "Amazing! The torch is used to navigate the cave. Now you are in level2. However, on the other side there is a mountain.You see a mountain surrounded by rocks and chockstones.Have a look at them.",

    ('torch', 'burrow'): "Torch doesn't work with burrows. Try something else.",

    ('torch', 'tree'): "Why put the torch back in the tree? You've just picked it up!",

    ('rope', 'mountain'): "Great! You successfully used the rope to climb the mountain. Welcome to level 3! Infront of you there is the deepest river with deadly predators in it and on the banks of river there is sand and shells on it. Fortunately there is bridge on it but it is locked, Take a close look at each object around you",

    ('rope', 'mountain'): "Great! You successfully used the rope to climb the mountain. Welcome to level 3! Infront of you there is the deepest river with deadly predators in it and on the banks of river there is sand and shells on it. Fortunately there is bridge on it but it is locked, Take a close look at each object around you ",

    ('rope', 'rock'): "Why put the rope back in the rock? It's probably super useful.",

    ('key', 'bridge'): """Hey, the key fits! Amazing! The key is now able to open the gate of the bridge.
    
                        ********** CONGRATULATIONS:) YOU HAVE ESCAPED FROM MYSTIC FOREST ***********.
                       
                       Please take a moment to provide your valuable feedback by filling out the feedback form responses
                       [feedback form](https://docs.google.com/forms/d/e/1FAIpQLSeMYMxEMvHnHjk57msht-SDd7YowjzbqO9CmRE1w1J4HRIr7A/viewform?usp=sf_link). We appreciate your input!""",

    ('key', 'sand'): "Why put the key back in the sand? It's probably super useful."
}


combinations.update({(i2, i1): v for (i1, i2), v in combinations.items()})


class ActionUse(Action):
    def name(self) -> Text:
        return "action_use"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = [e['value'] for e in tracker.latest_message['entities'] if e['entity'] == 'object']
        if len(entities) == 0:
            dispatcher.utter_message(text="I think you want to combine items but something is unclear.")
            dispatcher.utter_message(text="Could you retry and make sure you spelled the items correctly?.")
            return []
        elif len(entities) == 1:
            dispatcher.utter_message(text="I think you want to combine items but something is unclear.")
            dispatcher.utter_message(text=f"I could only make out that you wanted to use {entities[0]}.")
            dispatcher.utter_message(text="Could you retry and make sure you spelled the items correctly?.")
            return []
        elif len(entities) > 2:
            dispatcher.utter_message(text="I think you want to combine items but something is unclear.")
            dispatcher.utter_message(text=f"I could only make out that you wanted to combine {' and '.join(entities)}.")
            dispatcher.utter_message(text="You can only combine two items at a time.")
            return []
        # there are two items and they are confirmed
        item1, item2 = entities
        if (item1, item2) in combinations.keys():
            dispatcher.utter_message(text=combinations[(item1, item2)])
        else:
            dispatcher.utter_message(text=f"I don't think combining {item1} with {item2} makes sense.")
        return []
