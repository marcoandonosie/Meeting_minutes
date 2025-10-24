import streamlit as st

st.title("Danantara MoM Generator")

def fetch_metadata(): 
    date = "21 October 2025"
    place = "Jakarta"
    time = "11:41 AM"
    return [date, place, time]




'''
option = st.radio("Choose input type:", ["Upload Audio", "Paste Transcript"])

if option == "Upload Audio":
    audio_file = st.file_uploader("Upload meeting recording", type=["mp3", "wav", "m4a"])
    if audio_file and st.button("Generate MoM"):
        path, data = process_meeting(audio_file=audio_file)
        st.success("Minutes generated!")
        st.download_button("Download MoM", open(path, "rb"), file_name="MoM.docx")

else:
    transcript = st.text_area("Paste transcript here")
    if transcript and st.button("Generate MoM"):
        path, data = process_meeting(transcript_text=transcript)
        st.success("Minutes generated!")
        st.download_button("Download MoM", open(path, "rb"), file_name="MoM.docx")
        
        '''
