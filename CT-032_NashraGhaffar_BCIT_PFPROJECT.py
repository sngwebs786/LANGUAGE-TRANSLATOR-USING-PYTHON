# pip install googletrans
# pip install textblob 


from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from textblob import TextBlob
################################################################ screenmaking
root = Tk()

################################################################ screen formatting
root.title("N.R TRANSLATOR")
root.geometry("500x500")
root.resizable(False,False)
# root.iconbitmap('logo.ico')  
root.configure(bg="black")

#################################################################  Dropdown language menu


 
lang_dict={'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 
'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 
'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 
'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo',
'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka',
'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw',
'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 
'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 
'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 
'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt',
'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no',
'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro',
'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn',
'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es',
'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th',
'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh',
'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu', 'Filipino': 'fil', 'Hebrew': 'he'}

languages = StringVar()
lang_box = Combobox(root,textvariable=languages,state='readonly',width=30)
lang_box ['values']=[e for e in lang_dict.keys()] #entering the values of dict in the dropdown
lang_box.current(96) #set the default value as English(21 is the key of english) we found it by printing the whole dict.
lang_box.place(x=296,y=0)



################################################################# Making Input Box
varname1 = StringVar() #set the default value as empty
inputbox1=Entry(root,width=25,textvariable=varname1,font=('times',15,'italic bold'))
inputbox1.place(x=220,y=60)

varname2 = StringVar() #set the default value as empty
inputbox2=Entry(root,width=25,textvariable=varname2,font=('times',15,'italic bold'))
inputbox2.place(x=220,y=120)


########################################################## Labels(Headings) formatting
inputbox1_label = Label(root,text="Enter your word :",font=('times',15,'bold'),foreground="crimson",bg="black")
inputbox1_label.place(x=50,y=60)

inputbox2_label = Label(root,text="Translated text :",font=('times',15,'bold'),foreground="crimson",bg="black")
inputbox2_label.place(x=50,y=120)

#it will show the translated text again below(becasue of limited space in the upper box we again printed it)
label3 = Label(root,text="",font=('times',15,'bold'),foreground="white",bg="black")
label3.place(x=50,y=200)





########################################################## Button making

def conv(event=None):                 #click btn function
    try:
        word = TextBlob(varname1.get())
        lang_of_word = word.detect_language()
        combo_lang = languages.get()
        main_lang = lang_dict[combo_lang]
        word = word.translate(from_lang=lang_of_word,to=main_lang)
        word2 = word.split(' ')
        rev_word = ' '.join(reversed(word2))
        label3.configure(text=rev_word)
        varname2.set(rev_word)
    except:
        varname2.set("Try another word please")


def main_exit():            #exit btn function
    message = messagebox.askyesnocancel("Notification","Are you sure you want to exit ??",parent=root)
    if message==TRUE:
        root.destroy()



btn1=Button(root,text="Click",bg="crimson",foreground="white",activebackground="maroon",width=12,
font=('times',15,'italic bold'),bd=10,command=conv)
btn1.place(x=60,y=300)
root.bind('<Return>',conv)   #enterkey

btn2=Button(root,text="Exit",bg="crimson",foreground="white",activebackground="maroon",width=12,
font=('times',15,'italic bold'),bd=10,command=main_exit)
btn2.place(x=280,y=300)





root.mainloop()


#JAZAKALLAH
