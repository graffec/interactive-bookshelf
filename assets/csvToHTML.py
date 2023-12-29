import csv
from collections import Counter
from collections import defaultdict


# Path to CSV file
csv_file_path = 'books.csv'

# CSV headers
title_header = 'Title'
genre_header = 'Genre'
author_header = 'Author'

string_1 = '<div class= "book '
string_2 = '<h2>'
string_3 = '</h2></div>'


# additional_string = " (Special Genre)"

titles = []

with open(csv_file_path, 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

sorted_data = sorted(data, key=lambda row: row['Title'])

genres_list = set()

formatted_title = ''
for row in sorted_data:
    title = row['Title']
    genres = row['Genre'].split(', ')

    if  genres and genres[0] == "Biography":
        formatted_title = string_1 + 'bio">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title)
    elif genres and genres[0] == "Classic":
        formatted_title = string_1 + 'classic">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title)
    elif genres and genres[0] == "Fantasy":   
        formatted_title = string_1 + 'fantasy">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title) 
    elif genres and genres[0] == "Fiction":
        formatted_title = string_1 + 'fiction">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title)
    elif genres and genres[0] == "Graphic Novel":   
        formatted_title = string_1 + 'graphic">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title) 
    elif genres and genres[0] == "Historical Fiction":    
        formatted_title = string_1 + 'historical">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title)  
    elif genres and genres[0] == "History":    
        formatted_title = string_1 + 'history">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title)  
    elif genres and genres[0] == "Horror/Suspense/Thriller":    
        formatted_title = string_1 + 'hst">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title)   
    elif genres and genres[0] == "Humor":    
        formatted_title = string_1 + 'humor">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title)   
    elif genres and (genres[0] == "Memoir" or genres[0] == "Autobiography"):
        formatted_title = string_1 + 'memoir">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title)
    elif genres and genres[0] == "Mystery":
        formatted_title = string_1 + 'mystery">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title)
    elif genres and genres[0] == "Mythology":  
        formatted_title = string_1 + 'myth">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title)      
    elif genres and genres[0] == "Nonfiction":
        formatted_title = string_1 + 'nonfiction">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title)
    elif genres and (genres[0] == "Philosophy" or genres[0] == "Philosphy"):
        formatted_title = string_1 + 'phil">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title)
    elif genres and genres[0] == "Plays":
        formatted_title = string_1 + 'play">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title)
    elif genres and genres[0] == "Poetry":
        formatted_title = string_1 + 'poetry">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title)          
    elif genres and genres[0] == "Psychology":
        formatted_title = string_1 + 'psych">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title)       
    elif genres and genres[0] == "Romance":  
        formatted_title = string_1 + 'romance">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title)    
    elif genres and genres[0] == "Self-Help":  
        formatted_title = string_1 + 'self-help">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title)      
    elif genres and genres[0] == "Science Fiction":  
        formatted_title = string_1 + 'sci-fi">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title)      
    elif genres and genres[0] == "True Crime":  
        formatted_title = string_1 + 'true">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title) 
    elif  genres and genres[0] == "Young Adult":
        formatted_title = string_1 + 'young-adult">' + string_2 + f"{title}" + string_3
        titles.append(formatted_title)
    else:
        titles.append(f"{title}\n")
    genres_list.add(genres[0])

# with open(html_file_path, 'w') as output_file:
#     output_file.write('\n'.join(titles))

for g in titles:
    print(g)