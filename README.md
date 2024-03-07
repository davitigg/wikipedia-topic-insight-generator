# Wikipedia Topic Insight Generator

## Description

The Wikipedia Topic Insight Generator is a Python application that retrieves topic-related data from Wikipedia, analyzes
it using Large Language Models (LLMs) to generate insights, and stores the outcomes in a database.

## Features

- Fetch data from Wikipedia based on user-specified topics.
- Analyze the retrieved data using LLMs to identify key themes, trends, and insights.
- Store the analyzed data in a MongoDB database for easy access.
- Provide a RESTful API to interact with the application.
- Dockerize the application for ease of deployment and scalability.

## Installation

To set up the project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/wikipedia-topic-insight-generator.git
    cd wikipedia-topic-insight-generator
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:

   Create a `.env` file in the root directory and add the following:

    ```plaintext
    MONGO_URI=mongodb://localhost:27017
    REPLICATE_API_TOKEN=your_replicate_api_token_here
    ```

   Replace `your_replicate_api_token_here` with your actual Replicate API token.

## Usage

To run the application, use the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server on `http://localhost:8000`.

### API Endpoints

- `POST /analysis`: Analyze a Wikipedia topic.
- `GET /analysis`: Get all analysis results.
- `GET /analysis/{analysis_id}`: Get a specific analysis result.
- `DELETE /analysis`: Delete all analysis results.
- `DELETE /analysis/{analysis_id}`: Delete a specific analysis result.
- `GET /topics`: Get a list of all analyzed topics.

## Docker

To run the application using Docker, use the following commands:

1. Build the Docker image:

    ```bash
    docker-compose build
    ```

2. Start the Docker containers:

    ```bash
    docker-compose up
    ```

This will start the application and MongoDB in separate Docker containers.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](https://en.wikipedia.org/wiki/MIT_License).
