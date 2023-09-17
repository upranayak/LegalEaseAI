import numpy as np
import pickle

# Load the saved model
with open("C:/Users/Admin/OneDrive/Desktop/LegalEaseAI/summarizer_model.sav", "rb") as model_file:
    loaded_summarizer = pickle.load(model_file)

# Example text for summarization
input_text = """
SECTION 1. SHORT TITLE. This Act may be cited as the ``Native American Energy Act''. SEC. 2. TABLE OF CONTENTS. The table of contents for this Act is as follows: Sec. 1. Short title. Sec. 2. Table of contents. Sec. 3. Appraisals. Sec. 4. Standardization. Sec. 5. Environmental reviews of major Federal actions on Indian lands. Sec. 6. BLM oil and gas fees. Sec. 7. Bonding requirements and nonpayment of attorneys' fees to promote Indian energy projects. Sec. 8. Tribal biomass demonstration project. Sec. 9. Tribal resource management plans. Sec. 10. Leases of restricted lands for the Navajo Nation. Sec. 11. Nonapplicability of certain rules. SEC. 3. APPRAISALS. (a) Amendment...
"""
# Use the loaded summarizer for summarization
summary = loaded_summarizer(input_text, max_length=160, min_length=50, do_sample=False)

# Print the summary
print(summary[0]['summary_text'])