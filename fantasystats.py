print ('Are you ready to go on journey filled with peril and excitement?')
print ('Good, I have just the quest for you.')
print ('Now then, my eyes are not as young as they used to be')
print ('Are you a:')
print ('DWARF; These are shorter and stockier than Elves and Men, able to withstand both heat and cold. They are excellent metal-workers and strong with two-handed weapons. They have bad dexterity and very good strength. They are quite intelligent but are have low agility.')
print ('HUMAN; These are medium height and have average strength, intelligence, agility and dexterity. Their main weapons are one-handed swords and bows.')
print ('ELF; These are slight of build and are excellent magicians. They have a high intelligence and agility. They are not that strong though. Their dexterity is average.')

inputVal=raw_input()
inputVal=inputVal.upper()
if (inputVal=='DWARF'):
    print ('A good race, you shall go far in my quest.')
    strength=20
    agility=5
    intelligence=15
    dexterity=8
if (inputVal=='HUMAN'):
    print ('I like Humans, well I should, as I am one!')
    strength=15
    agility=15
    intelligence=15
    dexterity=15
if (inputVal=='ELF'):
    print ('An Elf eh? Oh well, you will do.')
    strength=6
    agility=20
    intelligence=23
    dexterity=15
print ('And what is your name, young ' + inputVal)

myName=raw_input()
print ('I like that name, hmmm, ' + myName)
print ('It tastes good in my mouth')
print ('Anyway, its time for me to magicianize you, you choose what you want upgraded or downgraded, and I do it!')
print ('But I can only upgrade 6 things.')
print ('Are you ready?')
print ('Meh, I do not care if you say yes or no, I am going to do it anyway.')
print ('This is what you are like already')
print ''
count=6
print ("Narrator's Magic: "+str(count))
print ''
print ('Str: ' + str(strength))
print ('Agt: '+str(agility))
print ('Int: '+str(intelligence))
print ('Dex: '+str(dexterity))
print ''
print ('Tell me which ones you want changing and I will change them')
print ('Helpful Voice: "For instance, if you wanted to change strength up, you would put "up str", and if you wanted to make agility go down, you would put "down agt",(You also gain another of the Narrators Magic). You can also skip this part by typing "skip""')

while count > 0:

	statChange= raw_input()
	statChange= statChange.lower()

	if (statChange=='skip'):
		break
	if (statChange=='up str'):
		strength=strength+1
		count =count-1
	if (statChange=='up agt'):
		agility=agility+1
		count =count-1
	if (statChange=='up int'):
		intelligence=intelligence+1
		count =count-1
	if (statChange=='up dex'):
		dexterity=dexterity+1
		count =count-1

	if (statChange=='down str'):
		strength=strength-1
		count =count+1
	if (statChange=='down agt'):
		agility=agility-1
		count =count+1
	if (statChange=='down int'):
		intelligence=intelligence-1
		count =count+1
	if (statChange=='down dex'):
		dexterity=dexterity-1
		count =count+1
	print ''
	print ("Narrator's Magic: "+str(count))	
	print ''
	print ('Str: '+str(strength))
	print ('Agt: '+str(agility))
	print ('Int: '+str(intelligence))
	print ('Dex: '+str(dexterity))

print (myName)


