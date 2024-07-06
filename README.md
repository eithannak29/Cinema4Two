# CinemaForTwo

This project implements a movie recommendation system using machine learning and collaborative filtering techniques. The system is designed to predict movies that would appeal to a couple of users, taking into account their respective preferences.

<div style="text-align: center;">
  <img src="image/README/logo.png" alt="CinemaForTwo Logo" />
</div>

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Data](#data)
4. [Data Preprocessing](#data-preprocessing)
5. [Model](#model)
6. [Optimization](#optimization)
7. [Evaluation](#evaluation)

## Introduction

The goal of this project is to create a movie recommendation system using user movie rating data. The system uses advanced machine learning techniques to provide personalized recommendations.

## Installation

To run this project locally, please follow the instructions below:

1. Clone the repository:

   ```bash
   git clone https://github.com/eithannak29/CinemaForTwo.git
   cd CinemaForTwo
   ```
2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   The python version used for this project is 3.12.2

## Data

The data used for this project comes from the MovieLens 1M dataset and the IMDb database. It includes information about users, movies, and the ratings given by users to movies.

## Data Preprocessing

1. **Data Cleaning:**

   - Transform user and movie identifiers for uniformity.
   - Separate the release date and the year of the movie for use in analyses.
   - Remove missing values and handle data inconsistencies.
2. **Data Transformation:**

   - Encode movie genres.
   - Convert ratings to floats for better manipulation.
   - Prefix identifiers to avoid collisions during joins.
3. **Data Aggregation:**

   - Aggregate movie data from different sources to enrich the dataset with additional information such as average ratings and number of votes.

## Model

The recommendation model uses a collaborative filtering approach based on the rating matrix.

To do this, we used the SVD (Singular Value Decomposition) model, which is a widely used matrix factorization technique for movie recommendations.

The factorization of the rating matrix allows decomposing the matrix into three matrices: U, S, and V, where U and V are matrices of latent vectors for users and movies, and S is a diagonal matrix of singular values.

These are used to predict missing ratings and recommend movies to users based on their preferences.Moreover, we used weighting to give more influence to the user who watches more movies.

Once the predictions are made, we used a post-processing method to filter out movies already seen by the users and only recommend movies not seen by both users. We then sort them based on average ratings and number of votes to provide high-quality recommendations.

## Optimization

In order to optimize the model, we used the Optuna method, which is an automatic hyperparameter optimization library, allowing us to find the best hyperparameters for the SVD model using Bayesian search.

## Evaluation

The model evaluation is carried out using the following metrics:

- **RMSE (Root Mean Square Error):** To measure the error in rating predictions.