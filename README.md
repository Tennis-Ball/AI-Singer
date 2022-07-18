# AI-Singer 🎶🎶

Hola!!! Thanks for checking out this project. 

The AI-Singer does 2 things, it generates original lyrics based on the top 100 top pop song lyrics as training data, and generates original music in .midi output from a select few pip song midi inputs.
The program operates in the following steps:
1. Scrape lyrics from an online website
2. Clean those lyrics and transform them into a proper intput
3. Input the cleaned data into an LSTM Tensorflow model
4. Train and generate output lyrics
5. Clean lyrics of profanity
6. Calculate the total syllable count to determine song length
7. Clean input MIDI data and feed into another LSTM model for training
8. Output the final song and prompt to save the file


Note: playing around with input songs, lyrics, and hyper parameters may result in different results. Play around!

Note after the note: run get_generated.py to execute the entire script
