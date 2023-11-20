# LAMATA BRT  BUS
import time

bus = [] 
stand_queue = ['Mr Paul', 'Miss Jane', 'John'] # List of people on standing queue
sit_queue = ['Pa Okonkwo', 'Bode', 'Sister Jennifer', 'Usman', 'Emeka', 'Zainab', 'Joshua', 'Ilerika', 'Ekukeu', 'Prof. Johnson', 'Iyalode', 'Rish kid', 'Alagba']  # List of people on sitting queue
balance = {}   # Dictionary to store balance of money on cowry card

# Board Bus function
def board(person):
    fare = 250
    if person in balance:
        time.sleep(3)
        print("\n\n>>>Ikorodu Terminal (Ikorodu - Oshodi)<<<")
        if stand_queue.count(person) > 0:
            if balance[person] >= fare:
                balance[person] -= fare
                bus.append(person) 
            elif balance[person] <= fare:
                time.sleep(2)
                print(f"\n\n--{person}, sorry you cannot board this bus.")
                time.sleep(1)
                print("\n--You no get money for ya card!")
                cowrycard_topup(balance, person)

        else:
            print("\nBRT bus no dey, go enter danfo.")
        
        
def cowrycard_topup(balance, person):
    print("\n>>> Top-up ya card!! We no dey collect waso ooh!")
    
    try:
        while True:
            price = int(input("How much do you want to buy into your card? ₦"))
            if price % 100 != 50 and price > 0:
                print(f"\n>>You have successfully loaded ₦{price} into your card 💰")
                balance[person] += price
                break
          
            else:
                print(f"\nI say we no dey collect waso. I no fit type {price}")
                continue
            
    except ValueError:
        print("\nAbeg no waste my time ooh! Wetin you wan do for here sef? 😒")       


def queue(person):       
    print("\n1. Standing queue: ", len(stand_queue), 'people', '| Waiting time: ', len(stand_queue), 'seconds''⏳')
    print("2. Sitting queue: ", len(sit_queue), 'people', '| Waiting time: ', len(sit_queue), 'seconds''⏳')
    while True:
        choice = input("\nSelect queue number to join (1/2): ")
        if choice == '1':
            print("\nStanding queue joined.", "(Queued behind", stand_queue[-1],")")
            break
        elif choice == '2':
            print("\nSitting queue joined.", "(Queued behind", sit_queue[-1],')')
            break
        else:
            print("\nYou no wan enter queue? No chance me ooh!!")
            continue
def entering(person):   #
    while True:
        choice = input("Standing or Sitting (1/2): ")
        if  choice == '1':
            print("\nSeats full! Enter in with your Cowry cards to stand in bus. 💳")
            time.sleep(len(stand_queue))
            print(f"{person} tap in your card to enter. 💳")
            print(balance[person])
            break
        elif choice == '2':
            print("\nBus well parked! Enter in with your Cowry cards to seat in bus. 💳")
            time.sleep(len(sit_queue))
            print(f"\n{person} tap-in your card to enter. 💳")
            print("Balance: ₦", balance[person])
            break
        else:
            print("\nYou no go enter bus. Comot for road, make i enter jare..")
            continue

def bus_moving():
    print("...🚌 The bus in on the move...")
    time.sleep(10)
    print("Mile 12 wa ooh! ")
    print("(brakes screech) 🚌 The bus stopped. 🛑")
    print("On bole ooh!")
    time.sleep(7)
    print("\n ...🚌 The bus in on the move...🛣️")
    print('\n Ojota wa ooh! On bole ooh...')
    time.sleep(4)
    print('\n ...🚌 The bus in on the move...')
    print('\n Driver!! Maryland wa ooh...')
    time.sleep(5)
    print("\n ...🚌 The bus in on the move...")
    print("\n ...........Arrived at final destination............")
    print('All passengers, please alight gently from the bus')
    time.sleep(3)

def replay():
    ask = input("Do you wan to play again? y/n").lower()
    if ask == 'y':
        login(person)
    else:
        print("\nSee ya 👋🏼")
        
def login(person):
        while True:
            print("\n1. Join queue")
            print("2. Check balance")
            print("3. Top-up your card")
            print("4. Quit")
    
            opera = input("Select Action (1/2/3/4): ")
            if opera == '1':
                queue(person)
                entering(person)
                if board(person):
                    bus_moving()
                    break
            elif opera == '2':
                print(balance[person])
                continue
            elif opera == '3':
                cowrycard_topup(balance, person)
                continue
            elif opera == '4':
                print("Come back anytime.\nExiting application.....")
                break
            else:
                print("Invalid choice! choose again.")
                continue

        
def main():
    print("\nBRT Boarding Transport Simulator 🚍")
    person = input("Enter name to start: ")
    time.sleep(2)
    if person not in balance:
        balance[person] = 0
    while True:
        print("\n1. Join queue")
        print("2. Check balance")
        print("3. Top-up your card")
        print("4. Quit")
        opera = input("Select Action (1/2/3/4): ")
        if opera == '1':
            queue(person)
            if board(person):
                if entering(person):
                    bus_moving()
                    replay()
            break
        elif opera == '2':
            print(balance[person])
        elif opera == '3':
            cowrycard_topup(balance, person)
            continue
        elif opera == '4':
            print("Come back anytime.\nExiting application.....")
            break
        else:
            print("Invalid choice! choose again.")
            continue
        


# Execution of main function
if __name__ == '__main__':
    main()
# %%
