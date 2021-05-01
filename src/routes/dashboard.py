from flask import Blueprint, render_template

bp = Blueprint("dashboard", __name__)

stocks = [
    {   
        "id": 1,
        "companyShortName": "Indian Oil Corp.",
        "companyName": "Indian Oil Corporation",
        "imageUrl": "https://assets-netstorage.groww.in/stock-assets/logos/INE242A01010.png",
        "closePrice": 90.85,
        "dayChange": 1.9499999999999886,
        "dayChangePerc": 2.1934758155230467
    },
    {
        "companyShortName": "Aditya Vision",
        "companyName": "Aditya Vision",
        "imageUrl": None,
        "closePrice": 264.65,
        "dayChange": 5.149999999999977,
        "dayChangePerc": 1.9845857418111665
    },
    {
        "companyShortName": "Hindustan Unilever",
        "companyName": "Hindustan Unilever",
        "imageUrl": "https://assets-netstorage.groww.in/stock-assets/logos/INE030A01027.png",
        "closePrice": 2353.75,
        "dayChange": -53.84999999999991,
        "dayChangePerc": -2.2366672204685125
    },
    {
        "companyShortName": "Motilal Oswal Fin",
        "companyName": "Motilal Oswal Financial Services",
        "imageUrl": "https://assets-netstorage.groww.in/stock-assets/logos/INE338I01027.png",
        "closePrice": 637.7,
        "dayChange": 8.400000000000091,
        "dayChangePerc": 1.3348164627363883
    },
    {
        "companyShortName": "JSW Energy",
        "companyName": "JSW Energy",
        "imageUrl": "https://assets-netstorage.groww.in/stock-assets/logos/INE121E01018.png",
        "closePrice": 109.6,
        "dayChange": 0.5999999999999943,
        "dayChangePerc": 0.5504587155963251
    },
    {
        "companyShortName": "Future Retail",
        "companyName": "Future Retail",
        "imageUrl": "https://assets-netstorage.groww.in/stock-assets/logos/INE752P01024.png",
        "closePrice": 51.1,
        "dayChange": -0.19999999999999574,
        "dayChangePerc": -0.3898635477582763
    },
    {
        "companyShortName": "JSW Steel",
        "companyName": "JSW Steel",
        "imageUrl": "https://assets-netstorage.groww.in/stock-assets/logos/INE019A01038.png",
        "closePrice": 717.85,
        "dayChange": -8.649999999999977,
        "dayChangePerc": -1.1906400550584966
    },
    {
        "companyShortName": "Tata Coffee",
        "companyName": "Tata Coffee",
        "imageUrl": "https://assets-netstorage.groww.in/stock-assets/logos/INE493A01027.png",
        "closePrice": 131.0,
        "dayChange": 3.200000000000003,
        "dayChangePerc": 2.5039123630672946
    },
    {
        "companyShortName": "Wipro",
        "companyName": "Wipro",
        "imageUrl": "https://assets-netstorage.groww.in/stock-assets/logos/INE075A01022.png",
        "closePrice": 492.75,
        "dayChange": 2.8999999999999773,
        "dayChangePerc": 0.5920179646830616
    },
    {
        "companyShortName": "Page Industries",
        "companyName": "Page Industries",
        "imageUrl": "https://assets-netstorage.groww.in/stock-assets/logos/INE761H01022.png",
        "closePrice": 29660.6,
        "dayChange": -230.10000000000218,
        "dayChangePerc": -0.7698046549595766
    }
]



@bp.route("/")
def login():
    current_user = {
        "username": "Yogesh Upadhyay"
    }
    return render_template("index.html", stocks=stocks, current_user=current_user)
