# Engagement Rate Prediction using Machine Learning

## Overview
This project predicts Instagram engagement rates using supervised machine learning. By analyzing key account and content features, it provides valuable insights for brands and marketers to optimize influencer selection and improve engagement performance.

## Documentation
- [Project Documentation](documentation/A5_Engagement_Rate_Prediction%20(4).pdf) - Detailed project report and analysis

## Key Features
- Collected and merged datasets using `Instaloader` (scraped) and public sources (Kaggle)
- Performed extensive preprocessing and feature engineering
- Trained and evaluated multiple machine learning models
- Delivered business-relevant insights on engagement trends across influencer types and content formats

## Machine Learning Models
- XGBoost (best performance, R² = 0.94)
- Gradient Boosting Regressor
- CatBoost
- K-Nearest Neighbors (KNN)
- Random Forest
- Decision Tree
- Linear Regression
- Support Vector Machine (SVM)

## Features Used
- `Followers`
- `Average Likes`
- `Average Comments`
- `Engagement Rate (60 days)`
- `Posting Frequency (60 days)`
- `Posts (Image)`
- `Posts (Video)`
- `Posts (Carousel)`

## Results
- **XGBoost** achieved the best performance with an R² score of **0.94** and **lowest RMSE**
- **Video and carousel posts** received higher engagement than image posts
- **Nano influencers** had the highest median engagement rates, outperforming mega influencers
- **Hashtag count** had minimal impact on engagement rates

## Technologies & Tools
- Python, Pandas, NumPy
- Scikit-learn, XGBoost, CatBoost
- Matplotlib, Seaborn
- Instaloader (for Instagram scraping)

## Project Structure
```
├── data/          # Raw and processed datasets
├── models/        # Trained models
├── notebooks/     # EDA and results
├── src/          # Source code (preprocessing, training)
├── requirements.txt
└── README.md
```

## Running the Project
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the main model training script:
```bash
cd src
python main.py
```

## Future Improvements
- Expand dataset to include other platforms (TikTok, X/Twitter)
- Integrate real-time prediction via backend API
- Incorporate NLP features from captions/hashtags to improve model inputs

## PPT Link
[PPT Link](https://www.canva.com/design/DAGZbvmqOIg/8FXAP1hayWKL0m3Hgp9gBQ/edit)
