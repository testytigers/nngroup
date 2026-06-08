# Variable Fonts and Wide-Screen Layouts: Adopting Data-Driven Progressive Enhancements - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">4</span>

<div class="article-header">

<h1 class="article-h1">Variable Fonts and Wide-Screen Layouts: Adopting Data-Driven Progressive Enhancements</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Kathryn Whitenton, Sarah Gibbons</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/Kathryn_1.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/20211213_Vegas-22.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/kathryn-whitenton/">

Kathryn Whitenton</a> and

<a class="ga-article-author" href="/articles/author/sarah-gibbons/">

Sarah Gibbons</a></span>

<p class="publication-date">

November 25, 2018

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2018-11-25</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Variable Fonts and Wide-Screen Layouts: Adopting Data-Driven Progressive Enhancements&amp;body=https://www.nngroup.com/articles/variable-fonts-wide-screen-layout/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/variable-fonts-wide-screen-layout/&amp;title=Variable Fonts and Wide-Screen Layouts: Adopting Data-Driven Progressive Enhancements&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/variable-fonts-wide-screen-layout/&amp;text=Variable Fonts and Wide-Screen Layouts: Adopting Data-Driven Progressive Enhancements&amp;via=nngroup" data-share-type="Twitter">

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

</span>The NN/g website homepage now incorporates variable fonts and a wide-screen layout — 2 technical adjustments which improve the user experience for a subset of users on supported devices.

</div>

<div class="article-body">

<p>We recently <a href="https://www.nngroup.com/articles/case-study-iterative-design-prototyping/">updated our website homepage</a>, and, in addition to changing the content and visual design, we’ve incorporated two major technical changes: adding a new layout for users with wide screens, and using a variable font. These changes are <a href="https://www.nngroup.com/articles/enhancement/">progressive enhancements</a>, because they only affect users with particular types of devices.</p>

<p>Since these changes are also complex to implement, we decided to adopt them only after reviewing our website traffic to determine how many of our visitors would benefit and if the changes were worth our business resources.</p>

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

<a class="ga-article-toc-item" href="#toc-wide-screen-breakpoint-1">Wide-Screen Breakpoint</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-variable-fonts-2">Variable Fonts</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-prioritizing-by-audience-size-3">Prioritizing by Audience Size</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-4">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-wide-screen-breakpoint-1">Wide-Screen Breakpoint</h2>

<p>In 2006, we recommended <a href="https://www.nngroup.com/articles/screen-resolution-and-page-layout/">designing layouts for viewports 1024-pixel</a> wide. But with today’s higher-resolution screens, that approach can leave many users with inches of unused space on both sides of the content — even on a small 13-inch laptop. To decide whether to invest in creating wide-screen layouts, we took a look at our website analytics, and realized that 77% <strong>of our sessions are on browser windows wider than 1100 pixels</strong>.</p>

<figure class="caption"><img alt="" height="413" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/30/browser-width-distribution-july-sep-2018.png" width="692"/>

<figcaption><em>Analytics data for nngroup.com from July through September 2018 show that about 16% of visitors have browser less than 500 pixels wide; about 7% have browsers between 500 and 1100 pixels wide, and the remaining 77% of visitors had browsers wider than 1100 pixels.</em></figcaption>

</figure>

<p>To support these users, the new homepage adjusts to large screens. (As of this writing, only the homepage adjusts; in the coming months we’ll be extending this feature to other pages, as well.)</p>

<figure class="caption"><img alt="" height="315" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/30/1580px.png" width="692"/>

<figcaption><em>Left: When viewed on wide screens, many websites display blank space on either side of the page content. Right: A responsive design optimized for wide screens can adjust to use that wasted space to show additional content (in this case, articles and event information). These screenshots were taken at a width of 1580 px.</em></figcaption>

</figure>

<h2 id="toc-variable-fonts-2">Variable Fonts</h2>

<p>Users want websites that <a href="https://www.nngroup.com/articles/aesthetic-usability-effect/">look good</a>, but they also detest websites that <a href="https://www.nngroup.com/articles/website-response-times/">load slowly</a>. Unfortunately, many design tactics for enhancing visual appeal result in slow page rendering. This dilemma is a common one: what do you prioritize and when do you make tradeoffs?</p>

<p>The tradeoff between aesthetics and performance is especially apparent when it comes to typefaces: rendering text in a custom font can significantly increase the visual appeal, but comes with delays due to the extra time needed for browsers to load the custom font files. The delay is even greater when your text requires different weights (such as bold or light weights), since each weight involves a separate font-file download. Font-file compression and caching help, but these techniques don’t completely solve the problem.</p>

<p>To expedite page load time, we previously used just one custom font for headings, and relied on standard browser-safe fonts for most text, since browsers can render both normal and bold weights without needing to download any font files at all. This approach wasn’t ideal because it was a compromise in both directions: having to load a custom font and still not achieving our ideal visual aesthetic (which would have taken more 3 custom-font weights).</p>

<p>This time around we discovered a new solution: <strong>variable fonts</strong>, which allow using a single font file but adjusting the weight of the characters. <a href="https://en.wikipedia.org/wiki/Variable_fonts">Variable fonts were introduced in September 2016</a> as a joint effort by Adobe, Apple, Google, and Microsoft; in just 2 years, <a href="https://caniuse.com/#feat=variable-fonts">browser support for variable fonts</a> has increased from 2% to 70%.</p>

<figure class="caption"><img alt="" height="359" loading="lazy" src="https://media.nngroup.com/media/editor/2018/10/30/source-sans-variable.gif" width="692"/>

<figcaption><em>Variable fonts allow you to download a single font file and adjust it to heavy or light weights within the browser. This example demonstrates heavy and light weights for Adobe’s Source Sans variable font. (Image credit: <a href="https://v-fonts.com/">https://v-fonts.com/</a>)</em></figcaption>

</figure>

<p>We consulted our own web analytics and found that, for our audience, adoption is even higher than 70%: currently, 80% of sessions on nngroup.com are on browsers that support variable fonts, and we expect this number to increase further soon, when Firefox for Windows will implement its planned support for this feature. The 20% of traffic from browsers that do not support variable fonts will see a fallback, with browser-safe fonts plus one custom font, as our legacy site used to have. (We are grateful to Adobe, for releasing <a href="https://github.com/adobe-fonts/source-sans-pro">Source Sans Pro</a> as an open-source variable font and to Richard Rutter, whose <a href="http://clagnut.com/blog/2390/">article about implementing variable fonts with a fallback</a> was extremely helpful.)</p>

<h2 id="toc-prioritizing-by-audience-size-3">Prioritizing by Audience Size</h2>

<p>Each of the changes described here benefits about 80% of users. But what about the other 20% of users? When prioritizing design options and making <a href="https://www.nngroup.com/courses/design-tradeoffs/">tradeoffs</a>, it’s important to consider both the <strong>size of the affected audience groups</strong> and the <strong>severity of the effect</strong> on each group. A change that benefits most users may not be worthwhile if it creates a very negative impact on a minority of users (assuming that minority is actually part of your target audience).</p>

<p>Let’s consider a case from the history of the web, at the time when 20% of users were still using slow dial-up modems. You would like to use a nice big hero image that would increase page load time by 1 minute for these dial-up users, even though the delay would be negligible for broadband users. Don’t do it. The penalty for the 20% of users would be too big. Similarly, it would not be wise to distribute a document in a format that 80% of users would be able to view, but 20% of users could not open at all.</p>

<p>In these two examples (and many more), the enhancement that would benefit 80% of the users ends up imposing severe pain on the remaining 20% of users.</p>

<p>Luckily, wide-screen layouts and variable fonts don’t fall into this category. Yes, the 80% of users will see a better-looking website, but the 20% of users will still see a good-looking site. Nothing terrible will happen to them — in fact, their experience will be exactly as before. The existence of the fallback solution makes all the difference to the feasibility of helping the 80% without hurting the 20%.</p>

<h2 id="toc-conclusion-4">Conclusion</h2>

<p>We’re well-known for our conservative approach to design. We came by it honestly: in <a href="https://www.nngroup.com/articles/nielsen-norman-group-20-years/">20 years of user research</a>, we’ve observed too many design fads that didn’t help — and some that even hurt —the end-user’s experience.</p>

<p>But a cautious approach to trends doesn’t mean rejecting all innovation. We’re picky about which bandwagons we join, choosing only <a href="https://nngroup.com/videos/3-bs-design-trends/">trends that provide true UX value</a>. Less scrolling and more content for large-screen users is a clear winner. And although variable fonts are not yet widely adopted, we bet that this innovative technology is here to stay, given its overwhelming industry support and demonstrable benefit to both appearance and performance.</p>

<p>These examples demonstrate just a few of the ways in which <a href="https://www.nngroup.com/articles/analytics-user-experience/">analytics can drive meaningful adjustments to improve users’ experiences</a>. Whether it be new technology or extensive breakpoints, look at your own website’s analytics before deciding where it is worth investing your design and development resources.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Emerging Patterns in Interface Design" href="/courses/emerging-patterns-interface-design/?lm=variable-fonts-wide-screen-layout&amp;pt=article">

<h4 class="title heading-small">Emerging Patterns in Interface Design</h4>

<p id="emerging-patterns-in-interface-design" class="description body-small">

Trending UX patterns and their impact on the total user experience

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">responsive design,Design Patterns,homepages,new technologies,response time,web trends,Visual Design,Site Optimization,screen size</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Design Patterns</span>

<a class="ga-article-related-topic" href="/topic/design-patterns/">Design Patterns</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/visual-design/">Visual Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>