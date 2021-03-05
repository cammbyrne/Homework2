def BMICalc(weight,heightF,heightI):
    height = (heightF*12) + heightI
    meters = height * .025
    kilograms = weight * .45
    m = meters*meters
    BMI = kilograms/m
    BMI = round(BMI,1)

    if (BMI < 18.5):
        weightPlacement = "Underweight"
        return BMI, weightPlacement
    elif (BMI >= 18.5 and BMI < 29.9):
        weightPlacement = "Average Weight"
        return BMI, weightPlacement
    else:
        weightPlacement = "Overweight"
        return BMI, weightPlacement

