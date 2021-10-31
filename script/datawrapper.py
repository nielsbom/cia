import re
import os

dw_list = {
    "Afghanistan": "Afghanistan",
    "Albania": "Albania",
    "Algeria": "Algeria",
    "Andorra": "Andorra",
    "Angola": "Angola",
    "Antigua and Barbuda": "Antigua-and-Barbuda",
    "Arab Republic of Egypt": "Egypt",
    "Argentina": "Argentina",
    "Armenia": "Armenia",
    "Australia": "Australia",
    "Austria": "Austria",
    "Azerbaijan": "Azerbaijan",
    "Bahrain": "Bahrain",
    "Bangladesh": "Bangladesh",
    "Barbados": "Barbados",
    "Belarus": "Belarus",
    "Belgium": "Belgium",
    "Belize": "Belize",
    "Benin": "Benin",
    "Bhutan": "Bhutan",
    "Bolivia": "Bolivia",
    "Bosnia and Herzegovina": "Bosnia-and-Herzegovina",
    "Botswana": "Botswana",
    "Brazil": "Brazil",
    "Brunei Darussalam": "Brunei",
    "Bulgaria": "Bulgaria",
    "Burkina Faso": "Burkina-Faso",
    "Burundi": "Burundi",
    "Cambodia": "Cambodia",
    "Cameroon": "Cameroon",
    "Canada": "Canada",
    "Cape Verde": "Cabo-Verde",
    "Central African Republic": "Central-African-Republic",
    "Chad": "Chad",
    "Chile": "Chile",
    "China": "China",
    "Colombia": "Colombia",
    "Comoros": "Comoros",
    "Congo": "Congo-Republic-of-the",
    "Costa Rica": "Costa-Rica",
    "Côte d'Ivoire": "Cote-d'Ivoire",
    "Croatia": "Croatia",
    "Cuba": "Cuba",
    "Cyprus": "Cyprus",
    "Czech Republic": "Czechia",
    "D. P. R. of Korea": "Korea-North",
    "Democratic Republic of Congo": "Congo-Democratic-Republic-of-the",
    "Denmark": "Denmark",
    "Djibouti": "Djibouti",
    "Dominica": "Dominica",
    "Dominican Republic": "Dominican-Republic",
    "Ecuador": "Ecuador",
    "El Salvador": "El-Salvador",
    "Equatorial Guinea": "Equatorial-Guinea",
    "Eritrea": "Eritrea",
    "Estonia": "Estonia",
    "Eswatini": "Eswatini",
    "Ethiopia": "Ethiopia",
    "Federated States of Micronesia": "Micronesia-Federated-States-of",
    "Fiji": "Fiji",
    "Finland": "Finland",
    "France": "France",
    "Gabon": "Gabon",
    "Georgia": "Georgia",
    "Germany": "Germany",
    "Ghana": "Ghana",
    "Greece": "Greece",
    "Greenland (Den.)": "Greenland",
    "Grenada": "Grenada",
    "Guatemala": "Guatemala",
    "Guinea": "Guinea",
    "Guinea-Bissau": "Guinea-Bissau",
    "Guyana": "Guyana",
    "Haiti": "Haiti",
    "Honduras": "Honduras",
    "Hong Kong, SAR": "Hong-Kong",
    "Hungary": "Hungary",
    "Iceland": "Iceland",
    "India": "India",
    "Indonesia": "Indonesia",
    "Iraq": "Iraq",
    "Ireland": "Ireland",
    "Islamic Republic of Iran": "Iran",
    "Israel": "Israel",
    "Italy": "Italy",
    "Jamaica": "Jamaica",
    "Japan": "Japan",
    "Jordan": "Jordan",
    "Kazakhstan": "Kazakhstan",
    "Kenya": "Kenya",
    "Kiribati": "Kiribati",
    "Kosovo": "Kosovo",
    "Kuwait": "Kuwait",
    "Kyrgyz Republic": "Kyrgyzstan",
    "Lao People's Democratic Republic": "Laos",
    "Latvia": "Latvia",
    "Lebanon": "Lebanon",
    "Lesotho": "Lesotho",
    "Liberia": "Liberia",
    "Libya": "Libya",
    "Liechtenstein": "Liechtenstein",
    "Lithuania": "Lithuania",
    "Luxembourg": "Luxembourg",
    "Macau, SAR": "Macau",
    "Madagascar": "Madagascar",
    "Malawi": "Malawi",
    "Malaysia": "Malaysia",
    "Maldives": "Maldives",
    "Mali": "Mali",
    "Malta": "Malta",
    "Marshall Islands": "Marshall-Islands",
    "Mauritania": "Mauritania",
    "Mauritius": "Mauritius",
    "Mexico": "Mexico",
    "Moldova": "Moldova",
    "Monaco": "Monaco",
    "Mongolia": "Mongolia",
    "Montenegro": "Montenegro",
    "Morocco": "Morocco",
    "Mozambique": "Mozambique",
    "Myanmar": "Burma",
    "Namibia": "Namibia",
    "Nauru": "Nauru",
    "Nepal": "Nepal",
    "Netherlands": "Netherlands",
    "New Zealand": "New-Zealand",
    "Nicaragua": "Nicaragua",
    "Niger": "Niger",
    "Nigeria": "Nigeria",
    "North Macedonia": "North-Macedonia",
    "Norway": "Norway",
    "Oman": "Oman",
    "Pakistan": "Pakistan",
    "Palau": "Palau",
    "Panama": "Panama",
    "Papua New Guinea": "Papua-New-Guinea",
    "Paraguay": "Paraguay",
    "Peru": "Peru",
    "Philippines": "Philippines",
    "Poland": "Poland",
    "Portugal": "Portugal",
    "Qatar": "Qatar",
    "R. B. de Venezuela": "Venezuela",
    "Republic of Korea": "Korea-South",
    "Republic of Yemen": "Yemen",
    "Romania": "Romania",
    "Russian Federation": "Russia",
    "Rwanda": "Rwanda",
    "Saint Kitts and Nevis": "Saint-Kitts-and-Nevis",
    "Saint Lucia": "Saint-Lucia",
    "Saint Vincent and the Grenadines": "Saint-Vincent-and-the-Grenadines",
    "Samoa": "Samoa",
    "San Marino": "San-Marino",
    "São Tomé and Príncipe": "Sao-Tome-and-Principe",
    "Saudi Arabia": "Saudi-Arabia",
    "Senegal": "Senegal",
    "Serbia": "Serbia",
    "Seychelles": "Seychelles",
    "Sierra Leone": "Sierra-Leone",
    "Singapore": "Singapore",
    "Slovak Republic": "Slovakia",
    "Slovenia": "Slovenia",
    "Solomon Islands": "Solomon-Islands",
    "Somalia": "Somalia",
    "South Africa": "South-Africa",
    "South Sudan": "South-Sudan",
    "Spain": "Spain",
    "Sri Lanka": "Sri-Lanka",
    "Sudan": "Sudan",
    "Suriname": "Suriname",
    "Sweden": "Sweden",
    "Switzerland": "Switzerland",
    "Syrian Arab Republic": "Syria",
    "Taiwan": "Taiwan",
    "Tajikistan": "Tajikistan",
    "Tanzania": "Tanzania",
    "Thailand": "Thailand",
    "The Bahamas": "Bahamas-The",
    "The Gambia": "Gambia-The",
    "Timor-Leste": "Timor-Leste",
    "Togo": "Togo",
    "Tonga": "Tonga",
    "Trinidad and Tobago": "Trinidad-and-Tobago",
    "Tunisia": "Tunisia",
    "Turkey": "Turkey",
    "Turkmenistan": "Turkmenistan",
    "Tuvalu": "Tuvalu",
    "Uganda": "Uganda",
    "Ukraine": "Ukraine",
    "United Arab Emirates": "United-Arab-Emirates",
    "United Kingdom": "United-Kingdom",
    "United States of America": "United-States",
    "Uruguay": "Uruguay",
    "Uzbekistan": "Uzbekistan",
    "Vanuatu": "Vanuatu",
    "Vietnam": "Vietnam",
    "West Bank and Gaza": "West-Bank",
    "Western Sahara": "Mauritania",
    "Zambia": "Zambia",
    "Zimbabwe": "Zimbabwe",
}

for i in (os.listdir("../datawrapper/")):
    f = open(f"../datawrapper/{i}", "r").read()

    for key, value in dw_list.items():
        f = f.replace(value, key)

    n = open(f"../datawrapper/{i}", "w")
    n.write(f)