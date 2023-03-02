import streamlit as st

st.title("A little story about markdown.")

# Initialization of session state and logic of session state

if 'level' not in st.session_state:
    st.session_state['level'] = 0
    
if 'meme' not in st.session_state:
    st.session_state['meme'] = ""

def init():
    st.session_state['level'] = 0

def increase():
    st.session_state['level'] += 1


# Grab a random meme from reddit using meme-api.com
def grab_meme_url():
    import requests
    import json

    ups = 0
    url = "https://meme-api.com/gimme/wholesomememes"
    while ups < 300:
        response = requests.get(url)
        data = json.loads(response.text)
        ups = data['ups']
    meme = data['url'] + "?width=250"
    return meme

# Story parts

mdtext1 = """
:blue[Our story begins with a simple text, that wanted to be stronger, and wished to become a title. Let's help it!]  
:green[_We can create a title by using # in front of the text._]  
  
I wish I could be stronger...
"""

mdtext2 = """
:blue[Having received the help that it needed, it now is stronger than ever, and became a title.]  

# Now I am stronger!

:blue[But now it was too big, and wanted to be a little bit smaller. Let's help him with that!]  
:green[_Titles have different sizes, and we can lower the size by adding more # in front of the text._]
"""

mdtext3 = """
## I am now smaller!

:blue[Still feeling too big, it wanted to be even smaller. Let's see where this goes...]
"""

mdtext4 = """
### I am now even smaller!
:blue[Now THIS is the perfect size! It is now a subtitle, and is happy with its size.]  
  
I want to be bold!!!

:blue[Huh? Who's this? Oh it's a paragraph! And it wants to become bold! Forget about the title, let's help it!]  
:green[_We can make a part of the paragraph bold by using ** in front and after the text._]  

"""

mdtext5 = """
**I am now bold!**  
  
:blue[The paragraph, now bold, realized that it didn't want to be bold, but it wanted to be italicized.]  
:green[_We can make a part of the paragraph italicized by using * (or \_ ) in front and after the text._]
"""

mdtext6 = """
*Now I am italicized!*

:blue[The paragraph, now italicized, realized that it still wasn't happy, so it wanted to be both bold and italicized!]  
:green[_We can make a part of the paragraph bold and italicized by using *** (or **\_ )in front and after the text._]
"""

mdtext7 = """
***Now I am bold and italicized!***

:blue[The paragraph, now bold and italicized, realized that it was happy with its style, and lived happily ever after.]  

To be or not to be... that is the question.  

:blue[Hmm, that's not right! The paragraph is not a quote! Let's fix that!]  
:green[_We can make a part of the paragraph a quote by using > in front of the text._]
"""

mdtext8 = """
> To be or not to be... that is the question.

:blue[Nice! The paragraph is now a quote! And I believe we've reached the end of our story, and-]  
I need to be a list!  
I have eggs, milk and bread to buy!

:blue[Never-mind then! Let's help the list with its needs!]  
:green[_We can make a part of the paragraph a list by using - in front of the text._]  
:green[_We can add multiple levels of lists by adding more spaces and - in front of the text._]
"""

mdtext9 = """
**Shopping list:**
- Eggs
- Milk
- Bread
    - White bread
    - Brown bread

:blue[However the list still wasn't happy, and wanted to be a list with numbers instead of bullets.]  
:green[_We can make a part of the paragraph a numbered list by adding spaces, numbers and a dots (1. ) in front of the text._]
"""

mdtext10 = """
**Shopping list:**
1. Eggs
2. Milk
3. Bread
    1. White bread
    2. Brown bread

:blue[Now that the list is happy, it can go shopping! But hey, what's this? a line?]  
:green[_Lines are great separators, and we can create one by using --- ._]
"""

mdtext11 = """
**Shopping list:**
1. Eggs
2. Milk
3. Bread
    1. White bread
    2. Brown bread

---

:blue[Oh, the line just needed the shopping list, but I see a link! Let's see where it goes...]  
:green[_We can create a link by using [text that is shown](destination link) in the text._]
"""

mdtext12 = """

[What a wonderful video!](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

:blue[Oh, the link just wanted to show us a video, but I see an image! Let's see what that is about...]  
:green[_We can create an image by using ![Alternate text](image link) in the text._]  
:green[_The alternate text is shown if the image doesn't load._]
"""

mdtext13 = """
![A random meme](&&URL&&)

:blue[Oh, what a nice meme! (I hope it's a meme, it's random after all...)]  
:blue[And this is the end of our story!]  
:blue[You will see a button to show the markdown code of this story.]  
:blue[Thank you for reading!]
"""

mdtextfinish = """
```markdown
Here are the various markdown elements that we used in this story:

Titles:
# Now I am stronger!
## I am now smaller!
### I am now even smaller!
You can add up to 6 # to create a title.

Bold:
**I am now bold!**

Italicized:
*Now I am italicized!*

Bold and italicized:
***Now I am bold and italicized!***

Quotes:
> To be or not to be... that is the question.

Lists:
**Shopping list:**
- Eggs
- Milk
- Bread
    - White bread
    - Brown bread

Numbered lists:
**Shopping list:**
1. Eggs
2. Milk
3. Bread
    1. White bread
    2. Brown bread

Lines:
---

Links:
[What a wonderful video!](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

Images:
![A random meme](&&URL&&)

    And of course, this code, is shown using markdown!
    ```markdown
    to start, and
    ```
    to end.

```

instead, to display markdown using Streamlit, you can use `st.markdown("your markdown text here")`. 
"""




if st.session_state['level'] == 0:
    st.markdown(mdtext1)
    st.button("Click me to make the text stronger!", on_click=increase, help='Let\'s go forward with the story!')
elif st.session_state['level'] == 1:
    st.markdown(mdtext2)
    st.button("Click me to make the title smaller!", on_click=increase, help='Let\'s go forward with the story!')
elif st.session_state['level'] == 2:
    st.markdown(mdtext3)
    st.button("Click me to make the subtitle even smaller!", on_click=increase, help='Let\'s go forward with the story!')
elif st.session_state['level'] == 3:
    st.markdown(mdtext4)
    st.button("Click me to make the paragraph bold!", on_click=increase, help='Let\'s go forward with the story!')
elif st.session_state['level'] == 4:
    st.markdown(mdtext5)
    st.button("Click me to make the paragraph italicized!", on_click=increase, help='Let\'s go forward with the story!')
elif st.session_state['level'] == 5:
    st.markdown(mdtext6)
    st.button("Click me to make the paragraph bold and italicized!", on_click=increase, help='Let\'s go forward with the story!')
elif st.session_state['level'] == 6:
    st.markdown(mdtext7)
    st.button("Click me to make the paragraph a quote!", on_click=increase, help='Let\'s go forward with the story!')
elif st.session_state['level'] == 7:
    st.markdown(mdtext8)
    st.button("Click me to help the list!", on_click=increase, help='Let\'s go forward with the story!')
elif st.session_state['level'] == 8:
    st.markdown(mdtext9)
    st.button("Click me to make the list numbered!", on_click=increase, help='Let\'s go forward with the story!')
elif st.session_state['level'] == 9:
    st.markdown(mdtext10)
    st.button("The line arrives", on_click=increase, help='Let\'s go forward with the story!')
elif st.session_state['level'] == 10:
    st.markdown(mdtext11)
    st.button("The link arrives", on_click=increase, help='Let\'s go forward with the story!')
elif st.session_state['level'] == 11:
    st.markdown(mdtext12)
    st.button("The image arrives", on_click=increase, help='Let\'s go forward with the story!')
elif st.session_state['level'] == 12:
    st.session_state['meme'] = grab_meme_url()
    st.markdown(mdtext13.replace("&&URL&&", st.session_state['meme']))
    st.button("Click me to see the markdown code!", on_click=increase, help='Show the markdown code!')
elif st.session_state['level'] == 13:
    st.markdown(mdtextfinish.replace("&&URL&&", st.session_state['meme']))

# Separate things a bit
st.write("")
st.write("")

st.button("Click me to reset the story!", on_click=init, help="Let's start over!")