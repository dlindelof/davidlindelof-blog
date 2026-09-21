# Services contact form

The site is published to GitHub Pages. The form in `services.qmd` posts to the
owner-supplied Formspree endpoint `https://formspree.io/f/xdekewdr`. This is a
public submission URL, not a private API key.

The form uses a native HTML POST with the fields `name`, `email`, `service`,
and `message`. Required fields and email format are checked by the browser.
Formspree handles the response after submission; no JavaScript is required.
The page includes a Formspree privacy link and LinkedIn as an alternative.

Recipient settings and spam controls are managed in the Formspree dashboard.
Before publishing, send an enquiry manually and confirm that it appears in
Formspree and reaches the intended inbox. Check the confirmation and failure
experience as well. No test messages have been sent during implementation.
