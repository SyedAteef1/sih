import streamlit as st

from streamlit_option_menu import option_menu


import home, trending, test, your, about ,temp,livedata
st.set_page_config(
        page_title="Poly Pulley Failure",
)



class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        st.sidebar.image("data/SIH.png", caption="Online Analytics")
        with st.sidebar:        
            app = option_menu(
                menu_title='Poly Pulley Failure ',
                options=['Home','Account','Live Data','Manual prediction','about','temp'],
                icons=['house-fill','person-circle','chat','chat-fill','info-circle-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "Home":
            home.app()
        if app == "Account":
            test.app()    
        if app == "Live Data":
            livedata.app()        
        if app == 'Manual prediction':
            your.app()
        if app == 'temp':
            temp.app()
        if app == 'about':
            about.app() 
        
             
          
             
    run()            
         
