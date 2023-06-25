import os
import random
def healing() :
	heal = random.randint(0,8)
	return heal
def health_display(user_hp,bot_hp) :
	print("your hp :- ",user_hp)
	print ("bot hp :- ",bot_hp )
print ("\t\tbot has challenged you")
print ("  [a] - attack the bot \n  [d] - deflect the attack \n  [h] - regain some hp")
user_hp = 20
bot_hp = 50
moves = ["attack", "defend", "heal", "attack", "defend", "heal", "attack", "defend", "heal"]
print(" \tyour hp = ",user_hp)
print (" \tbot hp = ", bot_hp)
while(1) :
	if user_hp <= 0 or bot_hp <= 0 :
		break
	user = input()
	bot = random.choice(moves)
	os.system('cls')	
	if user == "a" :
		if bot == "attack":
			print ("bot chosen attack")
			damage = random.randint(0,9)
			botdamage = random.randint(0,9)
			print ("you dealt",damage," damage")
			print("bot dealt",botdamage," damage")
			user_hp = user_hp - botdamage
			bot_hp = bot_hp - damage
			health_display(user_hp, bot_hp)
		elif bot == "defend" :
			print("bot chosen defend")
			damage = 0
			botdamage = 0
			print ("bot deflected the attack")
			print("you dealt no damage")
			user_hp = user_hp - 0
			bot_hp = bot_hp - 0
			health_display (user_hp, bot_hp)
		elif bot == "heal" :
			print ("bot chosen heal")
			if bot_hp < 50 :				
				damage = random.randint(0,9)
				healed = random.randint(0,8)
				botdamage = 0
				print("you dealt", damage," damage")
				print("bot healed ",healed," hp")
				user_hp = user_hp - botdamage				
				if (bot_hp+healed) > 50 :
					h =bot_hp + healed
					h = 50
				bot_hp = (bot_hp + healed)
				bot_hp = bot_hp - damage
				health_display(user_hp, bot_hp)
			else :
				print ("no use")
				damage = random.randint(0,9)
				print ("you dealt ",damage," damage")
				user_hp = user_hp - 0
				bot_hp = bot_hp - damage
				health_display(user_hp,bot_hp)			
	if user == "d" :
		if bot == "attack" :
			print("bot used attack")
			damage = 0
			botdamage = 0
			print("you deflected the attack")
			print("bot dealt no damage")
			user_hp = user_hp - 0
			bot_hp = bot_hp - 0
			health_display(user_hp, bot_hp)
		elif bot == "defend" :
			print("bot used defend" )
			damage = 0
			botdamage = 0
			print ("you deflected the attack")
			print ("bot deflected the attack")
			user_hp = user_hp - 0
			bot_hp = bot_hp - 0
			health_display(user_hp, bot_hp)
		elif bot == "heal" :
			print("bot used heal")
			if bot_hp < 100 :								
				damage = random.randint(0,9)
				botdamage = 0
				healed = random.randint(0,8)
				print ("you dealt ",damage, "damage")
				print("bot healed ",healed," hp")
				user_hp = user_hp - 0
				bot_hp = (bot_hp + healed)
				health_display(user_hp, bot_hp)
			else :
				print ("no use")
				damage = 0
				print ("you deflected nothing")
				user_hp = user_hp - 0
				bot_hp = bot_hp - 0
				health_display(user_hp, bot_hp)
	elif user == "h" :
			if bot == "attack" :
				print ("bot used attack")
				if user_hp < 20 :					
					damage = 0
					botdamage = random.randint(0,9)
					healed = random.randint(0,8)
					if (user_hp+healed) > 20 :
						s = (user_hp+healed)
						s = 20
					print ("bot dealt ", botdamage, "damage")
					print ("you healed ",healed, " hp")
					user_hp = (user_hp + healed) - botdamage
					bot_hp = bot_hp - 0
					health_display(user_hp, bot_hp)
				else :					
					print ("no use of heal")
					damage = 0
					botdamage = random.randint(0,9)
					print ("bot dealt ", botdamage,"damage")
					user_hp = user_hp  - botdamage
					bot_hp = bot_hp - 0
					health_display(user_hp, bot_hp)			
			elif bot == "defend" :
								print("bot used defend")
								if user_hp < 20 :
									damage = 0
									botdamage = 0
									healed = random.randint(0,8)
									print("bot deflected nothing")
									print ("you healed ",healed, " hp")
									user_hp = user_hp + healed
									if user_hp > 20 :
										user_hp = 20
									bot_hp = bot_hp - 0
									health_display (user_hp, bot_hp)
								else :
									print ("no use of heal")
									damage = 0
									botdamage = 0
									print ("bot deflected nothing")
									user_hp = user_hp - 0
									bot_hp = bot_hp - 0
									health_display (user_hp, bot_hp)
			elif bot == "heal" :
				print ("bot used heal")
				if user_hp < 20 :
					healed = healing()
					user_hp = user_hp + healed
					print("you healed ",healed," hp")
					if user_hp > 20 :
						user_hp = 20
				elif user_hp > 20 :
					print ("no use of healing")
				else : 
					healed = 0
				if bot_hp < 50 :
					healed1 = healing()
					bot_hp = bot_hp + healed1
					print("bot healed ",healed1," hp")
					if bot_hp > 50 :
						bot_hp = 50
				elif bot_hp > 50 :
					print ("no use of healing")
				else :
					healed1 = 0 
				if healed == 0 and healed1 == 0 :
					print("no use of healing for both")
				health_display(user_hp, bot_hp)				
if user_hp <= 0 :
	os.system ('cls')
	print("your hp :- 0")
	print ("game over ")
	print ("\n\n🥺🥺🥺you lost🥺🥺🥺")
else :
	os.system('cls')
	print("bot hp :- 0")
	print("\n\n🎉🎉🎉you won🎉🎉🎉")
	

									