#class defining players in baseball
#rating = elo based system to predict head to head outcomes
#contribution = rating system to predict contribution to team winning
#last_three_hundred_faced = last outcomes of ab only k,bb,hr,h considered, other outcomes considered irrelevant
#1 k = strikeouts, 2 bb = walks, 3 hr = homeruns, 4 h = hits
#these the three true outcomes plus hits are the things pitchers themselves really have control over
class Player:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.rating = 1200
        self.contribution = 0
        self.last_five_hundred = []


    #adjust last_five_hundred at_bats based on the new at_bat and adjust rating
    def at_bat(self,outcome,rating_change):
        if self.last_five_hundred.__len__() <= 500:
            self.last_five_hundred.append(outcome)
        else:
            self.last_five_hundred.pop(0)
            self.last_five_hundred.append(outcome)

        self.rating += rating_change

    #dividing the number of strikouts by the number of at bats gives the strikout precentage of the last 300 at_bats
    def strikout_precentage(self):
        return self.last_five_hundred.count(1)/self.last_five_hundred.__len__()

    #dividing the number of walks by the number of at bats gives the walk precentage of the last 300 at_bats
    def walk_precentage(self):
        return self.last_five_hundred.count(2)/self.last_five_hundred.__len__()

    #dividing the number of hits by the number of at bats gives the hit precentage of the last 300 at_bats
    def h_precentage(self):
        return self.last_five_hundred.count(3)/self.last_five_hundred.__len__()

    #dividing the number of hr by the number of at bats gives the hr precentage of the last 300 at_bats
    def hr_precentage(self):
        return self.last_five_hundred.count(4)/self.last_five_hundred.__len__()

    def k_recent_weighted(self):

        if self.last_five_hundred.__len__() > 100:
            last_500_perfromance = self.strikout_precentage()
            recent_perfromance = self.last_five_hundred[:100].count(1)/100
            weighted = (last_500_perfromance + recent_perfromance)/2
        else:
            weighted = 0

        return weighted



