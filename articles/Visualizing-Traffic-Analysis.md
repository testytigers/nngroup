# Data Visualization of Web Stats (Jakob Nielsen) - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">3</span>

<div class="article-header">

<h1 class="article-h1">Data Visualization of Web Stats: Logarithmic Charts and the Drooping Tail</h1>

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

August 13, 2006

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2006-08-13</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Data Visualization of Web Stats: Logarithmic Charts and the Drooping Tail&amp;body=https://www.nngroup.com/articles/visualizing-traffic-analysis/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/visualizing-traffic-analysis/&amp;title=Data Visualization of Web Stats: Logarithmic Charts and the Drooping Tail&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/visualizing-traffic-analysis/&amp;text=Data Visualization of Web Stats: Logarithmic Charts and the Drooping Tail&amp;via=nngroup" data-share-type="Twitter">

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

</span>Using a linear diagram to plot data from website traffic logs can lead you to overlook important conclusions. Sometimes advanced visualizations are worth the effort.

</div>

<div class="article-body">

<p>Whenever I show double-logarithmic charts in my <a class="new" href="http://www.nngroup.com/events/tutorials/usability.html" title="Nielsen Norman Group training tutorial"> usability seminars</a>, I see the audience members' eyes glaze over. People don't like anything but the simplest data visualizations, and I've certainly learned my lessons from the feedback sheets and scaled back on the amount of statistics I present.</p>

<p>Still, I can't help myself: there's data underlying the usability guidelines, and I <em> have </em> to show some of it. To understand traffic patterns found by Web analytics, for example, some of those hated advanced-visualization plots are sadly necessary. Without them, you simply can't tell what's going on.</p>

<p>As an example, consider the following <strong> linear graph </strong> of my log file analysis of <a class="old" href="/articles/traffic-log-patterns" title="Alertbox: Traffic Log Patterns"> how many visitors each page gets</a> on a given website:</p>

<p style="text-align:center"><img alt="Traffic diagram with linear axes" height="395" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/zipf_visualization_linear.gif" width="600"/></p>

<p>This linear graph shows what looks like the classic "long tail" distribution (which is really <a class="old" href="http://www.useit.com/alertbox/zipf.html" title="Alertbox: Traffic Log Patterns"> Zipf's Law</a>). And indeed, it <em> almost </em> is. The difference between theory and practice becomes clear, however, when we plot the same data on <strong> logarithmic scales</strong>:</p>

<p style="text-align:center"><img alt="Traffic diagram with linear axes" height="423" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/zipf_visualization_logarithmic.gif" width="620"/></p>

<p>It's now clear that we have a <strong> drooping tail</strong>: the site simply doesn't have enough content to supply the predicted demand at the low end.</p>

<p>Without this fancy log-log plot, we would have never seen the site's potential for increasing traffic by adding large amounts of low-volume content. I'm amazed at how often articles analyzing Web traffic or "long tail"-type businesses use linear plots that fail to show what's really going on.</p>

<p>To compare high-volume and low-volume events in the same diagram, it's typically best to use a logarithmic plot. (If you're using Excel to plot your charts, you can get logarithmic scales by simply double-clicking each axis, choosing the <em> Scale </em> tab in the resulting <em> Format Axis </em> dialog box, and checking the box for <em> Logarithmic scale</em>.)</p>

<p>In addition to the drooping tail, my <a class="old" href="/articles/traffic-log-patterns" title="Alertbox: Traffic Log Patterns"> original analysis also found a <strong> hump </strong> on the traffic plot for search queries</a> -- a different phenomenon that also only shows up on a log-log chart.</p>

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

<a class="ga-article-toc-item" href="#toc-wag-the-drooping-tail-1">Wag the Drooping Tail</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-analysis-outcome-2">Analysis Outcome?</a>

</li>

</ul>

</div>

</div><h2 id="toc-wag-the-drooping-tail-1">Wag the Drooping Tail</h2>

<p>So, what would happen if our sample site could wag its traffic tail up to the straight line representing the traffic potential the theory predicts?</p>

<p>In my analysis, current traffic with 1,000 pages was <strong> 2.6 M pageviews </strong> over an 8-week period. With 260,000 pages, the site could expect traffic to increase to 4.8 M pageviews over the same period. That is, the 259,000 new low-traffic pages would get 2.2 M pageviews, for an average of 9 views per page.</p>

<p>Now, if we extend the 8-week period to a full year, the total traffic would almost <strong> double -- from 16.9 M to 32.2 M pageviews </strong> -- giving each new page an average of <strong> 58 views</strong>.</p>

<p>What's the value of 58 pageviews?</p>

<p>Over the last several years, Yahoo! has made between 0.2 and 0.4 cents per non-search pageview. However, I believe that Internet advertising is over-hyped and that advertisers are deluding themselves into overpaying. In the long term, non-search advertising's value will drop to 0.1 cents or less per page.</p>

<p>So, at the expected long-term value of 0.1 cents per view, 58 pageviews have a value of about 6 cents. If we assume the new pages can attract traffic for five years, and then discount future cash flow by 10% per year, the present value of each new page is <strong> 24 cents</strong>.</p>

<p>Not much. But we're expecting to add 259,000 pages, so the total value would be <strong> $62,000</strong>.</p>

<p>It sounds like a nice sum -- but could the site create 259,000 new pages for $62K? Obviously not, assuming the employees creating the pages earned salaries higher than that of the average ant.</p>

<p>The only feasible approach is that chosen by many sites these days: to con users into contributing content for free. However, doing so requires that sites develop a system for user contributions, which (if done correctly) requires user testing and other quality assurance before being fielded. Given that the system's features aren't particularly advanced, our sample site could probably develop it for less than $62K. But it wouldn't be free.</p>

<p>(Update: Chris Anderson found a <a class="out" href="http://www.longtail.com/the_long_tail/2006/08/a_billion_dolla.html" title="Chris Anderson: 'a billion dollar question'"> drooping tail for the popularity of movies</a>. The drooping tail shape may be more common than previously expected. Maybe now people will go back and reanalyze their long tail statistics with the correct diagrams :-)</p>

<h2 id="toc-analysis-outcome-2">Analysis Outcome?</h2>

<p>It probably wouldn't pay for our sample site to take advantage of the opportunity that log analysis revealed. The long tail's end pays for aggregators who get their products from others, but companies who must develop their own are usually better served by staying away from the full tail.</p>

<p>That said, pursuing the tail's end might be valuable if a site meets one of two conditions: it has a better way than low-value ads to monetize traffic, or it has so many users that the total income would be substantially more than the cost of developing the new functionality.</p>

<p>In any case, you should certainly run through such exploratory ROI scenarios for your own site. To do so, you need correct data analysis and this typically requires more advanced visualizations than you see in most places. It's here that logarithmic plots deserve a chance -- despite their intimidating name.</p>

<p>(To avoid misunderstandings: you obviously shouldn't show log charts in websites targeted at a broad consumer audience. They're for internal use only -- or for websites like mine that target an intellectual audience.)</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Discovery: Building the Right Thing" href="/courses/discovery/?lm=visualizing-traffic-analysis&amp;pt=article">

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

<a class="tile ga-article-related-course" data-course-title="ResearchOps: Scaling User Research" href="/courses/researchops/?lm=visualizing-traffic-analysis&amp;pt=article">

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

<a class="tile ga-article-related-course" data-course-title="Survey Design and Execution" href="/courses/surveys/?lm=visualizing-traffic-analysis&amp;pt=article">

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