# Adventure Game Tasha Fernandez-Ross
print("You are lost underground in a maze of tunnels.")
import random
dangerTunnel = random.randint(1, 2)
#print("Dragon in tunnel ", dangerTunnel) # Checking for logic errors
tunnelChoice = 0
while tunnelChoice < 1 or tunnelChoice > 2:
    tunnelChoice = int(input("Choose tunnel 1 or tunnel 2: "))
print("You chose tunnel ", tunnelChoice)
if tunnelChoice == dangerTunnel:
    print("You entered a tunnel with a dragon. Watch out.")
else:
    print("You entered an empty tunnel. You are safe for now.")
   

#COM203
#Parsons, J. J. (2018). New perspectives on computer concepts 2018, comprehensive (20th ed.). Cengage.
#Lab: Tunnels and Dragons
#If program goes into an endless loop, use Ctrl-C to stop it.
