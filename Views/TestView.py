import streamlit as st
import time
from Controllers.QueryFunctions import *

def test_view() -> str:
    '''
    Casper
    This view is for test writes.
    '''
    st.title("This is a test view")
    # TESTING MOVIE SEARCH VIEW  

    # text = st.text_input(label="Search for a movie")

    # if st.button("Search"):
    #     results = search(text)
    #     if len(results) == 0:
    #         st.write("Sorry, we found no result.")
    #     else:
    #         for movie in results:
    #             st.subheader(movie.get_title())
    #             st.write(movie.get_year())
    #             st.write(movie.get_runtime())

    # TESTING FIND CAST QUERY FUNCTION
    # cast = find_cast(10)
    # for [member, role] in cast:
    #     st.subheader(member.get_name())
    #     st.write(member.get_birthYear())
    #     st.write(role)

    # TESTING COUNT CUSTOMER WATCHED FUNCTION
    # new_movie = Movie(mid=10, runtime=126, title='Iron Man', year=2008)
    # st.write(count_customer_watched(new_movie))

    # TESTING FOLLOW FUNCTION
    # follow(cid='c100', pid='p004')

    # Testing watch and end watch functions
    # sid = 18
    # cid = 'c300'
    # mid = 10
    # stime = watch(sid, cid, mid)
    # print(stime)
    # time.sleep(60)
    # end_watch(sid, cid, mid, stime)

    # Testing end_watch function
    # customer = Customer(cid='c300', name='Casper Nguyen', pwd='SCWinter')
    # session = start_session(customer)
    # time.sleep(60)
    # end_session(session)

    # buttons = []

    # for i in range(5):
    #     buttons.append(st.button(str(i)))

    # for i, button in enumerate(buttons):
    #     if button:
    #         st.write(f"{i} button was clicked")

    # button1 = st.button('Check 1')

    # if st.session_state.get('button') != True:

    #     st.session_state['button'] = button1

    # if st.session_state['button'] == True:

    #     st.write("button1 is True")

    #     if st.button('Check 2'):

    #         st.write("Hello, it's working")

    #         st.session_state['button'] = False

    #         st.checkbox('Reload')

    # TEST find_movie()
    # movie = find_movie(10)
    # print(movie.get_mid())
    # print(movie.get_title())
    # print(movie.get_year())
    # print(movie.get_runtime())