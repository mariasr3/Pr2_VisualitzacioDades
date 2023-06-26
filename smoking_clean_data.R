

income <- read.csv("/Users/mariasopenar/Documents/INCOME.csv")
income
income <- read.csv2("/Users/mariasopenar/Documents/INCOME.csv")
income
smoking <- read.csv2("/Users/mariasopenar/Documents/smoking.csv")

# PRÀCTICA 2. Processament de dades 

library(dplyr)

#llegeix el dataset complet 
all <- read.csv("/Users/mariasopenar/Downloads/all.csv")

# extreu informació d'Alemanya 
germany <- all[all$geo == "Germany",]
germany <- all[all$geo == "Germany",]

# informació estratidicada per edat i 2014 vs 2019
germany_age <- germany %>% filter(smoking == "Current smoker", sex=="Total")
age_germany <- germany_age %>% dplyr::select(age, value, time)

#guarda el dataset pel dotplot
write.csv(age_germany, "/Users/mariasopenar/Documents/age_germany.csv")

#informació de fumadors joves (15-19 anys per edat)
young <- all %>% filter(X_age == "Y15-19", smoking == "Current smoker", sex == "Total", quant_inc == "Total") %>% select(time, geo, sex, value)
write.csv(young, "/Users/mariasopenar/Documents/young.csv")

#separa la info per any (2019 vs 2014)
young_2019 <- all %>% filter(X_age == "Y15-19", smoking == "Current smoker", sex == "Total", quant_inc == "Total", time== "2019") %>% select(time, geo, sex, value)
young_2014 <-  all %>% filter(X_age == "Y15-19", smoking == "Current smoker", sex == "Total", quant_inc == "Total", time== "2014") %>% select(time, geo, sex, value)
write.csv(young_2019, "/Users/mariasopenar/Documents/young_2019.csv")
write.csv(young_2014, "/Users/mariasopenar/Documents/young_2014.csv")


# Llegeix dataset amb informació dels ingressos 
all_income <- read.csv2("/Users/mariasopenar/Documents/income.csv")
#filtra dades de fumadors per alemanya i grup d'edat joves
income_germany <-  all_income %>% dplyr::filter(geo == "Germany", X_age == "Y15-19", smoking == "Current smoker", sex== "Total")
write.csv(income_germany[income_germany$time == 2014,], "/Users/mariasopenar/Documents/income_germany_2014.csv")
write.csv(income_germany[income_germany$time == 2019,], "/Users/mariasopenar/Documents/income_germany_2019.csv")

# el mateix per sex
sex <-  all_income %>% dplyr::filter(geo == "Germany", X_age == "Y15-19", smoking == "Current smoker", quant_inc == "Total")
write.csv(sex[sex$time == 2019,], "/Users/mariasopenar/Documents/sex_germany_2019.csv")
write.csv(sex[sex$time == 2014,], "/Users/mariasopenar/Documents/sex_germany_2014.csv")

# Llegeix dataset amb informació d'urbanització 
all_urbanization <- read.csv("/Users/mariasopenar/Documents/urbanization.csv", sep = ";")
urbanization_germany <-  all_urbanization  %>% dplyr::filter(geo == "Germany", X_age == "Y15-19", smoking == "Current smoker", sex== "Total")
write.csv(urbanization_germany[urbanization_germany$time == 2014,], "/Users/mariasopenar/Documents/urbanization_germany_2014.csv")
write.csv(urbanization_germany[urbanization_germany$time == 2019,], "/Users/mariasopenar/Documents/urbanization_germany_2019.csv")

# Llegeix dataset amb informació de nivell educatiu  
all_education <- read.csv2("/Users/mariasopenar/Documents/education.csv")
education_germany <-  all_education  %>% dplyr::filter(geo == "Germany", X_age == "Y15-19", smoking == "Current smoker", sex== "Total")
write.csv(education_germany[education_germany$time == 2014,], "/Users/mariasopenar/Documents/education_germany_2014.csv")
write.csv(education_germany[education_germany$time == 2019,], "/Users/mariasopenar/Documents/education_germany_2019.csv")


young <- all %>% filter(geo == "Germany", X_age == "Y15-19", smoking == "Current smoker", sex != "total")
