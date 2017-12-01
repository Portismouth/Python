def score_grade():
    from random import randint
    random_num = 0

    for num in range(0, 10):
        random_num = randint(60, 100)

        if random_num >= 90:
            print "Score: "+str(random_num)+"; Your grade is A"
        elif random_num >= 80 and random_num < 90:
            print "Score: " + str(random_num) + "; Your grade is B"
        elif random_num >= 70 and random_num < 80:
            print "Score: " + str(random_num) + "; Your grade is C"
        elif random_num >= 60 and random_num < 70:
            print "Score: " + str(random_num) + "; Your grade is D"
    print "End of Program. Bye!"

score_grade()