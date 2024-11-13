"""
This module contains a Flask-based web application for detecting emotions
from a given text input. The application uses an emotion detection model to
analyze the emotional content of the text and returns emotion scores and the 
dominant emotion. The application also handles errors gracefully, providing 
user-friendly error messages for invalid inputs.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detector_api():
    """
    Endpoint to analyze the emotions of a given text.

    This function retrieves the text to analyze from the request arguments,
    passes it to the emotion detector, and returns the analysis results.
    If the input text is empty or invalid, appropriate error messages are returned.

    Returns:
        str: A formatted string containing emotion scores and dominant emotion, 
             or an error message if input is invalid.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Check if text_to_analyze is empty or None
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return "Invalid input! Please try again."

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # If the dominant emotion is None return the error message
    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    # Extract emotion scores and dominant emotion from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Return a formatted string with the emotion scores and dominant emotion
    return (
        f"For the given text, the emotions are as follows: "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """
    Renders the index page for the Emotion Detector.

    This function is used to serve the homepage of the application.
    It returns the index.html template for the frontend.

    Returns:
        str: The rendered HTML content for the index page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    # Start the Flask application on host 0.0.0.0 and port 5000
    app.run(host="0.0.0.0", port=5000)
