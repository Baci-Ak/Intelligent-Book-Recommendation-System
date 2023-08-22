#!/usr/bin/env python
# coding: utf-8

# In[39]:


#Load Dataset Module
import string
def loadBookRatings():  #load book rating information, userID, ISBN ID, and Ratings ('Book-Ratings').
    try:
        user_book_rating = {}
        f = open('Book-Ratings.csv', encoding ="ISO-8859-1")
        next(f)
        for line in f:
            line = line.replace('"', '')
            (userId, bookid, rating) = line.strip('\n').split(';')
            user_book_rating.setdefault(userId, {})
            user_book_rating[userId][bookid] = rating
        return user_book_rating
    
    #handling exceptions:
    except FileNotFoundError:
        print('the file you are trying to read is not in this working directory OR cannot be found')
    except OSError as err:
        print("OS error: {0}".format(err))
    except NameError:
        print('there is a name in the class method that is not defined, please check to fix this')
    except:
        print("Some other exception happened.")



#user_book_rating = loadBookRatings()
#user_book_rating


# In[40]:


import string

#function to load user dataset    
def UsersID():
    try:
        users = {}
        file = open('users.csv', encoding ="ISO-8859-1")
    #nexting the first row sine i dont need it
        next(file)
        for line in file:
            line = line.replace('"', '')
            (userid, Location) = line.split(';')[0:2]
            users[userid] = Location
        return users
    
    except FileNotFoundError:
        print('the file you are trying to read is not in this working directory OR cannot be found')
    except OSError as err:
        print("OS error: {0}".format(err))
    except NameError:
        print('there is a name in the class method that is not defined, please check to fix this')
    except:
        print("Some other exception happened.")



#users = UsersID()
#users


# In[41]:


import string
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



#Books = loadBooks()
#Books


# In[42]:


import string
def loadUserpreferenceData():
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
    except:
        print("Some other exception happened.")

#user_preference = loadUserpreferenceData()
#user_preference


# In[43]:


import string
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
#book_prefs = Book_preference()
#book_prefs


# In[ ]:




