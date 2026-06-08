# Usability Insights From Sun Microsystem&#x27;s 1997 Web Design - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">5</span>

<div class="article-header">

<h1 class="article-h1">Sun Microsystem&#x27;s 1997 Web Design</h1>

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

January 13, 1998

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">1998-01-13</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Sun Microsystem&#x27;s 1997 Web Design&amp;body=https://www.nngroup.com/articles/sun-microsystems-1997-web-design/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/sun-microsystems-1997-web-design/&amp;title=Sun Microsystem&#x27;s 1997 Web Design&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/sun-microsystems-1997-web-design/&amp;text=Sun Microsystem&#x27;s 1997 Web Design&amp;via=nngroup" data-share-type="Twitter">

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

</span>The 1997 redesign of the Sun Microsystems&#x27; Web site aimed to improve the visual appearance, ease of navigation, and performance of the Web site.

</div>

<div class="article-body">

<p>

We had several goals for the 1997 redesign of Sun's Web site:</p>

<ul>

<li>

Increase <strong> download speed</strong>.</li>

<li>

Facilitate <strong> navigation </strong> of our increasingly large site.</li>

<li>

Provide a <strong> unified visual appearance </strong> of our highly heterogeneous content.</li>

<li>

Make <strong> search </strong> available from every page; in particular, make search prominent on the home page. No matter how well one supports navigation, many users still want to search and you never know where they are when they decide to search.</li>

<li>

Ensure high <strong> usability </strong> and a quality user experience: we conducted user tests of several <a href="/articles/usability-testing-advanced-homepage-concepts-sun-microsystems-1997-web-design/"> advanced Web design concepts</a> but found that users preferred a simpler approach with established interaction principles.</li>

<li>

<strong>Replace our <a href="/articles/evolution-home-page-design-1995-sun-microsystems-website/"> 1995 design</a>  </strong> which had become outdated (it is a testament to its quality that a design launched in May 1995 lasted more than two years: normally it is recommended to redesign a site every year).</li>

</ul>

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

<a class="ga-article-toc-item" href="#toc-speed-1">

Speed</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-navigation-templates-2">

Navigation Templates</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-plan-for-growth-3">

Plan for Growth</a>

</li>

</ul>

</div>

</div><h2 id="toc-speed-1">

Speed</h2>

<p>

Fast downloads are the single most important usability consideration in Web design. We recently surveyed 1854 users and found that the regression weight between "download speed" and overall satisfaction was 0.264 in a multiple regression to predict users' overall satisfaction ratings from six different attributes of Web quality. In comparison, "looks great" only got a regression weight of 0.08. Simplistically stated, our users thought that <strong> speed was more than three times as important than looks</strong>.</p>

<p>

Of course, we still wanted the design to look good. Not only is .08 a positive weight (meaning that good graphic design adds quality in its own right), but we also found that a great visual appearance made users think more highly of the site. Our polished visual design made our test users say things like <em> you can tell that they have put a lot of thought into this site. </em></p>

<p>

The balance between looks and speed was resolved by a design that utilizes plain-and-fast HTML (prettied up with style sheets) to define the basic features of the page. Visual enhancements like the Sun logo and other graphic elements will fill in more slowly the first time a user visits but will appear immediately if they are cached on the user's local system. We wanted to optimize the download speed for repeat users since our user surveys have shown that the overwhelming majority of page views are due to repeat users. In fact, a very large proportion of users visit daily or several times a week.</p>

<p>

<img alt="Sun's new home page after 1 second ad ISDN speed" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/homepage_early_download.gif" style="width: 374px; height: 436px; "/></p>

<p>

The figure shows Sun's new home page as it appears for a repeat user early in the download process (after about one second). The home page is fully rendered (with the exception of the current feature stories) after a download of only 8 kilobytes if the user has the logo and other permanent graphics cached. Human factors research has shown that Web pages need to <strong> download in no more than one second for optimal usability </strong> of hypertext navigation: we have succeeded in getting below this limit for users connecting at ISDN speed or better. Even modem users will get a working home page after about 3-4 seconds; while not optimal, this is still faster than the 10 seconds that are the limit where users divert their attention from a site. Fast downloads were indeed one of the main arguments given for including Sun in <cite> FORTUNE </cite> Magazine's list of top corporate Web sites in their Winter 1998 Technology Buyer's Guide.</p>

<h2 id="toc-navigation-templates-2">

Navigation Templates</h2>

<p>

Sun's Web site is extremely large and has a very wide variety of content, including hardware and software product information ranging from complex electronics to mass-market Web authoring tools as well as financial information, job listings, news stories, events promotions, research projects, and much more. Each type of content has its own requirements, but our test users had been telling us that the resulting differences in appearance made the site look disorganized and more difficult to navigate under the old design.</p>

<p>

To <strong> unify the appearance of our highly heterogeneous content</strong>, we decided to use a visually striking page template that could surround a wide range of page content with a uniform set of navigation options. Universal options appear across the top of the page where they will be prominent when the page loads; special options for the current part of the site appear down the side in a colored stripe that remains visible no matter how far down the user scrolls. The "flipped-L" navigation area is dominated by the company's logo color since our studies have shown that many users strongly identify this color with Sun.</p>

<p>

<img alt="Conceptual diagram of a navigationhierarchy" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/navigationplan.gif" style="width: 400px; height: 359px; "/></p>

<p>

Most Web sites follow a <strong> hierarchical information architecture</strong>, and such sites need to provide two kinds of navigational information to users:</p>

<dl>

<dt>

Navigational <strong> Breadth</strong>:</dt>

<dd>

Show users which <strong> other options </strong> are available at a given level of the hierarchy. Sun's new templates provide breadth at two levels: global and local. The very top level of the site structure is visualized across the top of the horizontal navigation bar, giving users a global indication of the total scope of content that's available to them. Local alternatives are listed down the side of the vertical navigation stripe. The user's current location is highlighted to provide a sense of place.</dd>

<dt>

Navigational <strong> Depth</strong>:</dt>

<dd>

Shows users where their <strong> current location fits within the structure </strong> of the site. Ideally, depth is visualized as a complete path from the home page down through all levels of the information architecture, revealing all the higher-level structures inside of which the current page is nested. On a large site, a full list of all the levels can become overwhelming, so, as a compromise, the new Sun templates provide an abbreviated view of navigational depth, with three levels shown at the top of the page. If the current page is more than three levels deep, then intermediate levels are elided to simplify the display.</dd>

</dl>

<h3>

Does Your Site Need a Similar Template?</h3>

<p>

Only if you are running a large and heterogeneous site. Sun's website has a large amount of highly diverse content which is why we need elaborate navigation support and a strongly stated unifying visual look of the navigation template.</p>

<p>

<img alt="Navigation area fromwww.tbid.com" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/tbid.gif" style="width: 466px; height: 121px; "/></p>

<p>

Smaller sites can get away with a much simpler approach. The figure shows the navigation area from <a href="http://www.tbid.com/"> Toby Braun Information Design</a>. It is obvious that the user is in the "visioning" part of the site, which again is a part of the "information" area. This design provides two levels of navigational depth as well as navigational breadth on both the global level (the four main areas of the site) and the local level (neighboring pages). Also note how the use of standard link colors make it very clear to users what parts of the site they have already seen.</p>

<p>

Homogeneous sites can use simpler navigation that emphasizes one or two organizing principles for very large collections of pages. For example, news sites can use a time line to hide most older stories unless the user explicitly requests them. Also, by encoding richer attributes in XML, user-defined views can focus on pages of interest to individual users. For example, if all articles are encoded with an AUTHOR tag, it should be possible to automatically generate a list of all columns by, say, Jesse Berst, no matter what magazine they originally appeared in.</p>

<h2 id="toc-plan-for-growth-3">

Plan for Growth</h2>

<p>

Sun's web site went live in January 1994 when there were only 700 other sites on the Web. Our first site ran on a "liberated" workstation and was pretty small. Now, only four years later, the Web has about 2,500 times as many sites, Sun's own site has grown to 22,000 pages, and we are on our third major user interface redesign. There is every reason to believe that the Web and our site will both continue to grow as we build the WebTone vision of a network economy. Truly, on the Web, the only constant is change, and it is important to design a scalable information architecture that can accommodate such change. A site that works perfectly as long as it stays the same will quickly die.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="The Human Mind and Usability" href="/courses/human-mind/?lm=sun-microsystems-1997-web-design&amp;pt=article">

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

<a class="tile ga-article-related-course" data-course-title="Web Page UX Design" href="/courses/web-page-design/?lm=sun-microsystems-1997-web-design&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Navigation,Web Usability</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Navigation</span>

<a class="ga-article-related-topic" href="/topic/navigation/">Navigation</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/web-usability/">Web Usability</a>

</li>

</ul>

</div>

</div>

</div>

</div>