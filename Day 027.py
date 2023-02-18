'''
Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game.
'''
import time
# game question ans in list
kbc = [
[ 'The International Literacy Day is observed on','A. Sep 8', 'B. Nov 28','C. May 2','D. Sep 22', 1],
[' The language of Lakshadweep. a Union Territory of India, is', 'A. Tamil', 'B. Hindi', 'C. Malayalam', 'D. Telugu',3],
['In which group of places the Kumbha Mela is held every twelve years?', 'A. Ujjain, Purl; Prayag. Haridwar', 'B. Prayag, Haridwar, Ujjain, Nasik','C. Rameshwaram, Purl, Badrinath, Dwarika', 'D. Chittakoot, Ujjain, Prayag, Haridwar', 2],
['Bahubali festival is related to', 'A. Islam', 'B. Hinduism', 'C. Buddhism', 'D. Jainism', 4],
['Which day is observed as the World Standards  Day?','A. June 26', 'B. Oct 14', 'C. Nov 15', 'D. Dec 2', 2],
['Which of the following was the theme of the World Red Cross and Red Crescent Day?', "A. 'Dignity for all - focus on women'","B. 'Dignity for all - focus on Children'","C. 'Focus on health for all","D. 'Nourishment for all-focus on children'", 2],
["September 27 is celebrated every year as","A. Teachers' Day","B. National Integration Day","C. World Tourism Day", "D. International Literacy Day",3 ],
["Who is the author of 'Manas Ka-Hans' ?","A. Khushwant Singh","B. Prem Chand", "C. Jayashankar Prasad", "D. Amrit Lal Nagar", 4 ],
["The death anniversary of which of the following leaders is observed as Martyrs' Day?","A. Smt. Indira Gandhi","B. PI. Jawaharlal Nehru","C. Mahatma Oandhi", "D. Lal Bahadur Shastri",3],
[" Who is the author of the epic 'Meghdoot'?","A. Vishakadatta","B. Valmiki", "C. Banabhatta", "D. Kalidas",4],
["'Good Friday' is observed to commemorate the event of","A. birth of Jesus Christ","B. birth of' St. Peter","C. crucification 'of Jesus Christ","D. rebirth of Jesus Christ",3],
["Who is the author of the book 'Amrit Ki Ore'?","A. Mukesh Kumar","B. Narendra Mohan","C. Upendra Nath","D. Nirad C. Choudhary",2],
["Which of the following is observed as Sports Day every year?","A. 22nd April", "B. 26th  july", "C. 29th August", "D. 2nd October",3],
[" World Health Day is observed on", "A. Apr 7", "B. Mar 6", "C.Mat I5", "D. Apr 28",1],
["Pongal is a popular festival of which state?", "A. Karnataka", "B. Kerala", "C. Tamil Nadu", "D. Andhra Pradesh",3],
[" Ghototkach in Mahabharat was the son of","A. Duryodhana", "B. Arjuna", "C. Yudhishthir", "D. Bhima", 4]
]

levels = ['1,000', '2,000', '3,000', '5,000', '10,000', '20,000', '40,000', '80,000', '1,60,000','3,20,000', '6,40,000', '12,50,000', '25,00,000', '50,00,000', '1 Crore', '7 Crores']
options=[['A','a','1'],['B','b','2'],['C','c','3'],['D','d','4']]

print("*"*50)
print()
print("  Kaun Banega Crorepati (KBC) Lite  ".center(50, '*'))
print()
print("*"*50)
prize_money= 0

for i in range(len(kbc)):
    print(f"\n\nQuestion for prize money {levels[i]} is on your screen : \n")
    print('Q: '+ kbc[i][0])
    print("Options:\n")
    print(kbc[i][1])
    print(kbc[i][2])
    print(kbc[i][3])
    print(kbc[i][4])
    ans = input("\nChoose options or to quit the game enter 0\nYour answer : ")
    if ans == '0':
        print('You quit the game...')
        time.sleep(2)
        break
    elif ans in options[kbc[i][5]-1]:
        print('\nSahi Jawab! You won ',levels[i] )
        prize_money=levels[i]
    else:
        print("\nWrong Answer!!!\n")
        time.sleep(3)
        break
    time.sleep(2)
print(f"Your won  {prize_money} rupees in total...")
print("\n\nThank you for playing this game")