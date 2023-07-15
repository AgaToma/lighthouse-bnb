[Back to Readme](README.md)

# Table of Contents

- [Functional Testing](#functional-testing)
  - [Negative Testing](#negative-testing)
- [Validator Testing](#validator-testing)
  - [HTML](#html)
  - [CSS](#css)
  - [Python](#python)
- [Accessibility](#accessibility)
- [Responsiveness](#responsiveness)
- [Lighthouse Report](#lighthouse-report)
- [Unit Tests](#unit-tests)

# Functional Testing

## Negative Testing

# Validator Testing

## HTML

Validator used - [W3 Markup Validator](https://validator.w3.org/). All pages were tested. Initially 2 errors were found due to button
tag within a tag (closing button on room & booking details) and p tag within span (search bar tooltip). After fixing these home page is rendering no errors.

![HTML Validator](docs/readme_images/html_validator.png)

There are errors showing on forms pages (Create Room and New Booking) related to the form implementation. Validator also highlights errors in the Font Awesome code as rendered in the Elements of Chrome Developer Tools. Hopefully, this is acceptable, as it's not my own custom HTML. The code had to be copied from Elements section of Chrome Dev Tools and validated as text direct input due to the use of templating.

![HTML form error](docs/readme_images/html_validator_form_error.png)

## CSS

## Python

# Accessibility

# Responsiveness

# Lighthouse Report

# Unit Tests
