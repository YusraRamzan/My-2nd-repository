import streamlit as st
from groq import Groq

# Directly set your API key here
API_KEY = "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"  # Replace with your actual Groq API key

# Initialize the Groq client with the direct API key
client = Groq(api_key=API_KEY)

# Function to ask a question to Groq API
def ask_groq(question, model="mixtral-8x7b-32768"):
    try:
        # Send the question to Groq's chat completion endpoint
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
            model=model,
        )
        # Return the generated response
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# Streamlit App
def main():
    st.title("Groq API Q&A")
    st.write("Ask any question and get answers powered by the Groq API.")

    # Input field for the user's question
    question = st.text_input("Enter your question:", "")

    # Button to trigger the API call
    if st.button("Get Response"):
        if question.strip():
            with st.spinner("Fetching response..."):
                response = ask_groq(question)
            st.write("### Groq's Response:")
            st.write(response)
        else:
            st.warning("Please enter a question before clicking 'Get Response'.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
