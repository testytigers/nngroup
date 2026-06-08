# Screen Resolution and Page Layout - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">4</span>

<div class="article-header">

<h1 class="article-h1">Screen Resolution and Page Layout</h1>

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

July 30, 2006

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2006-07-30</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Screen Resolution and Page Layout&amp;body=https://www.nngroup.com/articles/screen-resolution-and-page-layout/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/screen-resolution-and-page-layout/&amp;title=Screen Resolution and Page Layout&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/screen-resolution-and-page-layout/&amp;text=Screen Resolution and Page Layout&amp;via=nngroup" data-share-type="Twitter">

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

</span>Optimize Web pages for 1024×768, but use a liquid layout that stretches well for any resolution, from 800×600 to 1280×1024.

</div>

<div class="article-body">

<p>One of the most frequently asked questions in my <a class="new" href="http://www.nngroup.com/courses/fundamentals/" title="Nielsen Norman Group training tutorial"> Web usability course</a> is "What screen resolution should we design for?" The full answer is a bit tricky, but the basic advice is clear:</p>

<ul>

<li><strong>Optimize for 1024×768</strong>, which is currently the most widely used screen size. Of course, the general guideline is to optimize for your target audience's most common resolution, so the size will change in the future. It might even be a different size now, if, say, you're designing an intranet for a company that gives all employees big monitors.</li>

<li><strong>Do <em> not </em> design solely for a specific monitor size </strong> because screen sizes vary among users. Window size variability is even greater, since users don't always maximize their browsers (especially if they have large screens).</li>

<li><strong>Use a liquid layout </strong> that stretches to the current user's window size (that is, avoid frozen layouts that are always the same size).</li>

</ul>

<p>Currently, about <strong> 60% </strong> of all monitors are set at <strong> 1024×768 </strong> pixels. (See <a href="http://www.nngroup.com/articles/computer-screens-getting-bigger/">historical trends and newer data for screen sizes</a>.)  In comparison, only about <strong> 17% </strong> use <strong> 800×600 </strong> so it's obviously less important to aim at perfection for these small-display users. What's equally obvious, however, is that you can't simply ignore 17% of your customer segment by providing a frozen layout that requires more screen space than they have available.</p>

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

<a class="ga-article-toc-item" href="#toc-optimizing-for-1024768-1">Optimizing for 1024×768</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-big-screens-2">Big Screens</a>

</li>

</ul>

</div>

</div><h2 id="toc-optimizing-for-1024768-1">Optimizing for 1024×768</h2>

<p>When I say "optimize" I mean that your page should <strong> look and work the <em> best </em> at the most common size</strong>. It should still look <em> good </em> and work <em> well </em> at other sizes, which is why I recommend a liquid layout. But it should be its best at 1024×768.</p>

<p>The three main criteria in optimizing a page layout for a certain screen size are:</p>

<ul>

<li><strong>Initial visibility</strong>: Is all key information visible above the fold so users can see it without scrolling? This is a tradeoff between how many items are shown vs. how much detail is displayed for each item.</li>

<li><strong>Readability</strong>: How easy is it to read the text in various columns, given their allocated width?</li>

<li><strong>Aesthetics</strong>: How good does your page look when the elements are at the proper size and location for this screen size? Do all the elements line up correctly — that is, are captions immediately next to the photos, etc.?</li>

</ul>

<p>You should also consider all three criteria at the full range of sizes, continuously resizing the browser window from 800×600 to 1280×1024. Your page should score high on all criteria throughout the entire resolution range.</p>

<p>Your page should also work at even smaller and bigger sizes, though such extremes are less important. Fewer than half a percent of users still have 640×480. Although such users should certainly be able to access your site, giving them a less-than-great design is an acceptable compromise.</p>

<p>As the first criterion implies, <strong> scrolling </strong> is always a key consideration. Users generally don't like to scroll (see newer data on the <a class="new" href="/articles/scrolling-and-attention/" title="Alertbox: Scrolling and Attention"> distribution of users' attention above vs. below the fold</a>). So, when you design, you should consider how much users can see if they scroll only a screenfull or two.</p>

<p>Both scrolling and initial visibility obviously depend on screen size: Bigger screens show more content above the fold and require less scrolling. This is where you have to optimize for 1024×768: present your most compelling material above the fold at this resolution (while ensuring that the absolutely critical information remains visible at 800×600).</p>

<p>So, what about tiny screens, such as those found on <strong> mobile devices</strong>? A liquid design should scale all the way down to a phone, but don't assume that this is how you should deliver your company's <a class="new" href="/articles/mobile-usability-update/" title="Alertbox: Mobile Usability"> mobile user experience</a>. Mobile environments are special; to optimize for them, you must design a separate service that provides fewer features, is written even more concisely, and is more context aware.</p>

<h2 id="toc-big-screens-2">Big Screens</h2>

<p>Many users have large displays. Currently, about 18% of users have at least 1280×1024. The percentage of users with big screens is growing, though not as fast as I would like.</p>

<p>Big monitors are the easiest way to increase white-collar productivity, and <strong> anyone who makes at least $50,000 per year ought to have at least 1600×1200 screen resolution</strong>. A flat-panel display with this resolution currently costs less than $500. So, as long as the bigger display increases productivity by at least 0.5%, you'll recover the investment in less than a year. (The typical corporate overhead doubles the company's per-employee cost; always remember to use loaded cost, not take-home salary, in any productivity calculation.)</p>

<p>Apple and Microsoft have both published reports that attempt to quantify the productivity gains from bigger monitors. Sadly, the studies don't provide credible numbers because of various methodological weaknesses. My experience shows estimated productivity gains of 5–10% when users do knowledge work on a big monitor. This translates into about an 0.5–1% increase in overall productivity for a person who does screen-focused knowledge work 10% of the day. There's no doubt that big screens are worth the money.</p>

<p>I personally use a 2048×1536 display, and I wouldn't even call that a really big screen. Within the next 10 years, I expect monitors of, say, 5000×3000 to be in fairly common use, at least among high-end business professionals.</p>

<p>Starting at 1600×1200, users rarely stretch their browser windows to the full screen because few websites work well on such a wide canvas. Big windows are magic for working on spreadsheets, graphic design, and many other tasks, but not for the current paradigm of Web pages. Today, big-screen Web users typically utilize their extra space for multiple windows and <a class="old" href="/articles/users-interleave-sites-and-genres/" title="Alertbox: Users Interleave Sites and Genres"> parallel browsing</a>.</p>

<p>To serve Web users with truly big screens in the future, we'll probably need a different paradigm than individual pages. Perhaps a more newspaper-like metaphor or a different information dashboard will prove superior down the road.</p>

<p>In any case, the need for a new paradigm in the future doesn't change current recommendations: optimize for 1024×768, but don't design solely for this size. Your pages should work at any resolution, from 800×600 to 1280×1024 and beyond.</p>

<p>(See also: newer article about <a href="http://www.nngroup.com/articles/homepage-real-estate-allocation/">page design for bigger monitors</a> than those discussed here.)</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Visual Design</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Visual Design</span>

<a class="ga-article-related-topic" href="/topic/visual-design/">Visual Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>