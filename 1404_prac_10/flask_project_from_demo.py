from flask import Flask

app = Flask(__name__)


@app.route('/convert_celsius_to_fahrenheit/<float:celsius>')
def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32

    return f"Celsius: {str(celsius)}\nFahrenheit: {str(fahrenheit)}"


if __name__ == '__main__':
    app.run()
