# Outliers and Luck in User Performance - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">6</span>

<div class="article-header">

<h1 class="article-h1">Outliers and Luck in User Performance</h1>

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

March 5, 2006

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2006-03-05</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Outliers and Luck in User Performance&amp;body=https://www.nngroup.com/articles/outliers-and-luck-in-user-performance/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/outliers-and-luck-in-user-performance/&amp;title=Outliers and Luck in User Performance&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/outliers-and-luck-in-user-performance/&amp;text=Outliers and Luck in User Performance&amp;via=nngroup" data-share-type="Twitter">

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

</span>6% of task attempts are extremely slow and constitute outliers in measured user performance. These sad incidents are caused by bad luck that designers can — and should — eradicate.

</div>

<div class="article-body">

<p>Generally, I advocate <b> qualitative </b> user testing: a <a class="old" href="http://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/" title="Alertbox: Quantitative Studies: How Many Users to Test?">handful of users is enough</a> to discover most design flaws. <a class="old" href="http://www.nngroup.com/articles/quantitative-studies-how-many-users/" title="Alertbox: Why You Only Need to Test With 5 Users"><b>Quantitative</b> testing</a> does have its place, however, and we've recently been running large tests for two different reasons:</p>

<ul>

<li>We're testing hundreds of users to generate in-depth findings for our <a class="new" href="http://www.nngroup.com/topic/eyetracking/" title="Overview of study findings">eyetracking research</a>. To determine whether men and women look at Web pages differently, for example, we have to test many people using the same websites. This is because users wander all over sites, and we need to test numerous men and women to get a sufficient number of samples for each page.</li>

<li>We're running large-scale usability benchmarks for several clients so they can track their design improvements over time. These studies are really expensive and not recommended for small projects. For big projects, however, they're a good long-term management tool.</li>

</ul>

<p>With all this fresh data at my disposal, I couldn't resist analyzing 1,520 measurements of user time-on-task performance for websites and intranets.</p>

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

<a class="ga-article-toc-item" href="#toc-does-usability-follow-a-normal-distribution-1">Does Usability Follow a Normal Distribution?</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-outliers-for-fast-performance-2">Outliers for Fast Performance</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-outliers-for-slow-performance-3">Outliers for Slow Performance</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-good-luck-in-user-performance-4">Good Luck in User Performance</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-bad-luck-in-user-performance-5">Bad Luck in User Performance</a>

</li>

</ul>

</div>

</div><h2 id="toc-does-usability-follow-a-normal-distribution-1">Does Usability Follow a Normal Distribution?</h2>

<p>Almost all statistical analyses assume that data follows a normal distribution (the famous bell curve). Most people take this on faith, because it's true for so many phenomena. But let's check.</p>

<p>One way of assessing a dataset's distribution is to draw a quantile-quantile scatterplot. In a QQ plot, we plot each observation's empirical value on the <i> x </i> -axis and its hypothetical value on the <i> y </i> -axis, under the assumption that the entire set is normally distributed. We draw a straight line to represent a case with identical empirical and hypothetical values.</p>

<p>If our plotted datapoints are very close to the straight line, we conclude that the empirical values are very close to the hypothetical values. In other words, the observed data are the same as what the theory predicted, so the dataset follows a normal distribution.</p>

<p>Any datapoints that are far from the straight line represent cases in which the real and theoretical worlds differ substantially — in other words, the data doesn't follow the normal distribution.</p>

<p>I've plotted seventy QQ plots from our recent quantitative usability studies, and they all look the same, whether they come from website or intranet studies. Here are two typical examples:</p>

<p style="text-align: center"><img alt="Two scatterplots, showing empirical user performance on the x-axis and the corresponding quantiles from a normal distribution on the y-axis." height="424" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/outliers_qq_plot.gif" style="cursor: default;" width="792"/><br/>

<i>QQ plots of two user studies: a test of a content-based magazine site (<a class="out" href="http://www.nymag.com"><cite>New York </cite> Magazine</a>, on the left) and a test of a transaction-based e-commerce site (<a class="out" href="http://www.kiehls.com">Kiehl's</a>, on the right).<br/>

Each dot represents the task time of one user. The x-axis indicates measured performance and the y-axis indicates the theoretically matching normal distribution. </i></p>

<p>(Note: Because my analysis didn't include users who failed at tasks, the diagrams show only people who used the sites successfully. All seventy studies measured time on task — see earlier article on the <a class="old" href="http://www.nngroup.com/articles/usability-101-introduction-to-usability/" title="Alertbox: Usability 101: Fundamentals and Definition - What, Why, How">definition of usability</a> for other main quality attributes.)</p>

<p>Although the dots aren't exactly on the straight line, they're pretty close. There are a few outliers, but it seems safe to conclude that most <b> users do follow a normal distribution</b>. Close enough for government work — or more to the point, close enough for any analysis you need in a practical development project.</p>

<h2 id="toc-outliers-for-fast-performance-2">Outliers for Fast Performance</h2>

<p>Outliers in the lower left corner of each QQ plot are shown as solid <b> blue dots</b>. These are users who <b> were fast, but not as fast as the theory predicted</b>. In fact, in the left-hand QQ plot, two dots are below the <i> x</i>-axis, indicating negative <i> y </i> values. The theory predicts that these two users would have finished their task before they started, which is obviously impossible.</p>

<p>In usability testing, there's a clear floor effect for measured task times: people simply can't be faster than a certain minimum, no matter how efficiently they use a site. Downloading pages and moving your hand between mouse and keyboard require a certain amount of time. Even the fastest typists still need time to type in search engine queries; the fastest readers still need time to read, regardless of how quickly they can find the salient information on a page.</p>

<p>All the studies I've analyzed included a few fast outliers. These fast (but not quite fast enough) users are easy to explain, however, and I don't think they should impact our thinking about Web usability.</p>

<h2 id="toc-outliers-for-slow-performance-3">Outliers for Slow Performance</h2>

<p>Outliers in the upper right corner are shown as solid <b> red dots</b>. These are users who were <b> dramatically slower than the slowest predicted users</b>.</p>

<p>Of 1,520 cases, eighty-seven were outliers with exceedingly slow task times. This means that <b> 6% of users are slow outliers</b>. This is too many people to ignore. Of course, you should first and foremost improve the user experience for the 94% of users who are not outliers, but it's worth allocating some usability resources to that slow 6% as well.</p>

<p>The most seemingly obvious explanation for these outliers is simply that a few people are almost incompetent at using the Web, and they'll show up as slow outliers every time they test something. <i> But this hypothesis is false</i>. Once we recruit people for a study, we ask them to do multiple things, so we know how the slow outliers perform on several other tasks. In general, the same users who were extremely slow on some tasks were fast on other tasks.</p>

<p>Sixty different users were responsible for the eighty-seven slow outliers, for an average of 1.5 outliers each. Given that users were tested on an average of 6.7 tasks across the analyzed studies, each of these users had an average of 5.2 "normal" tasks — 3.5 times as many as their outlying tasks.</p>

<p>This topic clearly needs more research, and would make for several good graduate theses. For now, my best conclusion is that <b> slow outliers are caused by bad luck </b> rather than by a persistent property of the users in question.</p>

<h2 id="toc-good-luck-in-user-performance-4">Good Luck in User Performance</h2>

<p>Before turning to bad luck, let's acknowledge that good luck also happens on the Web. People are sometimes "undeservedly" lucky on a website and get exactly what they want in fewer clicks than expected. Maybe, for example, they're looking to buy something that happens to be the homepage's featured promotion that day. In other cases, some users happily skirt gross usability mistakes that cause other people grave difficulties and much frustration.</p>

<p>Here's an example of good luck from a <a class="old" href="http://www.nngroup.com/topic/accessibility/" title="Nielsen Norman Group report: Beyond ALT Text - Making the Web Easy to Use for Users With Disabilities, 75 Best Practices for Design of Websites and Intranets, Based on Usability Studies with People Who Use Assistive Technology">test with disabled users</a> trying to use the website of the IRS (the U.S. tax authorities). One blind user wanted to find out whether she could deduct money donated to a high school band.</p>

<p>Because the IRS page was long and overwhelming, the user decided to have her screen reader device read out the list of links on the page. Further, because the user was looking for tax rules about "donations" she commanded the screen reader to read links that started with a "D." As it turns out, the IRS uses the term "deduction" rather than "donation" — something the user would never discover from a simple page or site search using the word "donation." However, because both words start with "D" and the person was using a screen reader, she easily happened upon "deduction" as the correct link. A joyful outcome, but one that's purely due to good luck.</p>

<p>(There are a few additional usability notes here. First, by using the term "deduction" rather than "donation," the site opts for system-oriented language over a term describing the user's action, which the site is presumably supposed to support. Second, using the screen reader shortcut is an expert behavior; you shouldn't use it as an excuse for long pages, which hurt less-experienced screen reader users. Finally, the "read links" feature is one of the reasons it's a guideline to <a href="https://www.nngroup.com/articles/learn-more-links/">avoid links with labels such as "click here" or "more,"</a> which don't make sense out of context.)</p>

<h2 id="toc-bad-luck-in-user-performance-5">Bad Luck in User Performance</h2>

<p>Most website and intranet users are all too familiar with bad luck. Typical examples include:</p>

<ul>

<li><b>Clicking the wrong link </b> and being lost forever in the wrong part of the site.</li>

<li><b>Using the wrong words</b>. In contrast to the "good luck" example above, users can waste significant time scouring a site for a term that the site doesn't use and doesn't cross-reference to its own preferred term.</li>

<li>Companies with <b> multiple websites </b> often bounce users off to the wrong site, but users don't realize the error.</li>

<li>The link or information the user needs is <b> scrolled just off the screen </b> and so the user never sees it. (See also newer data on <a href="https://www.nngroup.com/articles/scrolling-and-attention/">users' scrolling behavior</a>.)</li>

<li>A <b> pop-up distracts users </b> just as they were about to get it right.</li>

<li><a class="old" href="http://www.nngroup.com/reports/ecommerce/checkout.html" title="Nielsen Norman Group report: E-commerce User Experience - Design Guidelines for Shopping Carts, Checkout, and Registration"><b>Registration hiccups</b></a> take users on detours long enough that their attempts to buy stuff are doomed, even when they've successfully found what they wanted and placed it safely in the shopping cart.</li>

<li><b>Multiple small problems </b> — any one of which could be easily handled in isolation — occur in a row and thus derail users.</li>

</ul>

<p>Of course, none of these issues are really "luck" in the superstitious sense of something "unnatural" happening. In fact, they're all small, but real defects in the design's usability. What qualifies these flaws as bad luck is that, under rare circumstances, they condemn users to terrible misfortune. If things had gone a tiny bit differently — say, a user had scrolled down one line further — he or she might have had good luck and a very pleasant user experience.</p>

<p>Given that slow outliers account for 6% of Web usage, it's unacceptable to simply write them off. Although the data shows that most users will avoid bad luck in their next online task, you can't just say "better luck next time"; if you do, their next user experience will likely be on somebody else's website.</p>

<p>People leave websites that hurt them — they don't know that it's just bad luck, and that next time will be better. It's therefore incumbent on you to hunt down the root causes of bad luck and eradicate them from your site.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Usability Testing" href="/courses/usability-testing/?lm=outliers-and-luck-in-user-performance&amp;pt=article">

<h4 class="title heading-small">Usability Testing</h4>

<p id="usability-testing" class="description body-small">

Plan, conduct, and analyze your own studies, whether in person or remote

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

<a class="tile ga-article-related-course" data-course-title="Analytics and User Experience" href="/courses/analytics-and-user-experience/?lm=outliers-and-luck-in-user-performance&amp;pt=article">

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

<a class="tile ga-article-related-course" data-course-title="Measuring UX and ROI" href="/courses/measuring-ux/?lm=outliers-and-luck-in-user-performance&amp;pt=article">

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

</ul>

</div>

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">User Testing,Analytics &amp; Metrics,errors</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">User Testing</span>

<a class="ga-article-related-topic" href="/topic/user-testing/">User Testing</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/analytics-and-metrics/">Analytics &amp; Metrics</a>

</li>

</ul>

</div>

</div>

</div>

</div>