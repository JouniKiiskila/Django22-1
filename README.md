django-harjoitus-2022-09
Django-harjoitus 2022 syksy

Asennus
Luo virtuaaliympäristö: python -m venv venv
Aktivoi virtuaaliympäristö
esim. VSCodessa avaamalla jokin Python-tiedosto ja valitsemalla alhaalta Pythonin versionumeroa klikkaamalla ('venv': venv)
muista käynnistää terminaali-ikkuna uudelleen ja tarkista, että venv on aktiivinen katsomalla, että siinä lukee (venv)
Asenna Django: pip install django
Django-tutoriaali
https://docs.djangoproject.com/en/4.1/intro/tutorial01/

Projektin luonti
Aja django-admin startproject varaukset
Siirrä varaukset kansion sisältö yhden tason ylemmäksi hakemistopuussa.
Kehityspalvelimen ajaminen
Aja ensin migraatiot: python manage.py migrate
Käynnistä kehityspalvelin: python manage.py runserver
Migraatioiden luominen
Kun on tehty uusia modeleita tai muutoksia olemassa oleviin modeleihin (models.py-tiedostossa), niin pitää ajaa: python manage.py makemigrations APPLIKAATION_NIMI esim. python manage.py makemigrations varauskalenteri

Admin-käyttäjän luominen
python manage.py createsuperuser
