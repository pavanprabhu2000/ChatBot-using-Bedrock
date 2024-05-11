import streamlit as st
import json
import boto3
from botocore.exceptions import ClientError
import os

# will set up aws profile via aws-azure-login
os.environ['AWS_PROFILE'] = "aws-account-team-09-aws"

# this is a function for bedrock-model
def stream_multi_modal_prompt(bedrock_runtime, model_id, input_query, input_text, max_tokens):
    # Construct request body with the parameters
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": max_tokens,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": input_query},  #passing 2 tyes of arguments to the model
                    {"type": "text", "text": input_text}    #both in text format
                ]
            }
        ]
    })

    # calling the model using the body and model_id
    response = bedrock_runtime.invoke_model_with_response_stream(
        body=body, modelId=model_id)

    response_text = ""

    # process response chunks
    for event in response.get("body"):
        chunk = json.loads(event["chunk"]["bytes"])

        if chunk['type'] == 'message_delta':
            response_text += f"Stop reason: {chunk['delta']['stop_reason']}\n"
            response_text += f"Stop sequence: {chunk['delta']['stop_sequence']}\n"
            response_text += f"Output tokens: {chunk['usage']['output_tokens']}\n"

        if chunk['type'] == 'content_block_delta':
            if chunk['delta']['type'] == 'text_delta':
                response_text += chunk['delta']['text']

    # display response for output
    st.write(response_text)

def main():
    # CSS to set the background color to white
    st.markdown(
        """
        <style>
            body {
                background-color: #ffffff;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # app name and title withcss
    st.markdown("<h1 style='text-align: center; color: #ffffff; font-size: 60px;'>ITS Hackathon 🚀💡</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #9fffa6; font-size: 40px;'>AI Avengers</h1>", unsafe_allow_html=True)

    # heading for bottom bar
    # st.markdown("<h2 style='color: #008080;'>Lets Go!!</h2>", unsafe_allow_html=True)
    # input_text = st.text_input("Enter your question regarding the uploaded file:", "Show me the table columns")
    max_tokens = 10000


    #suggestions = ["Describe me all the tables", "Show me All the Columns", "What is the Appplication name for INCJCR", "what is business unit", "Total count of all the app id which belongs to A and G"]

    input_text = "Describe me all the tables"

    # if suggestions:
    #     filtered_suggestions = [s for s in suggestions if input_text.lower() in s.lower()]
    #     # Display the filtered suggestions
    #     for suggestion in filtered_suggestions:
    #         if st.button(suggestion, key=suggestion):
    #             input_text = str(suggestion)
    #             st.write(f"You selected: {suggestion}")


    suggestions = ["how to get number of user for a given application","give us the application with highest number of active users",
                   "give us the top 10 customers for a given application", "Show me the relationship between all the tables", "Show me the list of applications went live by year", "Total count of all the app id which belongs to A and G"]

    # drop box in sidebar
    select_box = st.sidebar.selectbox("Suggested Questions", suggestions, index=0)

    # developers = ["Pavan P", "Muralidharan A", "T Nandan Pai"]
    #
    # # display dev names in sidebar
    # st.sidebar.markdown("### Developers")
    # for developer in developers:
    #     st.sidebar.markdown(developer)

    input_text = st.text_input("Type your questions here...", select_box)

    # st.sidebar.write(f"You selected: {select_box}")


    # submit button to pass the arguments to the modal prompt
    if st.button("Submit"):
        with st.spinner("Executing..."):
            with open('sp.txt', 'r') as file:  # reading the sql/text file into a variable query
                query = file.read()


            # configuring the model to not go beyond the data that's provided to it and some beautification properties
            input_query = """
            # You are an expert in Data Engineering.<br>
            # Provide the correct and Full table names<br>
            # If you are unsure about an answer then add your inferences at the end with the tag Inference<br>
            # If the request comes with any visual representation then display in using matplot lib<br>
            # If You Are displaying any output data present in the file then show it in table format and also in visual representation or images<br>
            # Provide correct and with respect to the Answers<br>
            # Don't give SQL query as an output give the exact answer <br>
            # If the user is specifically asking for a sql statement then you can provide <br>
            # Here is some information about the SQL query you need to understand :<br>
            you have all information about linkedin members and you have premium subscription
            """ + query

            try:
                # spinup bedrock client
                bedrock_runtime = boto3.client('bedrock-runtime')
                # call the bedrock model
                stream_multi_modal_prompt(bedrock_runtime, "anthropic.claude-3-sonnet-20240229-v1:0", input_query, input_text, max_tokens)
                st.success("Done!")
            except ClientError as err:
                # Error handling with custom styling
                st.error("<h3 style='color: red;'>An error occurred: {}</h3>".format(err), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
