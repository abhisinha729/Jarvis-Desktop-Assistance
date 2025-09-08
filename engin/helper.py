def extract_yt_term(command):
    return command.replace("open youtube", "").replace("on youtube", "").strip()

    
    
    
#make helper function to remove unwanted words from query
def remove_words(input_string,words_to_remove):
    #splipe the input string into words
    words=input_string.split()
    
    #remove unwanted words
    filtered_words=[word for word in words if word.lower() not in words_to_remove]

    #join the remaining words back into a string
    result_string=''.join(filtered_words)

    return result_string

#example usages(demo)
# input_string="make a phone call to papa"
# words_to_remove=['make','a','call','to','phone','message','whatsapp','send']

# result=remove_words(input_string,words_to_remove)
# print(result)

