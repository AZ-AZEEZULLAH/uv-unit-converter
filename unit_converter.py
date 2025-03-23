import streamlit as st # type: ignore # streamlit is a library for building web apps


# Function to convert units based on predefinedconversion factors or formulas
def convert_units(value,unit_from,unit_to):
    
    conversions = {
        "meters_kilometers":0.001,  # 1 meter = 0.001 kilometer
        "kilometesr_metesr":1000,  # 1 kilometer = 1000 meter
        "grams_kilograms":0.001, # 1 gram = 0.001 kilogram
        "kilograms_grams":1000, # 1 kilogram = 1000 gram
    }
    key = f"{unit_from}_{unit_to}" #Generate a unique for the conversation 


# Logic toconvert units 
    if key in conversions:
        conversion = conversions[key]

        return value * conversion
    else:
        return "Conversion is not supported" # return a message if conversions is not supported
    
st.title("Unit_Converter") # Set the title of the web app

# user input : numerical value convert:
value = st.number_input("Enter the value :",min_value=1.0,step=1.0)# Create a number input field

# dropdown to select unit to convert from :
unit_from = st.selectbox("Convert from :", ["meters","kilometers","grams","kilograms"])

# dropdown to select unit to convert to :
unit_to = st.selectbox("Convert to", ["meters","kilometers","grams","kilograms"])


#button to trigger the conversion
if st.button("Convert"):
    result = convert_units(value,unit_from,unit_to)# call the conversion function
    st.write(f"Converted value : {result}") # display the result
    st.write("-----------------------") # line break

    st.write("© Azeezullah Noohpoto 🚀")# created by 
    