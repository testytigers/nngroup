# A Checklist for Designing Mobile Input Fields - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">1</span>

<div class="article-header">

<h1 class="article-h1">A Checklist for Designing Mobile Input Fields</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Raluca Budiu</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/2023-04-portraits-raluca.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/raluca-budiu/">

Raluca Budiu</a></span>

<p class="publication-date">

June 14, 2015

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2015-06-14</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: A Checklist for Designing Mobile Input Fields&amp;body=https://www.nngroup.com/articles/mobile-input-checklist/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/mobile-input-checklist/&amp;title=A Checklist for Designing Mobile Input Fields&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/mobile-input-checklist/&amp;text=A Checklist for Designing Mobile Input Fields&amp;via=nngroup" data-share-type="Twitter">

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

</span>When you design an input field for use on mobile devices, check whether it satisfies this list of 14 usability requirements.

</div>

<div class="article-body">

<p>Whether you're designing web pages, web-based applications (e.g., SaaS), or native mobile apps, one of the basic building blocks is the humble text-input field: a box where the user can enter some text. Uses of this widget are plenty and not the topic of this article. We should point out that there are many issues in application design relating to workflow and other big-picture questions that are important for good application user experience. (These topics are discussed in our full-day <a href="/courses/application-ux/">Application Design course</a>.)</p>

<p>In this article, we focus on the nitty-gritty of input fields. Each of these issues may seem minor, but we repeatedly see these usability guidelines violated — particularly in mobile user interfaces, where <a href="/articles/does-user-annoyance-matter/">even the smallest annoyance grows</a> from a molehill into a mountain in terms of its ability to delay users and prevent them completing tasks with your design.</p>

<p>Here's how an input field should look:</p>

<p><img alt="" height="87" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/05/14/inputfield.png" width="200"/></p>

<p><span style="line-height: 1.6;">Here's a checklist of 14 guidelines to follow for mobile input field UX:</span></p>

<table border="1" cellpadding="0" cellspacing="0" style="width:100%;">

<tbody>

<tr>

<td style="width:25%;"><strong>Should it be there at all</strong></td>

<td style="width:75%;">

<ol>

<li>Is this field absolutely necessary?</li>

</ol>

</td>

</tr>

<tr>

<td><strong>Description</strong></td>

<td>

<ol start="2">

<li>Is the label above it? (Not inside, not below)</li>

<li>Is the field marked as required (*) or optional?</li>

<li>Have you removed any <a href="/articles/form-design-placeholders/">placeholder</a> from inside the field?</li>

</ol>

</td>

</tr>

<tr>

<td><strong>Visibility</strong></td>

<td>

<ol start="5">

<li>Is the field big enough so that most possible field values are visible?</li>

<li>Is the field visible in both orientations when the keyboard is displayed?</li>

</ol>

</td>

</tr>

<tr>

<td><strong>Filling it in for the user</strong></td>

<td>

<ol start="7">

<li>Do you have any good defaults for this field?

<ul>

<li>Any history available?</li>

<li>Frequently used values?</li>

</ul>

</li>

<li>Can you use the phone features (camera, GPS, voice, contacts ) to populate it?</li>

<li>Can you compute it for the user based on other info (e.g., state based on zip code, coupon field)?</li>

</ol>

</td>

</tr>

<tr>

<td><strong>Typing</strong></td>

<td>

<ol start="10">

<li>Do you support copy &amp; paste into the field?</li>

<li>What is the right keyboard for this field?</li>

<li>Can you make suggestions/autocomplete based on the first letters typed?

<ul>

<li>Do not autocorrect for names, addresses and email addresses.</li>

</ul>

</li>

<li>Do you allow typos or abbreviations?</li>

<li>Do you allow users to enter it in whatever format they like? (e.g., phone numbers credit cards)

<ul>

<li>You can autoformat it for them.</li>

</ul>

</li>

</ol>

</td>

</tr>

</tbody>

</table>

<p>Go through your design and complete the checklist for every single input field. Yes, this is work, but better you suffer than the users suffer.</p>

<p>Ideally, you'll have 100% checklist compliance for 100% of the input fields in your site or app. Anything less, and you do have a substandard user experience.</p>

<p>Pragmatically, you may not have resources to deliver 100% on these UX requirements. In that case, prioritize the fields so that the ones that are used the most or are the most critical for task completion get the highest scores.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=mobile-input-checklist&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Mobile &amp; Tablet,forms,Application Design</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Mobile &amp; Tablet</span>

<a class="ga-article-related-topic" href="/topic/mobile-and-tablet-design/">Mobile &amp; Tablet</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/applications/">Application Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>