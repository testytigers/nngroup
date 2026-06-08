# Graceful Degradation of Scalable Internet Services - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">4</span>

<div class="article-header">

<h1 class="article-h1">Graceful Degradation of Scalable Internet Services</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Jakob Nielsen</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/Jakob-Nielsen-tie-800x800.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/jakob-nielsen/">

Jakob Nielsen</a></span>

<p class="publication-date">

October 31, 1999

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">1999-10-31</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Graceful Degradation of Scalable Internet Services&amp;body=https://www.nngroup.com/articles/graceful-degradation-of-scalable-internet-services/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/graceful-degradation-of-scalable-internet-services/&amp;title=Graceful Degradation of Scalable Internet Services&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/graceful-degradation-of-scalable-internet-services/&amp;text=Graceful Degradation of Scalable Internet Services&amp;via=nngroup" data-share-type="Twitter">

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

</span>Specialized Internet applications will return to provide richer UIs than are possible in browsers, but browsers will remain and new, smaller devices will arise, so content and features must work across three levels of sophistication. WAP will fail.

</div>

<div class="article-body">

<p>Many services will need to be offered at three levels of sophistication on the Internet:</p>

<ol>

<li><strong>Specialized applications </strong> that are optimized to provide the best possible user interface to a set of advanced features</li>

<li><strong>Traditional web pages </strong> that are highly standards-compliant and will work on two-years-old browsers with no or minimal use of plug-ins or anything else that goes beyond HTML and a few simple images.</li>

<li><strong>Narrowly focused small devices </strong> that cannot support the full range of features because of a lack of screen space or low bandwidth (mobile access to the Internet will typically use no more than 28.8 kbps the next few years)</li>

</ol>

<p>The advent of the graphical web browser in 1993 temporarily halted the development of specialized Internet applications. The main exception was email which is so important that most users refused to rely on the impoverished email access that can be provided through a browser. Email also provides an example of the interplay between specialized applications and toned-down web applications: it is often possible to access your email through a browser. Even though it is unpleasant to do so, the benefits of having access from odd places sometimes outweigh the downsides. And it is clearly <strong>the same email whether seen in a specialized client or a browser</strong>: same messages and the same basic features (delete, reply, send new message).</p>

<p>We are seeing a small renaissance in specialized Internet applications such as <a class="out" href="http://www.vertexdev.com/HeadlineViewer/" title="Software product page">Carmen's Headline Viewer</a> , (browsing headlines across a large number of XML-syndicated sites in a single UI), the <a a="" auction="" class="out" href="http://www.wired.com/news/news/technology/story/20771.html" title="WIRED news article by Lindsey Arent">  (monitoring a number of ongoing auctions in real time), and </a><a class="out" href="http://www.gurunet.com" title="Product page">GuruNet</a>  (pop-up window to retrieve dictionary definitions and other data across the Internet from inside any application). United Airlines has special <cite> United Connection </cite> software for ordering tickets over the Internet: even though it is clunky it is better in some ways than the web-based interface to the same backend. I predict that many more such specialized applications will emerge in 2000.</p>

<p><em>(Update 2003: Unfortunately specialized apps are emerging more slowly than I had thought. Kevin Lynch gives an <a href="http://www.klynch.com/archives/000014.html">overview of Internet Desktop applications</a>  available for the Mac as of February 2003.)</em></p>

<p>Most advanced applications don't work well inside a browser UI which is optimized for reading articles. Of course, browsers can improve, but if they deviate too much from the mission of reading and navigating online information, then they will reduce the usability of the Web. Information spaces and application spaces usually need different navigation support, so the best interfaces for the two will be different. No single UI is best for everything.</p>

<p>When offering multiple interfaces, it is important that they feel like <strong> variations of a <em> single </em>system</strong>, even though they have different designs:</p>

<ul>

<li>All system data should be the same across interfaces, even if not all information is shown in all versions. For example, prices should be the same, but a product listing may include only the best-selling items on a small screen with the rest relegated to a secondary "more products" page.</li>

<li>All user information must be preserved across the interfaces: if I use one access mechanism today and another tomorrow, then the changes I made in one UI are reflected in what I see in the other.</li>

<li>Unified login, user identification, and user profile (even though not all preference settings may apply to all UIs, those that do should be respected everywhere so that it is not necessary to manually define such preferences more than once).</li>

<li>Same functionality and side-effects of commands, even if certain special features or variations are eliminated in some versions. For example, an airline reservation system may make choosing a flight and buying the ticket two separate steps. This separation should be preserved in all versions instead of having the simplified version unify choosing and buying into a single step. It would be OK to have the advanced version include additional features (such as specifying a seating preference) that were not in the simplified version. Missing these features is a trade-off that the user would make in return for the benefits of being able to use the system under various limited circumstances.</li>

</ul>

<p>It is not necessary for all features to be found in all access mechanisms. For example, a low-end version may eliminate photos or it may show them in black-and-white. Similarly, text may be abbreviated on a small display, though it should be possible to retrieve the full text through a standardized command.</p>

<p>It will be a major design challenge to decide what features should be preserved in what versions of the system. I am hoping for <em> graceful </em> degradation so that users always have the features that they really need. Achieving this goal will require careful task analysis to determine how users behave when they are on the road or in other functionally limited circumstances.</p>

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

<a class="ga-article-toc-item" href="#toc-wap-w-rong-approach-to-portability-1">WAP: W rong Approach to Portability</a>

</li>

</ul>

</div>

</div><h2 id="toc-wap-w-rong-approach-to-portability-1">WAP: <em>W</em> rong <em>A</em>pproach to <em>P</em>ortability</h2>

<p>Having just toured Europe, I found great interest in WAP in Scandinavia and much skepticism in other countries.</p>

<p>WAP is a way to <strong> access the Internet through a mobile telephone</strong>, using its square-inch-sized window. This will lead to <strong> impoverished user interfaces </strong> for two reasons:</p>

<ul>

<li>a <strong> tiny screen cannot show any context </strong> , nor can it show menus or visualizations of alternatives</li>

<li>telephone <strong> push-buttons are poor controls </strong> for advanced functionality - as evidence just consider how few of the features on your cell phone you use...</li>

</ul>

<p><em>(See also <a href="/articles/wap-mobile-phones-field-study-findings/" title="Alertbox Dec. 2000: WAP Field Study Findings"> results from usability study of WAP</a>  conducted after I wrote this article.) </em></p>

<p>Mobile access to the Internet will be its third killer app (after email and Web browsing), so I believe that WAP will enjoy a temporary success while we await the arrival of true information appliances. In the long term, successful use of the Internet requires a bigger screen than the small window in mobile telephone handsets.</p>

<p><strong>I am a screen size bigot</strong>: Experience from many other user interface platforms indicates that a bigger screen leads to better usability than a small screen and that a graphical user interface adds even more usability. Obviously, in order to be mobile, the device must have a smaller screen than a desktop computer. A compromise somewhat along the lines of the Palm Pilot can combine mobility with a decent-sized screen.</p>

<p>A palm-sized form factor can double as a telephone through the use of a small headset; possibly connected wirelessly through Bluetooth. <em> Cellphones as currently known must die.</em></p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Mobile &amp; Tablet</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Mobile &amp; Tablet</span>

<a class="ga-article-related-topic" href="/topic/mobile-and-tablet-design/">Mobile &amp; Tablet</a>

</li>

</ul>

</div>

</div>

</div>

</div>