
# 🎬 Movie Recommendation System using Machine Learning and Streamlit

This project is a **Content-Based Movie Recommender System** built using Python, Streamlit, and the TMDB 5000 Movie Dataset. The system recommends top 5 similar movies based on textual metadata like genres, cast, crew, keywords, and movie overview.

![App Screenshot](screenshot.png)


---

## 👨‍💻 Developed by
**P. Dinesh Samba Siva Rao**  
B.Tech in Artificial Intelligence and Machine Learning  
Vishnu Institute of Technology, Bhimavaram

---

## 🚀 Features

- 🔍 Recommends top 5 similar movies from TMDB dataset
- 🧠 NLP-based content feature extraction
- 📊 Cosine similarity used for recommendations
- 💾 Model saved using Pickle (`movies.pkl`, `similarity.pkl`)
- 🎨 Interactive UI built with Streamlit
- 🖼 Movie posters shown via TMDB API

---

## 📦 Project Structure

```
movie_recommender/
│
├── app.py                      # Streamlit application
├── create_models.py            # Script to process and save ML models
├── models/
│   ├── movies.pkl              # Pickled movie metadata
│   └── similarity.pkl          # Pickled cosine similarity matrix
├── movie_recommendation_system.ipynb  # Full ML pipeline in notebook form
├── Screenshot 2025-06-06 163719.png   # Streamlit app screenshot
├── requirements.txt            # List of required Python libraries
└── README.md                   # Project documentation
```

---

## 📚 Dataset Used

- TMDB 5000 Movie Dataset (from Kaggle)
  - `tmdb_5000_movies.csv`
  - `tmdb_5000_credits.csv`

---

## 🧠 Machine Learning Pipeline

1. **Data Merging**:
   - Combine `movies` and `credits` on title

2. **Feature Extraction**:
   - Extract `overview`, `genres`, `keywords`, `cast`, and `crew`
   - Select top 3 cast members and director
   - Create a `tags` column combining all textual info

3. **Text Preprocessing**:
   - Convert to lowercase, remove spaces, apply stemming

4. **Vectorization**:
   - Use `CountVectorizer` to convert text into vectors

5. **Similarity Calculation**:
   - Compute `cosine_similarity` between all movie vectors

6. **Saving Models**:
   - Save `movies.pkl` and `similarity.pkl` using `pickle`

---

## 🖥️ How to Run the Project

### 1. Clone or Download the Repository

```bash
git clone https://github.com/yourusername/movie_recommender.git
cd movie_recommender
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate Movie Models

```bash
python create_models.py
```

### 5. Start the Streamlit App

```bash
streamlit run app.py
```

---

## 🔧 Technologies Used

- Python 🐍
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Natural Language Processing (NLP)
- Pickle for model storage

---

## 💡 Example Output

If you search for `"Spider-Man 3"`, the system might recommend:

1. Spider-Man 2  
2. Spider-Man  
3. The Amazing Spider-Man 2  
4. The Amazing Spider-Man  
5. Arachnophobia  

And you’ll see their posters along with titles (via TMDB API).

---

## 📸 Interface Screenshot

---

## 📝 License

This project is open-source and free to use for educational purposes.

© 2025 P. Dinesh Samba Siva Rao
