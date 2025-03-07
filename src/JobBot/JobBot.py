import streamlit as st
from langchain.chat_models import init_chat_model
from langgraph.graph import START, END, StateGraph
from JobBot import JobState
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from JobBot.JobModel import JobModel


@st.cache_resource
def init_model():
    print("Model initialized")
    model = init_chat_model("anthropic:claude-3-5-haiku-latest", temperature=0)
    return model

class JobBot:
    def __init__(self):
        self.model_initialized = False

    def init_job_bot(self):
        self.build_find_graph()
        self.model = init_model()
        self.model_initialized = True

    def human_feedback(self, state: JobState):
        """ No-op node that should be interrupted on """
        pass

    def find_job(self, state: JobState):
        """ Node to find a job """
        if not self.model_initialized:
            self.init_job_bot()
            
        with open('src/job_ad_1.txt', 'r') as file:
            content = file.read()
            #print(content)

        parse_instructions = """You are an analyst tasked with learning about a specific job opening. 
        Find the hiring company, job title, required skills, and location.
        """
        structured_llm = self.model.with_structured_output(JobModel)
        system_message = parse_instructions
        result = structured_llm.invoke([SystemMessage(content=system_message)]+[content])

        # Write messages to state
        return result     
       
    def query_graph(self, query):
        if not self.model_initialized:
            self.model = init_model()
            self.model_initialized = True
        return self.model.invoke(query).content

    def build_find_graph(self):
        # Add nodes and edges 
        interview_builder = StateGraph(JobState)
        interview_builder.add_node("find_job", self.find_job)
        interview_builder.add_node("human_feedback", self.human_feedback)

        # Flow
        interview_builder.add_edge(START, "find_job")
        interview_builder.add_edge("create_analysts", "human_feedback")
        interview_builder.add_conditional_edges("human_feedback", self.initiate_all_interviews, ["create_analysts", "conduct_interview"])
        interview_builder.add_edge("find_job", END)
