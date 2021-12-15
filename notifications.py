from plyer import notification

title = "My custom desktop notification"

message = "Subscribe CodeWithNiranjan for more awesome videos"

notification.notify(title = title,
                    message = message,
                    app_icon = "logo.ico",
                    timeout =  10,
                    toast = False)