#!/usr/bin/env python
# coding: utf-8

# In[3]:


import load_dataset_module_assg1_main as m  # importing the data set module

user_preference = m.loadUserpreferenceData()

user_preference


# In[4]:


book_prefs = m.Book_preference()
book_prefs


# # # MINKOWSKI DISTANCE SIMILARITY

# # the minkowski distance similarity formular is, m(x,y) = $(\sum|x - y|^p)^1/p$

# In[7]:


def minkowski_distance_similarity(prefs, user1, user2):
    try:
        total1 = [] # open two empty lists to read users rating scores into it as a float
        total2 = []
        p_value = float(input('please enter the p-value for the minkowski similarity between user1 and user2 : '))
        from math import sqrt
        for book in prefs[user1]:
            if book in prefs[user2]:
    #read the rating scores of the users into a the lists
                total1.append(float(prefs[user1][book])) 
                total2.append(float(prefs[user2][book]))
    #compute the minkowski distance formula
                m = (sum(pow(abs(a-b), p_value) for a, b in zip(total1, total2))**1/p_value) 
        return 1/m
#handle exceptions
    except KeyError:
        print('wrong user ID number, please enter the correct user ID')
    except ValueError:
        print("Wrong input for p_value.")
    except:
        print("Some other exception happened.")
        

#print('the minkowski similarity between user1 and user2 is = ', minkowski_distance_similarity(user_preference, user1, user2))


# # # SQUARED EUCLIDEAN SIMILARITY

# # the squared euclidean formula, D(x,y) = $\sum(x - y )^2$

# In[29]:



from math import sqrt

def squared_euclidean_similarity(prefs, user1, user2):
    try:
        t1 = []
        t2 = []
        for book in prefs[user1]:
            if book in prefs[user2]:
                t1.append(float(prefs[user1][book]))
                t2.append(float(prefs[user2][book]))
                d =  (sum(pow(a-b,2) for a, b in zip(t1, t2)))
        return 1/d
    except KeyError:
        print('wrong user ID number, please enter the correct user ID')
    except:
        print("Some other exception happened.")
#print('the squared Euclidean similarity between user1 and user2 is = ', squared_euclidean_similarity(user_preference, user1, user2))


# # # SPEARMAN CORRELATION SIMILARITY

# # spearman's rank correlation, p(x,y) = $1 - 6 \sum(d)^2/n(n^2 - 1)$

# In[30]:


def spearman_correlation_similarity(prefs, user1, user2):
    try:
        t1 = []
        t2 = []
        for book in prefs[user1]:
            if book in prefs[user2]:
                t1.append(float(prefs[user1][book]))
                t2.append(float(prefs[user2][book]))
    # sort the rating scores of the users according to the score
                x = sorted([t1])
                y = sorted([t2])
    # now rank the rating scores of the users starting from 1 to lower rate
                index1 = [x.index(v)+1 for v in x]
                index2 = [y.index(p)+1 for p in y]
                n1 = len(t1)
        #find the number of books that the users ranked for
                n2 = len(index1)
                sum_list = []  #find and empty lis
                for (a, b) in zip(index1, index2):
            #find the difference in ranks and leave the result in the list created as sum_list
                    sum_list.append(a-b)
            # now compute the spearman correlation formula
                    square_list = [number**2 for number in sum_list ]
                    s = sum(square_list)
        print('the number of books rated by user1 and user2 is : n1 = ', n1)
        print('the number of books ranked by user1 and user2 is : n2 = ', n2)
        print(' the rank of user1 and user2 ratingscore are : ranks = ', index1, 'and', index2)
        print('the difference between the two ranks observation is  : d = ', sum_list)
        print('the sum of square of the difference in ranks is : d^2 = ', s)
        print('the rating scores for user 1 & 2 are : = ', t1, 'and', t2)
            
        return 1 - (6*s/n2*(n2**2 - 1))
    except KeyError:
        print('wrong user ID number, please enter the correct user ID')
    except:
        print("Some other exception happened.")

#print('finally the spearman correlation similarity between user1 and user2 is = ', spearman_correlation_similarity(user_preference, user1, user2))


# # # CHEBYSHEV SIMILARITY

# # chebyshev = $max(| x - y|)$

# In[31]:


def chebyshev(prefs, user1, user2):
    try:
        distance = []
        t1 = []
        t2 = []
        for book in prefs[user1]:
            if book in prefs[user2]:
                t1.append(float(prefs[user1][book]))
                t2. append(float(prefs[user2][book]))
                for a, b in zip(t1, t2):
                    distance.append(abs(a-b))
        print('the distance between user 1 & 2 is :', distance)
        return max(distance)
    except KeyError:
        print('wrong user ID number, please enter the correct user ID')
    except:
        print("Some other exception happened.")

#print('the chebyshev similarity between user1 and user2 is = ', chebyshev(user_preference, user1, user2))


# # # HAMMING DISTANCE SIMILARITY

# In[32]:


def hamming_distance_similarity(prefs, user1, user2):
    try:
        d = 0
        for book in prefs[user1]:
            if book in prefs[user2]:
                t1 = [(float(prefs[user1][book]))]
                t2 = [(float(prefs[user2][book]))]
                for a, b in zip(t1, t2):
                    if a != b:  #when the rating score of user1 and user2 are not the same, then assign 1 otherwise assign 0
                        d += 1
        return d
    except KeyError:
        print('wrong user ID number, please enter the correct user ID')
    except:
        print("Some other exception happened.")
#print('the hamming similarity between user1 and user2 is = ', hamming_distance_similarity(user_preference, user1, user2))


# # # COSINE SIMILARITY

# # $\sum xy / \sqrt \sum x^2  \sqrt \sum y^2$
# 

# In[2]:


from math import sqrt
def cosine_similarity(prefs, user1, user2):
    try:
        L1 = []
        L2 = []
        numerator = 0
        sum_a = 0
        sum_b = 0
        for book in prefs[user1]:
            if book in prefs[user2]:
                L1.append(float(prefs[user1][book]))
                L2.append(float(prefs[user2][book]))
                for x, y in zip(L1, L2):
                    numerator += sum([x * y])
                    sum_a += sum([x**2])
                    sum_b += sum([y**2])
                denominator = round(sqrt(sum_a) * sqrt(sum_b))
        return numerator / denominator
    
    except KeyError:
        print('wrong user ID number, please enter the correct user ID')
    except:
        print("Some other exception happened.")
        
        
#print('the cosine similarity between user1 1 & 2 is = ', cosine_similarity(user_preference, user1, user2))


# # # PEARSON CORRELATION

# # $\sum XY - ((\sum X)(\sum Y)/n)/ \sqrt \sum X^2 - ((\sum X)/n)(\sum Y^2 - (\sum Y)^2/n)$

# In[9]:


from math import sqrt

def pearson_correlation(prefs, user1, user2):
    try:
        L1 = []
        L2 = []
        numer = 0
        sum_1 = 0
        sum_2 = 0
        for book in prefs[user1]:
            if book in prefs[user2]:
                L1.append(float(prefs[user1][book]))
                L2.append(float(prefs[user2][book]))
                for x, y in zip(L1, L2):
                    n = len(L1)
                    numer += sum([x*y]) - ((sum([x])* sum([y]))/n)
                    sum_1 += sum([x**2]) - ((sum([x])*2)/n)
                    sum_2 += sum([y**2]) - ((sum([y])*2)/n)
                    den = round(sqrt(sum_1)* sum_2)
                #if den == 0:
                    #return 0
                #else:
        return numer / den
    except KeyError:
        print('wrong user ID number, please enter the correct user ID')
    except:
        print("Some other exception happened.")
#print('the pearson correlation similarity between user 1 and 2 is = ', pearson_correlation(user_preference, '278633', '278106'))


# In[ ]:





# In[ ]:




