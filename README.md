# ChatBot-using-Bedrock
A small project for setting up a chat bot using bedrock API and Claude v3 

This repo contains code for an application developed using Streamlit, a library for creating web applications. The application integrates with AWS services using Boto3, the AWS SDK for Python, to interact with the Bedrock service.

<img width="800" alt="image (1)" src="https://github.com/pavanprabhu2000/ChatBot-using-Bedrock/assets/54540366/03d4efb0-e059-4a58-a48e-4d5e5170e49d">


# WORKING
Environment Setup: The code sets AWS profile using the AWS_PROFILE environment variable to specify the AWS account to use. Make sure you have appropriate set up the aws-azure-login profile before hand. Create necessary IAM roles to give access to bedrock service's.

Streamlit Function: The stream_multi_modal_prompt function used to interact with the Bedrock model. It constructs a request body with parameters such as anthropic_version, max_tokens, and messages, inturn calls the Bedrock model using Boto3's invoke_model_with_response_stream method.

Error Handling: The code includes error handling using Streamlit's st.error function to display custom error messages in case of any exceptions during execution.

Running: "streamlit run .\hackthon.py" 



# Future Setup:

<img width="552" alt="download" src="https://github.com/pavanprabhu2000/ChatBot-using-Bedrock/assets/54540366/430251b8-646f-4367-8cf8-734d86345f85">
