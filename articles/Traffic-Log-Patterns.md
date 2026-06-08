# Traffic Log Patterns - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">4</span>

<div class="article-header">

<h1 class="article-h1">Traffic Log Patterns</h1>

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

July 9, 2006

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2006-07-09</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Traffic Log Patterns&amp;body=https://www.nngroup.com/articles/traffic-log-patterns/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/traffic-log-patterns/&amp;title=Traffic Log Patterns&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/traffic-log-patterns/&amp;text=Traffic Log Patterns&amp;via=nngroup" data-share-type="Twitter">

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

</span>The relative popularity of a site&#x27;s pages, the number of visitors referred by other sites, and the traffic from search queries continue to follow a Zipf distribution.

</div>

<div class="article-body">

<p>About 10 years ago, I showed that the <a class="old" href="http://www.useit.com/alertbox/zipf.html" title="Alertbox sidebar: Zipf Curves and Website Popularity"> popularity of a website's pages followed a power law </a> . Briefly stated, a few pages on a website were extremely popular, a larger set was moderately popular, and <strong> the vast majority </strong> constituted the " <a class="out" href="http://www.amazon.com/exec/obidos/ISBN=1401302378/ref=nosim/useitcomusablein/" title="'The Long Tail : Why the Future of Business Is Selling Less of More' (Book page at Amazon.com)"> long tail </a> " of low-traffic pages.</p>

<p>Mathematically, the Zipf curve is a straight line on a double-logarithmic diagram, when we plot pages with their popularity rank on the <em> x </em> -axis and their number of hits on the <em> y </em> -axis.</p>

<p>The old analyses showed that this same distribution also described both the number of incoming references to a website from other sites and the outgoing traffic from a company's employees.</p>

<p>Do these findings continue to hold today? The <strong> Web is now 2,200 times bigger </strong> , so traffic patterns might have changed. I decided to find out.</p>

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

<a class="ga-article-toc-item" href="#toc-page-popularity-1">Page Popularity</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-incoming-traffic-from-other-sites-2">Incoming Traffic from Other Sites</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-search-engine-queries-3">Search Engine Queries</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-in-10-years-almost-no-change-4">In 10 Years, Almost No Change</a>

</li>

</ul>

</div>

</div><h2 id="toc-page-popularity-1">Page Popularity</h2>

<p>The following chart shows useit.com traffic during a recent eight-week period. Each dot represents one page, and the pages are sorted by popularity. The most popular page (the homepage) got 261,024 pageviews.</p>

<p> </p>

<p>For the most popular 350 pages, the empirical data follows the theory remarkably well. Thereafter, however, the data trails off and the next 700 pages have less traffic than predicted. Also, in theory, there should have been about a quarter-million additional pages with low traffic, but I simply haven't gotten around to writing that much.</p>

<p style="text-align:center"><img alt="Zipf distribution of the popularity of Web pages sorted by traffic rank" height="410" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/traffic_page_popularity_zipf.png" width='584"'/></p>

<p>The small insert in the upper right shows the equivalent diagram from my analysis 10 years ago. It's uncanny how closely it resembles the new data. In particular, the old curve also trailed off toward the end and was missing a vast number of low-traffic pages.</p>

<p><a class="new" href="/articles/visualizing-traffic-analysis" title="Alertbox: Data Visualization of Web Stats: Logarithmic Charts and the Drooping Tail">The end of the "long tail" is absent </a> from both diagrams because the sites haven't accumulated enough old content to have the expected number of low-traffic pages. Instead, they have a <strong> drooping tail </strong> . It might take hundreds of years for a site written by a single person (or even a single marketing department) to accumulate a quarter-million pages.</p>

<h2 id="toc-incoming-traffic-from-other-sites-2">Incoming Traffic from Other Sites</h2>

<p>The next diagram shows the number of visitors referred to useit.com through links from other websites during the eight-week period. Each dot represents one external site.</p>

<p> </p>

<p style="text-align:center"><img alt="Zipf distribution of incoming referrals from other sites, sorted by traffic rank" height="398" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/traffic_referrals_from_other_sites.png" width='582"'/></p>

<p>In this case, the empirical data hugs the theory's red line all the way down to the x-axis. The difference here is that there's no lack of other sites that might link to useit.com, and a huge number of these sites are low-traffic blogs that only occasionally refer individual users.</p>

<p>The chart's one obvious exception to the theory is that the site that referred the most visitors accounted for many more visits than predicted. Google (depicted as an extra-large dot) referred 257,040 visitors; in theory, it should have referred only 52,479.</p>

<p>Google is five times as popular as the theory predicts, but this phenomenon could fade as other search engines catch up. Only time will tell.</p>

<p>Also, while Google is disproportionally important, when taken together, the other 35,631 referring sites accounted for 35% more traffic. Clearly, it's not a good idea to focus only on #1.</p>

<h2 id="toc-search-engine-queries-3">Search Engine Queries</h2>

<p>To find useit.com, users employed a total of 110,399 different queries across various search engines. <strong> Of these queries, 83% were used only once </strong> during the eight-week period.</p>

<p> </p>

<p>The top 10 queries accounted for 10% of the total traffic, so each one of these queries is obviously more important than those that brought only one visitor. Taken together, however, the <strong> single-use queries accounted for three times as much traffic </strong> as the top 10 queries. This statistic shows the folly of focusing search engine optimization solely on a few high-performing queries. Your site must be found when users enter relevant queries -- and the possibilities are typically vast.</p>

<p>The following diagram shows the distribution of search engine queries, sorted by the number of incoming users who arrived after searching for that string.</p>

<p style="text-align:center"><img alt="Zipf distribution of the search queries sorted by traffic rank" height="425" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/traffic_incoming_queries.png" width='591"'/></p>

<p>This chart shows roughly the expected distribution, but with a hump for queries #5300. In other words, <strong> queries in the middle range are more important than the theory predicts </strong> . Sample queries in this range include <a class="old" href="http://www.useit.com/papers/responsetime.html" title="Jakob Nielsen: Response Times - The Three Important Limits"> response time </a> , <a class="old" href="/articles/open-new-windows-for-pdfs" title="Alertbox: Open New Windows for PDF and other Non-Web Documents"> open link in new window </a> , <a class="old" href="http://www.useit.com/alertbox/20050131.html" title="Alertbox: Usability of Websites for Teenagers"> teenagers </a> , <a class="old" href="http://www.useit.com/alertbox/20020106.html" title="Alertbox sidebar: Sitemap Usability"> site maps </a> , <a class="old" href="http://www.useit.com/eyetracking/" title="Jakob Nielsen: overview of eyetracking research into Web usability"> eye tracking </a> , and <a class="old" href="/articles/change-the-color-of-visited-links" title="Alertbox: Change the Color of Visited Links"> link color </a> . Useit.com is not particularly focused on any of these topics, which is why they're not at the top of the list. For each query, however, I have at least one good related article.</p>

<p>In general, my site covers a broad range of topics in some depth, which is probably why it has this hump of mid-range queries with extra traffic.</p>

<p>As we proceed down the list of query popularity, the queries become longer and longer. The following diagram shows the number of query words for each of the first nineteen groups of a thousand queries. (That is, queries #1-1,000 are first, followed by queries #1,001-2,000, and so on through queries #18,001-19,000.)</p>

<p style="text-align:center"><img alt="Length of search queries by traffic cohort" height="380" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/traffic_incoming_queries_length.png" width='566"'/></p>

<p>Single-word queries were fairly common among the first thousand queries (i.e., those that generated the most traffic), but drop off quite quickly. Conversely, four- and five-word queries are rare among the most popular queries, but are a big proportion of queries starting at about #7,000.</p>

<p>This shows the importance of considering longer queries in your search engine marketing: Multiple-word queries are the best way to capture the vast range of user interests.</p>

<p>In this case, long queries in the #7,000 traffic range included <a class="old" href="/articles/checkboxes-vs-radio-buttons" title="Alertbox: Checkboxes vs. Radio Buttons"> radio buttons and check boxes </a> (five words) and <a class="old" href="/articles/scrolling-and-scrollbars" title="Alertbox: Scrolling and Scrollbars"> horizontal scrollbar in html </a> (four words).</p>

<h2 id="toc-in-10-years-almost-no-change-4">In 10 Years, Almost No Change</h2>

<p>In comparing the new data with data from 10 years ago, the biggest finding is that the <strong> curves look almost the same </strong> . Several measures of Web traffic followed a Zipf curve in 1996, and they still do.</p>

<p> </p>

<p>The two exceptions are both search related:</p>

<ul>

<li>A single search engine is disproportionally popular. Is this a temporary fluke or a fundamental change in the Internet's fabric? Check back in 10 years!</li>

<li>Users today enter more long queries. (I discuss this trend in more detail in my course on <a class="old" href="http://www.nngroup.com/events/tutorials/usability.html" title="Nielsen Norman Group training tutorial"> Fundamental Guidelines for Web Usability </a> .)</li>

</ul>

<p>Mainly, though, the big patterns of Web use remain remarkably robust. This is explained by the same phenomenon that dictates the <a class="old" href="/articles/durability-of-usability-guidelines" title="Alertbox: Durability of Usability Guidelines"> long-term durability of usability guidelines </a> . In both cases, conclusions are <strong> independent of changes in technology or fashion </strong> . Rather, they are due to the fundamental nature of human behavior.</p>

<p> </p>

<p>Knowing that a single distribution describes these many forms of Web use can <strong> help you analyze your own log files </strong> : plot your statistics on a log-log scale and see if they fall on a straight line. If yes, your site follows the theory. If no, see where you deviate: In the head, the middle, or the tail? Above or below the prediction line? Any deviations help you understand ways in which your traffic is different than the norm. These insights may also help you spot opportunities for growth.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Discovery: Building the Right Thing" href="/courses/discovery/?lm=traffic-log-patterns&amp;pt=article">

<h4 class="title heading-small">Discovery: Building the Right Thing</h4>

<p id="discovery-building-the-right-thing" class="description body-small">

Conduct successful discovery phases to ensure you build the best solution

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-research" />

</svg>

<p class="ux-specialty ux-research">Research</p>

</div>

</div>

</a>

</li>

<li>

<a class="tile ga-article-related-course" data-course-title="ResearchOps: Scaling User Research" href="/courses/researchops/?lm=traffic-log-patterns&amp;pt=article">

<h4 class="title heading-small">ResearchOps: Scaling User Research</h4>

<p id="researchops-scaling-user-research" class="description body-small">

Orchestrate and optimize research to amplify its impact

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-research" />

</svg>

<p class="ux-specialty ux-research">Research</p>

</div>

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-management" />

</svg>

<p class="ux-specialty ux-management">Management</p>

</div>

</div>

</a>

</li>

<li>

<a class="tile ga-article-related-course" data-course-title="Survey Design and Execution" href="/courses/surveys/?lm=traffic-log-patterns&amp;pt=article">

<h4 class="title heading-small">Survey Design and Execution</h4>

<p id="survey-design-and-execution" class="description body-small">

Use surveys to drive and evaluate UX design

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-research" />

</svg>

<p class="ux-specialty ux-research">Research</p>

</div>

</div>

</a>

</li>

</ul>

</div>

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Research Methods</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Research Methods</span>

<a class="ga-article-related-topic" href="/topic/research-methods/">Research Methods</a>

</li>

</ul>

</div>

</div>

</div>

</div>