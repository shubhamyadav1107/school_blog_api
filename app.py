import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/docs"  # Update this if deploying FastAPI separately

# Streamlit App Title
st.title("School Blog API with FastAPI and Streamlit")

# Form to create a blog post
with st.form(key="create_blog_post"):
    title = st.text_input("Title")
    content = st.text_area("Content")
    author = st.text_input("Author")
    submitted = st.form_submit_button("Create Post")

    if submitted:
        if title and content and author:
            # Make a POST request to FastAPI backend
            response = requests.post(
                f"{API_URL}/posts/",
                json={"title": title, "content": content, "author": author}
            )
            if response.status_code == 200:
                st.success("Blog Post Created!")
                st.write(response.json())  # Show the blog post details
            else:
                st.error("Failed to create blog post")

# Display all blog posts
st.header("All Blog Posts")
response = requests.get(f"{API_URL}/posts/")
if response.status_code == 200:
    posts = response.json().get("posts", [])
    for post in posts:
        st.subheader(post["title"])
        st.write(post["content"])
        st.write(f"By: {post['author']} on {post['created_at']}")
        st.write("---")
else:
    st.error("Failed to fetch blog posts")
