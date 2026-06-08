# Date-Input Form Fields: UX Design Guidelines - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">5</span>

<div class="article-header">

<h1 class="article-h1">Date-Input Form Fields: UX Design Guidelines</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Angie Li</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/IMG_2729_copy-square-close-800px.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list">

Angie Li

</span>

<p class="publication-date">

January 22, 2017

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2017-01-22</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Date-Input Form Fields: UX Design Guidelines&amp;body=https://www.nngroup.com/articles/date-input/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/date-input/&amp;title=Date-Input Form Fields: UX Design Guidelines&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/date-input/&amp;text=Date-Input Form Fields: UX Design Guidelines&amp;via=nngroup" data-share-type="Twitter">

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

</span>Date-entry fields must be unambiguous and support task completion by using the right design pattern. Small design changes can prevent big user errors.

</div>

<div class="article-body">

<p>Formatting a date-entry field may seem like a minor detail; however, even small interactions can draw a process to a standstill if implemented improperly. Poorly designed date input leads to distressed or annoyed users — risking the abandonment of the form altogether. Even worse, if the user specifies the wrong date, the entire transaction could be a disaster -- think, for example, how you'd feel if you showed up at the theater excited for a new show, only to discover that you bought tickets for a different day.</p>

<p>Considerations for users on mobile devices and for global audiences must be taken into account to improve this small, but fundamental input. This article discusses common input patterns, error handling, and international input for date fields.</p>

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

<a class="ga-article-toc-item" href="#toc-date-input-patterns-1">Date-Input Patterns</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-date-input-design-guidelines-2">Date-Input Design Guidelines</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-3">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-date-input-patterns-1">Date-Input Patterns</h2>

<p>Calendar pickers are control elements that display a full calendar month at one time. They typically show the days of the week across the top and match the metaphor of desk or wall calendars.</p>

<figure class="caption"><img alt="" height="623" loading="lazy" src="https://media.nngroup.com/media/editor/2016/11/28/01-material-design-blur.PNG" width="350"/>

<figcaption><em>Example of calendar picker on mobile shown on Google Calendar app</em></figcaption>

</figure>

<p>Calendar pickers should be used for <strong>events close to the present time</strong> — within less than a year. However, they can be frustrating for users who choose dates far in advance because they require too much navigation to get to the desired input; for these users, it would be faster to simply type the year.  </p>

<p>Calendar pickers are especially useful for selecting a date range. In those situations, they often display two months side by side.</p>

<figure class="caption"><img alt="Examples/Revision%20Examples/Expedia%20Return%20-%20Highlight.png" height="380" loading="lazy" src="https://media.nngroup.com/media/editor/2016/11/28/02-expedia.png" width="692"/>

<figcaption><em>Expedia used a soft blue highlight to show the date range for the selected departure and return dates. The departure and return dates are colored differently in the calendar.</em></figcaption>

</figure>

<ul>

<li><strong>Scrolling date pickers on mobile devices </strong>are common, yet they can be annoying if the picker contains many dates. In those situations, scrolling in a small space is slow and unproductive; it’s better to allow users to type the date directly.<br/>

<br/>

In the Todoist app, users can enter the deadline for each task using an endless scrolling list. This is not an issue if the deadline occurs on that Friday or Saturday, as shown below, however, if the deadline is even a few weeks away it is easier for the user to type the date instead (a functionality that the app also provides).

<p> </p>

<figure class="caption"><img alt="Examples/Revision%20Examples/Todoist.PNG" height="623" loading="lazy" src="https://media.nngroup.com/media/editor/2016/11/28/03-todoist.PNG" width="350"/>

<figcaption><em>The iPhone Todoist app allowed users to scroll as well as type for date input. (Note the benefit of denoting the current date as “today:” it removes any uncertainty in case the user doesn’t remember today’s date.)</em></figcaption>

</figure>

</li>

<li><strong>Split date fields with drop-downs for month, day, and year</strong> require a lot of unnecessary steps. This method increases <a href="/articles/interaction-cost-definition/">interaction cost</a> by adding additional clicks and scrolling. We advise against using this pattern.

<figure class="caption"><img alt="" border="0" height="616" loading="lazy" src="https://media.nngroup.com/media/editor/2016/11/28/04-deviantart.png" width="692"/>

<figcaption><em>DeviantArt provided drop-downs for each section of the date field.</em></figcaption>

</figure>

</li>

<li><strong>Typing the date </strong>is the most basic option for date input, yet in many cases it is the most efficient one, especially when the date is further away in the past (e.g., birthdate) or future. We recommend that you allow users to type the date even if other input methods are available.</li>

</ul>

<h2 id="toc-date-input-design-guidelines-2">Date-Input Design Guidelines</h2>

<ul>

<li><strong>For a limited number of date options, provide a list of the applicable dates.</strong><br/>

In some cases, users will have only few date choices. For example, Google Express, an online shopping service, makes it possible for customers to order groceries online and schedule a delivery time. Rather than offering blank date fields or a calendar picker of limitless options, Google Express provides a short list of date options. Any dates that are unavailable have been grayed out and disabled. (Alternatively, unavailable dates may not even be included in the list.)

<figure class="caption"><img alt="../../../Downloads/express-date.PNG" border="0" height="464" loading="lazy" src="https://media.nngroup.com/media/editor/2016/11/28/05-google-express.PNG" width="692"/>

<figcaption><em>Google Express provided a drop-down with delivery options. The selection that is not available has been disabled and grayed out.</em></figcaption>

</figure>

<p>In general, we don't recommend this method when there are more than 10 dates available however, as it can become tedious for people to scan and scroll through the list of dates.</p>

</li>

<li><strong>Do not require users to enter special characters to format dates.</strong>

<p>Whatever format users chose for entering the date (dashes, spaces, slashes, dots between the month, day, and year components), their input should be recognized. Moreover, leftmost zeros should not affect the date. In the Priceline example below, the date 9-3-17 is rejected and 09/08/17 is accepted, although no format requirements were visible before submitting the form.</p>

<figure class="caption"><img alt="../../../Documents/Priceline%20-%20Different%20Formats%20-%20Error%20" border="0" height="376" loading="lazy" src="https://media.nngroup.com/media/editor/2016/11/28/06-priceline.png" width="692"/>

<figcaption><em>Priceline rejected the date 9-3-17 without even providing suggestions on how to properly format it. Instead, it should have accepted it and parsed it for the user.</em></figcaption>

</figure>

</li>

<li><strong>Report errors appropriately.</strong><br/>

If a user enters a date that is obviously a mistake, such as 11/81/17, do not make any assumptions. Give the user feedback and provide suggestions on how to resolve the error.</li>

<li><strong>Remove illogical date options.</strong><br/>

Prevent users from selecting illogical dates. Obviously, what’s reasonable will depend from case to case: for example, dates older than 130 years will be unlikely for birthdates, but quite acceptable for document dates. Users should be prevented from entering a return date that takes place before the departure date or that is in the past. Make the choices clear by disabling and graying out options that are not available or are illogical pairs.</li>

</ul>

<ul>

<li><strong>Preserve users’ work.</strong><br/>

If the same date information is required in a separate part of the form or later during a task, then don’t make users enter that date twice.</li>

<li><strong>Keep date ranges consistent.</strong><br/>

Avoid shifting date ranges for departure and return pairs. For example, if November—December is shown for departure, do not shift and show December—January for the return date range. The change may go unnoticed and <a href="https://www.nngroup.com/articles/slips/">cause users to slip</a> by clicking where the intended date used to be.

<figure class="caption"><img alt="" height="375" loading="lazy" src="https://media.nngroup.com/media/editor/2016/11/28/southwest.png" width="692"/>

<figcaption><em>Southwest Airlines shifted the return date range based on the </em><em>departure-date</em><em> selection. After selecting the departure date 8-16-16 from the July–August date range, the return date range changed to show August–September. </em></figcaption>

</figure>

</li>

<li><strong>If your site caters to international users, your date format should be clear and understandable.</strong>

<p>Date-entry fields are culture dependent, and can cause major problems for those users who are accustomed to a different format. “10/11/2016” could mean 11<sup>th</sup> of October 2016 to an American, but November 10<sup>th</sup> to someone from Europe. Follow these rules of thumb when designing date input for a global audience:</p>

<ul>

<li><strong>Add labels and separate the fields</strong> to make it clear which fields are for the month, day, and year.

<figure class="caption"><img alt="../Google%20Drive/Articles/Date%20Input%20Format/Examples/dateandtime.PNG" border="0" height="245" loading="lazy" src="https://media.nngroup.com/media/editor/2016/11/28/09-countdown-timer.png" width="359"/>

<figcaption><em>This countdown timer separated the date components and labeled them clearly.</em></figcaption>

</figure>

</li>

<li><strong>Spell out the name of the month</strong> to distinguish it from the day.

<figure class="caption"><img alt="../Google%20Drive/Articles/Date%20Input%20Format/Examples/tepwireless.png" border="0" height="474" loading="lazy" src="https://media.nngroup.com/media/editor/2016/11/28/10-tep-wireless.png" width="692"/>

<figcaption><em>The Tep Wireless site, where users can rent portable WiFi devices, spelled out the name of the month to serve its global audience.</em></figcaption>

</figure>

<figure class="caption"><img alt="eurostar-en.png" border="0" height="462" loading="lazy" src="https://media.nngroup.com/media/editor/2016/11/28/11-eurostar.png" width="692"/>

<figcaption><em>The Eurostar website, shown in English (US), supported several languages but did not say what date format it expected.  Here, the departure date could be read as July 2 or February 7.</em></figcaption>

</figure>

</li>

<li><strong>Utilize calendar pickers with clearly spelled out names for months.</strong>

<p>Some frameworks, such as Bootstrap, provide calendar pickers to support unambiguous date selection.</p>

<figure class="caption"><img alt="bootstrap calendar picker.png" border="0" height="342" loading="lazy" src="https://media.nngroup.com/media/editor/2016/11/28/12-bootstrap.png" width="350"/>

<figcaption><em>The Bootstrap calendar picker spelled out the name of the month, making it clear which date to select.</em></figcaption>

</figure>

<figure class="caption"><img alt="ctrip-english.png" border="0" height="392" loading="lazy" src="https://media.nngroup.com/media/editor/2016/11/28/13-ctrip.png" width="692"/>

<figcaption><em>The calendar picker on the English version of Ctrip did not spell the name of the month. Users had to infer that the month comes before the day. </em></figcaption>

</figure>

</li>

</ul>

</li>

</ul>

<h2 id="toc-conclusion-3">Conclusion</h2>

<p>Date-input patterns are not created equal. Implement design patterns that are appropriate for your context. When designing date-entry fields support text input and consider whether or not you have an international audience. Avoid designs that are ambiguous because they can cause people to become frustrated and annoyed with your site. Follow these guidelines to prevent form abandonment and catastrophic errors.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=date-input&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">forms,Application Design,Design Patterns</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Application Design</span>

<a class="ga-article-related-topic" href="/topic/applications/">Application Design</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/design-patterns/">Design Patterns</a>

</li>

</ul>

</div>

</div>

</div>

</div>