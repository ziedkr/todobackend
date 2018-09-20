#!/bin/bash
# actiovation de l'environement virtuelle 
. /appenv/bin/activate

# telchargement requis pour contruire le cache (qui sont les depend dd test et de l'app)
# et les copier dans /build
pip download -d /build -r requirements_test.txt --no-input

# install les dependence de l'app qui serons ds le fichier requirements_pour_test_txt
#pip install -r requirements_test.txt

# ne telecharge auccune dependace depuis internet !!!!
pip install --no-index -f /build -r requirements_test.txt
# Run test.sh arguments
exec $@