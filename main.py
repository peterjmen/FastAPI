from fastapi import FastAPI, HTTPException
from starlette.responses import RedirectResponse
import joblib

# Load the sentiment analysis model
sentiment_model = joblib.load("sentiment_model.pkl")

# Create an instance of FastAPI with a custom title and description
app = FastAPI(
    title="Pete's API's",  # Change this to your desired title
    description="Description of stuff",  # Change this to your desired description
)


# TODO: uvicorn main:app --host 127.0.0.1 --port 1987 --reload
# FIXME:
# HACK:
# XXX:
# NOTE:


# Redirect to the /docs endpoint when accessing the root URL
@app.get('/', include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url='/docs')

# Simplified root endpoint
@app.get('/docs', include_in_schema=False)
async def root():
    return {'message': 'Go to /docs for API documentation'}

# Sentiment analysis endpoint with a custom operation ID
@app.get('/sentiment/{text_to_analyse}', tags=["Sentiment, yay!"], summary="Click me!        ➡️   Go Try it out")
async def sentiment_analyser(text_to_analyse: str):
    try:
        sentiment_probs = sentiment_model.predict_proba([text_to_analyse])[0]
        sentiment_rating = 0 * sentiment_probs[0] + 4 * sentiment_probs[1]

        if sentiment_rating >= 2.5:
            sentiment_meaning = "Positive"
        elif sentiment_rating > 1.5 and sentiment_rating < 2.5:
            sentiment_meaning = "Neutral"
        else:
            sentiment_meaning = "Negative"

        return {"text": text_to_analyse, "sentiment_rating": sentiment_rating, "sentiment": sentiment_meaning}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
