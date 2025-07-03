#A program that maps country codes to the country
#Prompt a user to input a country then we provide them the country the country_code.

country_dict = {
    'Uganda':'+256', 
    'Kenya' :'+254',
    'Burundi':'+257',
    'Tanzania':'+255',
    'RWANDA' :'+250',
    'USA'    : ['+1','+2'],
    'UK'     :'+44',
    'UAE'   :'+971', 
    'EGYPT' :'+20'

}
while True:
    country = input("Type Country in Upper Case: ")
    if country.isupper():
        print(f"The Code for {country} is {country_dict.get(country,'Not Provided')}")
        break
    else:
        print("Type in uppercase only")