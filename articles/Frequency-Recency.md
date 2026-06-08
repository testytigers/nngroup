# Frequency &amp; Recency of Site Visits: 2 Metrics for User Engagement - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">7</span>

<div class="article-header">

<h1 class="article-h1">Frequency &amp; Recency of Site Visits: 2 Metrics for User Engagement</h1>

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

October 9, 2016

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2016-10-09</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Frequency &amp; Recency of Site Visits: 2 Metrics for User Engagement&amp;body=https://www.nngroup.com/articles/frequency-recency/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/frequency-recency/&amp;title=Frequency &amp; Recency of Site Visits: 2 Metrics for User Engagement&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/frequency-recency/&amp;text=Frequency &amp; Recency of Site Visits: 2 Metrics for User Engagement&amp;via=nngroup" data-share-type="Twitter">

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

</span>How often people visit your site and how long they wait between two visits can help to gauge visitor loyalty and to uncover the behavioral trends distinguishing frequent users from occasional ones.

</div>

<div class="article-body">

<p>For most websites and apps, visitors go through a long dating process, not a one-night stand: they rarely convert after the first visit. Most commonly, the first visit is used to <a href="/articles/trustworthy-design/">gauge credibility</a>. Subsequent visits may involve more complex interactions and, possibly, <a href="/articles/conversion-rates/">conversion events</a>, which may happen <a href="/articles/long-sales-cycles-online/">weeks or months after the initial visit</a>. Thus, to better support our users, we need to understand the actual dating process for our site visitors. Do people use our site every day or even multiple times per day? How many visits precede that final conversion? Does this behavior fluctuate based on the time of year?</p>

<p>Analytics tools help you answer these questions and can inform decisions regarding content strategy, schedules for marketing emails and promotions, or whether to design mostly for novice first-time visitors or for expert frequent visitors.</p>

<blockquote style="padding-top:0;margin-top:1.25rem;">

<p>Definition: <strong>Frequency</strong> of site visits indicates the overall number of visits made by each user on your site. This metric allows you to assess the percentage of new users on the site as well as the familiarity level of all returning users.</p>

<p>Definition: <strong>Recency </strong>measures the number of days that have passed since each user’s last visit. This measure allows you to see the average amount of time between visits for your user base.</p>

</blockquote>

<p>Combined, frequency and recency measure how “sticky” a website or app is — do people return regularly to it or not? Analyzing the behaviors of loyal customers can lead to valuable insights — for example, you may find pages or tools used frequently by returning users, but ignored by occasional visitors (particularly “<a href="/articles/why-site-tourists-are-worthless/">siteseers</a>” who only visit once). When you uncover such trends, you can then adjust the design of the site to increase the discoverability of those features that your repeat users find valuable.</p>

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

<a class="ga-article-toc-item" href="#toc-frequency-how-many-visits-1">Frequency: How Many Visits?</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-recency-when-did-people-last-visit-2">Recency: When Did People Last Visit?</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-3">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-frequency-how-many-visits-1">Frequency: How Many Visits?</h2>

<p>When using analytics tools such as Google Analytics or Adobe Analytics, frequency is described by a histogram of the number of visits. (A histogram is a type of bar chart in which each bar shows the number of data points that have a certain value or fall inside a range of values.) In Google Analytics, this histogram is called the <strong>count-of-session report</strong> and in Adobe Analytics it is the <strong>visit-number report</strong>.</p>

<p>Rather than merely measuring whether users are new or returning, such reports allow us to more precisely understand the familiarity level of users: how many of the visitors are highly familiar with the site (say, have had their 6<sup>th</sup> visit or more) versus how many are relatively fresh to the site?</p>

<p>Count-of-session (or visit-number) reports are usually defined for a specific period of time T (e.g., August) and they tell us, for each possible number of visits (i.e., count of sessions) n, how many users have had their nth visit within the time period T. So, for example, for count of sessions n=2 and the month of August, the histogram would tell you how many users had their second visit in August. (Note that some of these users may have had their first visit before August and some may have had it in August — they are all included in the count of sessions for n=2, as analytics tools report visit number as a lifetime value for each user.)</p>

<figure class="caption"><img alt="Screenshot of frequency report in Google Analytics" loading="lazy" src="https://media.nngroup.com/media/editor/2016/09/09/figure1-frequency-allvisitors.png" width="692"/>

<figcaption><em>Google Analytics count-of-sessions report for all site visitors during the month of August: The first row shows that 225,966 users had their first visit during this time window, the second row shows that 47,859 users had their second visit, and so on. Note that the bins in this histogram are not equally spaced: the ones towards the bottom include bigger and bigger ranges instead of a single number n.</em></figcaption>

</figure>

<p>A user may be included in several count-of-sessions bins: for example, users who had their first two visits in August would be included in both the count of sessions for n=1 and the one for n=2. If there were many more new visitors than returning, you’d expect the first bar (for n=1) to be a lot bigger than the others.</p>

<p>In order to get more detailed data about a particular category of users, we need to create a special <a href="/articles/analytics-persona-segment/">segment</a> (a subset of the data obtained by applying a chosen filter). For example, to see the frequency graph for those users who visited only one time in a given month, we would specify the rule “Sessions =1” as a filter to create a segment.</p>

<figure class="caption"><img alt="Screenshot of frequency report for a segment of users in Google Analytics" loading="lazy" src="https://media.nngroup.com/media/editor/2016/09/09/figure2-frequency-segment_1sessiononly.png" width="693"/>

<figcaption><em>This Google Analytics report shows the count of sessions for the segment of users who had exactly 1 session in a month period. There were 191,800 users who had their first and only visit during this period; there were 9,106 second-time visitors who had only one visit during this period, and so on. You can see that, although all these users visited the site exactly once within the given time frame, they go in different count-of-sessions bins depending on how many other sessions they have had in the past.</em></figcaption>

</figure>

<p>In isolation, looking at a frequency report does not reveal much because the rows generally just decrease in number as the count increments (not particularly surprising — as you increase the loyalty level, you can expect fewer and fewer users at that level). The real value emerges from looking at the segment of visits where important events (such as conversions for a certain goal) occurred and determining how many other visits preceded the event of interest.</p>

<figure class="caption"><img alt="Screenshot of frequency report for a segment of sessions in Google Analytics" loading="lazy" src="https://media.nngroup.com/media/editor/2016/09/09/figure3-frequency-registrationsession.png" width="692"/>

<figcaption><em>This Google Analytics frequency report shows only the segment of sessions where a conversion for a certain goal (e.g., sale of a product) was completed during a specified month. Thus, we see that 307 users were on their 1<sup>st</sup> visit to the site when they converted, 231 users on their second visit, and so on.</em></figcaption>

</figure>

<p>By uncovering the typical number of visits a user has had before converting, we can better design for our users’ actual journeys. For example, if the majority of conversions occur on a users’ 5<sup>th</sup> or 6<sup>th</sup> visit, we can implement tools to remind people what they were doing in the past to help them pick up where they left off, email users with only 3 or 4 visits to persuade them to revisit the site, and so on. We could also <a href="/articles/usability-test-checklist/">plan a usability study</a> or <a href="/articles/diary-studies/">diary study</a> to learn what the barriers to conversion may be: perhaps it takes so many visits to convert because users have difficulty comparing our offerings to those of competitors, or because they believe it will take too long to sign up and get started.</p>

<h2 id="toc-recency-when-did-people-last-visit-2">Recency: When Did People Last Visit?</h2>

<p>To measure recency, analytics tools report the number of days that have passed since each user’s previous visit.</p>

<p>In Google Analytics, for users who are new, the recency value (<em>Days Since Last Session</em>) is recorded as 0 days —the same as for users who have visited twice (or more) during the same day. Thus, when looking at Google Analytics recency reports, it is helpful to filter new users out by applying a segment including only multisession users. In Adobe Analytics, the return-frequency report already excludes first-time visitors. (Other tools may report this type of data using either method, so be sure to check how your analytics tool functions.)</p>

<figure class="caption"><img alt="Screenshot of recency report for 2 segments in Google Analytics" loading="lazy" src="https://media.nngroup.com/media/editor/2016/09/09/figure4-recency-allusersvsmultisession.png" width="692"/>

<figcaption><em>This Google Analytics report shows the number of days since their last visit for all users who visited the site during a specified month. The report displays data for 2 user segments: </em>All Users (blue bars)<em> and </em>Multi-session Users<em> (orange bar). The latter</em> <em>includes only those users who had more than 1 visit during the given time frame. New users (who had no previous visit) are placed in the 0 bin, together with people who have had two visits within the same day: This is why the </em>All Users <em>bar is so much larger than the </em>Multi-session Users <em>bar for a recency value of 0 — new users tend to be the majority.</em></figcaption>

</figure>

<p>Recency data helps uncover how regularly people tend to visit, compared to how frequently content or promotions are updated. If your content strategy were to change, would the rate between visits also change? Is it worthwhile to design a new banner image every day, if most users only visit once every few weeks? (Hint: no.) On the other hand, if you see a spike in the visitation rate each time your site pushes new content, it may make sense to increase the frequency of your updates.</p>

<p>For example, in the screenshot above, we can see that most multi-session users return to the site within the same day as the previous visit (the longest bar is the one in the row <em>Days Since Last Session </em>= 0) or just 1 day later. Notice also a small bump at the <em>Days Since Last Session =</em> 6. In this case, the bump corresponds to a weekly email newsletter.</p>

<p>Segments can help uncover desirable usage patterns — in particular, those of frequent visitors vs. those of occasional visitors. If people who return every day or every other day tend to convert more, whereas less frequent visitors end up never converting, then you should investigate what other behaviors are different between the two groups. Is there a feature or tool that more-engaged visitors use and that you could make more discoverable for everybody? Are frequent visits triggered by certain email promotions? Do frequent visitors have a different experience due to being kept logged in to the system? Different times of year can also be compared to uncover usage trends based on seasonality or specific marketing efforts.</p>

<p>Recency data also helps you make sense of the frequency data, to better understand when people return to the site. For example, if your count-of-sessions report shows a large number of users coming to the site 3–4 times, you can create a segment for that group and see if those visits occur within 0–1 days or over the course of a few weeks.</p>

<h2 id="toc-conclusion-3">Conclusion</h2>

<p>Frequency and recency data are helpful to better understand the <a href="/articles/customer-journeys-omnichannel/">customer journey</a> of your users, as well as their needs and behaviors. They can help create or <a href="/articles/revising-personas/">maintain your personas</a>, and also discover how to better support not only your visitors, but also your business goals. How many times do people visit before they finally convert or take some other desirable action? Do those visits occur within a short time frame or are there large gaps between sessions? Such knowledge can be used to turn visitors into valuable, engaged users.</p>

<p>Learn more about using analytics data for UX insights in our <a href="/courses/analytics-and-user-experience/">full-day training course on Analytics and User Experience</a>.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Analytics and User Experience" href="/courses/analytics-and-user-experience/?lm=frequency-recency&amp;pt=article">

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

<a class="tile ga-article-related-course" data-course-title="Measuring UX and ROI" href="/courses/measuring-ux/?lm=frequency-recency&amp;pt=article">

<h4 class="title heading-small">Measuring UX and ROI</h4>

<p id="measuring-ux-and-roi" class="description body-small">

Use metrics from quantitative research to demonstrate value

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

<a class="tile ga-article-related-course" data-course-title="Statistics for UX" href="/courses/ux-statistics/?lm=frequency-recency&amp;pt=article">

<h4 class="title heading-small">Statistics for UX</h4>

<p id="statistics-for-ux" class="description body-small">

Calculate, interpret, and report the numbers from your quantitative UX studies

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Analytics &amp; Metrics,longitudinal studies</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Analytics &amp; Metrics</span>

<a class="ga-article-related-topic" href="/topic/analytics-and-metrics/">Analytics &amp; Metrics</a>

</li>

</ul>

</div>

</div>

</div>

</div>