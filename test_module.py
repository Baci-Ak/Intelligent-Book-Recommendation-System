#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


from load_dataset_module import User_preference, Book_preference
from similarity_module1 import minkowski_distance_similarity,spearman_correlation_similarity2,squared_euclidean_similarity,hamming_distance_similarity,pearson_correlation_similarity,cosine_similarity,evaluate_similarity_matrices


# In[16]:


#invoke the User_preference function

#user_pref = User_preference()
#user_pref


# In[15]:


#calling the the book_prefernce function

#book_pref = Book_preference()
#book_pref


# In[ ]:





# In[14]:


# generating test data for evaluation metrices

#test_data = [('276725', '276726', 0.8),
             #('276727', '276729', 0.6),
                #('276725', '276733', 0.2)]

#test_data 


# In[ ]:





# In[19]:


def user_interface(user_preference, test_data):
    
    while True:
        print("\nMenu:")
        print("1. Compute Similarity between Users")
        print("2. Compute Similarity between Books")
        print("3. Evaluate Similarity Matrices and Find Best Matrix")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            user1_id = input("Enter the ID of the first user: ")
            user2_id = input("Enter the ID of the second user: ")
            
            print("\nSelect Similarity Matrix:")
            print("1. Minkowski Distance")
            print("2. Pearson Correlation")
            print("3. Cosine Similarity")
            print("4. Squared Euclidean Distance")
            print("5. Hamming Distance")
            print("6. Spearman Correlation")
            
            matrix_choice = input("Enter your choice: ")
            
            if matrix_choice == '1':
                try:
                    p_value = float(input("Enter the p value for Minkowski Distance: "))
                    similarity_score = minkowski_distance_similarity(user_preference, user1_id, user2_id, p_value)
                    print(f"Minkowski Distance Similarity between User {user1_id} and User {user2_id}: {similarity_score:.4f}")
                except ValueError:
                    print("Invalid input for p value. Please enter a valid number.")
                except KeyError:
                    print("Invalid user ID. User ID not found in user_preference.")
            elif matrix_choice == '2':
                try:
                    similarity_score = pearson_correlation_similarity(user_preference, user1_id, user2_id)
                    print(f"Pearson Correlation Similarity between User {user1_id} and User {user2_id}: {similarity_score:.4f}")
                except KeyError:
                    print("Invalid user ID. User ID not found in user_preference.")
            elif matrix_choice == '3':
                try:
                    similarity_score = cosine_similarity(user_preference, user1_id, user2_id)
                    print(f"Cosine Similarity between User {user1_id} and User {user2_id}: {similarity_score:.4f}")
                except KeyError:
                    print("Invalid user ID. User ID not found in user_preference.")
            elif matrix_choice == '4':
                try:
                    similarity_score = squared_euclidean_similarity(user_preference, user1_id, user2_id)
                    print(f"Squared Euclidean Similarity between User {user1_id} and User {user2_id}: {similarity_score:.4f}")
                except KeyError:
                    print("Invalid user ID. User ID not found in user_preference.")
            elif matrix_choice == '5':
                try:
                    similarity_score = hamming_distance_similarity(user_preference, user1_id, user2_id)
                    print(f"Hamming Distance Similarity between User {user1_id} and User {user2_id}: {similarity_score:.4f}")
                except KeyError:
                    print("Invalid user ID. User ID not found in user_preference.")
            elif matrix_choice == '6':
                try:
                    similarity_score = spearman_correlation_similarity2(user_preference, user1_id, user2_id)
                    print(f"Spearman Correlation Similarity between User {user1_id} and User {user2_id}: {similarity_score:.4f}")
                except KeyError:
                    print("Invalid user ID. User ID not found in user_preference.")
            else:
                print("Invalid choice for Similarity Matrix.")
                
        elif choice == '2':
            book1_isbn = input("Enter the ISBN of the first book: ")
            book2_isbn = input("Enter the ISBN of the second book: ")
            
            print("\nSelect Similarity Matrix:")
            print("1. Cosine Similarity")
            print("2. Hamming Distance")
            
            matrix_choice = input("Enter your choice: ")
            
            if matrix_choice == '1':
                try:
                    similarity_score = cosine_similarity(user_preference, book1_isbn, book2_isbn)
                    print(f"Cosine Similarity between Book {book1_isbn} and Book {book2_isbn}: {similarity_score:.4f}")
                except KeyError:
                    print("Invalid book ISBN. Book ISBN not found in user_preference.")
                except NameError:
                    print('Invalid function name, please check to fix')
            elif matrix_choice == '2':
                try:
                    similarity_score = hamming_distance_similarity(user_preference, book1_isbn, book2_isbn)
                    print(f"Hamming Distance Similarity between Book {book1_isbn} and Book {book2_isbn}: {similarity_score:.4f}")
                except KeyError:
                    print("Invalid book ISBN. Book ISBN not found in user_preference.")
            else:
                print("Invalid choice for Similarity Matrix.")
                
        elif choice == '3':
            
            justification = evaluate_similarity_matrices(user_preference, test_data)
            print(justification)
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")




# In[ ]:


#user_interface(user_pref, test_data)


# In[ ]:




