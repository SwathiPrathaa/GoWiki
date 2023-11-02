import streamlit as st
from subprocess import call
st.title("GoWiki")

search_query = st.text_input("Enter your search query:")
with open('input.txt', 'w') as f:
    f.write(search_query)

def execute():
    call(["python", "search.py"])

def search_function(query):
    with open('output.txt', 'r') as f:
        results = f.readlines()
    return results

if st.button("Search"):
    if search_query:
        execute()
        search_results = search_function(search_query)

        st.write(f"Search results for: {search_query}")
        if search_results:
            for result in search_results:
                st.write(result)


st.write("You can enter a search query in the input box above and click the 'Search' button.")