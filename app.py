"""Flet Weather app"""
# modules
import flet
from flet import *
import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# note: the API used here is taken from an online website - it's not my personal API key.
api_key = os.environ.get('WEATHER_API_KEY')

_current = requests.get(
    f"https://api.openweathermap.org/data/3.0/onecall?lat=126.9996417&lon=37.56100278&exclude=minutely,hourly,alerts&appid={api_key}"
)

# list of days of the week
days = [
    "Mon",
    "Tue",
    "Wed",
    "Thu",
    "Fri",
    "Sat",
    "Sun"
]

#
def main(page: Page):
    page.horizontal_alignment='center'
    page.vertical_alignment='center'
    
    # animation
    def _expand(e):
        if e.data == "true":
            _c.content.controls[0].height = 560
            _c.content.controls[0].update()
        else:
            _c.content.controls[0].height = 660 * 0.40
            _c.content.controls[0].update()
            
    # current temp
    def _current_temp():
        # at the start of the app we called the API from open weather to get some data regarding temp
        _current_temp = _current.json()
        
        return [_current_temp]
    
    # top contaioner
    def _top():
        
        _today = _current_temp()
        
        top = Container(
            width=310,
            height=660 * 0.40,
            gradient= LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=["lightblue600", "lightblue900"],
            ),
            border_radius=35,
            animate=animation.Animation(duration=350,curve="decelerate"),
            on_hover=lambda e: _expand(e),
            content=Column(
                alignment='start',
                spacing=10,
                controls=[
                    Row(
                        alignment='center',
                        controls=[
                            Text(
                                "Seoul, Jongro",
                                color='white',
                                size=16,
                                weight="w500",
                            )
                        ],
                    ),
                    Container(
                        padding=padding.only(bottom=5)
                    ),
                    Row(
                        alignment='center',
                        spacing=30,
                        controls=[
                            Column(
                                controls=[
                                    Container(
                                        width=90,
                                        height=90,
                                        image_src="./assets/cloudy.png",
                                    ),
                                    
                                ]
                            ),
                            Column(
                                spacing=5,
                                horizontal_alignment='center',
                                controls=[
                                    Text(
                                        "Today",
                                        size=12,
                                        text_align="center",
                                        color="white",
                                    ),
                                    Row(
                                      vertical_alignment='start',
                                      spacing=0,
                                      controls=[
                                          Container(
                                              content=Text(
                                                  _today[0],
                                                  size=52,
                                              ),
                                          )
                                      ],  
                                    ),
                                ]
                            )
                        ],
                    )
                ],
            ),
        )
        
        return top
    
    _c = Container(
        width=310,
        height=660,
        border_radius=35,
        bgcolor='black',
        padding=10,
        content=Stack(
            width=300,
            height=550,
            controls=[
                _top(),
            ]
        ),
    )
    
    page.add(_c)

if __name__ == "__main__":
    flet.app(target=main, assets_dir='assets')