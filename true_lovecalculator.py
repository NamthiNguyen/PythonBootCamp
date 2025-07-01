def calculate_love_score(name_1,name_2):
  
    
    combined_name = (name_1 + name_2).lower()
    
    count_true = 0
    
    for char in "true":
        count_true += combined_name.count(char)
    
    
    count_love = 0
    
    for char in "love":
        count_love += combined_name.count(char)
        
    
    score = int(str(count_true) + str(count_love))
    
    print(score)
    
    
calculate_love_score("church", "Nam")