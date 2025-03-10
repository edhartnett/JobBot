import streamlit as st
from JobBot.VectorStore import query_faq

st.title("JobBot")
#st.set_page_config(page_title="JobBot", page_icon=":robot_face:", layout="wide")

# if "message_history" not in st.session_state:
#     st.session_state.message_history = [
#         {
#             "role": "assistant",
#             "content": "Hello! Ask me what kind of job you are looking for.",
#         }
#     ]

# st.title("JobBot")
# left_col, main_col, right_col = st.columns([1,2,1])

# with left_col:
#     if st.button("Clear"):
#         st.session_state.message_history = []

#     # if st.button("Find Job"):
#     #     st.session_state.message_history.append({
#     #         "role": "user",
#     #         "content": "Find a job",
#     #     })
#     #     with st.chat_message("user"):
#     #         st.markdown("Find a job")
#     #         print("Find a job")

# with main_col:
#     user_input = st.chat_input("Your question...")
#     if user_input:
#         #related_questions = query_faq(user_input)
#         st.session_state.message_history.append({
#             "role": "user",
#             "content": user_input,
#         })
#         st.session_state.message_history.append({
#             "role": "assistant",
#             "content": related_questions,
#         })

        # with st.chat_message("user"):
        #     st.markdown(user_input)
        #     print(user_input)

    # for i in range(1, len(st.session_state.message_history) + 1):
    #     this_message = st.session_state.message_history[-i]
    #     message_box = st.chat_message(this_message["role"])
    #     message_box.markdown(this_message["content"])


# with right_col:
#     st.text(st.session_state.message_history)

        # with st.spinner("Thinking..."):
        #     response = st.session_state.jobbot.invoke("Find a job")
        # with st.chat_message("assistant"):
        #     st.markdown(response)
        #     st.session_state.message_history.append({
        #         "role": "assistant",
        #         "content": response,
        #    })
