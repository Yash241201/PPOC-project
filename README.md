
##Fake News Detection Chatbot##

This project is an AI-powered chatbot that can detect whether a news article is **real** or **fake**. It uses a **transformer model** (like BERT or DistilBERT) to classify news text entered by the user.

#Features

- User-friendly chatbot interface using **Streamlit**
- Uses machine learning to predict if news is **Fake** or **True**
- Built with a fine-tuned transformer model
- Can be run locally or shared online

#Requirements 

You also need to install the following libraries:

pip install streamlit
pip install transformers
pip install torch
pip install scikit-learn
pip install pandas
```

#Project Files

- `chatbot_app.py`: Main Streamlit app
- `model/`: Folder containing your trained transformer model
- `true.csv` and `fake.csv`: Datasets used for training (optional)
- `README.md`: You're reading it!

#How to Run the App Locally

1. Open Terminal (or Anaconda Prompt)**  
   Go to the folder where `chatbot_app.py` is saved.
2. Run streamlit run chatbot_app.py
3. A new browser tab will open automatically. If not, copy the link from the terminal (something like `http://localhost:8501`) and paste it into your browser.


#Example Input

Type or paste a news headline like:

"NASA's Stratospheric Observatory for Infrared Astronomy (SOFIA) has confirmed, for the first time, water on the sunlit surface of the Moon. This discovery indicates that water may be distributed across the lunar surface and not limited to cold, shadowed places"

The chatbot will reply whether the news is real or fake and will give the percantage of its confidence .

#Model Used

We use **DistilBERT** or **BERT** model fine-tuned on a dataset made from `true.csv` and `fake.csv`.

Made by --
Yash pratap singh 
241201
