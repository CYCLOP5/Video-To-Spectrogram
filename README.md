
<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/CYCLOP5/Video-To-Spectrogram">
    <img src="![512x512bb](https://github.com/CYCLOP5/Video-To-Spectrogram/assets/85669579/767575d9-862c-4ecc-a26d-84e91d3a9c58)" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">A Video to Spectrogram Generator</h3>

  <p align="center">
    Program inputs an "Input.mp4" file and converts each frame into a spectrogram with amplitude charted and adds the original videos' audio back after frame merging. 
    <br />
    <a href="https://github.com/CYCLOP5/Video-To-Spectrogram"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/CYCLOP5/Video-To-Spectrogram">View Demo</a>
    ·
    <a href="https://github.com/CYCLOP5/Video-To-Spectrogram/issues">Report Bug</a>
    ·
    <a href="https://github.com/CYCLOP5/Video-To-Spectrogram/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The project inputs an "Input.mp4" file which then gives an option to either generate spectrogram frames which can be ended abruptly and conitnued later if required. The other option merges the generated frames and creates a spectrogram with the original video's audio.


<p align="right">(<a href="#readme-top">Back To Top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* Open-CV
* matplotlib
* ffmpeg-python
* moviepy
 

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites
Python should be installed.

* python
  ```sh
  python --version
  ```
* Make sure directory has only 1 Input.mp4 file. (Preferably make sure the clone directory is clean.)
  ```sh
  python --version
  ```
  
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/CYCLOP5/Video-To-Spectrogram.git
   ```
2. Install needed packages
   ```sh
   pip install -r requirements.txt
   ```
3. Linux distros might need to create an environment first with :
   ```sh
   python -m venv env
   . env/bin/activate
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage



<p align="right">(<a href="#readme-top">Back To Top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] GUI


See the [open issues](https://github.com/CYCLOP5/Video-To-Spectrogram/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>



<!-- CONTACT -->
## Contact

Varun Jhaveri - varun.jhaveri23@spit.ac.in

Project Link: [https://github.com/CYCLOP5/Video-To-Spectrogram](https://github.com/CYCLOP5/Video-To-Spectrogram)

<p align="right">(<a href="#readme-top">Back To Top</a>)</p>






[contributors-shield]: https://img.shields.io/github/contributors/CYCLOP5/Video-To-Spectrogram.svg?style=for-the-badge
[contributors-url]: https://github.com/CYCLOP5/Video-To-Spectrogram/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/CYCLOP5/Video-To-Spectrogram.svg?style=for-the-badge
[forks-url]: https://github.com/CYCLOP5/Video-To-Spectrogram/network/members
[stars-shield]: https://img.shields.io/github/stars/CYCLOP5/Video-To-Spectrogram.svg?style=for-the-badge
[stars-url]: https://github.com/CYCLOP5/Video-To-Spectrogram/stargazers
[issues-shield]: https://img.shields.io/github/issues/CYCLOP5/Video-To-Spectrogram.svg?style=for-the-badge
[issues-url]: https://github.com/CYCLOP5/Video-To-Spectrogram/issues
[license-shield]: https://img.shields.io/github/license/CYCLOP5/Video-To-Spectrogram.svg?style=for-the-badge
[license-url]: https://github.com/CYCLOP5/Video-To-Spectrogram/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/vnjhaveri
[product-screenshot]: images/screenshot.png
[Python]: ![python-logo](https://github.com/CYCLOP5/Video-To-Spectrogram/assets/85669579/77c33e52-7eba-4e59-aab3-2af789ddc2ea)
[Python-url]:https://www.python.org/
