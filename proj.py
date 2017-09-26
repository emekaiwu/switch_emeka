def findside(side_unknown,knownsideA,knownsideB):
    unknown_side =""
    side_unknown = input('please enter the side u want to find "hyp" or "adj" or "opp"')
    side_list=["hyp","adj","opp"]
    if side_unknown in side_list:
        if side_unknown=="hyp":
           unknown_side= (knownsideC**2 + knownsideA**2)**0.5
        elif side_unknown=="opp":
          unknown_side= (knownsideC**2 - knownsideB**2)**0.5
        elif side_unknown=="adj":
          unknown_side= (knownsideA**2 - knownsideB**2)**0.5
        print ("The unknown side is",unknown_side)
        return unknown_side
findside("adj",12,9)

