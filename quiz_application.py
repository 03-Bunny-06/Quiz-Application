def quiz_application(name):
    score_li = []
    print(f'Hello {name}! Welcome to the Geopolitics Quiz.\n')

    #Q1
    question1 = 'Who won the America Elections in 2024?\n1. Kamala Harris\n2. Joe Biden\n3. Donald Trump\n4. Barak Obama '
    print(question1)
    answer1 = int(input('Select the options(1/2/3/4): '))
    if answer1 == 3:
        score_li.append('Correct')
    else:
        score_li.append('Wrong')

    #Q2
    question2 = 'Which country has the most permanent seats on the United Nations Security Council (UNSC)?\n1. France\n2. United States\n3. China\n4. All of the Above '
    print(question2)
    answer2 = int(input('Select the options(1/2/3/4): '))
    if answer2 == 4:
        score_li.append('Correct')
    else:
        score_li.append('Wrong')

    #Q3
    question3 = 'Which African country is currently the largest economy in the continent by GDP?\n3. South Africa\n2. Egypt\n3. Nigeria\n4. Kenya '
    print(question3)
    answer3 = int(input('Select the options(1/2/3/4): '))
    if answer3 == 3:
        score_li.append('Correct')
    else:
        score_li.append('Wrong')

    #Q4
    question4 = 'Which treaty was signed in 1991 to officially dissolve the Soviet Union?\n1. Yalta Agreement\n2. Belavezha Accords\n3. Warsaw Pact\n4. Paris Peace Accord '
    print(question4)
    answer4 = int(input('Select the options(1/2/3/4): '))
    if answer4 == 2:
        score_li.append('Correct')
    else:
        score_li.append('Wrong')

    #Q5
    question5 = 'Which country has the highest number of land borders with other countries?\n1. China\n2. Russia\n3. Brazil\n4. India '
    print(question5)
    answer5 = int(input('Select the options(1/2/3/4): '))
    if answer5 == 1:
        score_li.append('Correct')
    else:
        score_li.append('Wrong')

    #Q6
    question6 = 'Which country is known for being the largest producer of uranium in the world?\n1. Australia\n2. Kazakhstan\n3. Canada\n4. Russia '
    print(question6)
    answer6 = int(input('Select the options(1/2/3/4): '))
    if answer6 == 2:
        score_li.append('Correct')
    else:
        score_li.append('Wrong')

    #Q7
    question7 = 'Which region has been a long-standing point of conflict between India and Pakistan?\n1. Punjab\n2. Kashmir\n3. Rajasthan\n4. Himachal Pradesh '
    print(question7)
    answer7 = int(input('Select the options(1/2/3/4): '))
    if answer7 == 2:
        score_li.append('Correct')
    else:
        score_li.append('Wrong')

    #Q8
    question8 = 'What is the primary objective of the North Atlantic Treaty Organization (NATO)?\n1. Economic Collaboration\n2. Military Alliance and Collective Defense\n3. Space Exploration\n4. Environmental Conservation '
    print(question8)
    answer8 = int(input('Select the options(1/2/3/4): '))
    if answer8 == 2:
        score_li.append('Correct')
    else:
        score_li.append('Wrong')

    #Q9
    question9 = 'Which country was the first to withdraw from the European Union?\n1. Greece\n2. Italy\n3. United Kingdom\n4. Ireland '
    print(question9)
    answer9 = int(input('Select the options(1/2/3/4): '))
    if answer9 == 3:
        score_li.append('Correct')
    else:
        score_li.append('Wrong')
    
    #Q10
    question10 = 'What is the name of the agreement that ended World War I in 1919?\n1. Treaty of Versailles\n2. Treaty of Trianon\n3. Treaty of Brest-Litovsk\n4. Treaty of Ghent '
    print(question10)
    answer10 = int(input('Select the options(1/2/3/4): '))
    if answer10 == 1:
        score_li.append('Correct')
    else:
        score_li.append('Wrong')
    
    #Q11
    question11 = 'Which city serves as the headquarters of the International Criminal Court (ICC)?\n1. Geneva\n2. The Hague\n3. New York\n4. Brussels '
    print(question11)
    answer11 = int(input('Select the options(1/2/3/4): '))
    if answer11 == 2:
        score_li.append('Correct')
    else:
        score_li.append('Wrong')

    #Q12
    question12 = 'Which country has territorial claims over the Arctic due to its continental shelf?\n1. Norway\n2. Canada\n3. Russia\n4. All of the Above '
    print(question12)
    answer12 = int(input('Select the options(1/2/3/4): '))
    if answer12 == 4:
        score_li.append('Correct')
    else:
        score_li.append('Wrong')
    
    #Q13
    question13 = 'Which sea is at the center of territorial disputes involving China, Vietnam, the Philippines, and others?\n1. East China Sea\n2. South China Sea\n3. Yellow Sea\n4. Sea of Japan '
    print(question13)
    answer13 = int(input('Select the options(1/2/3/4): '))
    if answer13 == 2:
        score_li.append('Correct')
    else:
        score_li.append('Wrong')
    
    #Q14
    question14 = 'Which African nation recently joined the BRICS group in its expanded form?\n1. Algeria\n2. Egypt\n3. Ethiopia\n4. Kenya '
    print(question14)
    answer14 = int(input('Select the options(1/2/3/4): '))
    if answer14 == 3:
        score_li.append('Correct')
    else:
        score_li.append('Wrong')
    
    #Q15
    question15 = 'Which treaty established the European Union (EU) in its modern form?\n1. Maastricht Treaty\n2. Lisbon Treaty\n3. Rome Treaty\n4. Schengen Agreement '
    print(question15)
    answer15 = int(input('Select the options(1/2/3/4): '))
    if answer15 == 1:
        score_li.append('Correct')
    else:
        score_li.append('Wrong')
    
    score = score_li.count('Correct')
    print(f'{name} scored {score} points is the GeoPolitics Quiz.')
    print(f"{name}'s accuracy percentage would be {(score/15)*100:.2f}%")
    
name = input("Enter your name to start the Quiz: ")
quiz_application(name)

while True:
    play_again = input('\nDo you want to play again? (Yes/No): ').upper()
    if (play_again == 'YES'):
        name = input("Enter your name to start the Quiz: ")
        quiz_application(name)
    else:
        print('Thanks for playing. Have a great day!')
        break