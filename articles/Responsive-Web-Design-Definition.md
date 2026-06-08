# Responsive Web Design (RWD) and User Experience - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">4</span>

<div class="article-header">

<h1 class="article-h1">Responsive Web Design (RWD) and User Experience</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Amy Schade</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/amy_schade_headshot.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list">

Amy Schade

</span>

<p class="publication-date">

May 4, 2014

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2014-05-04</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Responsive Web Design (RWD) and User Experience&amp;body=https://www.nngroup.com/articles/responsive-web-design-definition/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/responsive-web-design-definition/&amp;title=Responsive Web Design (RWD) and User Experience&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/responsive-web-design-definition/&amp;text=Responsive Web Design (RWD) and User Experience&amp;via=nngroup" data-share-type="Twitter">

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

</span>Responsive design teams create a single site to support many devices, but need to consider content, design and performance across devices to ensure usability.

</div>

<div class="article-body">

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

<a class="ga-article-toc-item" href="#toc-defining-responsive-design-1">Defining Responsive Design</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-creating-usable-experiences-2">Creating Usable Experiences</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-focusing-on-content-3">Focusing on Content</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-considering-performance-4">Considering Performance</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-5">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-defining-responsive-design-1">Defining Responsive Design</h2>

<p>Responsive web design (RWD) is a web development approach that creates <strong>dynamic changes</strong> to the appearance of a website, <strong>depending on the screen size and orientation</strong> of the device being used to view it. RWD is one approach to the problem of designing for the multitude of devices available to customers, ranging <a href="http://www.nngroup.com/articles/transmedia-design-for-3-screens/">from tiny phones to huge desktop monitors</a>.</p>

<p>RWD uses so-called breakpoints to determine how the layout of a site will appear: one design is used above a breakpoint and another design is applied below that breakpoint. The breakpoints are commonly based on the width of the browser.</p>

<div class="captioned">

<video controls="" preload="" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2014/04/25/london_700_2.mp4" width="100%"> </video>

<div class="caption"><em>This brief video (0:37) shows the responsive Transport for London website changing as the browser window is narrowed and widened.</em></div>

</div>

<p>The <strong>same HTML is served to all devices</strong>, using CSS (which determines the layout of webpage) to change the appearance of the page. Rather than creating a separate site and corresponding codebase for wide-screen monitors, desktops, laptops, tablets and phones of all sizes, a single codebase can support users with differently sized viewports.</p>

<p>In responsive design,<strong> page elements reshuffle</strong> as the viewport grows or shrinks. A three-column desktop design may reshuffle to two columns for a tablet and a single column for a smartphone. Responsive design relies on proportion-based grids to rearrange content and design elements.</p>

<p>While responsive design emerged as a way to provide equal access to information regardless of device, it is also possible to hide certain items — such as background images, as in the Transport for London example above, <a href="http://www.nngroup.com/articles/defer-secondary-content-for-mobile/">secondary content</a> or supplementary navigation — on smaller screens. Decisions about hiding content and functionality or altering appearance for different device types should be based on knowledge about your users and their needs.</p>

<p>RWD has potential advantages over developing separate sites for different device types. The use of a single codebase can make development faster, compared to developing 3 or 4 distinct sites, and makes <strong>maintenance easier over time</strong>, as one set of code and content needs to be updated rather than 3 or 4. RWD is also relatively “future-proof” in that it can support new breakpoints needed at any time. If a 5-inch device or 15-inch device takes off in the market, the code can support the new devices. RWD doesn’t tie design to a particular device.</p>

<figure class="caption"><img alt="" height="528" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2014/04/24/bostonglobe_desktop.png" width="720"/>

<figcaption></figcaption>

</figure>

<figure class="caption"><img alt="" height="626" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2014/04/25/boston_tab_mob.png" width="720"/>

<figcaption><em>The Boston Globe is well-known for using responsive design. The 3-column desktop version (top) changes to a 2-column design on tablets (bottom left) and a single column for mobile (bottom right).</em></figcaption>

</figure>

<p>Because elements need to be able to resize and shuffle, it is often easier to implement a responsive design on a site that is focused on content, rather than functionality. Complex data or interactions can be hard to fit into modular pieces that are easy to shuffle around a page, while preserving clarity and functionality.</p>

<h2 id="toc-creating-usable-experiences-2">Creating Usable Experiences</h2>

<p>Because responsive design relies on shuffling elements around the page, design and development need to work closely together to ensure a usable experience across devices. Responsive design often turns into solving a puzzle — how to reorganize elements on larger pages to fit skinnier, longer pages or vice versa. However, <strong>ensuring that elements fit within a page is not enough</strong>. For a responsive design to be successful, the design must also be usable at all screen resolutions and sizes.</p>

<p>When elements move around the page, the user experience can be completely different from one view of the site to the next. It is important that design and development teams work together not to just determine how the content should be shuffled around, but to also see <strong>what the end result of that shift looks like</strong> and how it affects the user experience.</p>

<p>Many teams look to popular responsive-design frameworks, such as Bootstrap to help create designs. Such frameworks can be a great help in moving development along. However, carefully consider how the framework will work with the content and functionality of your site, rather than how it works in general.</p>

<p>We always recommend <a href="http://www.nngroup.com/articles/mobile-usability-testing/">conducting usability testing</a> on designs. For responsive designs, we recommend <strong>testing across platforms</strong>. It’s tricky enough to design a website that is usable on a desktop. It is even trickier to design a website that is usable in many rearrangements or configurations of its elements, across various screen sizes and orientations. The same design element that may work swimmingly on a desktop may work horribly on a smartphone, or vice versa.</p>

<h2 id="toc-focusing-on-content-3">Focusing on Content</h2>

<p><a href="http://www.nngroup.com/articles/responsive-design-intranets">Content prioritization</a> is one key aspect to doing responsive design well. Much <a href="http://www.nngroup.com/articles/scaling-user-interfaces/">more content is <u>visible</u></a> without scrolling on a large desktop monitor than on a small smartphone screen. If users don’t instantly see what they want on a desktop monitor, they can easily glance around the page to discover it. On a smartphone, users may have to scroll endlessly to discover the content of interest. Smart content prioritization helps users find what they need more efficiently.</p>

<h2 id="toc-considering-performance-4">Considering Performance</h2>

<p><a href="http://www.nngroup.com/articles/website-response-times/">Performance</a> can also be an issue with responsive design. RWD delivers the <strong>same code to all devices</strong>, regardless if the piece of code applies to that design or not. Changes to the design occur on the client-side, meaning each device — the phone, tablet or computer — receives the full code for all devices and takes what it needs.</p>

<p>A 4-inch smartphone receives the same code as a 24-inch desktop monitor. This can bog down performance on a smartphone, which may be relying on a slower, spottier data connection. (This is why some sites turn to <strong>adaptive design</strong>, where the server hosting the website detects the device that makes the request and delivers different batches of HTML code based on that device.)</p>

<p>To truly assess the user experience of a responsive design, do not test your responsive designs only in the comfort of your own office, on your high-speed connection. Venture out into the wild with your smartphone— between tall buildings in a city, in interior conference rooms or basements, in remote areas with spotty connectivity, in known trouble spots for your own cell-phone’s network connection — and see how your site performs in varied conditions. The goal of many responsive designs is to give equivalent access to information regardless of device. A smartphone user does not have an equivalent experience to a desktop user if download times are intolerable.</p>

<h2 id="toc-conclusion-5">Conclusion</h2>

<p>Responsive design is a tool, not a cure-all. While using responsive design has many perks when designing across devices, using the technique does not ensure a usable experience (just as using a gourmet recipe does not ensure the creation of a magnificent meal.) Teams must focus on the details of content, design, and performance in order to support users across all devices.</p>

<p>For more about designing for different devices, see our course <a href="http://www.nngroup.com/courses/scaling-responsive-design/">Scaling User Interfaces</a>.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="The Human Mind and Usability" href="/courses/human-mind/?lm=responsive-web-design-definition&amp;pt=article">

<h4 class="title heading-small">The Human Mind and Usability</h4>

<p id="the-human-mind-and-usability" class="description body-small">

Use psychology to predict and explain how your customers think and act

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

<li>

<a class="tile ga-article-related-course" data-course-title="Web Page UX Design" href="/courses/web-page-design/?lm=responsive-web-design-definition&amp;pt=article">

<h4 class="title heading-small">Web Page UX Design</h4>

<p id="web-page-ux-design" class="description body-small">

Strategically combine content, visuals, and interactive components to design successful web pages

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Mobile &amp; Tablet,Web Usability,responsive design,performance</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Mobile &amp; Tablet</span>

<a class="ga-article-related-topic" href="/topic/mobile-and-tablet-design/">Mobile &amp; Tablet</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/web-usability/">Web Usability</a>

</li>

</ul>

</div>

</div>

</div>

</div>