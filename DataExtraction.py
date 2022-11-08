#!/usr/bin/env python
from selenium.webdriver import Chrome, Safari, Edge, Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
from jinja2 import Environment, FileSystemLoader
# from google_trans_new import google_translator
# from deep_translator import GoogleTranslator
import googletrans
import hashlib
from datetime import datetime

# driver path setup
driver_path = 'Selenium\geckodriver.exe'
browser = Firefox(executable_path=driver_path)

# read dataset
data = pd.read_csv("compoundCID.csv")
unique_data = pd.DataFrame(data['CID'].unique())
# print(len(unique_data))

compound_base_url = "https://pubchem.ncbi.nlm.nih.gov/compound"

# properties = []
property = {}


def chemical_physical_properties1(soup):
    w = soup.find(id="Computed-Properties").find_all('tr')

    for i in range(1, len(w)):
        current_w = w[i].find_all('td')
        if current_w[0].text == "Molecular Weight":
            property['molecular_weight'] = current_w[1].text
        if current_w[0].text == "XLogP3" or current_w[0].text == "XLogP3_AA":
            property['XLogP3_AA'] = current_w[1].text
        if current_w[0].text == "Hydrogen Bond Donor Count":
            property['Hydrogen_Bond_Donor_Count'] = current_w[1].text
        if current_w[0].text == "Hydrogen Bond Acceptor Count":
            property['Hydrogen_Bond_Acceptor_Count'] = current_w[1].text
        if current_w[0].text == "Rotatable Bond Count":
            property['Rotatable_Bond_Count'] = current_w[1].text
        if current_w[0].text == "Exact Mass":
            property['Exact_Mass'] = current_w[1].text
        if current_w[0].text == "Monoisotopic Mass":
            property['Monoisotopic_Mass'] = current_w[1].text
        if current_w[0].text == "Topological Polar Surface Area":
            property['Topological_Polar_Surface_Area'] = current_w[1].text
        if current_w[0].text == "Heavy Atom Count":
            property['Heavy_Atom_Count'] = current_w[1].text
        if current_w[0].text == "Formal Charge":
            property['Formal_Charge'] = current_w[1].text
        if current_w[0].text == "Complexity":
            property['Complexity'] = current_w[1].text
        if current_w[0].text == "Isotope Atom Count":
            property['Isotope_Atom_Count'] = current_w[1].text
        if current_w[0].text == "Defined Atom Stereocenter Count":
            property['Defined_Atom_Stereocenter_Count'] = current_w[1].text
        if current_w[0].text == "Undefined Atom Stereocenter Count":
            property['Undefined_Atom_Stereocenter_Count'] = current_w[1].text
        if current_w[0].text == "Defined Bond Stereocenter Count":
            property['Defined_Bond_Stereocenter_Count'] = current_w[1].text
        if current_w[0].text == "Undefined Bond Stereocenter Count":
            property['Undefined_Bond_Stereocenter_Count'] = current_w[1].text
        if current_w[0].text == "Covalently-Bonded Unit Count":
            property['Covalently_Bonded_Unit_Count'] = current_w[1].text


def remove_curly_index(text):
    open_curly = text.find("(")
    if open_curly < 0:
        return text
    text = text[0:open_curly]
    return text


def chemical_physical_properties2():
    # print(sections[31].find_all('p'))
    if soup.find(id="Color-Form"):
        property['Color'] = soup.find(
            id="Color-Form").find_all('div')[5].find('p').text
    else:
        property['Color'] = "not known"

    # Odor
    if soup.find(id="Odor"):
        property['Odor'] = soup.find(id="Odor").find_all('div')[
            5].find('p').text
    else:
        property['Odor'] = "not known"

    # Taste
    if soup.find(id="Taste"):
        property['Taste'] = remove_curly_index(
            soup.find(id="Taste").find_all('div')[5].find('p').text)
    else:
        property['Taste'] = "not known"

    # Boiling Point
    if soup.find(id="Boiling-Point"):
        property['Boiling_Point'] = remove_curly_index(
            soup.find(id="Boiling-Point").find_all('div')[5].find('p').text)
    else:
        property['Boiling_Point'] = "not known"

    # Melting Point
    if soup.find(id="Melting-Point"):
        property['Melting_Point'] = remove_curly_index(
            soup.find(id="Melting-Point").find_all('div')[5].find('p').text)
    else:
        property['Melting_Point'] = "not known"

    # Flash Point
    if soup.find(id="Flash-Point"):
        property['Flash_Point'] = remove_curly_index(
            soup.find(id="Flash-Point").find_all('div')[5].find('p').text)
    else:
        property['Flash_Point'] = "not known"

    # Solubility
    if soup.find(id="Solubility"):
        property['Solubility'] = remove_curly_index(
            soup.find(id="Solubility").find_all('div')[5].find('p').text)
    else:
        property['Solubility'] = "not known"

    # Density
    if soup.find(id="Density"):
        property['Density'] = remove_curly_index(
            soup.find(id="Density").find_all('div')[5].find('p').text)
    else:
        property['Density'] = "not known"

    # Vapor Density
    if soup.find(id="Vapor-Density"):
        property['Vapor_Density'] = remove_curly_index(
            soup.find(id="Vapor-Density").find_all('div')[5].find('p').text)
    else:
        property['Vapor_Density'] = "not known"

    # Vapor Pressure
    if soup.find(id="Vapor-Pressure"):
        property['Vapor_Pressure'] = remove_curly_index(
            soup.find(id="Vapor-Pressure").find_all('div')[5].find('p').text)
    else:
        property['Vapor_Pressure'] = "not known"

    # LogP
    if soup.find(id="LogP"):
        property['LogP'] = remove_curly_index(
            soup.find(id="LogP").find_all('div')[5].find('p').text)
    else:
        property['LogP'] = "not known"

    # LogS
    if soup.find(id="LogS"):
        property['LogS'] = remove_curly_index(
            soup.find(id="LogS").find_all('div')[5].find('p').text)
    else:
        property['LogS'] = "not known"

    # LogKoa
    if soup.find(id="LogKoa"):
        property['LogKoa'] = remove_curly_index(
            soup.find(id="LogKoa").find_all('div')[5].find('p').text)
    else:
        property['LogKoa'] = "not known"

    # Henrys Law Constant
    if soup.find(id="Henry's-Law-Constant"):
        temp = remove_curly_index(
            soup.find(id="Henry's-Law-Constant").find_all('div')[5].find('p').text)
        if temp[0] == 'H':
            temp = temp[23:len(temp)]
        property['Henrys_Law_Constant'] = temp
    else:
        property['Henrys_Law_Constant'] = "not known"

    # Atmospheric OH Rate Constant
    if soup.find(id="Atmospheric-OH-Rate-Constant"):
        property['Atmospheric_OH_Rate_Constant'] = remove_curly_index(
            soup.find(id="Atmospheric-OH-Rate-Constant").find_all('div')[5].find('p').text)
    else:
        property['Atmospheric_OH_Rate_Constant'] = "not known"

    # Stability/Shelf Life
    if soup.find(id="Stability-Shelf-Life"):
        property['Stability'] = remove_curly_index(
            soup.find(id="Stability-Shelf-Life").find_all('div')[5].find('p').text)
    else:
        property['Stability'] = "not known"

    # Autoignition Temperature
    if soup.find(id="Autoignition-Temperature"):
        property['Autoignition_Temperature'] = remove_curly_index(
            soup.find(id="Autoignition-Temperature").find_all('div')[5].find('p').text)
    else:
        property['Autoignition_Temperature'] = "not known"

    # Decomposition
    if soup.find(id="Decomposition"):
        property['Decomposition'] = remove_curly_index(
            soup.find(id="Decomposition").find_all('div')[5].find('p').text)
    else:
        property['Decomposition'] = "not known"

    # Viscosity
    if soup.find(id="Viscosity"):
        property['Viscosity'] = remove_curly_index(
            soup.find(id="Viscosity").find_all('div')[5].find('p').text)
    else:
        property['Viscosity'] = "not known"

    # Corresivity
    if soup.find(id="Corrosivity"):
        property['Corrosivity'] = remove_curly_index(
            soup.find(id="Corrosivity").find_all('div')[5].find('p').text)
    else:
        property['Corrosivity'] = "not known"

    # Heat of Combustion
    if soup.find(id="Heat-of-Combustion"):
        property['Heat_of_Combustion'] = remove_curly_index(
            soup.find(id="Heat-of-Combustion").find_all('div')[5].find('p').text)
    else:
        property['Heat_of_Combustion'] = "not known"

    # Heat of Vaporization
    if soup.find(id="Heat-of-Vaporization"):
        property['Heat_of_Vaporization'] = remove_curly_index(
            soup.find(id="Heat-of-Vaporization").find_all('div')[5].find('p').text)
    else:
        property['Heat_of_Vaporization'] = "not known"

    # pH
    if soup.find(id="pH"):
        property['pH'] = remove_curly_index(
            soup.find(id="pH").find_all('div')[5].find('p').text)
    else:
        property['pH'] = "not known"

    # Surface Tension
    if soup.find(id="Surface-Tension"):
        property[' Surface_Tension'] = remove_curly_index(
            soup.find(id="Surface-Tension").find_all('div')[5].find('p').text)
    else:
        property[' Surface_Tension'] = "not known"

    # Ionization Potential
    if soup.find(id="Ionization-Potential"):
        property['Ionization_Potential'] = remove_curly_index(
            soup.find(id="Ionization-Potential").find_all('div')[5].find('p').text)
    else:
        property['Ionization_Potential'] = "not known"

    # Polymerization
    if soup.find(id="Polymerization"):
        property['Polymerization'] = remove_curly_index(
            soup.find(id="Polymerization").find_all('div')[5].find('p').text)
    else:
        property['Polymerization'] = "not known"

    # Odor Threshold
    if soup.find(id="Odor-Threshold"):
        if len(soup.find(id="Odor-Threshold").find_all('div')[5].find_all('p')) == 1:
            property['Odor_Threshold'] = remove_curly_index(
                soup.find(id="Odor-Threshold").find_all('div')[5].find('p').text)
        else:
            low = remove_curly_index(
                soup.find(id="Odor-Threshold").find_all('div')[5].find_all('p')[0].text)
            low = low[19:len(low)]
            property['Odor_Threshold_min'] = low
            high = remove_curly_index(
                soup.find(id="Odor-Threshold").find_all('div')[5].find_all('p')[1].text)
            high = high[20:len(high)]
            property['Odor_Threshold_max'] = high
    else:
        property['Odor_Threshold_min'] = "not known"
        property['Odor_Threshold_max'] = "not known"

    # Refractive Index
    if soup.find(id="Refractive-Index"):
        ref_index = soup.find(
            id="Refractive-Index").find_all('div')[5].find('p').text
        ref_index = ref_index[21:len(ref_index)]
        property['Refractive_Index'] = remove_curly_index(ref_index)
    else:
        property['Refractive_Index'] = "not known"


# template setup
file_loader = FileSystemLoader('templates')  # laod the directory
env = Environment(loader=file_loader)        # laod the invironment
template = env.get_template('test.j2')   # get the file


for i in range(10197, 10200):
    # setup for web scrapping
    print("{}. cid of the compound : {} ".format(i+1, unique_data[0][i]))
    link = f"{compound_base_url}/{unique_data[0][i]}"
    property['cid'] = unique_data[0][i]
    browser.get(link)
    browser.implicitly_wait(80)
    time.sleep(8)
    soup = BeautifulSoup(browser.page_source, 'lxml')

    # compound name
    property['name'] = soup.find('h1').text

    table = soup.find_all('table')
    t = table[0].find_all('tr')

    # molecular formula
    molecular_formula = soup.find(
        id="Molecular-Formula").find_all('div')[5].find('p').text
    property['molecular_formula'] = molecular_formula

    # synonym
    for i in range(0, len(t)-1):
        if t[i].find('th').text == "Synonyms":
            synonyms_p = t[i].find('td').find('div').find('div').find_all('p')
            synonyms = []
            for key, value in enumerate(synonyms_p):
                synonyms.append(synonyms_p[key].text)
            property['synonyms'] = synonyms

    # introduction to the compound
    intro_p = t[len(t)-1].find('td').find_all('p')
    intro = []
    for key, value in enumerate(intro_p):
        intro.append(intro_p[key].text)
    property['intro'] = intro

    # iupac name
    if soup.find(id="IUPAC-Name"):
        iupac_name = soup.find(
            id="IUPAC-Name").find_all('div')[5].find('p').text
        property['iupac_name'] = iupac_name
    else:
        property['iupac_name'] = property['molecular_formula']

    # physical and chemical properties
    chemical_physical_properties1(soup)
    chemical_physical_properties2()

    # adding SHA1 to chemical name
    result = hashlib.sha1(property['name'].encode())
    property['sha'] = result.hexdigest()

    # adding current time to dictionary property
    property['date_time'] = datetime.now().strftime("%Y-%m-%dT%H-%M-%SZ")

    # adding all the properties of the compound in the list
    # properties.append(property)

    # .................................................................................................................
    # Abhishek your job : property is a dictionary, where all the data of a compound is stored, ur job is to
    # take those data and replace it with the translated data [translation into Hindi (unit should be in Latin only(not in Hindi))].
    # for example property[''name] will give u name of the compound.
    # If u done with ur code send the zip file back to me.
    # Feel free to contact me if u have any doubt.
    # After writting the code successfully, run it and wait for aroud 5 mins, coz browser will take some time to get the data.
    # DO NOT MODIFY ANYTHING WHICH IS ALREADY WRITTEN HERE.
    # ....................................... write your code below......................................
    exclude_property = {'Boiling_Point', 'Melting_Point', 'Flash_Point',
                        'Solubility', 'Vapor_Pressure', 'Autoignition_Temperature'}
    # special_property = {}

    translator = googletrans.Translator()

    temp_dict = {}
    for cur_property in property.keys():
        if property[cur_property] != 'not known':
            temp_dict[cur_property] = property[cur_property]

    property = temp_dict

    for cur_property in property.keys():
        if cur_property == "sha" or cur_property == "date_time":
            continue
        if cur_property == 'Refractive_Index' and property[cur_property] != 'not known':
            continue
        elif cur_property == 'Henrys_Law_Constant' and property[cur_property] != 'not known':
            continue
        elif cur_property == 'Atmospheric_OH_Rate_Constant' and property[cur_property] != 'not known':
            continue
        elif cur_property == 'Boiling_Point' and property[cur_property] != 'not known':
            continue
        elif cur_property == 'Melting_Point' and property[cur_property] != 'not known':
            continue
        elif cur_property == 'Flash_Point' and property[cur_property] != 'not known':
            continue
        elif cur_property == 'LogP' and property[cur_property] != 'not known':
            continue
        elif cur_property == 'LogS' and property[cur_property] != 'not known':
            continue
        elif cur_property == 'LogKoa' and property[cur_property] != 'not known':
            continue
        elif cur_property == 'Heat_of_Combustion' and property[cur_property] != 'not known':
            continue
        elif cur_property == 'Heat_of_Vaporization' and property[cur_property] != 'not known':
            continue
        elif cur_property == 'Ionization_Potential' and property[cur_property] != 'not known':
            continue
        elif cur_property == 'LogKoa' and property[cur_property] != 'not known':
            continue
        elif cur_property == 'iupac_name' and property[cur_property] != 'not known':
            continue
        elif cur_property == 'molecular_formula':
            continue
        elif cur_property not in exclude_property and cur_property is not None:
            if type(property[cur_property]) == list:
                temp = []
                for temp_val in property[cur_property]:
                    if temp_val is None:
                        continue
                    temp.append(translator.translate(
                        temp_val, dest='hi', src='en').text)
                property[cur_property] = temp
            else:
                property[cur_property] = translator.translate(
                    property[cur_property], dest='hi', src='en').text

    # print(property)
    # .........................................Your code ends here.......................................

    # for key in property:
    #     print(key, " : ", property[key])
    #     print()

    output = template.render(chemCompounds=property)
    fp = open(f"final_template/{property['name']}.txt", 'w+', encoding='utf-8')
    fp.write(output)
    fp.close()
    time.sleep(2)


# for key in property:

#     print(key, " : ", property[key])
#     print()

# print(property.__len__())


# for i in range(0, 5):
#     output = template.render(chemCompounds=properties[i])
#     fp = open(f"templates/{properties[i]['name']}.txt", 'w+', encoding='utf-8')
#     fp.write(output)
#     fp.close()
