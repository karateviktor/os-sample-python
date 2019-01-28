from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

magazineVar = [
    {
        "DokumentenID": "1",
        "DokumentenTitel": "investmentkonzept 1",
        "TeaserText": "investmentkonzept",
        "Bild": "Bild in 64",
        "Publikationsdatum": "2019-01-18",
        "Thema": "investmentkonzept",
        "Link": "www.link.de"
    },
    {
        "DokumentenID": "2",
        "DokumentenTitel": "investmentkonzept 2",
        "TeaserText": "investmentkonzept",
        "Bild": "Bild in 64",
        "Publikationsdatum": "2019-01-18",
        "Thema": "investmentkonzept",
        "Link": "www.link.de"
    },
    {
        "DokumentenID": "3",
        "DokumentenTitel": "investmentonline 3",
        "TeaserText": "investmentonline",
        "Bild": "Bild in 64",
        "Publikationsdatum": "2019-01-18",
        "Thema": "investmentonline",
        "Link": "www.link.de"
    },
    {
        "DokumentenID": "4",
        "DokumentenTitel": "investmentspezial 4",
        "TeaserText": "wochenbericht",
        "Bild": "Bild in 64",
        "Publikationsdatum": "2019-01-18",
        "Thema": "investmentspezial",
        "Link": "www.link.de"
    }
]

berichteVar = [
    {
        "DokumentenID": "11",
        "DokumentenTitel": "kapitalmarktindizes 18",
        "TeaserText": "kapitalmarktindizes",
        "Bild": "Bild in 64",
        "Publikationsdatum": "2018-12-27",
        "Thema": "kapitalmarktindizes",
        "Link": "www.link.de"
    },
    {
        "DokumentenID": "12",
        "DokumentenTitel": "kapitalmarktindizes 12",
        "TeaserText": "kapitalmarktindizes",
        "Bild": "Bild in 64",
        "Publikationsdatum": "2019-01-18",
        "Thema": "kapitalmarktindizes",
        "Link": "www.link.de"
    },
    {
        "DokumentenID": "15",
        "DokumentenTitel": "fondswertentwicklung 15",
        "TeaserText": "fondswertentwicklung",
        "Bild": "Bild in 64",
        "Publikationsdatum": "2019-01-18",
        "Thema": "fondswertentwicklung",
        "Link": "www.link.de"
    },
    {
        "DokumentenID": "7",
        "DokumentenTitel": "wochenbericht 7",
        "TeaserText": "wochenbericht",
        "Bild": "Bild in 64",
        "Publikationsdatum": "2019-01-18",
        "Thema": "wochenbericht",
        "Link": "www.link.de"
    }
]

fondsberichteVar = [
    {
        "ISIN": "DE00001",
        "PublicationDate": "2019-01-18",
        "Size": 123,
        "Link": "www.link.de"
    },
    {
        "ISIN": "22",
        "PublicationDate": "2019-01-18",
        "Size": 222,
        "Link": "www.link22.de"
    },
    {
        "ISIN": "33",
        "PublicationDate": "2019-01-18",
        "Size": 333,
        "Link": "www.link33.de"
    }
]


# def abort_if_thema_doesnt_exist(thema):
#    if thema not in berichteUndMagazineVar:
#        abort(404, message="thema {} doesn't exist".format(thema))


class berichteUndMagazine(Resource):

    def get(self):

        # Für Berichte:
        # [GET]<LR-URL>/dokumente-berichte-und-magazine/?Thema=kapitalmarktindizes&Thema=fondswertentwicklung&Thema=wochenbericht&Thema=monatsbericht_foliensammlung&Thema=privatfonds_news&letztesVersanddatum=2018-12-24
        # Für Magazine:
        # [GET]<LR-URL>/dokumente-berichte-und-magazine/?Thema=investmentkonzept,investmentonline,investmentspezial&letztesVersanddatum=2018-12-24

        thema_arr = request.args.getlist('Thema')
        letztes_versanddatum = request.args.get('letztesVersanddatum', None)

        # abort_if_thema_doesnt_exist(thema)

        liste_von_dokumenten = []

        berichte_themen = ['kapitalmarktindizes', 'fondswertentwicklung', 'wochenbericht',
                          'monatsbericht_foliensammlung', 'privatfonds_news']
        for thema in thema_arr:
            if thema in berichte_themen:
                for bericht in berichteVar:
                    if thema == bericht["Thema"] and letztes_versanddatum == bericht["Publikationsdatum"]:
                        liste_von_dokumenten.append(bericht)

        magazine_themen = ['investmentkonzept', 'investmentonline', 'investmentspezial']

        for thema in thema_arr:
            if thema in magazine_themen:
                for magazin in magazineVar:
                    if thema == magazin["Thema"] and letztes_versanddatum == magazin["Publikationsdatum"]:
                        liste_von_dokumenten.append(magazin)

        if not liste_von_dokumenten:
            return "Bericht oder Magazin not found", 404
        else:
            return {"Liste von Dokumenten": liste_von_dokumenten}, 200


class dokumentefondsberichte(Resource):

    def get(self):

        letztes_versanddatum = request.args.get('letztesVersanddatum', None)

        liste_von_dokumenten = []

        for fondsberichte in fondsberichteVar:
            if letztes_versanddatum == fondsberichte["PublicationDate"]:
                liste_von_dokumenten.append(fondsberichte)

        if not liste_von_dokumenten:
            return "Fondsberichte not found", 404
        else:
            return {"Liste von Dokumenten": liste_von_dokumenten}, 200


##
## Actually setup the Api resource routing here
##
api.add_resource(berichteUndMagazine, '/berichteUndMagazine/')
api.add_resource(dokumentefondsberichte, '/dokumentefondsberichte/')

if __name__ == '__main__':
    app.run()
    #app.run(debug=True, port=5000)


#application = Flask(__name__)


#@application.route("/")
#def hello():
#    return "Hello World!"


#if __name__ == "__main__":
#    application.run()
