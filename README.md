# LANFlix
Lanflix is a lightweight local movie streaming server built with Flask. It can run in development mode or as a systemd service for production environments.

## 📦 Installation
### Install the requirements

Install Python dependencies using pip:
```bash
pip install -r requirments.txt
```

> Make sure you're using a Python environment with version 3.8 or higher.

### Install the Systemd Service
1. Move the Project Files

Move the `lanflix/` folder to a local share directory:
```bash
cp -r lanflix/ ~/.local/share/
```

2. Update the Service File

Edit the lanflix.service file and replace `<username>` with your actual username (e.g., penguinboi):
```bash
# change <username> to your username
WorkingDirectory=/home/<username>/.local/share/lanflix/app
```

3. Install the Service

Copy the modified service file to the systemd directory:
```bash
sudo cp lanflix.service /etc/systemd/system/lanflix.service
```

## 🚀 Usage
### Run in Development Mode

Start the Flask server with debug mode:
```bash
flask --app lanflix/app run --debug
```

### Run in Production Mode (Gunicorn)
> See [Flask’s Gunicorn deployment guide](https://flask.palletsprojects.com/en/stable/deploying/gunicorn/)

Run with Gunicorn:
```bash
cd lanflix/app
gunicorn -w 1 -b 0.0.0.0:8012 'app:app'
```


### Start as a Service
```bash
sudo service lanflix start
```


## 🎬 Adding Movies
Place your movie folders in:
```
~/Videos/Medias/
```

Each movie must be inside its own folder. Within that folder:
- Only one .mp4 file is allowed
- Any number of subtitle files (.vtt) are supported
- (Optional) A poster.jpg image to display as the movie's cover in the UI

Example structure:
```
~/Videos/Medias/
└── 2001: A Space Odyssey 1968/
    ├── 2001 a space odyssey 1080p.mp4
    ├── english.vtt
    └── french.vtt
```