# Forms

Welcome to the Forms Project! This project aims to help you understand and create usable, accessible, and well-designed web forms. Below are the resources and learning objectives that will guide you through this project.

## Resources

Here are some valuable resources to get you started with web forms:

### Articles and Guides
- [An Extensive Guide To Web Form Usability — Smashing Magazine](https://www.smashingmagazine.com/2011/11/extensive-guide-web-form-usability/)
- [Forms - UX Movement](https://uxmovement.com/forms/)
- [Placeholders in Form Fields are Harmful (Video)](https://www.youtube.com/watch?v=9Yx2f8RmU-4)
- [The Anatomy of Accessible Forms: Best Practices | Deque](https://www.deque.com/blog/anatomy-of-accessible-forms-best-practices/)
- [Pure CSS Custom Error Messaging for Default Form Elements – Sarah Holley Design](https://sarahholleydesign.com/pure-css-custom-error-messaging-for-default-form-elements/)

### MDN Resources
- [HTML forms - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn/Forms)
- [form - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)
- [fieldset: The Field Set element - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset)
- [legend - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/legend)
- [label - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)
- [input: The Input (Form Input) element - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)
- [tabindex - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/tabindex)
- [accesskey - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/accesskey)
- [button: The Button element - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button)
- [select - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select)
- [optgroup - HTML: Hypertext Markup Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup)
- [datalist - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist)
- [textarea - HTML: Hypertext Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea)
- [Form Validation UX in HTML and CSS | CSS-Tricks](https://css-tricks.com/form-validation-ux-html-css/)
- [Constraint validation - Developer guides | MDN](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Constraint_validation)
- [:invalid - CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/:invalid)
- [:valid - CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/:valid)
- [:optional - CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/:optional)

## Learning Objectives

By the end of this project, you should be able to explain and demonstrate the following concepts:

1. **How to create an HTML5 form**:
   - Understand the structure and elements required to create a form in HTML5.
   - Learn how to use form elements like `<form>`, `<input>`, `<textarea>`, `<button>`, `<select>`, `<fieldset>`, and `<legend>`.

2. **How to choose the right input type**:
   - Learn about different input types (e.g., `text`, `email`, `number`, `password`, etc.) and when to use each type to ensure proper data collection and validation.

3. **How to constrain a form field with regular expressions**:
   - Understand how to use the `pattern` attribute in input elements to enforce specific input formats using regular expressions.

4. **How to style inputs for invalid, valid, and required fields**:
   - Learn how to use CSS pseudo-classes (`:invalid`, `:valid`, `:required`, etc.) to style form elements based on their validation state.

5. **How to build a comment form**:
   - Create a form that allows users to submit comments, including fields like name, email, and message.

6. **How to build a simple search form**:
   - Create a basic search form with an input field and a submit button.

7. **How to create usable and accessible forms**:
   - Apply best practices for form usability and accessibility, ensuring that forms are easy to use and accessible to all users, including those with disabilities.

## Getting Started

To get started with this project, follow these steps:

1. **Review the resources** provided to build a strong understanding of web form usability, accessibility, and best practices.
2. **Create an HTML5 form** with various input types, using the appropriate elements and attributes.
3. **Add validation constraints** using regular expressions and the `pattern` attribute.
4. **Style the form** using CSS to provide visual feedback for valid, invalid, and required fields.
5. **Build specific forms** like a comment form and a search form.
6. **Ensure the forms are usable and accessible** by following the best practices outlined in the resources.

### Example Code Snippet

Here is an example snippet to help you get started with creating an HTML5 form:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <style>
        input:valid {
            border-color: green;
        }
        input:invalid {
            border-color: red;
        }
        input:required {
            border-color: blue;
        }
    </style>
</head>
<body>
    <form id="contact-form">
        <fieldset>
            <legend>Contact Us</legend>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <br>
            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>
            <br>
            <button type="submit">Submit</button>
        </fieldset>
    </form>
</body>
</html>
