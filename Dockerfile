# Utiliser l'image Python officielle comme base
FROM python:3.8

# Définir le répertoire de travail dans l'image
WORKDIR /app

# Copier les fichiers requis dans l'image
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Définir la commande à exécuter lors du démarrage du conteneur
CMD ["python", "weather_wrapper.py"]
