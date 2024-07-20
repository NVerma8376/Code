import io
import ollama
import requests
import SpeechToText as stt



transcript = stt.listen()

# Print the transcription
print("Transcript:", transcript)


def generate_questions(transcript, num_questions=10):
    prompt = f"Generate {num_questions} questions based on the following transcript:\n\n{transcript}\n\nQuestions:"
    response = ollama.chat(model="llama3", messages=[{'role': 'user', 'content': prompt}], stream=False)
    answer = response['message']['content']
    return answer

# Generate 10 questions based on the transcript
questions = generate_questions(transcript, 10)

if questions:
    # Print the generated questions
    print("Generated Questions:")
    print(questions)
else:
    print("Failed to generate questions.")