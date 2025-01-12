# Music Script

[![Python](https://img.shields.io/badge/Python-%2302569B.svg?style=for-the-badge&logo=python&logoColor=lightblue)](https://python.org)  
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![GitHub issues](https://img.shields.io/github/issues/Mrityunjayyshukla/Music_Script.svg)](https://github.com/Mrityunjayyshukla/Music_Script/issues)

## Overview

Music Script is a script created using **python**🐍 to search and download songs in your local device💻. It uses **Spotify and YouTube API** to fetch the song information and change metadata.<br>
For the processing of the audio files, the program uses **FFmpeg**. So FFmpeg has to be installed to use the program

## Features

* Provides a user interface created using streamlit for user experience.
* For Command Line Users, the program also provides command line based working
* User can search for the songs and can get the information of that song
* Audio files contains the song information saved in the audio's metadata

## Technologies and Tools Used
- **Python**: To create the script
- **FFmpeg**: To save the audio and audio postprocessing to prevent corrupt audio files
- **Streamlit**: To create the User Interface (UI) of the program
- **Spotify API**: To search and get song information
- **YouTube API**: To search the song on YouTube and return video link of the song

## Installation
### Installing FFmpeg
[Installing FFmpeg](https://github.com/Mrityunjayyshukla/Music_script/tree/main)

### Cloning the Repository
```bash
git clone https://github.com/Mrityunjayyshukla/Music_script.git
cd Music_script
```
For streamlit UI based program
```bash
git checkout main
```
For command line based program
```bash
git checkout cli-based
```

### Installing dependencies
All the required python libraries are stored in `requirements.txt` file<br>
To install these libraries, run
```bash
pip install -r requirements.txt
```

### Run the Program
- For Streamlit UI program
```bash
streamlit run main.py
```
- For Command line based program
```bash
python main.py
```

## 🤝 Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue if you have suggestions to improve the portfolio.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 💬 Connect with Me

- [LinkedIn](https://linkedin.com/in/mrityunjayyshukla)
- [GitHub](https://github.com/Mrityunjayyshukla)
- [Email](mailto:shuklamrityunjay60@gmail.com)

---

> Built with ❤️ using [Python](https://python.org/).
