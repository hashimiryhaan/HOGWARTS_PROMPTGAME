import time
import pygame
import random
def intro():
    castle=r"""                                _
                /\                            / \
               /  \                          /   \
               |  |                         /_____\
              _|  |_    /\                   | - |
              | -- |   /__\                  | - |
              | -- |___|  |     /\____ /\____| - |________
              | -- |___\  |____/__\___/__\__/\ - |_______/_\
              |____|___|__|_()_|___||||__|__||___|_______|_|
              H O G W A R T S  S C H O O L  O F  W I T C H
              C R A F T  A N D  W I Z A R D D R Y
              """                                                    ## The 'r' before the quotes makes it a raw string so backslashes don't break the code
    print(castle)
    print('________________________________________________________________')
    time.sleep(3)
    print('                  WELCOME TO HOGWARTS           ')
    print('________________________________________________________________')
    time.sleep(3)
def role_name():
    print('='*80)   
    print('        LEVEL 1 : THE HERO\'S AWAKENING     ')  
    print('='*80)
    time.sleep(2)                                                                   #charcter selection
    print('Your magical journey is about to begin.')
    time.sleep(3)
    print('Are you a hero driven by loyalty? A brilliant mind seeking knowledge? Or perhaps... a shadowed soul hungry for power?')
    time.sleep(4)
    print("""The story is yours to write. Who are you?""")
    roles=['HARRY POTTER       - Impulsive and Protective',
           'HERMIONE GRANGER   - Intellectual and Brave ',
           'RON WEASLY         - Loyal and Humorous',
           'DRACO MALFOY       - Insecure and Ambitious',
           'NEVILLE LONGBOTTOM - Kind and Resilient']
    for i,role in enumerate(roles,1):
        print(f'{i}.{role}')
        time.sleep(1)
    while True:
     try:
      choice_num=int(input('Choose who you want to be : '))
      if 1<=choice_num<=len(roles):
            if choice_num==1:
             character='HARRY POTTER'
            elif choice_num==2:
             character='HERMIONE GRANGER'
            elif choice_num==3:
             character='RON WEASLY'
            elif choice_num==4:
             character='DRACO MALFOY'
            elif choice_num==5:
             character='NEVILLE LONGBOTTOM'
            return character
      else:
            print('invalid choice! please enter a valid number')
     except ValueError:
      print("Invalid input.please enter a number")
def intro_bgm():                                                           #play harry potter bgm
    pygame.mixer.init()
    pygame.mixer.music.load("harry_potter.mp3")
    pygame.mixer.music.play(-1)
def hogwarts_letter(character_name):
    print("Hey you got a letter from hogwarts")
    time.sleep(2)
    letter=f"""
            ===========================================================================================================
                                          HOGWARTS SCHOOL OF WITCHCRAFT and WIZARDRY

                                              From Headmaster Albus Dumbledore
            
                Dear {character_name} ,
                We are pleased to inform you that you have been accepted at HOGWARTS SCHOOL of WITCHCRAFT and WIZARDRY
            =============================================================================================================
                """
    print(letter)
    print(f'Congratulations on joining Hogwarts {character_name}  ...')
    time.sleep(3)
def ollivander_merch(character_name):
   print('='*80)
   print('           LEVEL 2 : THE WAND CHOOSES THE WIZARD           ')
   print('='*80)
   time.sleep(2)
   print(f'Every wizard needs a magic wand before going to the hogwarts\n')
   time.sleep(2)
   print('Lets go to the Ollivanders....\n' )
   time.sleep(3)
   print(f'"Ollivander : Ah, {character_name}... I wondered when I did be seeing you."\n "Every Ollivander wand has a core of a powerful magical substance. Which of these materials do you feel drawn to?"\n')
   time.sleep(4)
   print('1.Dragon Heartstring (Produces wands with the most power)\n')
   time.sleep(3)
   print('2.Phoenix Feather (Capable of the greatest range of magic)\n')
   time.sleep(3)
   print('3.Unicorn Hair (Produces the most consistent magic)\n')
   time.sleep(3)
   while True:
     try: 
          choice_num=int(input('Choose your wand : '))
          if choice_num==1:
            wand='Dragon Heartstring'
            print('"Dragon heartstring... a powerful choice. Wands with this core learn magic quicker than any other. Just be careful, they are prone to accidents if you lack focus. I expect you will cast some truly brilliant spells."\n')
            time.sleep(5)
            break
          elif choice_num==2:
            wand='Phoenix Feather'
            print('"Curious... very curious. Phoenix feathers are the rarest of all cores. They show the most initiative, sometimes acting of their own accord. A wand like this means you are destined to walk your own unique path."\n')
            time.sleep(5)
            break
          elif choice_num==3:
            wand='Unicorn Hair'
            print('"Ah, unicorn hair. You will find no wand more loyal or consistent. It is a core that is incredibly difficult to turn to the Dark Arts. Treat it well, and it will never fail you in a duel."\n')
            time.sleep(5)
            break
          else:
             print('Invalid Choice! please enter a valid number')
     except ValueError:
        print('Invalid Choice! please enter a number')
     print(f"""
            "The wand has chosen, {character_name}. Remember, we do not know what secrets the wand holds... but I think we can expect great things from you."
            """)
     time.sleep(5)
def sorting_hat(character_name):
   print('='*80)
   print('           LEVEL 3 : THE SORTING CEREMONY            ')
   print('='*80)
   time.sleep(2)
   print("\n" + "="*80)
   print('"The Great Hall\'s ceiling reflects a star-filled night sky."')
   time.sleep(3)
   print("Professor McGonagall places the Sorting Hat on your head...")
   time.sleep(3)
   print('It\'s time for the Sorting Ceremony.')
   time.sleep(3)
   print('Sorting Hat : "Hmm... difficult. Very difficult," whispers a voice in your ear.')
   time.sleep(3)
   # --- QUESTION 1 ---
   print(f"\nTell me, {character_name} what do you value most?")
   time.sleep(3)
   print("1. Bravery and standing up for what is right.")
   time.sleep(3)
   print("2. Knowledge and understanding the mysteries of magic.")
   time.sleep(3)
   print("3. Loyalty and working hard for my friends.")
   time.sleep(3)
   print("4. Ambition and achieving greatness at any cost.")
   while True:
      try:
         q=int(input(' : '))
         if q==1:
            house_name="GRYFFINDOR"
            print("You have fire in your heart... better be.. \n",house_name)
            break
         elif q==2:
            house_name="RAVENCLAW"
            print("A sharp mind, always questioning always learning. better be.. \n",house_name)
            break
         elif q==3:
            house_name="HUFFLEPUFF"
            print("A true and steadfast soul , your loyalty is unmatched. better be.. \n",house_name)
            break
         elif q==4:
            house_name="SLYTHERIN"
            print("Ah, a clever one. you aren't afraid to take the necessary steps to get it. better be.. \n",house_name)
            break
         else:
            print("OH DEAR! Please choose 1, 2, 3, or 4. ")
         time.sleep(3)
      except ValueError:
            print("Invalid input. Please enter a number.")
      time.sleep(5)
def climax(character_name):
   print('='*80)
   print('           LEVEL 4 - THE DARK LORD CHALLENGE         ')
   print('='*80)
   time.sleep(2)
   print("\n" + "="*80)
   print('You step through a mist-filled archway, the air instantly freezing around you.\nTombstones jut out of the ground like crooked teeth.')
   time.sleep(3)
   print('I have been waiting for you," a high, cold voice hisses from the shadows.')
   time.sleep(3)
   print("Lord Voldemort steps forward, twirling his yew wand. His red eyes lock onto yours.")
   time.sleep(3)
   print(f'"Let us see what kind of wizard you truly are, {character_name}!"')
   #health points
   player_hp=100
   voldemort_hp=100
   while player_hp>0 and voldemort_hp>0:
        print("\n" + "="*40)
        print(f"YOUR HP: {player_hp}  |  VOLDEMORT HP: {voldemort_hp}")
        print("="*40)
        print("\nChoose your spell:")
        print("1. Expelliarmus (Moderate Damage)")
        print("2. Reducto (High Damage, Chance to Miss)")
        print("3. Avada Kedavra (The Killing Curse)")
        time.sleep(4)
        try:
           spell=int(input('Cast Your Spell'))
           if spell==1:
              # random.randint(min, max) picks a random number between the two values
                damage = random.randint(10, 40)
                voldemort_hp -= damage
                print(f"\nYou cast EXPELLIARMUS! It hits Voldemort for {damage} damage!")
           elif spell==2:
                hit_chance = random.randint(1, 10)
                if hit_chance > 3:
                 damage=random.randint(40,60)
                 voldemort_hp-=damage
                 print(f"\nYou cast REDUCTO! A massive blast hits Voldemort for {damage} damage!")
                else:
                 print("\nYou cast REDUCTO... but Voldemort deflects it! (Missed!)")
                 player_hp-=random.randint(40,60)
                 break
           elif spell==3:
              kill_chance=random.randint(1,100)
              if kill_chance>=15:
                 print("\nYou roar 'AVADA KEDAVRA!' A blinding flash of green light erupts from your wand.")
                 print("It strikes Voldemort square in the chest!")
                 voldemort_hp = 0 # Instant kill!
              else:
                    print("\nYou shout 'AVADA KEDAVRA!'... but only a few green sparks shoot out.")
                    print('Voldemort laughs. "You have to mean it, fool!"')
                    player_hp=0
                    break
           else:
                print("Invalid choice! You stumble and miss your turn!")
                
        except ValueError:
            print("Invalid input! You drop your wand in a panic!")
            continue 
        time.sleep(2)
   if player_hp>0:
           print('YOU WIN! You have saved the wizarding world! ==========================')
   else:
           print('Your shield shatters, and you are thrown backward.As your vision fades to black, Voldemort steps over you, victorious.The wizarding world falls into shadow...')
           time.sleep(3)
           print('Don\'t give up. The timeline can be rewritten. *** GAME OVER ***')
def main():
    while True:
     intro_bgm()
     intro()
     character_name=role_name()
     print(f'Welcome {character_name} ...')
     hogwarts_letter(character_name)
     time.sleep(8)
     ollivander_merch(character_name)
     sorting_hat(character_name)
     climax(character_name)
     # --- THE REPLAY CHECK ---
     print("\n" + "="*80)
     print("Would you like to play again? (Y/N)")
     # .lower().strip() handles it if they type 'y', 'Y', ' yes ', etc.
     play_again = input("> ").lower().strip()
     if play_again == 'y' or play_again == 'yes':
      print("\nResetting the timeline...\n")
      time.sleep(2)
     else:
        print("\nThank you for playing! Mischief Managed.")
        break
if __name__ == "__main__":
    main()
 
