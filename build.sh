set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --not-input
python manage.py migrate
