# UX Debt: How to Identify, Prioritize, and Resolve - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">12</span>

<div class="article-header">

<h1 class="article-h1">UX Debt: How to Identify, Prioritize, and Resolve</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Anna Kaley</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/20181001_Raleigh-106.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/anna-kaley/">

Anna Kaley</a></span>

<p class="publication-date">

November 11, 2018

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2018-11-11</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: UX Debt: How to Identify, Prioritize, and Resolve&amp;body=https://www.nngroup.com/articles/ux-debt/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/ux-debt/&amp;title=UX Debt: How to Identify, Prioritize, and Resolve&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/ux-debt/&amp;text=UX Debt: How to Identify, Prioritize, and Resolve&amp;via=nngroup" data-share-type="Twitter">

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

</span>Like tech debt, UX debt piles up over time and, if left unaddressed, leads to compounding user problems and costly cleanup efforts. Agile teams can modify their processes to track and resolve UX debt.

</div>

<div class="article-body">

<p>Continually prioritizing fast and easy solutions may help us hit release dates in the short term, but over time, repeatedly choosing shortcuts will leave us with mounting experience issues that adversely impact our users. These issues are known as UX debt and, if left unaddressed for too long, lead to costly, time-consuming problems that take effort to fix later on. <a href="https://www.nngroup.com/videos/effective-agile-ux/">Agile teams</a> are particularly prone to UX debt as a result of heightened pressure to regularly ship new features and functionality. However, <strong>UX debt can accumulate in any project, regardless of the development methodology employed</strong>, and too much of it will result in a loss of trust, traffic, and revenue. In this article, we define UX debt and show how it can be identified; we also discuss methods for how to prioritize UX-debt issues and resolve them. While these methods are framed for Agile environments, they can easily be adapted to other development processes.</p>

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

<a class="ga-article-toc-item" href="#toc-what-is-ux-debt-1">What Is UX Debt?</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-identifying-ux-debt-2">Identifying UX Debt</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-tracking-and-prioritizing-issues-3">Tracking and Prioritizing Issues</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-resolving-ux-debt-4">Resolving UX Debt</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-5">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-what-is-ux-debt-1">What Is UX Debt?</h2>

<p>UX debt is similar to its technical counterpart, known as<strong> technical (or tech) debt</strong>. Originally devised by Ward Cunningham in 1992, tech debt refers to the additional time and effort costs that result from launching faster or easier technical solutions, instead of releasing the best approach. It implies that the cost of having to go back and fix problems after launch is always higher than launching ideal solutions in the first place (i.e., the debt is repaid with usurious interest). <strong>Like tech debt, UX debt is often incurred when designers and researchers are working under tight timelines or impractical project constraints.</strong> Other factors that contribute to UX debt include:</p>

<ul>

<li>Skipping <a href="https://www.nngroup.com/videos/user-testing-jakob-nielsen/">user testing</a></li>

<li>Disregarding brand standards and <a href="https://www.nngroup.com/articles/front-end-style-guides/">style guides</a></li>

<li>Design by committee</li>

<li>Misinterpreting the product vision</li>

<li>Acquiring or merging with other products</li>

<li>Poor communication or documentation</li>

<li>Insufficient QA testing</li>

<li>Legacy code or delayed refactoring</li>

</ul>

<p>Why is it more expensive to fix a UX problem later, rather than before launch? For many reasons. First, redesigning and recoding consumes many resources: the team has to refamiliarize with the nuances and details of the already launched features, spend time debugging them, and then possibly retrofit other parts of the software. From a pure software-engineering perspective, coding the UI right the first time is much easier on the developers than having to change shipped code. But there are also user-experience reasons for the extra cost of UX debt:</p>

<ul>

<li>Launching a suboptimal design impacts long-term market share, because many customers will give you one try and then give up when the design is too difficult or doesn’t satisfy their needs. Even if you fix their complaint later, the users won’t know, because they won’t resample your site or product once they’ve had a bad experience.</li>

<li>Users will become accustomed to the bad design. Then, after you change the design, people will be forced to change their habits and hate you for that.</li>

<li>Changing the design back and forth for any particular component of the overall UX will degrade the feelings of consistency and coherency.</li>

<li>Your failures will live forever on the internet. Since learning is social, users will continue to be “informed” for years of your missteps by blogs, message boards, video channels, and other sources that discuss the old version. Not only will this outdated information be harmful rather than helpful to your users, it will also scare away new prospects who come across descriptions of the bad design and any awkward workarounds people had discovered and posted.</li>

</ul>

<p>Any UX debt will incur some of these costs. But the longer the UX debt remains unpaid, the more these costs will mount (think of “compound interest” as an analogy).</p>

<p>An example of UX debt can be seen on FedEx’s website in a carousel that appears on the product page for printed posters. Initially, the carousel displays four related products; however, clicking on the right arrow to view more related products reveals only one additional item. Rather than filling the content area with more images and links to related products, the carousel shows empty white space. A user looking for invitations or similar printed materials may grow frustrated at the lack of relevant products in this carousel. FedEx should add more related products to the carousel or update the functionality to accommodate varying amounts of content. <strong>As time goes by, teams easily forget about these seemingly small issues and the likelihood of going back to fix them diminishes when there’s pressure to move on to other priorities.</strong> However, these <a href="https://www.nngroup.com/articles/does-user-annoyance-matter/">issues do impact users</a> and should be addressed to preserve the website’s integrity.</p>

<figure class="caption"><img alt="A product carousel on FedEx that is missing several items. " height="510" loading="lazy" src="https://media.nngroup.com/media/editor/2018/09/27/fedexproductcarousel.png" width="692"/>

<figcaption><em>To resolve this example of UX debt, FedEx should add more related products or update the carousel functionality to accommodate varying amounts of content.</em></figcaption>

</figure>

<p>Though the word <em>debt</em> is daunting for most people, the metaphor does not imply that UX debt should be avoided at all costs. Especially when working in Agile, there will be cases when speed to market and pressure to meet release dates necessitate time-saving alternatives. While certain types of UX debt (such as problems with integration, inconsistencies, and trouble preserving a simple conceptual model that explains and unites the entire user experience) are more likely in Agile, any decisions that will deliberately result in UX debt should be made carefully and collectively. <strong>Consider if getting to market faster is worth the risk of negatively affecting user perceptions and the high costs of fixing issues later on. </strong>When the answer is yes, the resulting UX debt should be tracked, managed, and, paid back gradually over time so that users don’t notice it and abandon the website or application entirely.</p>

<h2 id="toc-identifying-ux-debt-2">Identifying UX Debt</h2>

<p>UX debt includes any ongoing problems in the experience due to launching a fast, easy, or careless solution that negatively impacts users. Whether it is introduced deliberately or accidentally, it’s important to look for UX debt in these areas of the experience that are prone to debt buildup:</p>

<ul>

<li>User interface (buttons, links, and visual styling)</li>

<li><a href="https://www.nngroup.com/topic/interaction-design/">Interaction design</a> (movement from page to page, animations, and scrolling effects)</li>

<li><a href="https://www.nngroup.com/articles/microcontent-how-to-write-headlines-page-titles-and-subject-lines/">Copy, content, and messaging</a> (labels, headlines, and written text)</li>

<li><a href="https://www.nngroup.com/articles/top-10-ia-mistakes/">Information architecture</a> (navigation structures and content classification)</li>

<li><a href="https://www.nngroup.com/articles/accessibility-is-not-enough/">Accessibility</a> elements (contrast, visual focus indicators, text alternatives, etc.)</li>

<li><a href="https://www.nngroup.com/articles/omnichannel-consistency/">Customer journey consistency</a></li>

<li><a href="https://www.nngroup.com/articles/seamless-cross-channel/">Omnichannel seamlessness</a></li>

</ul>

<p>For example, a press release on Symantec’s investor-relations website contains body copy that is too low contrast to be considered accessible. Though low contrast is not a bug, it is an example of UX debt that could negatively impact low-vision or color-blind users. Per the <a href="https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html">WCAG</a> guidelines, contrast ratios between text and background colors should be 4.5 to 1 for normal-size text. The contrast ratio between the text color and background color on this page is only 3.2 to 1 and therefore, too low to be considered accessible. Symantec should have selected a body-copy color that meets accessibility standards and must now remember to go back and fix this issue of UX debt.</p>

<figure class="caption"><img alt="A press release on Symantec's website has text that's too light for accessibility. " height="487" loading="lazy" src="https://media.nngroup.com/media/editor/2018/09/27/symantecpressrelease.png" width="692"/>

<figcaption><em>To resolve this example of UX debt, Symantec should select a darker body-copy color that results in a higher contrast ratio to meet accessibility standards.</em></figcaption>

</figure>

<p>The best way to uncover UX debt is by getting real user feedback often and in a <a href="https://www.nngroup.com/topic/research-methods/">variety of ways</a>. Though you should always conduct user testing before releasing sprint features, ongoing testing should also happen at least once a month and focus on the key flows and <a href="https://www.nngroup.com/articles/task-scenarios-usability-testing/">realistic tasks that users frequently do</a> on your website or application. This approach will help you understand the overall health of the user experience and identify the most serious issues. Other user-feedback methodologies that can help you find UX debt include:</p>

<ul>

<li><a href="https://www.nngroup.com/articles/live-intercept-remote-test/">Site-intercept surveys</a></li>

<li>CSAT or <a href="https://www.nngroup.com/articles/nps-ux/">NPS scores</a></li>

<li>Issues reported by customer service</li>

</ul>

<p>In addition to user feedback, set up recurring time with the entire product team, <a href="https://www.nngroup.com/videos/designer-developer-relationships/">including developers</a>, to review the overall health of the site or app. <strong>Open up the discussion for the rest of the team to bring forward any UX- or tech-debt items that may negatively impact the user experience.</strong> Product management can also bring up debt-related issues found by leadership or other stakeholders. If possible, share trends or patterns from <a href="https://www.nngroup.com/videos/turning-analytics-findings-usability-studies/">analytics</a> during the discussion so the team can decide together if further investigation is needed to identify debt.</p>

<p><strong>Inconsistencies in the UI can be considered UX debt, but not always.</strong> It’s possible to have occasional slight discrepancies in the user interface that fit within the brand guidelines and don’t cause problems for users. For example, during an A/B test, there may be some temporary UX issues until the team understands which variation is optimal and whether it should be added to a <a href="https://www.nngroup.com/videos/design-systems/">design system</a>. These types of inconsistencies should not be considered UX debt since the variations are temporary and intentional. (To avoid creating UX debt as a byproduct of an A/B test, teams should ensure that the winning elements are scaled into the design system with full consistency and clear standards for the new patterns or components.)</p>

<p>An example of an informational inconsistency in the UI that does count as UX debt was observed on Amazon. The shipping-for-returns page displayed inconsistent quantities for return items: the user wanted to return 4 pairs of pants, but the text on the page read <em>Returning 2 items </em>and the summary info said <em>Refund subtotal for 3 items</em>. This contradictory information caused the user to question the refund amount and to navigate back to the previous page to double check that the total estimated refund was correct. Amazon’s inconsistency is UX debt and should be addressed to help users move smoothly through the return process.</p>

<figure class="caption"><img alt="Amazon's returns page displays inconsistent quantity information. " height="456" loading="lazy" src="https://media.nngroup.com/media/editor/2018/09/27/amazonreturnspage.png" width="692"/>

<figcaption><em>A user on Amazon encountered contradictory, incorrect item quantities when executing a return. This inconsistency caused them to question Amazon’s credibility and accuracy. This type of issue counts as UX debt.</em></figcaption>

</figure>

<p>When actual UX-debt issues and bugs like these are found, their severity, frequency, and location in the users’ journey should drive the issue valuation and prioritization. Though in the following sections we discuss how to track, prioritize, and resolve issues when working in the Agile development process,<strong> the approaches and concepts outlined can be adapted and applied to any development methodology</strong> and will help you track, rank, and gradually clean up UX debt over time.</p>

<h2 id="toc-tracking-and-prioritizing-issues-3">Tracking and Prioritizing Issues</h2>

<p>Once UX debt items are identified, there are a few ways you can track them for prioritization. Each method has pros and cons, so it is important to choose one that works best for your team and organization. Common ways in which UX debt items are tracked include:</p>

<ul>

<li>Adding UX-debt items directly to the backlog for prioritization</li>

<li>Capturing UX-debt items in a spreadsheet, then adding them to the backlog</li>

</ul>

<h3>Adding UX-Debt Items Directly to the Backlog</h3>

<p>Putting UX debt items directly into the backlog can work well for teams that have well-organized backlogs with clear severity indicators and prioritization processes. However, for large, complex organizations that deal with many <a href="https://www.nngroup.com/articles/ux-user-stories/">user stories</a> and product-backlog items, adding UX debt directly to the backlog could mean those items get lost or continually deprioritized in favor of new features and functionality. One user-experience professional who favors this approach said:</p>

<blockquote>

<p>“We track our UX-debt items using an epic in our backlog. During backlog grooming, we review the list of technical and UX-debt items, then we collectively prioritize and decide what to tackle in the next two weeks. We do this before we plan for any new features and functionality so we can balance cleanup with new features."</p>

</blockquote>

<p>To make sure that UX debt gets the attention it deserves each sprint, create a product-backlog item or a label for UX debt and use the same severity indicators as for other items in the backlog. In this way, <strong>all items can be evaluated using the same dimensions for prioritization during grooming and planning.</strong> This method will also help teams look back and see how much UX debt was been paid back within a time period.</p>

<p>What will improve the product experience the most: a new feature or making an existing feature usable? Quite often, the latter choice is best, since a feature that people can’t use might as well not exist. Thus, fixing something that doesn’t work for users has the same effect as adding a new feature, in terms of what customers actually get to use. Therefore, UX problems with existing features could and should often get assigned higher priority than new features. Moreover, features are usually implemented in order of expected benefit, so that an old feature is likely to be intrinsically more valuable than a new feature, if only the old feature could be made to work for users.</p>

<h3>Organize and Prioritize in a Spreadsheet</h3>

<p>For teams with many UX debt items or complex backlogs, prioritize issues in a spreadsheet before adding them to the backlog. This method will protect the team from getting overwhelmed or ignoring long lists of product-backlog items. It will also help the product owner prioritize issues accordingly and add to the backlog only those UX-debt items that make the most sense for the product vision, users, and team workload. The following factors will <strong>reveal the biggest pain points in the users’ experience and should be included in the spreadsheet:</strong></p>

<ul>

<li>Description of the issue from users’ standpoint (how is it affecting them?)</li>

<li>Where in the experience it occurs (awareness, consideration, conversion)</li>

<li>Frequency of occurrence (how often does it happen?)</li>

<li>Who reported the issue? (user, team, stakeholder)</li>

<li>Level of UX and development effort needed to fix the issue (low, medium, or high)</li>

</ul>

<p><a href="https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/">Score each issue</a> by assigning a value to the experience area, frequency, reporter, and level of effort to fix the issue. Then, use a <a href="https://www.nngroup.com/articles/prioritization-matrices/">prioritization matrix in the form of a scatter plot</a> to see where the issues fall on the dimensions of user value and effort to fix. This visualization can help you rank issues and communicate progress in cleaning up UX debt back to <a href="https://www.nngroup.com/articles/collaborating-stakeholders/">stakeholders and leadership</a> over time.</p>

<figure class="caption"><img alt="Severity plot for UX debt prioritization" height="422" loading="lazy" src="https://media.nngroup.com/media/editor/2018/09/27/severityplotforuxdebt.png" width="692"/>

<figcaption><em>Visualizing UX debt in a scatter plot can help the team organize, understand, and prioritize issues based on user value and level of effort needed to fix the issue before adding them to the backlog.</em></figcaption>

</figure>

<p><strong>Though the costs associated with going back and fixing issues will always be higher than launching with the ideal solution in the first place</strong>, it is still important to weigh all of these factors when prioritizing to avoid wasting even more time, effort, and resources when cleaning up UX debt. One user-experience professional who favors this approach said:</p>

<blockquote>

<p>“We added our UX debt to the backlog, but it got lost and overlooked amidst all of the other competing priorities. By organizing items in a spreadsheet first, the product owner, lead developer, and user-experience designer can review them together and determine a few items to add to the backlog for the coming sprints. It feels more manageable to pay back our UX and tech debt over time.”</p>

</blockquote>

<p><strong>The most important consideration to keep in mind is that UX debt and technical debt should never be disregarded altogether.</strong> Many <a href="https://www.nngroup.com/articles/agile-development-and-usability/">Agile organizations</a> tend to prioritize tech debt over UX debt, but focusing on one type of debt over another will only lead to more problems for users and more expensive fixes in the end. It’s also important to realize that the two types of debt often go hand in hand. Don't completely abandon UX debt in favor of addressing tech debt, or vice versa. <strong>Prioritize efforts that aim to reduce tech and UX debt at the same time.</strong> It's more efficient and ensures you won't dig yourself further into debt by focusing on one type while abandoning the other. This approach will also help the product maintain full trust and credibility with users.</p>

<p>While the high-priority UX problems should definitely be fixed first, the lower-priority ones should not be abandoned completely. As the years go by, cumulated layers of barnacles will slow even the mightiest ship, and the user experience will feel like a lower and lower quality product, as users encounter small annoyances every step of their way.</p>

<h2 id="toc-resolving-ux-debt-4">Resolving UX Debt</h2>

<p>Paying down UX debt can feel daunting at first and will take time, but there are a few ways to resolve it while still making overall improvements to your digital products. <strong>One approach is to dedicate a specific number of story points to fix UX debt during each sprint or every other sprint.</strong> The number of story points can fluctuate over time depending on the team’s workload, but try to address at least one or two UX-debt items per sprint, preferably more if bandwidth allows. Use easy-to-understand visualizations, evidence from user testing, and clear explanations of what was accomplished in each sprint to help leadership and executives understand the progress made and why it’s important.</p>

<figure class="caption"><img alt="Communicate UX debt payback over time. " height="422" loading="lazy" src="https://media.nngroup.com/media/editor/2018/09/27/communicatinguxdebtpayback.png" width="692"/>

<figcaption><em>Showing progress and communicating the value of resolving UX debt over time will help leadership and executives understand the importance and positive impact that cleanup has on the user experience.</em></figcaption>

</figure>

<p>Another approach is to plan a <strong>quarterly sprint dedicated to cleaning up tech debt and UX debt</strong>. The team should collectively decide what areas to focus on in the cleanup sprint and, at the end, show what was cleaned up. If an entire sprint isn’t feasible, some teams will take a day (sometimes referred to as a <strong>cheese day</strong>) rather than a full sprint to address as much UX debt as possible. Approaching resolution in this manner gets stakeholders and leadership on board with addressing debt items frequently, especially when progress can be demonstrated and <strong>communicated in terms of user and business value generated.</strong></p>

<h2 id="toc-conclusion-5">Conclusion</h2>

<p>UX debt isn’t always avoidable but teams can organize and collaborate around how to address it. Include all of the right people as early as possible to discuss the risks of a premature or haphazard launch and develop a cadence in looking for less-than-optimal experience elements. Conduct regular user testing and <a href="https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/">heuristic reviews</a> of the experience to ensure new UX-debt issues are found and prioritized. Leverage data, such as the scores used in severity plotting, to make the case for why certain issues warrant resolution over others, and show progress in debt-cleanup efforts. Acknowledging and formulating a plan for paying UX debt back over time will help you resolve it, before your users start to notice.</p>

<p>For more information on how to identify, prioritize, and resolve UX debt, take our full-day training course, <a href="https://www.nngroup.com/courses/lean-ux-and-agile/">Lean UX and Agile</a>.</p>

<h3>Reference</h3>

<p><a href="http://wiki.c2.com/?TechnicalDebt">Technical Debt</a> Wiki</p>

<p> </p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Lean UX and Agile" href="/courses/lean-ux-and-agile/?lm=ux-debt&amp;pt=article">

<h4 class="title heading-small">Lean UX and Agile</h4>

<p id="lean-ux-and-agile" class="description body-small">

Strategies to stay user-centered in fast-paced Agile environments

</p>

<div class="ux-specialties">

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

<a class="tile ga-article-related-course" data-course-title="Storytelling to Present UX Work" href="/courses/storytelling-ux/?lm=ux-debt&amp;pt=article">

<h4 class="title heading-small">Storytelling to Present UX Work</h4>

<p id="storytelling-to-present-ux-work" class="description body-small">

Persuade and engage while presenting research findings and design ideas

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

<a class="tile ga-article-related-course" data-course-title="Leading Highly Effective UX Teams" href="/courses/leading-ux-teams/?lm=ux-debt&amp;pt=article">

<h4 class="title heading-small">Leading Highly Effective UX Teams</h4>

<p id="leading-highly-effective-ux-teams" class="description body-small">

Build and manage a successful user experience team

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-management" />

</svg>

<p class="ux-specialty ux-management">Management</p>

</div>

</div>

</a>

</li>

</ul>

</div>

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Agile,UX Teams,Site Optimization,Collaboration &amp; Teams,UX Leadership &amp; Management,definition,Design Process</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Agile</span>

<a class="ga-article-related-topic" href="/topic/agile/">Agile</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/ux-teams/">UX Teams</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/ux-design-process/">Design Process</a>

</li>

</ul>

</div>

</div>

</div>

</div>