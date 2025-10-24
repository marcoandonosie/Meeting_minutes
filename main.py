from transcribe import transcribe_audio
from parser import parse_meeting
from app import fetch_metadata
from docgen import create_doc
    #from docgen import create_docx

def main():
    #Step 0: accept and process transcript and metadata (dummy function for now)
    #print("Audio recieved...")
    metadata = fetch_metadata()

    # Step 1: Transcribe (dummy function for now)
    #print("process starting...")
    transcript = transcribe_audio("dummy_audio_file.mp3")

    # Step 2: Parse the transcript via GPT
    parsed_output = parse_meeting(transcript)
    print("notes cleaned!")

    doc_data = metadata + parsed_output
    # Step 3: Output result to terminal
    print("======= GPT OUTPUT =======") #change this header later lol
    
    for element in doc_data:
        print(element)

    #step  4: generate the document 
    create_doc(doc_data)
    print("we did it joe")
    print (doc_data[3])



'''
    
def process_meeting(audio_file=None, transcript_text=None):
    # Step 1: Get transcription (if audio provided)
    if audio_file:
        transcript = transcribe_audio(audio_file)
    else:
        transcript = transcript_text
    
    # Step 2: Parse the transcript into structured data
    parsed_data = parse_meeting(transcript)
    
    # Step 3: Generate the final document
    doc_path = create_docx(parsed_data)
    
    return doc_path, parsed_data
    



'''



if __name__ == "__main__":
    main() 