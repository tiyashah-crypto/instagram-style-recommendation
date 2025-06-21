````markdown
# 📱 Instagram-Style Content Recommendation System

This project demonstrates a basic content-based recommendation system using **cosine similarity** to suggest similar users based on their content preferences (Tech, Food, Travel Videos), mimicking an Instagram-like model.

## 🚀 Features
- Calculates user similarity based on content preferences
- Uses cosine similarity from `sklearn`
- Simulates user behavior with a sample dataset

## 🧠 Tech Stack
- Python 🐍
- Pandas
- NumPy
- Scikit-learn

## 📊 Dataset (Sample)
```python
data = {
    'User': ['A', 'B', 'C', 'D'],
    'Tech Videos': [5, 3, 0, 4],
    'Food Videos': [1, 4, 5, 2],
    'Travel Videos': [2, 1, 4, 5]
}
````

## 📌 Output

### User Preference Table

```
  User  Tech Videos  Food Videos  Travel Videos
0    A            5            1              2
1    B            3            4              1
2    C            0            5              4
3    D            4            2              5
```

### User Similarity Scores

```
  User  Similarity
0    A    0.8274
1    B    0.8663
2    C    0.8071
3    D    0.8724
```

## 📁 Files

* `recommendation.py`: Contains the code for similarity calculation
* `README.md`: Project documentation

## ⚙️ How to Run

```bash
pip install pandas numpy scikit-learn
python recommendation.py
```

## 📌 Future Ideas

* Include more content categories
* Add a GUI using Tkinter or Streamlit
* Connect with a real user database



