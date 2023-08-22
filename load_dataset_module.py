#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[4]:


def loadBooks():
    try:
        Books = {}
        file = open('Books.csv', encoding ="ISO-8859-1")
        next(file)
        for line in file:
            line = line.replace('"', '')
            (Id, Booktitle) = line.split(';')[0:2]
            Books.setdefault(Id, {})
            Books[Id] = Booktitle
        return Books
    #handling exceptions:
    except FileNotFoundError:
        print('the file you are trying to read is not in this working directory OR cannot be found')
    except OSError as err:
        print("OS error: {0}".format(err))
    except NameError:
        print('there is a name in the function that is not defined, please check to fix this')
    except:
        print("Some other exception happened.")
        
        
        



# In[ ]:





# In[ ]:





# # Loading the users preference Data

# In[5]:


def User_preference():
    try:
        user_preference = {}
        f = open('Book-Ratings.csv', encoding ="ISO-8859-1")
        next(f)
        for line in f:
            line = line.replace('"', '')
            (userId, bookid, rating) = line.strip('\n').split(';')
            user_preference.setdefault(userId, {})
            user_preference[userId][bookid] = float(rating)
        return user_preference
    
    #handling exceptions:
    except FileNotFoundError:
        print('the file you are trying to read is not in this working directory OR cannot be found')
    except OSError as err:
        print("OS error: {0}".format(err))
    except NameError:
        print('there is a name in the function that is not defined, please check to fix this')
    #except:
        #print("Some other exception happened.")



# In[ ]:





# In[ ]:





# # Rearranging the dictionary to have books ISBN as keys so its possible to find books similarities

# In[6]:


def Book_preference():
    try:
        book_prefs = {}
        f = open('Book-Ratings.csv', encoding ="ISO-8859-1")
        next(f)
        for line in f:
            line = line.replace('"', '')
            (userId, bookid, rating) = line.strip('\n').split(';')
            book_prefs.setdefault(bookid, {})
            book_prefs[bookid][userId] = float(rating)
        return book_prefs
    
    #handling exceptions:
    except FileNotFoundError:
        print('the file you are trying to read is not in this working directory OR cannot be found')
    except OSError as err:
        print("OS error: {0}".format(err))
    except NameError:
        print('there is a name in the function that is not defined, please check to fix this')
    except:
        print("Some other exception happened.")
        


# In[ ]:





# In[ ]:




