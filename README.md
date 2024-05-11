# ChatBot-using-Bedrock
A small project for setting up a chat bot using bedrock API and Claude v3 

This repo contains code for an application developed using Streamlit, a library for creating web applications. The application integrates with AWS services using Boto3, the AWS SDK for Python, to interact with the Bedrock service.

#WORKING
Environment Setup: The code sets AWS profile using the AWS_PROFILE environment variable to specify the AWS account to use.

Streamlit Function: The stream_multi_modal_prompt function used to interact with the Bedrock model. It constructs a request body with parameters such as anthropic_version, max_tokens, and messages, inturn calls the Bedrock model using Boto3's invoke_model_with_response_stream method.

Error Handling: The code includes error handling using Streamlit's st.error function to display custom error messages in case of any exceptions during execution.
