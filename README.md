# Table of Contents

1. [Test Automation Framework for WordPress Plugin (qa-test)](#test-automation-framework-for-wordpress-plugin-(qa-test))
   1. [Features](#features)
   2. [Getting Started](#getting-started)
      1. [Prerequisites](#prerequisites)
      2. [Clone Repository](#clone-repository)
      3. [Installation](#installation)
      4. [Running Tests](#running-tests)
      5. [Generating Allure Report](#generating-allure-report)
      
# Test Automation Framework for WordPress Plugin (qa-test)

This repository houses a powerful automated testing framework built with Python, Playwright incorporating Behavior-Driven Development (BDD) principles using Gherkin syntax. The framework is designed for the testing of a WordPress plugin and includes Allure reporting for comprehensive test result analysis.

## Features
Playwright Integration: Leverage the Playwright automation tool for seamless browser automation across different web browsers.

BDD Testing: Adopt Behavior-Driven Development by expressing test scenarios in Gherkin syntax. Write clear and concise feature files in the features directory.

Allure Reporting: Generate detailed and visually appealing test reports with Allure, providing insights into test execution, failures, and trends.

## Getting Started
### Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.7 or higher  
Pip (Python package installer)  
Playwright (installation instructions [here](https://playwright.dev/python/docs/intro))  
Allure (installation instructions [here](https://allurereport.org/docs/gettingstarted-installation/))
### Clone Repository
To clone the repository, run the following command in your terminal:


```bash
git clone https://github.com/vizallati/wp-mudev-qa-task-autotests.git
```
### Installation
Navigate to the project directory and install the required dependencies:

```bash
cd wp-mudev-qa-task-autotests
pip install -r requirements.txt
```
### Running Tests
Before running the tests edit the settings.yml with respective creds for your WordPress environment

Run the tests using the following command:

```bash
cd tests
pytest --alluredir=allure-results
```
This command will execute the tests and generate Allure report data in the allure-results directory.

### Generating Allure Report
To generate and view the Allure report, run the following commands:

```bash
allure serve path-to-allure-results
```
This will generate the Allure report and open it in your default web browser.
