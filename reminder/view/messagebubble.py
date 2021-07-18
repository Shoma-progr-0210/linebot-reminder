CAROUSEL = {
    "type": "carousel",
    "contents": []
}


REMIND_BUBBLE = {
  "type": "bubble",
  "size": "mega",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "time",
            "size": "sm",
            "color": "#ffffff",
            "align": "center",
            "gravity": "center",
            "offsetTop": "none",
            "weight": "bold"
          }
        ],
        "backgroundColor": "#ffa500",
        "flex": 0,
        "position": "relative",
        "cornerRadius": "sm",
        "width": "180px",
        "height": "30px",
        "offsetEnd": "8px",
        "offsetBottom": "10px"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "label",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "gravity": "center"
          }
        ],
        "backgroundColor": "#EC3D44",
        "paddingAll": "2px",
        "paddingStart": "4px",
        "paddingEnd": "4px",
        "flex": 0,
        "position": "absolute",
        "offsetStart": "210px",
        "offsetTop": "10px",
        "cornerRadius": "100px",
        "width": "75px",
        "height": "30px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "name",
            "size": "xl",
            "weight": "bold",
            "wrap": True
          }
        ]
      }
    ]
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "message",
        "margin": "none",
        "wrap": True,
        "offsetBottom": "lg"
      }
    ],
    "backgroundColor": "#ffffff"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "確認",
          "data": "check"
        },
        "margin": "none",
        "style": "primary",
        "height": "sm",
        "color": "#d2691e"
      }
    ],
    "backgroundColor": "#ffffff"
  }
}

SCHEDULE_BUBBLE = {
  "type": "bubble",
  "size": "mega",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "time",
            "size": "sm",
            "color": "#ffffff",
            "align": "center",
            "gravity": "center",
            "offsetTop": "none",
            "weight": "bold"
          }
        ],
        "backgroundColor": "#66cdaa",
        "flex": 0,
        "position": "relative",
        "cornerRadius": "sm",
        "width": "180px",
        "height": "30px",
        "offsetEnd": "8px",
        "offsetBottom": "10px"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "label",
            "size": "xs",
            "color": "#ffffff",
            "align": "center",
            "gravity": "center"
          }
        ],
        "backgroundColor": "#EC3D44",
        "paddingAll": "2px",
        "paddingStart": "4px",
        "paddingEnd": "4px",
        "flex": 0,
        "position": "absolute",
        "offsetStart": "210px",
        "offsetTop": "10px",
        "cornerRadius": "100px",
        "width": "75px",
        "height": "30px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "name",
            "size": "xl",
            "weight": "bold",
            "wrap": True
          }
        ]
      }
    ]
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "message",
        "margin": "none",
        "wrap": True,
        "offsetBottom": "lg"
      }
    ],
    "backgroundColor": "#ffffff"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "編集",
          "data": "edit"
        },
        "margin": "none",
        "style": "primary",
        "height": "sm",
        "color": "#385077"
      }
    ],
    "backgroundColor": "#ffffff"
  }
}