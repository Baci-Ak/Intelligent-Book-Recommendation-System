# Intelligent Book Recommendation System

This repository contains a project for building an intelligent recommendation system for an online book selling company. The recommendation engine suggests relevant books to users based on their preferences and past behavior. 

## Table of Contents
- [Project Overview](#project-overview)
- [Business Context and Problem](#business-context-and-problem)
- [Datasets](#datasets)
- [Modules](#modules)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

With the overwhelming volume of online content and increasing ubiquity of Internet-enabled devices, pervasive use of the Web for content sharing and consumption has become our everyday routines. However, people seeking online access to content or items of interest are becoming more and more frustrated due to information overload. Deciding the content to consume/buy from the deluge of available alternatives becomes increasingly difficult.

In this project, I aim to address the challenges faced by an online book selling company that has been experiencing declining sales. The solution involves designing and implementing an intelligent recommendation engine that suggests relevant books to users based on their consumption history.

This repository's distinctive feature is its approach to recommendation engine development using python objects without any other libraries. 

## Business Context and Problem

With the ever-growing online content and the ubiquity of Internet-enabled devices, users are facing information overload. This overload leads to difficulties in making decisions on what content or products to consume or purchase. The project focuses on helping an online book selling company that has been experiencing declining sales due to the overwhelming choices and challenges customers face when selecting books to buy.

The company's management recognizes the need for an intelligent recommendation engine to assist users in finding books aligned with their interests. This engine will not only enhance sales by providing personalized recommendations but also improve customer satisfaction by simplifying the decision-making process.

## Datasets
[Datasets](https://github.com/Baci-Ak/Datasets)

## Modules

1. `load_dataset_module`: This module retrieves user, book, and rating information from CSV files. It populates a dictionary with user preferences, including user IDs, ISBNs, book titles, authors, publication years, and ratings.

2. `similarity_module`: This module implements seven similarity functions, calculating similarity scores between users and between books using different metrics. These functions help identify commonly rated books and compute similarity based on shared ratings. The seven implemented similarity matrices are:
   - Squared Euclidean Distance
   - Minkowski Distance
   - Pearson Correlation
   - Spearman Correlation
   - Chebyshev Distance
   - Hamming Distance
   - Cosine Similarity

3. `test_module`: This module provides an interactive interface for users to query and display similarity scores. Users can input user IDs or book ISBNs to explore the recommendation engine's functionality.

## Getting Started

1. Clone this repository to your local machine using`
2. Navigate to the repository folder:

## Usage

1. Populate the required CSV files (`Users.csv`, `Books.csv`, and `Book-Rating.csv`) with user, book, and rating information on your working directory.
2. Run the `using_the_system.ipynb` to interact with the system, query and display similarity between users and books.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request. For major changes, please open an issue to discuss before making changes.

## License

This project is licensed under the [MIT License](LICENSE).

Please note that this repository specifically focuses on the development of a system that computes similarities between users or books using the seven specified similarity matrices. The complete recommendation system development resides in the [Book_recommendation_system repository](https://github.com/Baci-Ak/Book_recommendation_system). There, you'll find the broader implementation and deployment of the recommendation engine.
