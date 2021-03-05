def retirementCalc(age, salary, percentsaved, savingsgoal):
    spy = (salary * percentsaved) *1.35
    ytg = savingsgoal/spy
    agemet = age + ytg
    agemet = round(agemet,0)
    if (agemet <= 99):
        dead = False
        return agemet, dead
    else:
        dead = True
        return agemet, dead
