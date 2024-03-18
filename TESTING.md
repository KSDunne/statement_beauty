## Code Validation

### HTML

All HTML pages were tested with the [W3C HTML Validator](https://validator.w3.org/).

#### HTML Result

| page                   | validator                                                                                                                               | result |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| blog                   |  <details><summary>Blog Page</summary><img src="./docs/readme_images/validation/blog_page_html.PNG"></details>                          | PASS   |
| about                  |  <details><summary>About Page</summary><img src="./docs/readme_images/validation/about_page_html.PNG"></details>                        | PASS   |
| makeover               |  <details><summary>Makeover Page</summary><img src="./docs/readme_images/validation/book_makeover_page_html.PNG"></details>             | PASS   |
| post detail logged out |  <details><summary>Post Detail Logged Out</summary><img src="./docs/readme_images/validation/post_detail_loggedout_html.PNG"></details> | PASS   |
| post detail logged in  |  <details><summary>Post Detail Logged In</summary><img src="./docs/readme_images/validation/post_detail_loggedin_html.PNG"></details>   | PASS   |
| sign up page           |  <details><summary>Register</summary><img src="./docs/readme_images/validation/signup_page_html.PNG"></details>                         | PASS   |
| sign in page           |  <details><summary>Sign In</summary><img src="./docs/readme_images/validation/login_page_html.PNG"></details>                           | PASS   |
| logout page            |  <details><summary>Sign Out</summary><img src="./docs/readme_images/validation/logout_page_html.PNG"></details>                         | PASS   |
| edit booking page      |  <details><summary>Edit Booking</summary><img src="./docs/readme_images/validation/edit_makeover_page.PNG"></details>                   | PASS   |
| delete booking page    |  <details><summary>Delete Booking</summary><img src="./docs/readme_images/validation/booking_confirm_delete_html.PNG"></details>        | PASS   |
| delete comment page    |  <details><summary>Delete Comment</summary><img src="./docs/readme_images/validation/comment_confirm_delete_html.PNG"></details>        | PASS   |

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

- [Stack overflow](https://stackoverflow.com/questions/25946111/importing-css-is-ending-up-with-an-error) - the google style sheet is not checked in the validator

Warning 2: -webkit-transform is a vendor extension. This warning can be ignored in this instance.

- [Stack overflow](https://stackoverflow.com/questions/30607832/w3c-css-validation-error-using-calc-and-vendor-extensions) - vendor-specific extensions (mostly) do adhere to the CSS 2.1 grammar, but since they are not defined in the CSS 2.1 specification, they are marked as invalid in the validator.

Warning 3: -moz-transform is a vendor extension. This warning can be ignored in this instance.

- [Stack overflow](https://stackoverflow.com/questions/30607832/w3c-css-validation-error-using-calc-and-vendor-extensions) - vendor-specific extensions (mostly) do adhere to the CSS 2.1 grammar, but since they are not defined in the CSS 2.1 specification, they are marked as invalid in the validator.

### JavaScript

JavaScript code in the comment.js file was put through the [JSHint Validator](https://jshint.com/).

#### JS Result

![JS validation](docs/readme_images/validation/comments_js_code.PNG)

### Python

All python code was put through the [CI Python Linter](https://pep8ci.herokuapp.com/).

#### Python Result

| File            | Validator                                                                                                                | Result |
| --------------- | ------------------------------------------------------------------------------------------------------------------------ | ------ |
| About models    |  <details><summary>About Models</summary><img src="./docs/readme_images/validation/about_models_py.PNG"></details>       | PASS   |
| About views     |  <details><summary>About Views</summary><img src="./docs/readme_images/validation/about_views_py.PNG"></details>         | PASS   |
| About forms     |  <details><summary>About Forms</summary><img src="./docs/readme_images/validation/about_forms_py.PNG"></details>         | PASS   |
| About urls      |  <details><summary>About urls</summary><img src="./docs/readme_images/validation/about_urls_py.PNG"></details>           | PASS   |
| About admin     |  <details><summary>About Admin</summary><img src="./docs/readme_images/validation/about_admin_py.PNG"></details>         | PASS   |
| Blog models     |  <details><summary>Blog Models</summary><img src="./docs/readme_images/validation/about_models_py.PNG"></details>        | PASS   |
| Blog views      |  <details><summary>Blog Views</summary><img src="./docs/readme_images/validation/about_views_py.PNG"></details>          | PASS   |
| Blog forms      |  <details><summary>Blog Forms</summary><img src="./docs/readme_images/validation/about_forms_py.PNG"></details>          | PASS   |
| Blog urls       |  <details><summary>Blog urls</summary><img src="./docs/readme_images/validation/about_urls_py.PNG"></details>            | PASS   |
| Blog admin      |  <details><summary>Blog Admin</summary><img src="./docs/readme_images/validation/about_admin_py.PNG"></details>          | PASS   |
| Makeover models |  <details><summary>Makeover Models</summary><img src="./docs/readme_images/validation/makeover_models_py.PNG"></details> | PASS   |
| Makeover views  |  <details><summary>Makeover Views</summary><img src="./docs/readme_images/validation/makeover_views_py.PNG"></details>   | PASS   |
| Makeover forms  |  <details><summary>Makeover Forms</summary><img src="./docs/readme_images/validation/makeover_forms_py.PNG"></details>   | PASS   |
| Makeover urls   |  <details><summary>Makeover urls</summary><img src="./docs/readme_images/validation/makeover_urls_py.PNG"></details>     | PASS   |
| Makeover admin  |  <details><summary>Makeover Admin</summary><img src="./docs/readme_images/validation/makeover_admin_py.PNG"></details>   | PASS   |
| Settings        |  <details><summary>Settings</summary><img src="./docs/readme_images/validation/settings_py.PNG"></details>               | PASS   |

There were 4 'line too long' results left in the settings file. It was left without refactoring because this is Django specific code for password validation.

## Lighthouse

### Lighthouse result

This website's landing blog page got 100% score for accessibility, best practices and seo. Performance score is between 70-80.

![Lighthouse result](docs/readme_images/testing/lighthouse_result.PNG)

### Lighthouse result explaination

Performance is fluctuating between 70-80 everytime it is tested. [Documentation](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring/#fluctuations) says this is normal. The following was done during testing to try and imporve the performance score:

- The hero image size was reduced and image type was changed to webp
- The placeholder image for blogs was reduced in size and the type was changed from jpg to webp
- The cloudinary settings in the profile specific to me and this project were changed. I went to the optimization page of settings and I went to 'default image quality'. I changed this setting from 'good quality' to 'economy mode'.
- There were also console warnings saying that the image urls were not secure so a configuration of secure=True was added to settings.py.

The very first performance score I got on lighthouse was 69% and after doing all of these steps, it went up to a score of 81% during one test, so I think these steps did make an improvement. I will submit the project in this state. However, if time allowed there is one more solution that could be tried and that would be the following:

If time allowed, the image fields coule be switched to [django resized fields](https://pypi.org/project/django-resized/).

