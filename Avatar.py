import streamlit as st
import py_avataaars as pa
import os

# Define the available categories and their respective options
categories = {
    "General": {
        "Style": pa.AvatarStyle
    },
    "Face Features": {
        "Skin Color": pa.SkinColor,
        "Mouth Type": pa.MouthType,
        "Eye Type": pa.EyesType,
        "Eyebrow Type": pa.EyebrowType,
        "Nose Type": pa.NoseType
    },
    "Hair & Beard": {
        "Hair Color": pa.HairColor,
        "Facial Hair": pa.FacialHairType
    },
    "Clothing & Accessories": {
        "Top Type": pa.TopType,
        "Hat Color": pa.Color,
        "Accessories": pa.AccessoriesType,
        "Clothes Type": pa.ClotheType,
        "Clothes Graphic": pa.ClotheGraphicType
    }
}

# Dictionary to store the user-selected options
selected_options = {}

# Create 5 columns: Four for the categories and one for the avatar display
cols = st.columns(5)

# Loop through categories to generate selection options in the sidebar
for index, (section_name, section_categories) in enumerate(categories.items()):
    st.sidebar.header(section_name)  # Display a header for each section in the sidebar
    
    for category, values in section_categories.items():
        # Get available options from each category (excluding any hidden/private members)
        options = [item for item in dir(values) if not item.startswith("__")]
        
        # Allow the user to select an option from the available choices
        option = st.sidebar.selectbox(category, options)
        
        # Store the user's selected choice
        selected_options[category] = getattr(values, option)

# Generate the avatar using the user-selected options
avatar = pa.PyAvataaar(
    style=selected_options['Style'],
    skin_color=selected_options['Skin Color'],
    hair_color=selected_options['Hair Color'],
    facial_hair_type=selected_options['Facial Hair'],
    top_type=selected_options['Top Type'],
    hat_color=selected_options['Hat Color'],
    mouth_type=selected_options['Mouth Type'],
    eye_type=selected_options['Eye Type'],
    eyebrow_type=selected_options['Eyebrow Type'],
    nose_type=selected_options['Nose Type'],
    accessories_type=selected_options['Accessories'],
    clothe_type=selected_options['Clothes Type'],
    clothe_graphic_type=selected_options['Clothes Graphic']
)

# Specify the file path for saving the rendered avatar
avatar_filepath = 'avatar.png'

# Render the avatar to a PNG file
avatar.render_png_file(avatar_filepath)

# Display the avatar in the last column, if the rendering was successful
if os.path.exists(avatar_filepath):
    st.image(avatar_filepath, width=500)  # Display the avatar with a specified width
else:
    # Show a warning message if there was an issue with rendering
    st.warning("Failed to generate avatar. Please try again.")
