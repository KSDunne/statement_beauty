## Code Validation

### HTML

All HTML pages were tested with the [W3C HTML Validator](https://validator.w3.org/).

#### HTML Result

| page                   | validator                                                                                                                               | result |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| blog                   |  <details><summary>Blog Page</summary><img src="./docs/readme_images/validation/blog_page_html.PNG"></details>                          | PASS   |
| about                  |  <details><summary>About Page</summary><img src="./docs/readme_images/validation/about_page_html.PNG"></details>                        | PASS   |
| makeover               |  <details><summary>Makeover Page</summary><img src="./docs/readme_images/validation/book_makeover_page_html.PNG"></details>                  | PASS   |
| post detail logged out |  <details><summary>Post Detail Logged Out</summary><img src="./docs/readme_images/validation/post_detail_loggedout_html.PNG"></details> | PASS   |
| post detail logged in  |  <details><summary>Post Detail Logged In</summary><img src="./docs/readme_images/validation/post_detail_loggedin_html.PNG"></details>   | PASS   |
| sign up page           |  <details><summary>Register</summary><img src="./docs/readme_images/validation/signup_page_html.PNG"></details>                         | PASS   |
| sign in page           |  <details><summary>Sign In</summary><img src="./docs/readme_images/validation/login_page_html.PNG"></details>                           | PASS   |
| logout page            |  <details><summary>Sign Out</summary><img src="./docs/readme_images/validation/logout_page_html.PNG"></details>                         | PASS   |
| edit booking page      |  <details><summary>Edit Booking</summary><img src="./docs/readme_images/validation/edit_makeover_page.PNG"></details>                   | PASS   |
| delete booking page    |  <details><summary>Delete Booking</summary><img src="./docs/readme_images/validation/booking_confirm_delete_html.PNG"></details>        | PASS   |

The info messages that were ignored appeared in validation, because I used the [Prettier](https://prettier.io/) plugin in VS code. Prettier is hardcoded to add trailing slashes. Since all of my attributes were quoted, there is no effect of the trailing slash. After some research and finding the following 2 links I decided that it is ok to ignore these info messages in this instance.

- [Stack overflow](https://stackoverflow.com/questions/77343449/using-of-trailing-slash-in-void-element) - information on trailing slash

- [Github](https://github.com/validator/validator/wiki/Markup-%C2%BB-Void-elements#configuring-tools-to-not-output-trailing-slashes-for-void-elements) - information on trailing slash

### CSS

Custom CSS was put through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

#### CSS Result

Pass

![CSS validation](docs/readme_images/validation/css_validation.PNG)

Explaination of 3 warnings

![CSS validation](docs/readme_images/validation/css_validation_warnings.PNG)

Warning 1: Imported style sheets are not checked in direct input and file upload modes. This warning can be ignored in this instance.

- [Stack overflow](https://stackoverflow.com/questions/25946111/importing-css-is-ending-up-with-an-error)

Warning 2: -webkit-transform is a vendor extension. This warning can be ignored in this instance.

- [Stack overflow](https://stackoverflow.com/questions/30607832/w3c-css-validation-error-using-calc-and-vendor-extensions)

Warning 3: -moz-transform is a vendor extension. This warning can be ignored in this instance.

- [Stack overflow](https://stackoverflow.com/questions/30607832/w3c-css-validation-error-using-calc-and-vendor-extensions)