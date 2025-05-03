import streamlit as st
from datetime import timedelta, datetime, date
import os
import random
import requests
import uuid

st.set_page_config(
    page_title="Humiliation Place",
    initial_sidebar_state="expanded"
)

def calculate_days_difference(date_string):
    # Convert the input string to a date object
    input_date = datetime.strptime(date_string, "%Y-%m-%d").date()
    # Get today's date
    today = date.today()
    # Calculate the difference in days
    days_difference = (today - input_date).days
    return days_difference

def shuffle_array(arr):
    random.shuffle(arr)
    return arr

def download_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        st.error("Failed to fetch the image. Please check the URL.")
        return None

def days_to_string(days):
    if days == 0:
        return "today"
    elif days == 1:
        return "1 day ago"
    elif days < 7:
        return f"{days} days ago"
    elif days < 30:
        weeks = days // 7
        return f"{weeks} week{'s' if weeks > 1 else ''} ago"
    elif days < 365:
        months = days // 30
        return f"{months} month{'s' if months > 1 else ''} ago"
    else:
        years = days // 365
        return f"{years} year{'s' if years > 1 else ''} ago"

st.error('This product is in Alpha. There will be bugs and things will be broken. Please bear with us.')

st.title('Humiliation Place')

st.subheader('Browse the humiliation place, where you can say what you want about who you want!')

def Post(user_uuid, post_uuid, name, age, country, days, comments, category):
    imgPath = f"content/posts/users/{user_uuid}/{post_uuid}.jpg"
    
    with st.container():
        _content, _comments = st.columns(2)
        with _content:
            st.write("**" + name + "  |  " + age + "  |  " + country + "**")
            st.image(imgPath, caption="Posted " + days_to_string(days), width=300)

        with _comments:
            comment = st.text_input("Comment here", key=f'{user_uuid}_{post_uuid}_{category}_PCT')
            if st.button("Post Comment", key=f'{user_uuid}_{post_uuid}_{category}_PCB'):
                if comment.strip():  # Check if the comment is not empty
                    file_path = f"content/posts/users/{user_uuid}/{post_uuid}"  # Define the file path
                    with open(file_path, "a") as file:
                        file.write("\n" + comment)  # Append the comment to the file
                    st.success("Comment posted!")
                else:
                    st.warning("Comment cannot be empty.")

            st.divider()

            st.write("**Comments:**")

            if len(comments) > 5:
                for i in range(5):
                    if comments[i] != "":
                        st.write("*" + comments[i] + "*")
            else:
                for i in range(len(comments)):
                    if comments[i] != "":
                        st.write("*" + comments[i] + "*")
            
            if len(comments) > 5:
                st.write("*AND MORE...*")

def ShowPosts(category):
    didRun = False
    for details in shuffle_array(os.listdir("content/" + category)):
        didRun = True
        if not details.startswith("."):
            file_path = "content/posts/users/" + details.replace(" ", "/")

            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    _post = []
                    for line in file:
                        _post.append(line.strip())

                    _post.append("")
                    
                    Post(details.split(" ")[0], details.split(" ")[1], _post[0], _post[1], _post[2], calculate_days_difference(_post[3]), shuffle_array(_post[5:]), category)
            
                    st.divider()
            # else:
            #     print(f"The file '{file_path}' does not exist. The post was probably deleted.")
    # if not didRun:
    #     st.info("No posts available for this category.")
    
def Browse():
    st.write('**Filter by:**')

    sex, age = st.tabs(["Sex", "Age"])
    with sex:
        with st.expander("Male"):
            ShowPosts("male")
        with st.expander("Female"):
            ShowPosts("female")
        with st.expander("Trans & Other Identifications"):
            ShowPosts("trans")
    with age:
        with st.expander("18 To 21"):
            ShowPosts("under 22")
        with st.expander("Under 30"):
            ShowPosts("under 30")
        with st.expander("30 or Older"):
            ShowPosts("30 or older")

if st.checkbox('I have read and agree to the waiver.'):
    Browse()
# else:
#     st.divider()

#     st.write('**By using this product, you agree that you are 18 or over, and to the following terms:**')
#     st.write('1. You are responsible for the content you post.')
#     st.write('2. You will not post any illegal or harmful content.')
#     st.write('3. You will not post any content that violates the rights of others.')
#     st.write('4. You will not post any content that is offensive or cruel.')
#     st.write('5. You will not post any content that is spam or advertising.')
#     st.write('6. You will not post any content that is threatening or could be considered blackmail.')
#     st.write('7. You will not post any content that invovles a minor whether in front or behind the camera.')
