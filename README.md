
# School Blog API

Welcome to **School Blog API**! A powerful and efficient solution for managing blog posts within a school environment. This project consists of two main components:
1. **FastAPI Backend**: A RESTful API to manage blog data, written using **FastAPI**.
2. **Streamlit Frontend**: A simple user interface to interact with the blog API, allowing users to view and add blog posts.

---

## Project Overview

**School Blog API** allows users to perform the following operations:
- **Create Blog Posts**: Add new blog posts to the system.
- **Read Blog Posts**: Fetch all or specific blog posts.
- **CRUD Operations**: Easily manage your blog data with the power of FastAPI, MongoDB, and Streamlit.

This project is designed to serve as a full-stack web application where FastAPI handles the backend logic and data management, while Streamlit provides a sleek and interactive frontend for users.

---

## Key Features

- **FastAPI Backend**: Fast, modern, and flexible web framework for building APIs.
- **MongoDB Database**: Store your blog posts in MongoDB, a scalable NoSQL database.
- **Pydantic Data Validation**: Ensure data integrity and validity with Pydantic models.
- **Streamlit Frontend**: A beautifully simple interface to interact with the API, built with Streamlit.
- **Swagger Documentation**: Access the API documentation at `/docs` to interact with the API endpoints.

---

## Getting Started

Follow these simple steps to set up the project locally.

### Prerequisites

- Python 3.7+
- **Virtual Environment** (Recommended for managing dependencies)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/school_blog_api.git
cd school_blog_api
```

### 2. Set up Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

```bash
python -m venv venv
source venv/bin/activate   # For Mac/Linux
.\venv\Scripts\activate    # For Windows
```

### 3. Install Dependencies

Run the following command to install all necessary libraries listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Running the FastAPI Backend

Start the FastAPI backend server:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

This will start the API at `http://127.0.0.1:8000`.

### 5. Running the Streamlit Frontend

In a new terminal window (while the FastAPI server is running), navigate to the project folder and run Streamlit:

```bash
streamlit run app.py
```

This will start the frontend on `http://localhost:8501`.

---

## API Documentation

Once the FastAPI backend is running, you can access the full API documentation at:

- **FastAPI Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Swagger UI**: Visualize and interact with the API using the Swagger interface.

The API exposes the following endpoints:

- `GET /blogs`: Retrieve all blog posts.
- `GET /blogs/{blog_id}`: Retrieve a specific blog post by its ID.
- `POST /blogs`: Create a new blog post.
- `PUT /blogs/{blog_id}`: Update an existing blog post.
- `DELETE /blogs/{blog_id}`: Delete a blog post.

---

## Technologies Used

- **FastAPI**: Modern, fast (high-performance) web framework for building APIs with Python.
- **MongoDB**: NoSQL database for storing blog data.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Streamlit**: Simple and beautiful front-end for creating data apps.
- **Uvicorn**: ASGI server to run FastAPI.
- **GitHub Actions**: (Optional) For automating deployment and testing workflows.

---

## Contributing

If you would like to contribute to the development of this project, feel free to submit a pull request or open an issue. All contributions are welcome!

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Demo

Check out the live demo of the project (if hosted) or run it locally using the steps above to see how the **School Blog API** can be used to manage and view school blog posts!

---

## Contact

For any questions or inquiries, feel free to reach out via GitHub or email.

---

Thank you for checking out the School Blog API! 🚀

### Key Sections Explained:

- **Project Overview**: Gives a brief description of the project.
- **Key Features**: Lists the main functionalities your project offers.
- **Getting Started**: Detailed setup instructions for anyone who wants to run your app locally.
- **API Documentation**: Explains how to interact with your API endpoints.
- **Technologies Used**: Highlights the core technologies used in the project.
- **Contributing**: Encourages others to contribute if they want to add to the project.
- **License**: Mentions licensing info (you can replace it with the actual license you're using, or just keep it as MIT for simplicity).

