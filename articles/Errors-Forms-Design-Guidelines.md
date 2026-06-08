# 10 Design Guidelines for Reporting Errors in Forms - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">5</span>

<div class="article-header">

<h1 class="article-h1">10 Design Guidelines for Reporting Errors in Forms</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Rachel Krause</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/rachel-krause-2025-square.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/rachel-krause/">

Rachel Krause</a></span>

<p class="publication-date">

February 3, 2019 &centerdot; Updated Dec. 12, 2024

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2024-12-12</span>

</p>

</div>

</div>

</div>

<div class="article-share">

<a class="article-share-title ga-share" href="#">

<span class="article-share-icon"></span>

<p class="article-share-label body-medium">Share</p>

</a>

<div class="share-links tooltip">

<div class="tip-arrow"></div>

<ul>

<li class="body-medium">

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: 10 Design Guidelines for Reporting Errors in Forms&amp;body=https://www.nngroup.com/articles/errors-forms-design-guidelines/" data-share-type="Email">

<svg

width="24"

viewbox="0 0 24 24"

fill="none"

xmlns="http://www.w3.org/2000/svg"

class="icon"

>

<rect x="2.375" y="5" width="19.25" height="14" rx="0.65625" stroke="currentColor" stroke-width="1.3125"/>

<path d="M21.625 6.75L12.4156 14.285C12.1738 14.4828 11.8262 14.4828 11.5844 14.285L2.375 6.75" stroke="currentColor" stroke-width="1.3125"/>

</svg>Email article

</a>

</li>

<li class="body-medium">

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/errors-forms-design-guidelines/&amp;title=10 Design Guidelines for Reporting Errors in Forms&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/errors-forms-design-guidelines/&amp;text=10 Design Guidelines for Reporting Errors in Forms&amp;via=nngroup" data-share-type="Twitter">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-x" />

</svg>

Share on Twitter

</a>

</li>

</ul>

</div>

</div>

</div>

<div class="article-container">

<div class="article-content">

<div class="article-summary article-heading-small-light">

<span class="article-summary-label">

Summary:&nbsp;

</span>Help users recover from errors by clearly identifying the problems and allowing users to access and correct fields easily.

</div>

<div class="article-body">

<p>Forms are necessary components of many applications and websites. They are used to log in, purchase items, send feedback, enter personal information, and more. When mistakes are made in forms, good <a href="https://www.nngroup.com/articles/error-message-guidelines/">error messages</a> and thoughtful error flows can easily guide users to fixes.</p>

<div class="table-of-contents">

<div class="content">

<div class="header">

<div class="toc-header">

<h2 class="toc-title article-heading-small">

In This Article:

</h2>

<span class="expand-icon"></span>

</div>

<a class="current-element" href="#"></a>

</div>

<ul class="toc-items">

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-principles-of-designing-error-correction-flows-1">Principles of Designing Error-Correction Flows</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-1-aim-for-inline-validation-whenever-possible-2">1. Aim for Inline Validation Whenever Possible</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-2-indicate-successful-entry-for-complex-fields-3">2. Indicate Successful Entry for Complex Fields</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-3-keep-error-messages-next-to-fields-4">3. Keep Error Messages Next to Fields</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-4-use-color-to-differentiate-errors-from-normal-field-states-5">4. Use Color to Differentiate Errors from Normal Field States</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-5-add-iconography-or-subtle-animation-for-easy-scanning-6">5. Add Iconography or Subtle Animation for Easy Scanning</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-6-use-modals-or-confirmation-dialogs-sparingly-7">6. Use Modals or Confirmation Dialogs Sparingly</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-7-dont-validate-fields-before-input-is-complete-8">7. Don’t Validate Fields Before Input is Complete</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-8-dont-use-validation-summaries-as-the-only-indication-of-an-error-9">8. Don’t Use Validation Summaries as the Only Indication of an Error</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-9-dont-use-tooltips-to-report-errors-10">9. Don’t Use Tooltips to Report Errors</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-10-provide-extra-help-for-repeated-errors-11">10. Provide Extra Help for Repeated Errors</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-12">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-principles-of-designing-error-correction-flows-1">Principles of Designing Error-Correction Flows</h2>

<p>An error flow should allow users to easily fix their mistakes and proceed with their tasks. Effective error design makes sure that:</p>

<ul>

<li>Error messages are easily noticed and understood.</li>

<li>The field(s) in error are easy to locate.</li>

<li>Instructions for fixing errors are visible when the error is fixed.</li>

</ul>

<p>This article contains practical guidelines for designing error flows in forms.</p>

<h2 id="toc-1-aim-for-inline-validation-whenever-possible-2">1. Aim for Inline Validation Whenever Possible</h2>

<p>Ideally, all validation should be <strong>inline</strong>; that is, as soon as the user has finished filling in a field, an indicator should appear nearby if the field contains an error. This approach reduces <a href="https://www.nngroup.com/articles/interaction-cost-definition/">interaction cost</a> for the user by allowing them to fix errors immediately, without searching or returning to a field they thought was completed correctly.</p>

<p>Sometimes inline validation is not possible, and data entered by the user must be sent to a server for verification. In these cases, make sure error messages are clear, actionable, and easy to locate when the form or page is reloaded.</p>

<h2 id="toc-2-indicate-successful-entry-for-complex-fields-3">2. Indicate Successful Entry for Complex Fields</h2>

<p>Inline validation can also be used to indicate successful completion of fields. For example, when the user creates a username, a green checkmark and a message that the username is available provide clear feedback.</p>

<p>For complex inputs such as new passwords, instant inline validation (which appears as the field value is being typed) will prevent users from guessing or checking multiple times if what they’ve entered meets the system's guidelines. In the example below, the password-strength indicator changes as the user types and helps the user decide if the string entered is good enough or if more characters need to be added.</p>

<figure class="caption"><img alt="slack password strength" height="508" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/23/slack-password-validation.gif" width="692"/>

<figcaption><em>Slack indicated password rules and also provided instant validation by showing a password-strength meter as the user typed.</em></figcaption>

</figure>

<p>However, don’t go overboard with success indicators. Success indicators shouldn’t distract users from filling out forms and should only be used when the additional context helps complete the form faster or more accurately. For example, you don’t need to show a success message when the only requirement on the field is that it is filled in, as that message won’t provide much additional context to your user.</p>

<h2 id="toc-3-keep-error-messages-next-to-fields-4">3. Keep Error Messages Next to Fields</h2>

<p>With inline validation, error messages are naturally shown next to the field causing the error. But even when the fields are not validated inline, it’s helpful to show an actionable error message below or next to the problem field in order to help the user fix the error. The message should <strong>f<strong>ollow </strong><a href="https://www.nngroup.com/articles/error-message-guidelines/">error-message guidelines</a>:</strong> <strong>it should be explicit, human-readable, polite, precise, and give constructive advice.</strong></p>

<p>Keeping error messages next to the fields in error minimizes <a href="https://www.nngroup.com/articles/working-memory-external-memory/">working-memory</a> load: users can see the error message while fixing the error instead of having to remember it.</p>

<h2 id="toc-4-use-color-to-differentiate-errors-from-normal-field-states-5">4. Use Color to Differentiate Errors from Normal Field States</h2>

<p>Red is the color most associated with errors, along with orange or yellow for warnings and green or blue for success. Make sure that the validation text stands out from the rest of the form so the user will notice it quickly. Add a semitransparent background of the same color to the error field to make it stand out on a long page with many form fields.</p>

<h2 id="toc-5-add-iconography-or-subtle-animation-for-easy-scanning-6">5. Add Iconography or Subtle Animation for Easy Scanning</h2>

<p>In addition to color, an icon to the left of your error message or validation summary will draw attention to the error and help users who are colorblind. When the user scans the form, the icon will stand out and draw the eye to what needs to be fixed.</p>

<figure class="caption"><img alt="error icon" height="134" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/23/adobe-error-icon.png" width="692"/>

<figcaption><em>Adobe.com: The red color and the icon next to the error message drew users’ attention.</em></figcaption>

</figure>

<p>A subtle pulse or bounce <a href="https://www.nngroup.com/articles/animation-usability/">animation</a> on the icon corresponding to an error can further draw users’ attention to the error. However, don’t abuse animation: several animated icons can be overwhelming if there are multiple errors. And don’t animate text — animated error messages are hard to read.</p>

<h2 id="toc-6-use-modals-or-confirmation-dialogs-sparingly-7">6. Use Modals or Confirmation Dialogs Sparingly</h2>

<p>When you need to draw extra attention to a potential error, use a <a href="https://www.nngroup.com/articles/modal-nonmodal-dialog/">modal</a> or <a href="https://www.nngroup.com/articles/confirmation-dialog/">confirmation dialog</a> to explain details and help the user fix the issue. However, use such dialogs sparingly as they have two big disadvantages:</p>

<ul>

<li>They are disruptive.</li>

<li>The error message appears in a window that must be dismissed before fixing the error, forcing users to remember complex instructions and increasing <a href="https://www.nngroup.com/articles/minimize-cognitive-load/">cognitive load</a>.</li>

</ul>

<p> Modal dialogs are, however, okay if the error message is simple or the form could still be submitted as it is.</p>

<figure class="caption"><img alt="modal warning" height="291" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/23/modal-gmail.png" width="692"/>

<figcaption><em>Gmail.com used a modal to warn the users that the attachment was missing. This error presentation is suitable because the error message is fairly simple, and the user can choose to proceed without including an attachment.</em></figcaption>

</figure>

<h2 id="toc-7-dont-validate-fields-before-input-is-complete-8">7. Don’t Validate Fields Before Input is Complete</h2>

<p>In most cases, avoid showing an error until the user has finished with the field and moved to the next field. It’s frustrating to see an error message before being given the opportunity to finish typing.</p>

<figure class="caption"><img alt="Best Buy contact form" height="525" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/23/best-buy-error.png" width="692"/>

<figcaption><em>When placing an order on BestBuy.com, an error message appeared in the Email Address field after the user navigated away from it. However, going back to fix the error prompted another error to appear in the Phone Number field, although the user had not started typing in that field.</em></figcaption>

</figure>

<h2 id="toc-8-dont-use-validation-summaries-as-the-only-indication-of-an-error-9">8. Don’t Use Validation Summaries as the Only Indication of an Error</h2>

<p>A <strong>validation summary</strong> is shown at the top of a form and lets users know that there are errors that need to be fixed on the page, whether those errors are in the viewport or below the fold. A validation summary can give the user a global understanding of all the errors in a form but shouldn’t be used as the only form of error indication, as it forces the user to search for the field in error; moreover, the error message may no longer be present in the viewport when the user reaches the error field, thus forcing the user to memorize the error message while fixing the issue.</p>

<figure class="caption"><img alt="validation summary" height="502" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/23/survey-monkey-error.png" width="692"/>

<figcaption><em>SurveyMonkey provided error messages at the top of the form as well as below the specific field(s) causing errors.</em></figcaption>

</figure>

<h2 id="toc-9-dont-use-tooltips-to-report-errors-10">9. Don’t Use Tooltips to Report Errors</h2>

<p><a href="https://www.nngroup.com/articles/tooltip-guidelines">Tooltips</a> are sometimes used to indicate errors, typically with an alert icon displayed next to the field(s) in error. When users hover over the icon or focus on the field, a tooltip or a toast containing the error message appears.</p>

<p>This approach is generally not recommended for a few reasons:</p>

<ul>

<li><strong>Alert icons are hard to notice</strong>, especially on visually dense interfaces.</li>

<li><strong>Users may not realize that an error message is displayed</strong> and wonder what is wrong with the field without realizing that they need to hover or focus to see the message.</li>

<li><strong>It adds unnecessary effort</strong>, requiring users to take extra steps to access critical information.</li>

</ul>

<figure class="caption"><img alt="facebook tooltips" height="459" loading="lazy" src="https://media.nngroup.com/media/editor/2018/11/23/facebook-tooltips.png" width="692"/>

<figcaption><em>Facebook.com: The errors in the signup form were displayed as alert icons. Users had to click on each one to see what the problem was. While in this example, the errors are easy to infer, it would be harder to do so if the fields were filled in.</em></figcaption>

</figure>

<h2 id="toc-10-provide-extra-help-for-repeated-errors-11">10. Provide Extra Help for Repeated Errors</h2>

<p>When users encounter the same error repeatedly (3 or more times in a single form-filling attempt), it indicates a deeper issue in the user interface — unclear error messages, a mismatch between the design and users’ needs, or overly complex requirements in the form. Remember that when users make errors, it’s not their fault. Errors highlight flaws in your design.</p>

<figure class="caption"><img alt="Modal dialog that includes a form with an error message at the top, and a link to contact support" height="1189" loading="lazy" src="https://media.nngroup.com/media/editor/2024/12/12/quicken.png" width="1911"/>

<figcaption><em>Quicken provided a link to a contact form to get in touch with support if repeated errors occur.</em></figcaption>

</figure>

<p>To address repeated errors:</p>

<ul>

<li>Review analytics data for error patterns to identify common scenarios where errors occur.</li>

<li>Test and refine the design to uncover the root cause of errors.</li>

<li>Revise error messages to provide more actionable feedback.</li>

</ul>

<h2 id="toc-conclusion-12">Conclusion</h2>

<p>Error flows should be designed to help users fix mistakes in a form and help them avoid making more. Ensure that users can easily detect errors, understand how to fix them, and see the error message while correcting the corresponding error. Remove the guesswork and let users get on with their tasks.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=errors-forms-design-guidelines&amp;pt=article">

<h4 class="title heading-small">Application Design for Web and Desktop</h4>

<p id="application-design-for-web-and-desktop" class="description body-small">

Components, design patterns, workflows, and ways of interacting with complex data

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-interaction" />

</svg>

<p class="ux-specialty interaction-design">Interaction</p>

</div>

</div>

</a>

</li>

</ul>

</div>

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Design Patterns,Interaction Design,Application Design,Visual Design,errors,forms,help and user assistance,design mistakes,password</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Design Patterns</span>

<a class="ga-article-related-topic" href="/topic/design-patterns/">Design Patterns</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/interaction-design/">Interaction Design</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/applications/">Application Design</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/visual-design/">Visual Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>