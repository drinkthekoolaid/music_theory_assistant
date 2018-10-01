"""
This program is to assist people with music theory 
related questions.  It has a menu of questions, asks the
user for input, and outputs the appropriate info.
"""

"""
Version History:

1.0 - hackjob
2.0 - use of dictionary, working keys, bugs in keys with 6 or 
more accidentals
2.1 - keys working, added scales, chords, arpeggios as sub-menus
2.2 - cleaning up the look of the menu, created menu navigation 

BUGLIST:

1. (This is caused by the IDE while using python - no worries) 
When printing major scales, the sharp symbol (#) is greying
out the text following it.  Just a graphical inconsistency I 
suppose, and perhaps only in the IDE because of the python config.  
Keep it in mind though.  

"""

############################################################

"""
Notes Section - these are all twelve possible notes in 
western music, sharps and flats are separate lists for 
ease of access.  Some redundant notes in both lists but 
this seems to be the best possible way right now.
"""

sharp_notes = {"C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4,
"F":5 , "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11}
sharp_notes_list = ["C", "C#", "D", "D#", "E",
"F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E",
"F", "F#", "G", "G#", "A", "A#", "B"]
f_sharp = ["C", "C#", "D", "D#", "E",
"E#", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E",
"E#", "F#", "G", "G#", "A", "A#", "B"]
c_sharp = ["B#", "C#", "D", "D#", "E",
"E#", "F#", "G", "G#", "A", "A#", "B", "B#", "C#", "D", "D#", "E",
"E#", "F#", "G", "G#", "A", "A#", "B"]  
flat_notes = {"C": 0, "DB": 1, "D": 2, "EB": 3, "E": 4,
"F": 5, "GB": 6, "G": 7, "AB": 8, "A": 9, "BB": 10, "B": 11}
c_flat_notes = {"C": 0, "DB": 1, "D": 2, "EB": 3, "E": 4,
"F": 5, "GB": 6, "G": 7, "AB": 8, "A": 9, "BB": 10, "CB": 11}
flat_notes_list = ["C", "Db", "D", "Eb", "E",
"F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E",
"F", "Gb", "G", "Ab", "A", "Bb", "B"]
g_flat = ["C", "Db", "D", "Eb", "E",
"F", "Gb", "G", "Ab", "A", "Bb", "Cb", "C", "Db", "D", "Eb", "E",
"F", "Gb", "G", "Ab", "A", "Bb", "Cb"]
c_flat = ["C", "Db", "D", "Eb", "Fb",
"F", "Gb", "G", "Ab", "A", "Bb", "Cb", "C", "Db", "D", "Eb", "Fb",
"F", "Gb", "G", "Ab", "A", "Bb", "Cb"]
num_notes = [11]

scales_builder_sharp_notes = {"C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4,
"F":5 , "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11, "C": 12, "C#": 13, "D": 14, "D#": 15, "E": 16,
"F": 17, "F#": 18, "G": 19, "G#": 20, "A": 21, "A#": 22, "B": 23}  # this seems like a hacky way to fix the issue of base twelve math (well by avoiding it entirely...)
scale_builder_flat_notes = {"C": 0, "DB": 1, "D": 2, "EB": 3, "E": 4,
"F": 5, "GB": 6, "G": 7, "AB": 8, "A": 9, "BB": 10, "B": 11, "C": 12, "D": 13, "DB": 14, "Eb": 15, "E": 16,
"F": 17, "Gb": 18, "G": 19, "Ab": 20, "A": 21, "Bb": 22, "B": 23}


#Keys Section - These are the two halves of the circle of fifths
sharp_keys = {"C": 0, "G": 1, "D": 2, "A": 3, "E": 4, "B": 5, "F#": 6, "C#": 7} #C isn't really a shapr key...but I don't want to make a list just for it, let's see if that makes a bug later.
sharp_keys_n = [0, 7, 2, 9, 4, 11, 6, 1]
order_of_sharps = ["F", "C", "G", "D", "A", "E", "B"]
order_of_flats = ["B", "E", "A", "D", "G", "C", "F"]
flat_keys = {"C": 0, "F": 1, "BB": 2, "EB": 3, "AB": 4, "DB": 5, "GB": 6, "CB": 7} #C is also included here so that the index value remains equal to the number of sharps in a key
flat_keys_n = [0, 5, 10, 3, 8, 1, 6, 11]

#Scales Section - going to be writing a lot of these...
major_scale = [0, 2, 4, 5, 7, 9, 11]
minor_scale = [0, 2, 3, 5, 7, 8, 10]

#############################################################

def keys():   #now has user input. Still needs to be able to access dictionary
  while True:
    user_input = input("Please enter a key: ")
    if user_input.lower() == "menu":
      print("------")
      break
    if user_input.upper() in sharp_keys:
      print("this is a sharp key")
      k = str(user_input.upper())
      add_sharps = int(sharp_notes[k])
      sharpened = []
      print("numerical value: " + str(sharp_notes[k]) + ", with this many sharps: " + str(sharp_keys[k])) #will have to return as non str()
      numsharps = int(sharp_keys[k])
      counter = 0
      for n in order_of_sharps:
        if counter == numsharps:
          break
        sharpened.append(n)
        counter += 1
      print("these notes will be sharpened: " + str(sharpened))      
      for i in major_scale:
        if user_input.lower() == "f#":
          print(f_sharp[i + add_sharps], end=' ')
        elif user_input.lower() == "c#":
          print(c_sharp[i + add_sharps], end=' ')
        else: 
          print(sharp_notes_list[i + add_sharps], end=' ')
      print("")
      print("------") 

    elif user_input.upper() in flat_keys:
      print("this is a flat key")
      k = str(user_input.upper())
      flattened = []
      numflats = int(flat_keys[k])
      counter = 0

      if k == "CB":
        add_flats = int(c_flat_notes[k])
        print("numerical value: " + str(c_flat_notes[k]) + ", with this many flats: " + str(flat_keys[k]))
      else:  
        add_flats = int(flat_notes[k])      
        print("numerical value: " + str(flat_notes[k]) + ", with this many flats: " + str(flat_keys[k])) 
      

      for n in order_of_flats:
        if counter == numflats:
          break
        flattened.append(n)
        counter += 1
      print("these notes will be flattened: " + str(flattened))      
      for i in major_scale:
        if user_input.upper() == "GB":
          print(g_flat[i + add_flats], end=' ')
        elif user_input.upper() == "CB":
          print(c_flat[i + add_flats], end=' ')
        else:  
          print(flat_notes_list[i + add_flats], end=' ')
      print("")
      print("---------")
  main()

#############################################################

def scales():
  s_input = input("Please enter a scale or mode (eg: pentatonic, dorian, etc): ")
  if s_input.lower() == "menu":
    print("------")
    main()
  else:
    print("Coming soon...")
    print("------")
    main()

#############################################################

def chords():
  c_input = input("Please enter a chord type (eg: major, minor, m7b5): ")
  if c_input.lower() == "menu":
    print("------")
    main()
  else:
    print("Coming soon...")
    print("------")
    main()

#############################################################

def arpeggios():
  a_input = input("Please enter an arpeggio type (eg: major, minor, m7b5): ")
  if a_input.lower() == "menu":
    print("------")
    main()
  else:
    print("Coming soon...")
    print("------")
    main()

#############################################################  
      
menu = ["Keys", "Scales", "Chords", "Arpeggios"]

def main():
  print("Type 'menu' at any time to return to menu")
  print("")
  print("Menu: ")
  print("------")
  for i in menu:
    print (i)  
  print("")
  user_menu = input("Please select a menu item: ")
  if user_menu.lower() == "keys":
    keys()
  elif user_menu.lower() == "scales":
    scales()   
  elif user_menu.lower() == "chords":
    chords()
  elif user_menu.lower() == "arpeggios":
    arpeggios()  
  else:
    print("------")
    print("Please select a valid menu item")
    print("------")
    main()
main()   
