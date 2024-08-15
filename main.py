import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

llm=Ollama(model='llama3')
# llm.to('cuda')
def resp(weight,height,goal,body_comp):
    template="""
            Give a gym advice to a person of height{height},weight{weight} and goal is to {goal}, and current body composition is {body_comp}
            """
    prompt=PromptTemplate(input_variables=["height","weight","goal","body_comp"],template=template)
    response=llm.stream(prompt.format(height=height,weight=weight,goal=goal,body_comp=body_comp),stop=['<|eot_id|>'])
    
    return response


st.title("FitAdvisor💪🏽")

weight=st.slider("Enter Weight.",0,200,75)
height=st.slider("Enter Height.",0,200,175)
goal=st.selectbox("What is your main goal",("Fat loss","Muscle Gain","Shredded","Lean"))
body_comp=st.selectbox("What is your current body type",("Fat","Skinny","SkinntFat"))
if st.button("Generate"):
        with st.spinner("Generating Answer..."):
            st.write_stream(resp(weight,height,goal,body_comp))
