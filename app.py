# # # # def ask_gemini(prompt):
# # # #     # Simulated AI output
# # # #     return "Civil engineering designs and builds infrastructure like roads and bridges to support society."

# # # # question = "Explain civil engineering importance."

# # # # answer = ask_gemini(question)

# # # # print("\nGemini Response:\n")
# # # # print(answer)







# # # # Function to simulate Gemini response
# # # def get_gemini_response(prompt):
# # #     """
# # #     Returns AI response for given prompt.
# # #     Currently simulated for internship project.
# # #     """
# # #     # Simulated response (replace later with real API)
# # #     return (
# # #         "Civil engineering focuses on planning, designing, and constructing "
# # #         "infrastructure like roads, bridges, and buildings to support society."
# # #     )


# # # # Test the function
# # # question = "Explain civil engineering importance."

# # # response = get_gemini_response(question)

# # # print("\nGemini Response:\n")
# # # print(response)







# # from PIL import Image

# # def prepare_image_for_gemini(image_path):
# #     """
# #     Reads image and prepares it for Gemini input.
# #     """
# #     try:
# #         image = Image.open(image_path)

# #         # Convert to RGB format
# #         image = image.convert("RGB")

# #         print("Image loaded successfully.")
# #         return image

# #     except Exception as e:
# #         print("Error loading image:", e)
# #         return None


# # # Example test
# # img = prepare_image_for_gemini("kick.jpg")

# # def build_civil_prompt():
# #     """
# #     Prompt used for civil engineering analysis.
# #     """
# #     prompt = (
# #         "You are a civil engineering expert. "
# #         "Analyze the given construction image and provide:\n"
# #         "1. Type of construction project\n"
# #         "2. Materials observed\n"
# #         "3. Construction stage\n"
# #         "4. Safety observations\n"
# #         "5. Suggestions for improvement\n"
# #         "Provide response in simple structured points."
# #     )

# #     return prompt


# # # Test prompt
# # prompt_text = build_civil_prompt()
# # print("\nGenerated Prompt:\n")
# # print(prompt_text)





import streamlit as st
from PIL import Image


# ---------- Gemini Simulation ----------
# def get_gemini_response(prompt):
#     return f"Analysis Result:\nBased on input '{prompt}', the system predicts a construction-related project requiring safety monitoring and proper material management."

def get_gemini_response(prompt):
    return (
        "Project appears to be a building construction site.\n"
        "Materials: Concrete and steel observed.\n"
        "Stage: Mid construction phase.\n"
        "Safety: Workers should use helmets and safety gear.\n"
        "Suggestion: Improve site safety monitoring."
    )


# ---------- Prompt ----------
def build_civil_prompt():
    return "Analyze construction image and give insights."


# ---------- Image Handling ----------
def prepare_image(uploaded_file):
    image = Image.open(uploaded_file)
    return image


# ---------- Streamlit UI ----------
st.title("🏗 Civil Engineering Insight Studio")

uploaded_file = st.file_uploader(
    "Upload Construction Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = prepare_image(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Analyze Image"):
        prompt = build_civil_prompt()
        response = get_gemini_response(prompt)

        st.subheader("Analysis Result")
        st.write(response)

# ---------- Landmark Description ----------
st.subheader("Generate Landmark Description")

landmark_name = st.text_input("Enter Landmark / Project Name")

if st.button("Generate Description"):
    if landmark_name:
        prompt = f"Describe the civil engineering landmark: {landmark_name}"

        description = get_gemini_response(prompt)

        st.subheader("Landmark Description")
        st.write(description)
    else:
        st.warning("Please enter a landmark name.")

