from flask import Flask
import requests as r

app = Flask(__name__)

@app.route('/')
def home():
	return """
	<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aayush's Personal Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            color: #333;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #5eb7ff;
            color: white;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            position: fixed;
            width: 100%;
            top: 0;
            left: 0;
            z-index: 1000;
        }
        nav {
            text-align: center;
            padding: 10px;
            background-color: #333;
            color: white;
            margin-top: 80px; /* Adjust to match the header height */
        }
        nav a {
            color: white;
            margin: 0 15px;
            text-decoration: none;
        }
        section {
            padding: 20px;
            margin: 20px;
            background: white;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-top: 60px; /* Adjust to provide space for the fixed header */
        }
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px;
            position: fixed;
            width: 100%;
            bottom: 0;
        }
    </style>
</head>
<body>

<header>
    <h1>Welcome to Aayush's Personal Website</h1>
</header>

<nav>
    <a href="#bio">About Me</a>
    <a href="#projects">Projects</a>
</nav>

<section id="bio">
    <h2>About Me</h2>
    <p>Hello! I'm Aayush. I am 10 years old and I love creating websites. This site is a fun way to share more about myself, my projects, and my interests.</p>
</section>

<section id="projects">
    <h2>Projects</h2>
    <p>Here are some of the projects I've worked on:</p>
    <ul>
        <li><a href="https://www.bluetubers.great-site.net">My Website</a></li>
        <!-- Add more project links here -->
    </ul>
</section>
<section id="message">
  <!-- More Here -->
</section>

<footer>
    <p>&copy; 2024 Aayush. All rights reserved.</p>
</footer>

</body>
</html>
	"""
	
@app.route('/youtube')
def youtube():
	res = r.get("https://youtube.com")
	html= res.text
	return html
	
@app.route('/google')
def google():
	res = r.get("https://google.com")
	html= res.text
	return html
		
if __name__ == '__main__':
	app.run(debug=True)
