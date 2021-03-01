txt="Leasee-Net Bonus | RiskLeaseholdInterestOutput.BonusPaymentsNLIaI, Leasee-PremBonus | RiskLeaseholdInterestOutput.BonusPaymentsPremium, Leasee-MonthlyImprovemnts | RiskLeaseholdInterestInput.ImprovementsAndBetterments, Leasee-NetImprovemnts | RiskLeaseholdInterestOutput.ImprovementsAndBettermentsNLIaILeasee-Improvements Prem |RiskLeaseholdInterestOutput.ImprovementsAndBettermentsPremium, Leasee-MonthlyPrePaid Rent | RiskLeaseholdInterestInput.PrepaidRent, Leasee-Net PrePaid Rent |RiskLeaseholdInterestOutput.PrepaidRentNLIaI, Leasee-PrePaid Rent Prem |RiskLeaseholdInterestOutput.PrepaidRentPremium, Leasee-Net Total |RiskLeaseholdInterestOutput.TotalCoveredLeaseholdInterestNLIaI, Leasee-Total Prem| RiskLeaseholdInterestOutput.TotalCoveredLeaseholdInterestPremium"
    

all=txt.split(",")
print(len(all))

for x in (all):
	print(x.split("|")[1])
    
    
