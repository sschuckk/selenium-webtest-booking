<!-- Template get from: https://github.com/othneildrew/Best-README-Template -->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Selenium Webtest Booking.com</h3>

  <p align="center">
    <br />
    <a href="https://github.com/sschuckk/selenium-webtest-booking/issues">Report Bug</a>
    ·
    <a href="https://github.com/sschuckk/selenium-webtest-booking/issues">Request Feature</a>
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
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

The project utilizes Selenium and Pytest to automate and conduct comprehensive web page testing, with end-2-end testing script.
The website under test is the www.booking.com where you can search and filter for the hotels you want.
You can use this project to test the website, as a bot to perform searches, or as example to learn about using selenium and pytest.

[![Product presentation][product-gif]](https://github.com/sschuckk/selenium-webtest-booking)

### Built With

[![Python][Python.com]][Python-url] [![Selenium][Selenium.com]][Selenium-url] [![Pytest][Pytest.com]][Pytest-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

* Chrome: https://www.google.com/chrome/
* Python: https://www.python.org/downloads/
* Pip: https://pip.pypa.io/en/stable/installation/
* Git: https://git-scm.com/downloads


### Installation

1. Clone the repo.
   ```sh
   git clone https://github.com/sschuckk/selenium-webtest-booking.git
   ```
2. Install the packages according to the configuration file requirements.txt.
   ```sh
   pip install -r requirements.txt
   ```
3. Verify your Chrome browser version, in the search bar.
   ```sh
   chrome://version/
   ```
4. Ensure that the ChromeDriver version on the folder 'drivers' match your browser version. Download the chromedriver here: https://chromedriver.chromium.org/downloads

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

The project can be run by a terminal or directly in your favorite IDE.
In your terminal go to the tests pages e run:
1. For a simples execution:
   ```sh
   pytest -v
   ```
2. To genarate a report page:
   ```sh
   pytest -v --html=report.html
   ```

Example of an execution by windows CMD:
[![Product presentation][product-exec]]()

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [ ] Extend browser support
- [ ] Add datasets from excel
- [ ] Improve style of HTML report 

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some new feature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the [MIT](https://opensource.org/license/mit/) License. It’s free, no legal restrictions, why not try it out?

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT 
## Contact

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-gif]: images/selenium_project.gif
[product-exec]: images/screenshoot_exec1.png
[Python.com]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/ 
[Selenium.com]: https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white
[Selenium-url]: https://www.selenium.dev/
[Pytest.com]: https://img.shields.io/badge/PYTEST-007ACC?style=for-the-badge&logo=pytest&logoColor=orange
[Pytest-url]: https://docs.pytest.org/