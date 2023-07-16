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

## Links & anchors

**Description**
Test all links on the site to ensure they direct to correct pages.

**Steps to test**

Click all listed links and anchors -> Check if the correct page displays

Tested Navigation Links:

- Home -> index.html
- Register -> signup.html
- Log in -> login.html
- Log out -> logout.html
- Rooms -> rooms.html
- Book -> new_booking.html
- My Bookings -> mybookings.html
- Admin -> Django admin

Links from Home page (index.html):

- Rooms page - rooms.html
- Booking form - new_booking.html
- Show on map - external google maps link with location
- Logo link - directs to home page, introduced for SEO, navigation use only secondary

Collapsibles on Home page (index.html)

- Payments and bookings - displays relevant content
- Find us - displays relevant content

Anchors - cards:

- Rooms page cards - open detail pages for correct rooms (room_details.html)
- Bookings page cards - open booking detail pages for correct bookings (booking_details.html)

Anchors - buttons:

- Rooms page (admin access):

  - Create Room - add_room.html

- Room details:

  - Book Room - new_booking.html
  - Edit Room - edit_room.html
  - Delete Room - delete_room.html

- Booking details:

  - Edit Booking - edit_booking.html
  - Delete Booking - delete_booking.html

- Edit Room:

  - Cancel - rooms.html

- Edit Booking:
  - Cancel - mybookings.html

**Expected result**
Correct pages and/or content display from all links

**Actual Result**
As Expected

**Assessment**
Pass

## Forms

**Description**
Test all forms on the site to ensure they function as designed.

### Authentication (Users)

#### Sign up

<hr>
Test 1:
**Steps to test**

Enter email address -> Enter password -> Repeat same password -> Click submit

**Expected result**
Form submits, new user is created, success message is displayed to user, new user is showing in admin

Test 2:
**Steps to test**

Enter email address -> Enter password -> Enter different password -> Click submit

**Expected result**
Form doesn't sumbit, password doesn't match error message is displayed to user

<hr>

**Actual Results**
As Expected

**Assessment**
Pass

#### Log in

<hr>
Test 1:

**Steps to test**

Enter email address -> Enter password -> Click Sign in

**Expected result**
Form submits, user is logged in, success message is displayed to user

Test 2:
**Steps to test**

Enter email address -> Enter wrong password -> Click Sign in

**Expected result**
Form doesn't sumbit, password doesn't match error message is displayed to user

<hr>

**Actual Results**
As Expected

**Assessment**
Pass

#### Log out

**Steps to test**

Click Sign out button on navbar -> Click Signout on confirmation

**Expected result**
User gets logged out

**Actual Result**
As Expected

**Assessment**
Pass

#### Create Room

<hr>
Test 1:

**Steps to test**

Enter room name & number -> Select view from dropdown -> Enter number of people, price, description - > Select photo -> enter alt
-> click submit

**Expected result**
Form submits, room is created with all fields displayed as selected on the form

Test 2:
**Steps to test**
Fill out all fields on the form, but omit number of people

**Expected result**
Form doesn't submit and scrolls to the field that needs to be filled out, if photo or photo alt field a message shows to fill them out

<hr>

**Actual Results**
As Expected

**Assessment**
Pass

<hr>

#### Edit Room

Test 1:
**Steps to test**
Edit price -> click Submit

**Expected result**
Form submits, price field is displayed with the new value

Test 2:
**Steps to test**
Remove price value -> click Submit

**Expected result**
Form doesn't submit, a message shows to fill out the price field

<hr>

**Actual Results**
As Expected - As a result of testing edit forms, a need for Cancel button was identified to increase edit forms user friendliness.

**Assessment**
Pass

## Booking logic

## Admin

## Responsiveness

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
