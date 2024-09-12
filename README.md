# HelloWorldAPI-APP
This project is a simple Flask-based API that returns greetings in different languages based on the language parameter passed to the API. It also includes a webpage (index.html) that interacts with the API to display the greetings.
Features:
REST API that returns greetings in different languages based on the request parameter.
Webpage (index.html) that allows users to select a language and display the corresponding greeting.
Easy setup and deployment using Flask.

Steps required to deploy API implementation:
1. Create a virtual environment: to isolate the project's dependencies by using command "python -m venv venv"
2. Install Flask: using command "pip install Flask"
3. Create the API in Python: "app.py" file
4. Run the API: by using command "python app.py" in the terminal.
5. Test the API: Open a browser and navigate to the following URLs to see the expected responses:
http://localhost:5000/hello?language=English → "Hello world"
http://localhost:5000/hello?language=French → "Bonjour le monde"
http://localhost:5000/hello?language=Hindi → "Namastey sansar"
6. Open the webpage: Open index.html in any web browser. Choose a language from the dropdown menu and click "Get Greeting." The greeting message will be displayed on the webpage by fetching the response from the API.
7. Deploy Project on Netlify : https://hrushi-helloworldapi.netlify.app/

