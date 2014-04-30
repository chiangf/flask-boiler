import flaskboiler


if __name__ == '__main__':
    app = flaskboiler.create_app()

    if app.debug:
        app.run(use_debugger=True, use_reloader=False)
    else:
        app.run(debug=True)
