import webbrowser

def make_list_page(item_list):
    f = open("PotionRoller.html", "w")

    html_opener = """
    <html>
    <head>
    <title>Potion Roller</title>
    </head>
    <body>
    <p>You found the following treasure: </p>
    <p>
    """

    html_closer = """
    </p>
    </body>
    </html>
    """

    content = ""

    for item in item_list:
        content += "<li>" + str(item) + "</li>"

    new_page = html_opener + content + html_closer

    f.write(new_page)
    f.close()

    webbrowser.open("PotionRoller.html")
