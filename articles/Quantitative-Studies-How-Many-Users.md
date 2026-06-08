# Quantitative Studies: How Many Users to Test? - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">5</span>

<div class="article-header">

<h1 class="article-h1">Quantitative Studies: How Many Users to Test?</h1>

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

June 25, 2006

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2006-06-25</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Quantitative Studies: How Many Users to Test?&amp;body=https://www.nngroup.com/articles/quantitative-studies-how-many-users/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/quantitative-studies-how-many-users/&amp;title=Quantitative Studies: How Many Users to Test?&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/quantitative-studies-how-many-users/&amp;text=Quantitative Studies: How Many Users to Test?&amp;via=nngroup" data-share-type="Twitter">

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

</span>When collecting usability metrics, testing with 20 users typically offers a reasonably tight confidence interval.

</div>

<div class="article-body">

<p>We can <a class="old" href="https://www.nngroup.com/articles/usability-101-introduction-to-usability/" title="Alertbox: Usability 101 - Fundamentals and Definition - What, Why, How"> define usability</a> in terms of quality metrics, such as learning time, efficiency of use, memorability, user errors, and subjective satisfaction. Sadly, few projects collect such metrics because doing so is expensive: <strong> it requires 4 times as many users </strong> as simple user testing.</p>

<p>Many users are required because of the <a class="old" href="https://www.nngroup.com/articles/variability-in-user-performance/" title="Alertbox: Variability in User Performance"> substantial individual differences in user performance</a>. When you measure people, you'll always get some who are really fast and some who are really slow. Given this, you need to average these measures across a fairly large number of observations to smooth over the variability.</p>

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

<a class="ga-article-toc-item" href="#toc-standard-deviation-for-web-usability-data-1">Standard Deviation for Web Usability Data</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-removing-outliers-2">Removing Outliers</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-estimating-margin-of-error-3">Estimating Margin of Error</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-determining-the-number-of-users-to-test-with-4">Determining the Number of Users to Test With</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-quantitative-vs-qualitative-5">Quantitative vs. Qualitative</a>

</li>

</ul>

</div>

</div><h2 id="toc-standard-deviation-for-web-usability-data-1">Standard Deviation for Web Usability Data</h2>

<p>We know from previous analysis that <a class="old" href="https://www.nngroup.com/articles/outliers-and-luck-in-user-performance/" title="Alertbox: Outliers and Luck in User Performance"> user performance on websites follows a normal distribution</a>. This is happy, because normal distributions are fairly easy to deal with statistically. By knowing just two numbers — the <strong>mean</strong> and the <strong>standard deviation</strong> — you can draw the bell curve that represents your data.</p>

<p>I analyzed 1,520 measures of user time-on-task performance for 70 different tasks from a broad spectrum of websites and intranets. Across these many studies, the <strong> standard deviation was 52% of the mean </strong> values. For example, if it took an average of 10 minutes to complete a certain task, then the standard deviation for that metric would be 5.2 minutes.</p>

<h2 id="toc-removing-outliers-2">Removing Outliers</h2>

<p>To compute the standard deviation, I first removed the outliers representing excessively slow users. Is this reasonable to do? In some ways, no: slow users are real, and you should consider them when assessing a design's quality. Thus, even though I recommend removing outliers from the statistical analyses, you shouldn't forget about them. Do a qualitative analysis of outliers' test sessions and find out what "bad luck" (i.e., bad design) conspired to drag down their performance.</p>

<p>For most statistical analyses, however, you should eliminate the outliers. Because they occur randomly, you might have more outliers in one study than in another, and these few extreme values can seriously skew your averages and other conclusions.</p>

<p>The only reason to compute statistics is to <strong> compare them with other statistics. </strong> That my hypothetical task took an average of 10 minutes means little on its own. Is 10 minutes good or bad? You can't tell from putting that one number on a slide and admiring it in splendid isolation.</p>

<p>If you asked users to subscribe to an email newsletter, a 10-minute average task time would be extremely bad. We know from <a class="old" href="https://www.nngroup.com/articles/e-mail-newsletters-increasing-usability/" title="Alertbox: Email Newsletters: Surviving Inbox Congestion"> studies of many newsletter subscription processes</a> that the average task time across other websites is 1 minute, and users are only really satisfied if it takes less than 2 minutes. On the other hand, 10 minutes would indicate very high usability for more complex tasks, such as applying for a mortgage.</p>

<p>The point is that you collect usability metrics to compare them with other usability metrics, such as comparing your site with your competitors' sites or your new design with your old.</p>

<p>When you eliminate outliers from both statistics, you still have a valid comparison. True, average task time in both cases will be a bit higher if you keep the outliers. But, without the outliers, you're more likely to reach correct conclusions, because you're less likely to overestimate an average that happened to have a greater number of outliers.</p>

<h2 id="toc-estimating-margin-of-error-3">Estimating Margin of Error</h2>

<p>When you average together several observations from a normal distribution, the standard deviation (SD) of your average is the SD of the individual values divided by the square root of the number of observations. For example, if you have 10 observations, then the SD of the average is 1/sqrt(10) = 0.316 times the original SD.</p>

<p>We know that for user testing of websites and intranets, the SD is 52% of the mean. In other words, if we tested 10 users, then the SD of the average would be 16% of the mean, because .316 x .52 = .16.</p>

<p>Let's say we're testing a task that takes five minutes to perform. So, the SD of the average is 16% of 300 seconds = 48 seconds. For a normal distribution, 2/3 of the cases fall within +/− 1 SD from the mean. Thus, our average would be within 48 seconds of the 5-minute mean 2/3 of the time.</p>

<p>The following chart shows the margin of error for testing various numbers of users, assuming that you want a <strong> 90% confidence interval </strong> (blue curve). This means that 90% of the time, you hit within the interval, 5% of the time you hit too low, and 5% of the time you hit too high. For practical Web projects, you really don't need more accurate interval than this.</p>

<p>The red curve shows what happens if we relax our requirements to being right half of the time. (Meaning that we'd hit too low 1/4 of the time and too high 1/4 of the time.)</p>

<p style="margin-bottom:0px; margin-left:0px; margin-right:0px; margin-top:0px; text-align:center; width:701px"><img alt="Curve showing how big the margin of error is when testing different numbers of users." height="400" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/margin_of_error.gif" width="701"/></p>

<h2 id="toc-determining-the-number-of-users-to-test-with-4">Determining the Number of Users to Test With</h2>

<p>In the chart, the margin of error is expressed as a percent of the mean value of your usability metric. For example, if you test with 10 users, the margin of error is +/ 27% of the mean. This means that if the mean task time is 300 seconds (five minutes), then your margin of error is +/− 81 seconds. Your confidence interval thus goes from 219 seconds to 381 seconds: 90% of the time you're inside this interval; 5% of the time you're below 219, and 5% of the time you're above 381.</p>

<p>This is a rather wide confidence interval, which is why I usually recommend <strong> testing with 20 users </strong> when collecting quantitative usability metrics. With 20 users, you'll probably have 1 outlier (since <a class="old" href="https://www.nngroup.com/articles/outliers-and-luck-in-user-performance/" title="Alertbox: Outliers and Luck in User Performance"> 6% of users are outliers</a>), so you'll include data from 19 users in your average. This makes your confidence interval go from 243 to 357 seconds, since the margin of error is +/− 19% for testing 19 users.</p>

<p>You might say that this is still a wide confidence interval, but the truth is that it's extremely expensive to tighten it up further. To get a margin of error of +/− 10%, you need data from 71 users, so you'd have to test 76 to account for the five likely outliers.</p>

<p><strong>Testing 76 users is a complete waste of money </strong> for almost all practical development projects. You can get good-enough data on 4 different designs by testing each of them with 20 users, rather than blow your budget on only slightly better metrics for a single design.</p>

<p>In practice, a <strong> confidence interval of +/− 19% is ample </strong> for most goals. Mainly, you're going to compare two designs to see which one measures best. And the <a class="old" href="https://www.nngroup.com/articles/website-usability-differences/" title="Alertbox: How Big is the Difference Between Websites?"> average difference between websites is 68%</a> — much more than the margin of error.</p>

<p>Also, remember that the +/− 19% is pretty much a worst-case scenario; you'll do better 90% of the time. The red curve shows that <strong> half of the time you'll be within +/− 8% of the mean </strong> if you test with 20 users and analyze data from 19. In other words, half the time you get great accuracy and the other half you get good accuracy. That's all you need for non-academic projects.</p>

<h2 id="toc-quantitative-vs-qualitative-5">Quantitative vs. Qualitative</h2>

<p>Based on the above analysis, my recommendation is to test with 20 users in quantitative studies. This is <strong> very expensive, </strong> because test users are hard to come by and require <a class="old" href="https://www.nngroup.com/articles/recruiting-test-participants-for-usability-studies/" title="Alertbox: Recruiting Test Participants for Usability Studies"> systematic recruiting</a> to actually represent your target audience.</p>

<p>Luckily, <strong> you don't have to measure usability to improve it. </strong> Usually, it's enough to <a class="old" href="https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users" title="Alertbox: Why You Only Need to Test With 5 Users"> test with a handful of users</a> and revise the design in the direction indicated by a qualitative analysis of their behavior. When you see several people being stumped by the same design element, you don't really need to know <em> how much </em> the users are being delayed. If it's hurting users, change it or get rid of it.</p>

<p>You can usually run a qualitative study with 5 users, so quantitative studies are about 4 times as expensive. Furthermore, it's easy to <a class="old" href="https://www.nngroup.com/articles/risks-of-quantitative-studies/" title="Alertbox: Risks of Quantitative Studies"> get a quantitative study wrong</a> and end up with misleading data. When you collect numbers instead of insights, everything must be exactly right, or you might as well not do the study.</p>

<p>Because they're expensive and difficult to get right, I usually warn against quantitative studies. <strong> The first several usability studies you perform should be qualitative. </strong> Only after your organization has <a class="old" href="https://www.nngroup.com/articles/ux-maturity-model/" title="Alertbox: Corporate Usability Maturity: Stages 5-8"> progressed in maturity with respect to integrating user research</a> into the design lifecycle and you're routinely performing qual studies should you start including a few quant studies in the mix.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Analytics and User Experience" href="/courses/analytics-and-user-experience/?lm=quantitative-studies-how-many-users&amp;pt=article">

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

<a class="tile ga-article-related-course" data-course-title="ResearchOps: Scaling User Research" href="/courses/researchops/?lm=quantitative-studies-how-many-users&amp;pt=article">

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

<a class="tile ga-article-related-course" data-course-title="Survey Design and Execution" href="/courses/surveys/?lm=quantitative-studies-how-many-users&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Analytics &amp; Metrics,Research Methods,User Testing,quantitative studies,a/b testing</span>

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

<a class="ga-article-related-topic" href="/topic/user-testing/">User Testing</a>

</li>

</ul>

</div>

</div>

</div>

</div>