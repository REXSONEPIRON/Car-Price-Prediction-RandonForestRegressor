import requests
import streamlit as st
import pandas as pd
import pickle as pk
from streamlit_lottie import _st_lottie


st.set_page_config(page_title='Car Price Prediction App',page_icon=':car:',layout='wide')
model=pk.load(open('mode.pkl','rb'))

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#<h4 style="color:white;text-align:center;"> Car Price Prediction using ML Model.. </h4>
html_temp = """
		<div style="background-color:#1C3334;padding:09px;border-radius:06px">
		<h1 style="color:White;text-align:center;"> Car Price Prediction </h1>
		</div>
		"""

#st.radio('Select Owner: ',car_data['owner'].unique(), horizontal=True)
# m = st.markdown("""
# <style>
# div.stButton > button:first-child {
#     background-color: #1C3334;
#     color:#ffffff;
# }
# # div.stButton > button:hover {
# #     background-color: #1C3334;
# #     color:#1C3334;
#     }
# </style>""", unsafe_allow_html=True)

def main():
        # st.html(html_temp)
    # st.html(html_temp)
    # if st.button('Go to form'):

    df=pd.read_csv('Cardetails.csv')

    def get_brand_name(car_name):
        car_name=car_name.split(' ')[0]
        return car_name.strip()         
        return float(value)

    df['name']=df['name'].apply(get_brand_name)
        # name	year	km_driven	fuel	seller_type	transmission	owner	mileage	engine	seats
        # st.dataframe(car_data)
    st.html(html_temp)
   
    c1,c2,c3=st.columns(3)
    
    name=c1.selectbox('Select the Brand: ',df['name'].unique())
    year=c1.number_input("Year", min_value=1994, max_value=2020, step=1)
    km_driven=c1.number_input(label="Enter the KMS Driven",placeholder="Enter the KMS Driven of Your Car",value=None,min_value=11,max_value=200000,step=100)
    seats=c1.number_input('No of seats: ',min_value=5,max_value=10,step=1)

    fuel=c2.radio('Select the Fuel type:',df['fuel'].unique(),horizontal=True)
    mileage=c2.slider('Select mileage: ',10,42)
    transmission=c2.selectbox('Select transmission: ',df['transmission'].unique())

    owner=c3.selectbox('Select Owner: ',df['owner'].unique())
    seller_type=c3.selectbox('Select Seller Type: ',df['seller_type'].unique()) 
    engine=c3.slider('Select Engine CC: ',700,5000)
    
 
    with st.container():
        st.write("---")
        st.header("Contact Us ")
        st.write("##")##contract form
        contact_form = """
        <form action="https://formsubmit.co/ds215229132@bhc.edu.in" method="POST">
            <input type="hidden" name = "_captcha" value = "false">
            <input type="text" name="name" placeholder = "Your Name" required>
            <input type="email" name="email" placeholder = "Your Email" required>
            <textarea name = "message" placeholder = "Your Message Here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """

        left,right = st.columns(2)
        with left:
            st.markdown(contact_form, unsafe_allow_html = True)
    
        with right.expander("Click here to Download Source File"):
            st.download_button('Download',data=df.to_csv().encode('utf-8'),
                           file_name='car_details.csv',mime=('text/csv')) 
    def lottieurl(url):
            r = requests.get(url)
            if r.status_code !=200:
                return None
            return r.json()
       
    lottie_coading = lottieurl("https://lottie.host/1c47a0e6-cee7-4d57-a604-3ede224cd44e/l9DB7DsxYD.json")

    with right:
        st.lottie(lottie_coading,height=500, key = "coading")

    with left:
        st.header('Conclusion')
        st.write('This machine learning model has been developed and trained using historical data.')
        st.write('We applied three models LinearRegression,DecisionTreeRegressor,and RandomForestRegressor and KNeighborsRegressor.')
        st.write('As we can see RandomForestRegressor performing best (with accuracy ~ 0.96).')
        st.write('We kindly request your suggestions and feedback for our web application. Your insights will help us enhance the model, and we welcome any code contributions that could assist in fine-tuning its performance.')
        st.write('If you require the source code, clarification about the deployment process, or any other related information regarding this web application, please feel free to contact us through the "Contact Us" section.')
        st.write('We appreciate your feedback and suggestions. Please feel free to get in touch with us through the "Contact Us" section. Thank you for visiting our web application.')
    if c3.button('predict'):
        input_data_module=pd.DataFrame(
            [[name,year,km_driven,fuel,seller_type,transmission,owner,mileage,engine,seats]],
            columns=['name','year','km_driven','fuel','seller_type','transmission','owner','mileage','engine','seats']
            )
    #     
  
        # st.dataframe(input_data_module)
    # with c3.expander("Click here to view your selected values"):
    #     st.dataframe(input_data_module) 
        

        input_data_module['owner'].replace(['First Owner', 'Second Owner', 'Third Owner','Fourth & Above Owner', 'Test Drive Car'],[1,2,3,4,5],inplace=True)
        input_data_module['transmission'].replace(['Manual', 'Automatic'],[1,2],inplace=True)
        input_data_module['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'],[1,2,3],inplace=True)
        input_data_module['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'],[1,2,3,4],inplace=True)
        input_data_module['name'].replace(['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
            'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
            'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
            'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
            'Ambassador', 'Ashok', 'Isuzu', 'Opel'],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],inplace=True)
        # car=model.predict(input_data_module)
        # st.write(car)
    #Making Prediction by Trained ML Model)
        car_price=model.predict(input_data_module)
        if car_price>=0:
            with c3.expander("Click here to view your selected values"):
                st.dataframe(input_data_module) 
            c2.success('Predicted Price of Your Car is :' + str(car_price[0].round(2)), icon="✅")
            c2.link_button('Click Here to view My Profile','https://www.linkedin.com/in/rexson-epiron-a55814220')
            # c3.dataframe(,input_data_module)
        else:
            c2.error("Predicted Price is Below Zero, Please select Valid Inputs.", icon="⚠️")

        # if y_final_pred:

        #     if any([name is None, year is None, km_driven is None, fuel is None, seller_type is None,mileage is None,owner is None,transmission is None,engine is None,seats is None]):
        #       st.error("Please, Select all Inputs before Pressing Predict Button.",icon="📝")
        #     else:
        #         y_final_pred = model.predict(input_data_module)
        #         if y_final_pred < 0:
        #             st.error("Predicted Price is Below Zero, Please select Valid Inputs.", icon="⚠️")
           
        #         else:
        #              c2.success(f"Predicted Price of Your Car is : ₹{y_final_pred:,.0f}", icon="✅")
        # #            c2.link_button('About-Me😎','https://www.linkedin.com/in/rexson-epiron-a55814220')
            
    #     c2.link_button('Click Here to view My Profile','https://www.linkedin.com/in/rexson-epiron-a55814220')
    # #https://github.com/REXSONEPIRON
if __name__=='__main__':
    main()