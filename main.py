import streamlit as st
import requests
import json
from datetime import datetime
from streamlit_lottie import st_lottie
import base64


api_key_weather = '637663a2023233bce72b2c328744c62e'
api_key_time = 'U04UNIVUNXPM'
api_key_windy = '1Dh73IxM8eWmhOAFIn0PtJQSSDPK5Qbv'


def get_weather(city):
    request_url_weather = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key_weather}&units=metric'
    response_weather = requests.get(request_url_weather)
    
    data_weather = response_weather.json()
    if data_weather['cod'] == 200:
        
        global show_Weather
        global show_Country
        show_Weather = data_weather['weather'][0]['description'].title()
        show_Country = data_weather['sys']['country']
        temperature_Celsius = data_weather['main']['temp']
        humidity_level = data_weather['main']['humidity']
        wind_speed = data_weather['wind']['speed']
        wind_degree = data_weather['wind']['deg']
        temperature_Fahrenheit = round(data_weather['main']['temp'] + 273.15, 2)
        coordinate_Longitude = data_weather['coord']['lon']
        coordinate_Latitude = data_weather['coord']['lat']

        global show_Fahrenheit
        global show_Celsius
        global show_Humidity
        global show_Wspeed
        global show_Wdegree
        global Longitude
        global Latitude

        show_Fahrenheit = str(temperature_Fahrenheit)
        show_Celsius = str(temperature_Celsius)
        show_Humidity = str(humidity_level)
        show_Wspeed = str(wind_speed)
        show_Wdegree = str(wind_degree)
        Longitude = str(coordinate_Longitude)
        Latitude = str(coordinate_Latitude)

        
        global result
        result = 1        
    else:
        result = 0
        


def get_time():
    request_url_time = f'http://api.timezonedb.com/v2.1/get-time-zone?key={api_key_time}&format=json&by=position&lat={Latitude}&lng={Longitude}'
    response_time = requests.get(request_url_time)
    
    global Time
    Time = []

    if response_time.status_code == 200:
        data_Time = response_time.json()
        initial_Time = data_Time['formatted']
        split_dateTime = initial_Time.split(' ')
        del split_dateTime[0]
        convertToString = ''.join(split_dateTime)
        split_dateTime2 = convertToString.split(':')
        convertToInteger = [int(x) for x in split_dateTime2]

        if convertToInteger[0] > 12:
            hour = convertToInteger[0] - 12
            convertToInteger[0] = hour
            intToString = [str(x) for x in convertToInteger]
            show_Time = ':'.join(intToString)
            show_Time_PM = show_Time + ' PM'
            Time.clear()
            Time.append(show_Time_PM)

        else:
            intToString = [str(x) for x in convertToInteger]
            show_Time = ':'.join(intToString)
            show_Time_AM = show_Time + ' AM'
            Time.clear()
            Time.append(show_Time_AM)

#######3 gonna delete



def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


with open('cities.json', 'r') as file:
    cities_name = json.load(file)
cities = cities_name['cities']


st.set_page_config (
    page_title = "Weather Checker",
    page_icon = ":partly_sunny:",
    initial_sidebar_state = "collapsed"
    )




hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    div[data-testid="stDecoration"] {
    visibility: hidden;
    height: 0%;
    position: fixed;
    }
    div[data-testid="stStatusWidget"] {
    visibility: hidden;
    height: 0%;
    position: fixed;
    }
    </style>
    """
    
st.markdown(hide_menu_style, unsafe_allow_html = True)


    
    
#Set background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>

    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: 200%;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """, unsafe_allow_html = True)

add_bg_from_local('misc/background_img.png')






lottie_anim1 = load_lottiefile('lottie_anim/anim1.json')
lottie_anim2 = load_lottiefile('lottie_anim/anim2.json')

###########################################################################################

#SideBar (about)
with st.sidebar:
    col1, col2 = st.columns([3,2])

    with col1:
        container = st.container()
        container.markdown('')
        container.markdown('<p class="sidebar">About</p>', unsafe_allow_html = True)

    with col2:
        st_lottie(lottie_anim1, loop = True, quality = 'high')
        st.sidebar.info("""This app can quickly and easily check the current temperature,
        humidity, wind speed, and more for any location in the world.""")

    st.write("***")
    st.markdown(f""" Developed by ***KarGalan*** """, unsafe_allow_html = True)


st.markdown("""
    <style>
    .big-font {
    font-size: 80px;
    font-family: sans-serif;
    font-weight: bold;
    animation: fadeIn 3s;
    animation-delay: 2s;
    -webkit-animation: fadeIn 3s;
    -moz-animation: fadeIn 3s;
    -o-animation: fadeIn 3s;
    -ms-animation: fadeIn 3s;
    }
    @keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
    }

    @-moz-keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
    }

    @-webkit-keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
    }

    @-o-keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
    }

    @-ms-keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
    }
    </style>
    """, unsafe_allow_html = True)


c1, c2, c3 = st.columns([1,40,1])

st.markdown("""
    <style>
    [data-testid=column]:nth-of-type(2) [data-testid=stVerticalBlock] {
    gap: 0rem;
    }
    </style>
    """,unsafe_allow_html=True)

with c2:
    links="""
    <style>
    a:link , a:visited {
    color: skyblue;
    font-style: italic;
    background-color: transparent;
    text-decoration: none;
    }
    a:hover , a:active {
    color: white;
    font-style: italic;
    background-color: transparent;
    text-decoration: none;
    }
    </style>
    """
    #anim
    st.markdown("""
    <style>
    .norm {
    animation: fadeIn 3s;
    animation-delay: 7s;
    -webkit-animation: fadeIn 3s;
    -moz-animation: fadeIn 3s;
    -o-animation: fadeIn 3s;
    -ms-animation: fadeIn 3s;
    }
    @keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
    }

    @-moz-keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
    }

    @-webkit-keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
    }

    @-o-keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
    }

    @-ms-keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
    }
    </style>
    """, unsafe_allow_html = True)

    st_lottie(lottie_anim2, loop = True, quality = 'high', height = 100)
    c2.markdown('<p class="big-font">Weather Checker</p>', unsafe_allow_html = True)
    #links
    c2.markdown(links, unsafe_allow_html=True)
    streamlit_link = '<a href="https://www.streamlit.io">Streamlit</a>'
    openweather_link = '<a href="https://www.openweathermap.org">OpenWeather</a>'
  

    buff, col, buff2 = st.columns([1.6,6,1])
    col.markdown(f"""<p class="norm">Powered by {streamlit_link} and {openweather_link}</p>""", unsafe_allow_html = True)

st.markdown("""
    <style>
    .centered-title {
        font-size: 40px; 
        font-weight: bold;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="centered-title">Choose city</p>', unsafe_allow_html=True)
st.markdown('')

col1, col2 = st.columns([4, 1])

with col1:
    selected_city = st.selectbox('Choose city', options=cities, label_visibility='collapsed')

with col2:
    clicked_getwr_button = st.button('Get Weather', help=('Click'), type='primary')



st.markdown('***')

##weather got########################################################################################################################
def weather():
    weather_data = get_weather(selected_city)
    st.markdown(f'{show_Fahrenheit}°F')
    st.markdown(f'{show_Celsius}°C')
    st.markdown(f'{Longitude}')
    st.markdown(f'{Latitude}')
    st.markdown(f'{show_Wspeed}')
    if result ==1:
        get_time()
        st.markdown(f'{Time}')
        
        
    with st.container():
            tab0, tab1, tab2, tab3 = st.tabs(["\u2001\u2001\u2001\u2001OVERVIEW\u2001\u2001\u2001\u2001", "\u2001\u2001\u2001\u2001HUMIDITY\u2001\u2001\u2001\u2001", "\u2001\u2001\u2001\u2001WIND\u2001\u2001\u2001\u2001", "\u2001\u2001\u2001TEMPERATURE\u2001\u2001\u2001\u2001"])

            st.markdown("""
            <style>
            .med-font {
            font-size: 75px;
            font-family: sans-serif;
            font-weight: bold;
            }
            </style>
            """, unsafe_allow_html = True)

            st.markdown("""
            <style>
            .medb-font {
            font-size: 60px;
            font-family: sans-serif;
            font-weight: bold;
            color: skyblue;
            }
            </style>
            """, unsafe_allow_html = True)

            st.markdown("""
            <style>
            .sm-font {
            font-size: 30px;
            font-family: sans-serif;
            font-weight: bold;
            color: skyblue;
            opacity: 0.7;
            }
            </style>
            """, unsafe_allow_html = True)

            windy = f'<a href="https://www.windy.com/?{Latitude},{Longitude},11" style="text-decoration: none; color: skyblue; opacity: 0.7">See more</a>'
            windy_fm = f'<a style="text-decoration: none; font-size: 14px; font-family: sans-serif; color: white; opacity: 0.3;">Forecast Model: ECMWF\u2001\u2001\u2001\u2001・\u2001\u2001\u2001\u2001***{windy}***</a>'

            with tab0:
                st.markdown("")
                st.markdown("")

                buff1, col1, col2, buff2 = st.columns([5,100,30,4])

                d_weather_thun = load_lottiefile('weather_icons/d-thunderstorm.json')
                d_weather_clouds = load_lottiefile('weather_icons/d-clouds.json')
                d_weather_drizzlerain = load_lottiefile('weather_icons/d-drizzle-rain.json')
                d_weather_snowsleet = load_lottiefile('weather_icons/d-snow-sleet.json')
                d_weather_clear = load_lottiefile('weather_icons/d-clear.json')
                n_weather_thun = load_lottiefile('weather_icons/n-thunderstorm.json')
                n_weather_clouds = load_lottiefile('weather_icons/n-clouds.json')
                n_weather_drizzlerain = load_lottiefile('weather_icons/n-drizzle-rain.json')
                n_weather_snowsleet = load_lottiefile('weather_icons/n-snow-sleet.json')
                n_weather_clear = load_lottiefile('weather_icons/n-clear.json')

                with col1:
                    st.markdown("""
                    <style>
                    .invi-font {
                    font-size: 25px;
                    font-family: sans-serif;
                    font-weight: bold;
                    color: transparent;
                    }
                    </style>
                    """, unsafe_allow_html = True)

                    st.markdown("""
                    <style>
                    .time-font {
                    font-size: 15px;
                    font-family: sans-serif;
                    color: gray;
                    opacity: 0.5;
                    }
                    </style>
                    """, unsafe_allow_html = True)

                    whatTime = ''.join(Time)

                    container = st.container()
                    link = f'<a href="https://www.google.com/maps/search/?api=1&query={selected_city}" style="text-decoration: none; color: skyblue;">{selected_city.title()}</a>'

                    container.markdown("<p class='invi-font'>_</p>", unsafe_allow_html = True)
                    container.markdown(f""" 
                    ## The weather in {link} <br/> is ***{show_Weather.title()}***.
                    """, unsafe_allow_html = True)

                    container.markdown(f"<p class='time-font'>{whatTime} ・ {show_Country}</p>", unsafe_allow_html = True)

                with col2:
                    st.markdown("")
                    st.markdown("")
                    weather_desc = ['Thunderstorm', 'Drizzle', 'Rain', 'Snow', 'Sleet', 'Clear', 'Clouds']
                    showTime = ''.join(Time)
                    if showTime[2] == ':':
                        timeShow = 1
                    elif showTime[1] == ':':
                        timeShow = 0
                    for weather in weather_desc:
                        if weather in str(show_Weather):
                            weatherlink = str(weather)
                            if weatherlink == 'Thunderstorm':
                                if ('AM' in showTime) and (int(showTime[0]) < 5) and (timeShow == 0):
                                    st_lottie(n_weather_thun, loop = True, quality = "high", height = 150, key = 'n_weather_thun_am')
                                    break
                                elif ('PM' in showTime) and ((showTime[:2]) == '12'):
                                    st_lottie(n_weather_thun, loop = True, quality = "high", height = 150, key = 'midnight_thun')
                                    break
                                elif 'AM' in showTime:
                                    st_lottie(d_weather_thun, loop = True, quality = "high", height = 150, key = 'd_weather_thun_am')
                                    break
                                elif ('PM' in showTime) and (int(showTime[0]) < 6) and (timeShow == 0):
                                    st_lottie(d_weather_thun, loop = True, quality = "high", height = 150, key = 'd_weather_thun_pm')
                                    break
                                elif ('PM' in showTime) and (timeShow == 1):
                                    st_lottie(n_weather_thun, loop = True, quality = "high", height = 150, key = 'n_thun_pm')
                                    break
                                else:
                                    st_lottie(n_weather_thun, loop = True, quality = "high", height = 150, key = 'n_weather_thun_pm')
                                    break
                            elif weatherlink == 'Drizzle':
                                if ('AM' in showTime) and (int(showTime[0]) < 5) and (timeShow == 0):
                                    st_lottie(n_weather_drizzlerain, loop = True, quality = "high", height = 150, key = 'n_weather_drizzle_am')
                                    break
                                elif ('PM' in showTime) and ((showTime[:2]) == '12'):
                                    st_lottie(n_weather_drizzlerain, loop = True, quality = "high", height = 150, key = 'midnight_drizz')
                                    break
                                elif 'AM' in showTime:
                                    st_lottie(d_weather_drizzlerain, loop = True, quality = "high", height = 150, key = 'd_weather_drizzle_am')
                                    break
                                elif ('PM' in showTime) and (int(showTime[0]) < 6) and (timeShow == 0):
                                    st_lottie(d_weather_drizzlerain, loop = True, quality = "high", height = 150, key = 'd_weather_drizzle_pm')
                                    break
                                elif ('PM' in showTime) and (timeShow == 1):
                                    st_lottie(n_weather_drizzlerain, loop = True, quality = "high", height = 150, key = 'n_drizzle_pm')
                                    break
                                else:
                                    st_lottie(n_weather_drizzlerain, loop = True, quality = "high", height = 150, key = 'n_weather_drizzle_pm')
                                    break
                            elif weatherlink == 'Rain':
                                if ('AM' in showTime) and (int(showTime[0]) < 5) and (timeShow == 0):
                                    st_lottie(n_weather_drizzlerain, loop = True, quality = "high", height = 150, key = 'n_weather_rain_am')
                                    break
                                elif ('PM' in showTime) and ((showTime[:2]) == '12'):
                                    st_lottie(n_weather_drizzlerain, loop = True, quality = "high", height = 150, key = 'midnight_rain')
                                    break
                                elif 'AM' in showTime:
                                    st_lottie(d_weather_drizzlerain, loop = True, quality = "high", height = 150, key = 'd_weather_rain_am')
                                    break
                                elif ('PM' in showTime) and (int(showTime[0]) < 6) and (timeShow == 0):
                                    st_lottie(d_weather_drizzlerain, loop = True, quality = "high", height = 150, key = 'd_weather_rain_pm')
                                    break
                                elif ('PM' in showTime) and (timeShow == 1):
                                    st_lottie(n_weather_drizzlerain, loop = True, quality = "high", height = 150, key = 'n_rain_pm')
                                    break
                                else:
                                    st_lottie(n_weather_drizzlerain, loop = True, quality = "high", height = 150, key = 'n_weather_rain_pm')
                                    break
                            elif weatherlink == 'Snow':
                                if ('AM' in showTime) and (int(showTime[0]) < 5) and (timeShow == 0):
                                    st_lottie(n_weather_snowsleet, loop = True, quality = "high", height = 150, key = 'n_weather_snow_am')
                                    break
                                elif ('PM' in showTime) and ((showTime[:2]) == '12'):
                                    st_lottie(n_weather_snowsleet, loop = True, quality = "high", height = 150, key = 'midnight_snow')
                                    break
                                elif 'AM' in showTime:
                                    st_lottie(d_weather_snowsleet, loop = True, quality = "high", height = 150, key = 'd_weather_snow_am')
                                    break
                                elif ('PM' in showTime) and (int(showTime[0]) < 6) and (timeShow == 0):
                                    st_lottie(d_weather_snowsleet, loop = True, quality = "high", height = 150, key = 'd_weather_snow_pm')
                                    break
                                elif ('PM' in showTime) and (timeShow == 1):
                                    st_lottie(n_weather_snowsleet, loop = True, quality = "high", height = 150, key = 'n_snow_pm')
                                    break
                                else:
                                    st_lottie(n_weather_snowsleet, loop = True, quality = "high", height = 150, key = 'n_weather_snow_pm')
                                    break
                            elif weatherlink == 'Sleet':
                                if ('AM' in showTime) and (int(showTime[0]) < 5) and (timeShow == 0):
                                    st_lottie(n_weather_snowsleet, loop = True, quality = "high", height = 150, key = 'n_weather_sleet_am')
                                    break
                                elif ('PM' in showTime) and ((showTime[:2]) == '12'):
                                    st_lottie(n_weather_snowsleet, loop = True, quality = "high", height = 150, key = 'midnight_sleet')
                                    break
                                elif 'AM' in showTime:
                                    st_lottie(d_weather_snowsleet, loop = True, quality = "high", height = 150, key = 'd_weather_sleet_am')
                                    break
                                elif ('PM' in showTime) and (int(showTime[0]) < 6) and (timeShow == 0):
                                    st_lottie(d_weather_snowsleet, loop = True, quality = "high", height = 150, key = 'd_weather_sleet_pm')
                                    break
                                elif ('PM' in showTime) and (timeShow == 1):
                                    st_lottie(n_weather_snowsleet, loop = True, quality = "high", height = 150, key = 'n_sleet_pm')
                                    break
                                else:
                                    st_lottie(n_weather_snowsleet, loop = True, quality = "high", height = 150, key = 'n_weather_sleet_pm')
                                    break
                            elif weatherlink == 'Clear':
                                if ('AM' in showTime) and (int(showTime[0]) < 5) and (timeShow == 0):
                                    st_lottie(n_weather_clear, loop = True, quality = "high", height = 150, key = 'n_weather_clear_am')
                                    break
                                elif ('PM' in showTime) and ((showTime[:2]) == '12'):
                                    st_lottie(n_weather_clear, loop = True, quality = "high", height = 150, key = 'midnight_clear')
                                    break
                                elif 'AM' in showTime:
                                    st_lottie(d_weather_clear, loop = True, quality = "high", height = 150, key = 'd_weather_clear_am')
                                    break
                                elif ('PM' in showTime) and (int(showTime[0]) < 6) and (timeShow == 0):
                                    st_lottie(d_weather_clear, loop = True, quality = "high", height = 150, key = 'd_weather_clear_pm')
                                    break
                                elif ('PM' in showTime) and (timeShow == 1):
                                    st_lottie(n_weather_clear, loop = True, quality = "high", height = 150, key = 'n_clear_pm')
                                    break
                                else:
                                    st_lottie(n_weather_clear, loop = True, quality = "high", height = 150, key = 'n_weather_clear_pm')
                                    break
                            elif weatherlink == 'Clouds':
                                if ('AM' in showTime) and (int(showTime[0]) < 5) and (timeShow == 0):
                                    st_lottie(n_weather_clouds, loop = True, quality = "high", height = 150, key = 'n_weather_clouds_am')
                                    break
                                elif ('PM' in showTime) and ((showTime[:2]) == '12'):
                                    st_lottie(n_weather_clouds, loop = True, quality = "high", height = 150, key = 'midnight_clouds')
                                    break
                                elif 'AM' in showTime:
                                    st_lottie(d_weather_clouds, loop = True, quality = "high", height = 150, key = 'd_weather_clouds_am')
                                    break
                                elif ('PM' in showTime) and (int(showTime[0]) < 6) and (timeShow == 0):
                                    st_lottie(d_weather_clouds, loop = True, quality = "high", height = 150, key = 'd_weather_clouds_pm')
                                    break
                                elif ('PM' in showTime) and (timeShow == 1):
                                    st_lottie(n_weather_clouds, loop = True, quality = "high", height = 150, key = 'n_clouds_pm')
                                    break
                                else:
                                    st_lottie(n_weather_clouds, loop = True, quality = "high", height = 150, key = 'n_weather_clouds_pm')
                                    break
                            else:
                                if ('AM' in showTime) and (int(showTime[0]) < 5) and (timeShow == 0):
                                    st_lottie(n_weather_clouds, loop = True, quality = "high", height = 150, key = 'n_weather_am')
                                    break
                                elif ('PM' in showTime) and ((showTime[:2]) == '12'):
                                    st_lottie(n_weather_clear, loop = True, quality = "high", height = 150, key = 'midnight')
                                    break
                                elif 'AM' in showTime:
                                    st_lottie(d_weather_clouds, loop = True, quality = "high", height = 150, key = 'd_weather_am')
                                    break
                                elif ('PM' in showTime) and (int(showTime[0]) < 6) and (timeShow == 0):
                                    st_lottie(d_weather_clouds, loop = True, quality = "high", height = 150, key = 'd_weather_pm')
                                    break
                                elif ('PM' in showTime) and (timeShow == 1):
                                    st_lottie(n_weather_clouds, loop = True, quality = "high", height = 150, key = 'n_none_pm')
                                    break
                                else:
                                    st_lottie(n_weather_clouds, loop = True, quality = "high", height = 150, key = 'n_weather_pm')
                                    break

                wnd = show_Wspeed.split('.')
                if wnd and len(wnd) >= 2:
                    wnds = str(wnd[0]) + '.' + str(wnd[1][0])
                else:
                    wnds = str(wnd[0]) 
                fwnd = float(wnds)

                tmp = show_Celsius.split('.')
                tmps = str(tmp[0])
                ftmp = int(tmps)

                st.markdown("""
                <style>
                .overview-sign {
                font-size: 65px;
                opacity: 1;
                word-spacing: -3px;
                line-height: 1;
                transition: transform .2s;
                }

                .overview-text {
                font-size: 45px;
                font-family: sans-serif;
                font-weight: bold;
                color: white;
                line-height: 1;
                word-spacing: -3px;
                }

                .overview-text2 {
                font-size: 20px;
                font-family: sans-serif;
                font-weight: bold;
                color: gray;
                line-height: 1;
                word-spacing: 13px;
                }
                </style>
                """, unsafe_allow_html = True)

                st.write("")
                st.write("")
                cl1, cl2, cl3 = st.columns([70,70,70])

                with cl1:
                    space, text1, text2, space2 = st.columns([15,55,50,15])
                    with text1:
                        st.markdown('<p class="overview-sign">&#x1F4A7;</p>', unsafe_allow_html = True)
                    with text2:
                        st.markdown(f'<p class="overview-text">{show_Humidity}</p>', unsafe_allow_html = True)
                        st.markdown(f'<p class="overview-text2">%</p>', unsafe_allow_html = True)

                with cl2:
                    space, text3, text4, space2 = st.columns([15,55,50,5])
                    with text3:
                        st.markdown('<p class="overview-sign">&#x1F4A8;</p>', unsafe_allow_html = True)
                    with text4:
                        st.markdown(f'<p class="overview-text">{fwnd}</p>', unsafe_allow_html = True)
                        st.markdown(f'<p class="overview-text2">mph</p>', unsafe_allow_html = True)

                with cl3:
                    space, text5, text6, space2 = st.columns([15,55,50,5])
                    with text5:
                        st.markdown('<p class="overview-sign">&#x1F321;&#xFE0F;</p>', unsafe_allow_html = True)
                    with text6:
                        st.markdown(f'<div class="overview-text">{ftmp}</div>', unsafe_allow_html = True)
                        st.markdown(f'<div class="overview-text2">°C</div>', unsafe_allow_html = True)

                windy_view = f'<a style="text-decoration: none; font-size: 14px; font-family: sans-serif; color: white; opacity: 0.3;">Forecast Model: ECMWF\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001\u2001***{windy}***</a>'
                st.markdown('')
                st.write("***")

                st.markdown(f'<iframe width="700" height="400" src="https://embed.windy.com/embed2.html?lat={Latitude}&lon={Longitude}&detailLat={Latitude}&detailLon={Longitude}&width=650&height=450&zoom=11&level=surface&overlay=clouds&product=ecmwf&menu=None&message=&marker=&calendar=now&pressure=&type=map&location=coordinates&detail=&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1" frameborder="2"></iframe>', unsafe_allow_html = True)
                st.markdown(windy_view, unsafe_allow_html = True)

            with tab1:
                st.markdown("")
                st.markdown("")

                c1, c2 = st.columns([48,50])
                st.markdown("""
                    <style>
                    [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
                    gap: 0rem;
                    }
                    </style>
                    """,unsafe_allow_html=True)
                
                with c1:
                    st.markdown("""
                    <style>
                    .def-font {
                    font-size: 21px;
                    font-family: sans-serif;
                    text-align: justify;
                    color: white;
                    line-height: 1;
                    }
                    </style>
                    """, unsafe_allow_html = True)

                    humsign = f'<a style="text-decoration: none; font-size: 50px; font-family: sans-serif; font-weight: bold; color: white; opacity: 0.4;">%</a>'
                    hum = st.markdown(f'<p class="med-font">{show_Humidity}{humsign}</p>', unsafe_allow_html = True)
                    humd = st.markdown(f'<p class="sm-font">0.{show_Humidity} &#x1F4A7;</p>', unsafe_allow_html = True)

                    st.write("***")
                    st.markdown('<a class="def-font" style="color: white;">Humidity is the amount of water vapor in the air. If there is a lot of water vapor in the air, the humidity will be high. The higher the humidity, the wetter it feels outside.</a>', unsafe_allow_html = True)

                with c2:
                    st.markdown(windy_fm, unsafe_allow_html = True)
                    st.markdown(f'<iframe width="350" height="350" src="https://embed.windy.com/embed2.html?lat={Latitude}&lon={Longitude}&detailLat={Latitude}&detailLon={Longitude}&width=650&height=450&zoom=11&level=surface&overlay=rh&product=ecmwf&menu=None&message=&marker=&calendar=now&pressure=&type=map&location=coordinates&detail=&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1" frameborder="10"></iframe>', unsafe_allow_html = True)
                    st.image('misc/humid-hue.png')
                
            with tab2:
                st.markdown("")
                st.markdown("")

                c1, c2 = st.columns([48,50])
                st.markdown("""
                    <style>
                    [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
                    gap: 0rem;
                    }
                    </style>
                    """,unsafe_allow_html=True)
                
                with c1:
                    st.markdown("""
                    <style>
                    .def-font {
                    font-size: 21px;
                    font-family: sans-serif;
                    text-align: justify;
                    color: white;
                    line-height: 1;
                    }
                    </style>
                    """, unsafe_allow_html = True)

                    windsign = f'<a style="text-decoration: none; font-size: 50px; font-family: sans-serif; font-weight: bold; color: white; opacity: 0.4;">mph</a>'
                    wndsp = st.markdown(f'<p class="med-font">{show_Wspeed}{windsign}</p>', unsafe_allow_html = True)
                    wnddg = st.markdown(f'<p class="sm-font">{show_Wdegree}° &#x1F4A8;</p>', unsafe_allow_html = True)
                    
                    st.write("***")
                    st.markdown("""<a class="def-font" style="color: white;">Wind is the movement of air, caused by the uneven heating of the Earth by the sun and the Earth's own rotation. Winds range from light breezes to natural hazards such as hurricanes and tornadoes.</a>""", unsafe_allow_html = True)
                
                with c2:
                    st.markdown(windy_fm, unsafe_allow_html = True)
                    st.markdown(f'<iframe width="350" height="350" src="https://embed.windy.com/embed2.html?lat={Latitude}&lon={Longitude}&detailLat={Latitude}&detailLon={Longitude}&width=650&height=450&zoom=11&level=surface&overlay=wind&product=ecmwf&menu=None&message=&marker=&calendar=now&pressure=&type=map&location=coordinates&detail=&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1" frameborder="10"></iframe>', unsafe_allow_html = True)
                    st.image('misc/wind-hue.png')

            with tab3:
                st.markdown("")
                st.markdown("")

                c1, c2 = st.columns([48,50])
                st.markdown("""
                    <style>
                    [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
                    gap: 0rem;
                    }
                    </style>
                    """,unsafe_allow_html=True)
                
                with c1:
                    st.markdown("""
                    <style>
                    .def-font {
                    font-size: 21px;
                    font-family: sans-serif;
                    text-align: justify;
                    color: white;
                    line-height: 1;
                    }
                    </style>
                    """, unsafe_allow_html = True)

                    tempsign = f'<a style="text-decoration: none; font-size: 50px; font-family: sans-serif; font-weight: bold; color: white; opacity: 0.4;">°C</a>'
                    cel = st.markdown(f'<p class="med-font">{show_Celsius}{tempsign}</p>', unsafe_allow_html = True)
                    fahr = st.markdown(f'<p class="sm-font">{show_Fahrenheit}°F &#x1F321;&#xFE0F;</p>', unsafe_allow_html = True)
                    
                    st.write("***")
                    st.markdown("""<a class="def-font" style="color: white;">Temperature is the measure of hotness or coldness expressed in terms of any of several scales, including Fahrenheit and Celsius. Temperature indicates the direction in which heat energy will spontaneously flow.</a>""", unsafe_allow_html = True)
                
                with c2:
                    st.markdown(windy_fm, unsafe_allow_html = True)
                    st.markdown(f'<iframe width="350" height="350" src="https://embed.windy.com/embed2.html?lat={Latitude}&lon={Longitude}&detailLat={Latitude}&detailLon={Longitude}&width=650&height=450&zoom=11&level=surface&overlay=temp&product=ecmwf&menu=None&message=&marker=&calendar=now&pressure=&type=map&location=coordinates&detail=&metricWind=mph&metricTemp=%C2%B0F&radarRange=-1" frameborder="10"></iframe>', unsafe_allow_html = True)
                    st.image('misc/temp-hue.png')
                    
#starting
if clicked_getwr_button:
    weather()
    





