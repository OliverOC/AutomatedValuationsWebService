from functionLib import inflation_calculator, mmyyyy_to_ddmmyyyy, list_of_boroughs
import flask
from flask import render_template
from inputForm import InputData

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'SecretKey'


@app.route('/', methods=['GET', 'POST'])
def form():
    """
    This function renders the form for the home page of the web service.
    """

    form = InputData()

    if form.validate_on_submit():
        q_price = form.price.data
        q_price_formatted = '{:,}'.format(int(q_price))
        q_date_from = mmyyyy_to_ddmmyyyy(form.date_from.data)
        q_date_to = mmyyyy_to_ddmmyyyy(form.date_to.data)
        q_borough = form.borough.data
        url = 'http://publicdata.landregistry.gov.uk/market-trend-data/' \
              'house-price-index-data/UK-HPI-full-file-2019-05.csv'
        q_inflated_price = inflation_calculator(q_price, q_date_from, q_date_to, q_borough, url)
        q_inflated_price_formatted = '{:,}'.format(int(q_inflated_price))

        if q_inflated_price == 0:
            error_message = '<font face="arial" size="4" color="#898989">' \
                   'Error!<br>' \
                   'Possible errors:<br><br>' \
                   'Dates not found -> please try a more recent date.<br><br>' \
                   'Borough not recognised -> see full list below.<br><br>' \
                   '{}</font>'.format(list_of_boroughs())
            return error_message

        result = '<font face="arial" size="4" color="#898989">' \
               '<center>' \
               '<br><h1>The original price on {} was...<br>£{}<br><br>' \
               'The  price on {} will be...<br>£{}<br>' \
               '</center>' \
               '</font>'.format(q_date_from, q_price_formatted, q_date_to, q_inflated_price_formatted)
        return result

    return render_template('form.html', form=form)


if __name__ == "__main__":
    app.run(port=8080)
