# No More Pogo Sticking: Protect Users from Wasted Clicks - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">5</span>

<div class="article-header">

<h1 class="article-h1">No More Pogo Sticking: Protect Users from Wasted Clicks</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Aurora Harley</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/Aurora-Harley-20190601SF.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/aurora-harley/">

Aurora Harley</a></span>

<p class="publication-date">

April 12, 2015

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2015-04-12</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: No More Pogo Sticking: Protect Users from Wasted Clicks&amp;body=https://www.nngroup.com/articles/pogo-sticking/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/pogo-sticking/&amp;title=No More Pogo Sticking: Protect Users from Wasted Clicks&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/pogo-sticking/&amp;text=No More Pogo Sticking: Protect Users from Wasted Clicks&amp;via=nngroup" data-share-type="Twitter">

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

</span>Misleading links and omitted information force users to bounce back and forth in a hub-and-spoke pattern between a routing page and subpages linked from it, increasing the interaction cost and decreasing engagement over time. Use web analytics tools to identify and monitor pogo-stick behavior on your site.

</div>

<div class="article-body">

<p>When people have problems finding content, both time and clicks are wasted hunting through extraneous pages on a site. The <strong>hub-and-spoke</strong> pattern of navigating from a routing page—a search-engine results page (SERP), section landing page, <a href="/reports/ecommerce-ux-homepages-and-category-pages/">product-category page</a>, or similar—to a page deeper in the site’s hierarchy, then immediately back to the routing page is referred to as <strong>pogo sticking</strong>.</p>

<p>Recently, I found myself pogo sticking through the Redbox website. Why, you ask, was I doing this? I had wanted to walk to my nearest Redbox location, to get a little exercise and avoid an extra trip in the car, and grab a movie to watch that evening. On the website, I searched for my specific Redbox kiosk location and was shown a list of movies to browse. Upon seeing a movie that interested me, I clicked to get more information only to find that it was not available to reserve at my chosen location. Disappointing. I returned to the list of movies to try another option and again it was not available. It became clear that this browse page contained numerous movies that were not available at my chosen location. This did not match what I had specifically asked for! The excess work and frustration nearly dissuaded me from renting a movie altogether—had it not been for others in my company wanting to watch a new movie, I would have just streamed something on Netflix.</p>

<p>When a company’s website makes customers think lovingly of the biggest competitor, something is wrong.</p>

<figure class="caption"><img alt="Pogo sticking between Redbox movie pages" border="0" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/02/27/redbox_pogo.png"/>

<figcaption><em>Pogo-stick behavior on the Redbox website: After specifying a kiosk location, the list of movies still included options not available to rent at the chosen kiosk. This did not match the expectation set by selecting a location, and forced me to pogo stick through each movie in the list until an available movie was found. Note: the browse page does display a tooltip showing availability when a user hovers over a movie, but the </em><a href="/articles/timing-exposing-content/"><em>delay is too long</em></a><em> and the hidden help can be easily missed.</em></figcaption>

</figure>

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

<a class="ga-article-toc-item" href="#toc-the-problem-with-pogo-sticking-1">The Problem with Pogo Sticking</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-identifying-pogo-stick-behavior-using-web-analytics-2">Identifying Pogo-Stick Behavior Using Web Analytics</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-investigate-using-qualitative-methods-3">Investigate Using Qualitative Methods</a>

</li>

</ul>

</div>

</div><h2 id="toc-the-problem-with-pogo-sticking-1">The Problem with Pogo Sticking</h2>

<p>Pogo-stick behavior is often discussed in regards to people bouncing off a site and returning to an external search engine. While this pattern may be generated by a poorly designed landing page, high <a href="/articles/reduce-bounce-rates/">bounce rates</a> could also be due to visitors who are not truly interested in the product or service offered, and thus are not valid prospective customers.</p>

<p>Within a website, <strong>pogo-stick behavior is an indication that people are struggling to find relevant content</strong>. Navigating repeatedly through the same pages quickly becomes tiresome, and is highly discouraging. Users in this situation may give up entirely, or settle with the most <a href="/articles/satisficing/">satisficing</a> answer encountered during the arduous journey through the site. Because of the excessive effort exerted, these users are not likely to extend their visit for a second purpose, nor do they ever return. This demonstrates the <a href="/articles/interaction-elasticity/">interaction elasticity</a> of websites, where a higher <a href="/articles/interaction-cost-definition/">interaction cost</a> results in lower usage over time.</p>

<p>Users pogo stick from a page because the content found upon arrival was disappointing—somehow the <strong>destination did not match the expectation</strong> set by the page leading to it. This <a href="/articles/link-promise/">mismatch between a link and its corresponding page</a> chips away at the credibility of the website, and at the brand as a whole. People resent sites that trick them into spending a click while getting nothing in return. In user’s eyes, these are not only <a href="/articles/clickable-elements">wasted clicks</a>, but also wasted time.</p>

<h2 id="toc-identifying-pogo-stick-behavior-using-web-analytics-2">Identifying Pogo-Stick Behavior Using Web Analytics</h2>

<p>Most often, pogo sticking is discovered by directly observing users during usability tests. However, web-analytics tools can also help identify this behavior and monitor improvements once changes have been implemented. The process of examining the sequence of pages that a user has visited during a single session on a website is known as path analysis.</p>

<p>The tool needed to find this data may be named differently in various web-analytics platforms, but it should be available in each of them. Analyzing specific navigational paths within a website can be a time-consuming task, so it is best to first identify those pages that are candidates for pogo sticking. Suspects may include your homepage, landing pages for main sections of content, your site’s internal search-results page, and product-browse pages. Prioritize which pages you tackle first, based on their visibility to your audience (overall unique traffic) and their potential for improvement. (Some personal judgment will be required for the latter, but you’re likely to gain the most from fixing those pages within your conversion funnel that have a high exit rate.)</p>

<p>The most simplistic way to identify a page where pogo-stick behavior may be occurring is to look at routing pages with a high ratio of page views to unique page views. This measure indicates that many users <em>repeatedly</em> navigate to those pages. However, this number alone does not necessarily mean that users pogo stick or otherwise fail to find information.</p>

<p>The exact same click behavior can be indicative of a positive user experience instead of pogo sticking if users repeatedly follow links from a routing page because they find all the destinations interesting. Consider, for example, a newspaper homepage with many news stories. If a user clicks, say, five of the headlines <em>and reads all those articles</em>, then this is good, not bad. On the other hand, if a user clicked those exact same five headlines and was disappointed with every single article (because of misleading teasers), then it would be bad. Simply counting clicks won’t differentiate between these two scenarios.</p>

<p>To get a better picture of how users interact with a routing page and with the pages it links to, the data must be narrowed to the session level and exclude paths where the user visited several pages before returning to the routing page or when the user spent substantial time engaging with the destination pages. In other words, you want to include only patterns of the type X-Y-X, where X is a routing page and Y is a page linked from X.  By creating a segment identifying that path sequence, you can measure the percentage of users exhibiting this pattern of navigation, and monitor it over time.</p>

<figure class="caption"><img alt="Segment by sequence screen in Google Analytics" border="0" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/02/27/sequencesegment-googleanalytics_resized.png"/>

<figcaption><em>Example of setting up a path-sequence segment using Google Analytics. Note the use of </em>is immediately followed by… <em>rather than the </em>is followed by…<em> option, in order to properly separate visits navigating directly between the specified pages without any detours.</em></figcaption>

</figure>

<h2 id="toc-investigate-using-qualitative-methods-3">Investigate Using Qualitative Methods</h2>

<p>Once pogo sticking has been identified, follow up with qualitative research—usability testing—to determine what may be spurring this behavior. Are people looking for a page or some content that they expected to find but doesn’t actually exist (or at least, isn’t available through that page)? Did a link on the page promise cute pictures of kittens but instead presented users with a wordy article scrutinizing society’s infatuation with prepubescent animals? Or, did that browse page not clearly display key differentiating information for people to easily find the product that fulfills their need—like what happened to me on the Redbox website? Quantitative data from analytics cannot explain <em>why</em> a behavior occurs, nor how to improve the experience, but only if and where that behavior may be happening.</p>

<p>Here are some of the common problems that can cause pogo-sticking behavior, along with suggested solutions and research activities that can be used to uncover the best way to implement those solutions.</p>

<table align="center" style="border:1px solid #d5d5d5; border-collapse:collapse;">

<thead>

<tr>

<th style="background-color:#003366; color:#ffffff; width:30%;"><strong>Problem</strong></th>

<th style="background-color:#003366; color:#ffffff; width:25%;"><strong>Solution</strong></th>

<th style="background-color:#003366; color:#ffffff; width:45%;"><strong>Research</strong></th>

</tr>

</thead>

<tbody>

<tr>

<td>

<p>Users want something that is not currently on your site.</p>

</td>

<td>

<p>Create that content.</p>

</td>

<td>

<p>User research—<a href="/articles/field-studies-done-right-fast-and-observational/">field studies</a>, task analysis, and search-log analysis (people tend to search for something if they want it but can’t find it)—can identify users’ top information needs.</p>

</td>

</tr>

<tr>

<td>

<p>Misleading links cause people to be disappointed after clicking.</p>

</td>

<td>

<p>Write plain-spoken links, using <a href="/articles/user-centric-language/">user-oriented language</a>, instead of ‘teasing’ links or links using your own internal terminology.</p>

</td>

<td>

<p>Search-log analysis can reveal the users’ preferred terminology, as can listening to users <a href="/articles/thinking-aloud-the-1-usability-tool/">thinking aloud</a> during usability studies.</p>

</td>

</tr>

<tr>

<td>

<p>Users can’t determine which of the items listed will meet their needs.</p>

</td>

<td>

<p>Improve the <a href="/articles/information-scent/">information scent</a> of each item’s description on the routing page.</p>

</td>

<td>

<p>Discover the strongest differentiating parameters by watching users solve problems in usability studies.</p>

</td>

</tr>

</tbody>

</table>

<p>After fixing a pogo-sticking problem, you will probably observe an immediate <strong>decline in your page views</strong>. But this is good! Users aren’t wasting as much time and effort navigating to pages they don’t need, and so the overall page count drops. This is an example where a more nuanced approach to interpreting website analytics data is required than simply wanting ever bigger numbers. Additionally, if you track analytics data for <em>returning</em> visitors you will likely find an increase in <a href="/articles/loyalty-on-the-web/">user loyalty</a>, driven by improved usability now that people can easily find what they’re looking for. Higher loyalty will again drive increased page views over the long term. But short-term numbers will be down, and that’s positive because it means that you <a href="/articles/does-user-annoyance-matter/">stopped annoying users</a> with wasted clicks.</p>

<p>Learn more tips on using analytics data to identify usability issues during our full-day course on <a href="/courses/analytics-and-user-experience/">Analytics and User Experience</a>.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Analytics and User Experience" href="/courses/analytics-and-user-experience/?lm=pogo-sticking&amp;pt=article">

<h4 class="title heading-small">Analytics and User Experience</h4>

<p id="analytics-and-user-experience" class="description body-small">

Study your users’ real-life behaviors and make data-informed design decisions

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

<a class="tile ga-article-related-course" data-course-title="ResearchOps: Scaling User Research" href="/courses/researchops/?lm=pogo-sticking&amp;pt=article">

<h4 class="title heading-small">ResearchOps: Scaling User Research</h4>

<p id="researchops-scaling-user-research" class="description body-small">

Orchestrate and optimize research to amplify its impact

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-management" />

</svg>

<p class="ux-specialty ux-management">Management</p>

</div>

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

<a class="tile ga-article-related-course" data-course-title="Survey Design and Execution" href="/courses/surveys/?lm=pogo-sticking&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Analytics &amp; Metrics,Research Methods,Web Usability</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Analytics &amp; Metrics</span>

<a class="ga-article-related-topic" href="/topic/analytics-and-metrics/">Analytics &amp; Metrics</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/research-methods/">Research Methods</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/web-usability/">Web Usability</a>

</li>

</ul>

</div>

</div>

</div>

</div>