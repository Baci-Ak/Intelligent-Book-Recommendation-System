#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # importing the load_dataset_module

# In[7]:


#from load_dataset_module import User_preference, Book_preference


# In[8]:


#invoke the User_preference function

#user_pref = User_preference()
#user_pref


# In[ ]:





# In[ ]:





# In[9]:


#calling the the book_prefernce function

#book_pref = Book_preference()
#book_pref


# In[ ]:





# In[10]:


# generating test data for evaluation metrices

#test_data = [('276725', '276726', 0.8),
             #('276727', '276729', 0.6),
                #('276725', '276733', 0.2)]

#test_data


# In[ ]:





# In[ ]:





# THE 7 SIMILARITY METRICES FORMULARS:
#     
#     
# 
# 1. the minkowski distance similarity formular is, m(x,y) =      $(\sum|x - y|^p)^1/p$
# 
# 
# 2. the squared euclidean formula, D(x,y) =                       ∑(𝑥−𝑦)2
# 
# 
# 3. spearman's rank correlation, p(x,y) =                         $1 - 6 \sum(d)^2/n(n^2 - 1)$
# 
# 
# 4. chebyshev =                                                 $max(| x - y|)$
# 
# 
# 5. hamming distance
# 
# 
# 6. cosine similarity =                                          $\sum xy / \sqrt \sum x^2  \sqrt \sum y^2$
# 
# 
# 7. pearson correlation similarity:     $\sum XY - ((\sum X)(\sum Y)/n)/ \sqrt \sum X^2 - ((\sum X)/n)(\sum Y^2 - (\sum Y)^2/n)$

# In[4]:


def minkowski_distance_similarity(user_preference, user1_id, user2_id, p=3):
    """
    Calculate the Minkowski distance similarity between two users.

    Parameters:
    user_preference (dict): Nested dictionary containing user preferences.
    user1_id (str): ID of the first user.
    user2_id (str): ID of the second user.
    p (int, optional): The order of the Minkowski distance. Defaults to 2.

    Returns:
    float: Minkowski distance similarity score.
    """
    try:
        user1_ratings = user_preference.get(user1_id, {})
        user2_ratings = user_preference.get(user2_id, {})
    
        common_books = set(user1_ratings.keys()) & set(user2_ratings.keys())
    
        if not common_books:
            return 0.0  # No common books, similarity is 0
    
        distance = sum(abs(user1_ratings[book] - user2_ratings[book]) ** p for book in common_books)
        similarity = 1 / (1 + distance ** (1/p))
    
        return similarity
    
    except Exception as e:
        print(f"Error in minkowski_distance_similarity function: {e}")
    
    except KeyError:
        print('wrong user ID number, please enter the correct user ID')
    except:
        print("Some other exception happened.")
            
        


# In[9]:


from scipy.stats import spearmanr

def spearman_correlation_similarity(user_preference, user1_id, user2_id):
    """
    Calculate the Spearman correlation similarity between two users.

    Parameters:
    user_preference (dict): Nested dictionary containing user preferences.
    user1_id (str): ID of the first user.
    user2_id (str): ID of the second user.

    Returns:
    float: Spearman correlation similarity score.
    """
    
    try:
        user1_ratings = user_preference.get(user1_id, {})
        user2_ratings = user_preference.get(user2_id, {})
    
        common_books = set(user1_ratings.keys()) & set(user2_ratings.keys())
    
        if not common_books:
            return 0.0  # No common books, similarity is 0
    
        user1_common_ratings = [user1_ratings[book] for book in common_books]
        user2_common_ratings = [user2_ratings[book] for book in common_books]
    
        correlation, _ = spearmanr(user1_common_ratings, user2_common_ratings)
    
        similarity = 1 / (1 + abs(correlation))
    
        return similarity
    
    except Exception as e:
        print(f"Error in spearman_correlation_similarity function: {e}")
    
    except KeyError:
        print('wrong user ID number, please enter the correct user ID')
    except:
        print("Some other exception happened.")


# In[ ]:





# In[ ]:





# In[11]:


def spearman_correlation_similarity2(user_preference, user1_id, user2_id):
    """
    Calculate the Spearman correlation similarity between two users.

    Parameters:
    user_preference (dict): Nested dictionary containing user preferences.
    user1_id (str): ID of the first user.
    user2_id (str): ID of the second user.

    Returns:
    float: Spearman correlation similarity score.
    """
    
    try:
        user1_ratings = user_preference.get(user1_id, {})
        user2_ratings = user_preference.get(user2_id, {})
    
        common_books = set(user1_ratings.keys()) & set(user2_ratings.keys())
    
        if not common_books:
            return 0.0  # No common books, similarity is 0
    
        user1_common_ratings = [user1_ratings[book] for book in common_books]
        user2_common_ratings = [user2_ratings[book] for book in common_books]
    
        n = len(common_books)
    
            # Calculate rank differences
        rank_diff_sum = sum(abs(user1_common_ratings[i] - user2_common_ratings[i]) for i in range(n))
    
            # Calculate Spearman's rank correlation coefficient
        correlation = 1 - (6 * rank_diff_sum) / (n * (n**2 - 1))
    
        similarity = 1 / (1 + abs(correlation))
    
        return similarity
    
    except Exception as e:
        print(f"Error in spearman_correlation_similarity2 function: {e}")
    
    except KeyError:
        print('wrong user ID number, please enter the correct user ID')
    except:
        print("Some other exception happened.")
        
        
        



# In[ ]:





# In[13]:


def squared_euclidean_similarity(user_preference, user1_id, user2_id):
    """
    Calculate the squared Euclidean distance similarity between two users.

    Parameters:
    user_preference (dict): Nested dictionary containing user preferences.
    user1_id (str): ID of the first user.
    user2_id (str): ID of the second user.

    Returns:
    float: Squared Euclidean distance similarity score.
    """
    try:
        user1_ratings = user_preference.get(user1_id, {})
        user2_ratings = user_preference.get(user2_id, {})
    
        common_books = set(user1_ratings.keys()) & set(user2_ratings.keys())
    
        if not common_books:
            return 0.0  # No common books, similarity is 0
    
        squared_distance = sum((user1_ratings[book] - user2_ratings[book]) ** 2 for book in common_books)
        similarity = 1 / (1 + squared_distance)
    
        return similarity
    
    except Exception as e:
        print(f"Error in squared_euclidean_similarity function: {e}")
    
    except KeyError:
        print('wrong user ID number, please enter the correct user ID')
    except:
        print("Some other exception happened.")


# In[ ]:





# In[15]:


def hamming_distance_similarity(user_preference, user1_id, user2_id):
    """
    Calculate the Hamming distance similarity between two users.

    Parameters:
    user_preference (dict): Nested dictionary containing user preferences.
    user1_id (str): ID of the first user.
    user2_id (str): ID of the second user.

    Returns:
    float: Hamming distance similarity score.
    """
    
    try:
        user1_ratings = user_preference.get(user1_id, {})
        user2_ratings = user_preference.get(user2_id, {})
    
        common_books = set(user1_ratings.keys()) & set(user2_ratings.keys())
    
        if not common_books:
            return 0.0  # No common books, similarity is 0
    
        hamming_distance = sum(1 if user1_ratings[book] != user2_ratings[book] else 0 for book in common_books)
        similarity = 1 - (hamming_distance / len(common_books))
    
        return similarity
    
    except Exception as e:
        print(f"Error in hamming_distance_similarity function: {e}")
    
    except KeyError:
        print('wrong user ID number, please enter the correct user ID')
    except:
        print("Some other exception happened.")



# In[17]:


def pearson_correlation_similarity(user_preference, user1_id, user2_id):
    """
    Calculate the Pearson correlation similarity between two users.

    Parameters:
    user_preference (dict): Nested dictionary containing user preferences.
    user1_id (str): ID of the first user.
    user2_id (str): ID of the second user.

    Returns:
    float: Pearson correlation similarity score.
    """
    
    try:
        user1_ratings = user_preference.get(user1_id, {})
        user2_ratings = user_preference.get(user2_id, {})
    
        common_books = set(user1_ratings.keys()) & set(user2_ratings.keys())
    
        if not common_books:
            return 0.0  # No common books, similarity is 0
    
        user1_values = [user1_ratings[book] for book in common_books]
        user2_values = [user2_ratings[book] for book in common_books]
    
           # Calculate means
        user1_mean = sum(user1_values) / len(common_books)
        user2_mean = sum(user2_values) / len(common_books)
    
          # Calculate Pearson correlation
        numerator = sum((user1_values[i] - user1_mean) * (user2_values[i] - user2_mean) for i in range(len(common_books)))
        denominator_user1 = sum((user1_values[i] - user1_mean)**2 for i in range(len(common_books)))
        denominator_user2 = sum((user2_values[i] - user2_mean)**2 for i in range(len(common_books)))
    
        if denominator_user1 == 0 or denominator_user2 == 0:
            return 0.0  # Denominator is 0, similarity is 0
    
        pearson_similarity = numerator / (denominator_user1**0.5 * denominator_user2**0.5)
    
        return pearson_similarity
    
    except Exception as e:
        print(f"Error in pearson_correlation_similarity function: {e}")
    
    except KeyError:
        print('wrong user ID number, please enter the correct user ID')
    except:
        print("Some other exception happened.")



# In[ ]:





# In[ ]:





# In[19]:


def cosine_similarity(user_preference, user1_id, user2_id):
    """
    Calculate the cosine similarity between two users.

    Parameters:
    user_preference (dict): Nested dictionary containing user preferences.
    user1_id (str): ID of the first user.
    user2_id (str): ID of the second user.

    Returns:
    float: Cosine similarity score.
    """
    
    try:
        user1_ratings = user_preference.get(user1_id, {})
        user2_ratings = user_preference.get(user2_id, {})
    
        common_books = set(user1_ratings.keys()) & set(user2_ratings.keys())
    
        if not common_books:
            return 0.0  # No common books, similarity is 0
    
        dot_product = sum(user1_ratings[book] * user2_ratings[book] for book in common_books)
    
        user1_squared_sum = sum(user1_ratings[book]**2 for book in common_books)
        user2_squared_sum = sum(user2_ratings[book]**2 for book in common_books)
    
        if user1_squared_sum == 0 or user2_squared_sum == 0:
            return 0.0  # Denominator is 0, similarity is 0
    
        cosine_similarity = dot_product / (user1_squared_sum**0.5 * user2_squared_sum**0.5)
    
        return cosine_similarity
    
    except Exception as e:
        print(f"Error in cosine_similarity function: {e}")
    
    except KeyError:
        print('wrong user ID number, please enter the correct user ID')
    except:
        print("Some other exception happened.")


# In[ ]:





# In[21]:


def evaluate_similarity_matrices(user_preference, test_data):
    """
    Evaluate the accuracy of different similarity matrices and justify the best matrix.

    Parameters:
    user_preference (dict): Nested dictionary containing user preferences.
    test_data (list): List of tuples containing (user1_id, user2_id, true_similarity).

    Returns:
    str: Justification for the best similarity matrix.
    """
    
    try:
        matrix_functions = [minkowski_distance_similarity,pearson_correlation_similarity,cosine_similarity,
                            squared_euclidean_similarity,hamming_distance_similarity, 
                            spearman_correlation_similarity2]
    
        best_matrix = None
        best_accuracy = float('inf')
    
        for matrix_function in matrix_functions:
            total_absolute_error = 0.0
        
            for user1_id, user2_id, true_similarity in test_data:
                calculated_similarity = matrix_function(user_preference, user1_id, user2_id)
                absolute_error = abs(calculated_similarity - true_similarity)
                total_absolute_error += absolute_error
        
            average_absolute_error = total_absolute_error / len(test_data)
        
            if average_absolute_error < best_accuracy:
                best_matrix = matrix_function.__name__
                best_accuracy = average_absolute_error
    
        justification = f"The best similarity matrix is '{best_matrix}' with average absolute error {best_accuracy:.4f}"
        return justification
    
    except Exception as e:
        print(f"Error in cosine_similarity function: {e}")
    
    except KeyError:
        print('wrong user ID number, please enter the correct user ID')
    except:
        print("Some other exception happened.")


# In[ ]:





# In[ ]:




