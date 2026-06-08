# Progressive Disclosure - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">6</span>

<div class="article-header">

<h1 class="article-h1">Progressive Disclosure</h1>

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

December 3, 2006

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2006-12-03</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Progressive Disclosure&amp;body=https://www.nngroup.com/articles/progressive-disclosure/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/progressive-disclosure/&amp;title=Progressive Disclosure&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/progressive-disclosure/&amp;text=Progressive Disclosure&amp;via=nngroup" data-share-type="Twitter">

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

</span>Progressive disclosure defers advanced or rarely used features to a secondary screen, making applications easier to learn and less error-prone.

</div>

<div class="article-body">

<p>Interaction designers face a dilemma:</p>

<ul>

<li>Users want <strong>power</strong>, features, and enough options to handle all of their special needs. <em>(Everybody </em> is a special case somehow. For example: Who wants line numbers in a word processor? Millions of users, that's who, including most big law firms.)</li>

<li>Users want <strong>simplicity</strong>; they don't have time learn a profusion of features in enough depth to select the few that are optimal for their needs.</li>

</ul>

<p>Progressive disclosure is one of the best ways to satisfy both of these conflicting requirements. It's a simple, yet powerful idea:</p>

<ol>

<li>Initially, show users <strong>only a few</strong> of the most important options.</li>

<li>Offer a <strong>larger set</strong> of specialized options upon request. Disclose these secondary features only if a user asks for them, meaning that most users can proceed with their tasks without worrying about this added complexity.</li>

</ol>

<p>The <strong>print dialog box</strong> is the classic example of progressive disclosure. When you issue the command to print a document, you'll get a dialog box with a small set of choices — mainly, how many copies to print, but possibly a few other variations, such as whether to print the entire document or a subset, and which printer to use. Sadly, print dialog boxes have grown bloated over the past decade, and some applications offer an initial dialog box with highly detailed options that would be better placed in a secondary dialog box.</p>

<p>The initial print dialog box typically contains one or more buttons for advanced options. These buttons lead to secondary dialogs that let users specify rarely used settings, such as scaling and printing the pages in reverse sequence. If the user clicks the advanced options button, the system discloses the additional features.</p>

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

<a class="ga-article-toc-item" href="#toc-applications-vs-websites-1">Applications vs. Websites</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-benefits-of-progressive-disclosure-2">Benefits of Progressive Disclosure</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-usability-criteria-for-progressive-disclosure-3">Usability Criteria for Progressive Disclosure</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-staged-disclosure-one-step-at-a-time-4">Staged Disclosure: One Step at a Time</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-managing-complexity-5">Managing Complexity</a>

</li>

</ul>

</div>

</div><h2 id="toc-applications-vs-websites-1">Applications vs. Websites</h2>

<p>Progressive disclosure has long been one of <a class="new" href="https://www.nngroup.com/courses/topic/applications/" title="UX Conference courses on Application Design"> application design's primary guidelines</a>, because most applications have so many commands, features, and options that it makes sense to defer some to a secondary area. Websites have grown so complex that <a href="https://www.nngroup.com/articles/accordions-complex-content/">progressive disclosure is a good idea for many information-rich sites</a> as well. <a href="https://www.nngroup.com/articles/defer-secondary-content-for-mobile/" title="Alertbox: Defer Secondary Content When Writing for Mobile Users">Deferring secondary material is also a key guideline for mobile design</a>.</p>

<p>An ecommerce site, for example, might mention a few key product attributes on the primary <a class="old" href="https://www.nngroup.com/reports/ecommerce-ux-product-pages-including-reviews/" title="Nielsen Norman Group report with design guidelines for ecommerce websites"> product page</a> and let users click through to a secondary page to see the product's full specifications.</p>

<p><strong>Hypertext</strong> provides a simple implementation of progressive disclosure: higher-level pages contain higher-level concepts and simplified descriptions, and lower-level pages fill in the details for those users who want to know everything.</p>

<h2 id="toc-benefits-of-progressive-disclosure-2">Benefits of Progressive Disclosure</h2>

<p>In a system designed with progressive disclosure, the very fact that something appears on the initial display tells users that it's <strong>important</strong>.</p>

<p>For <strong>novice users</strong>, this helps prioritize their attention so that they spend time only on features that are most likely to be useful to them. By hiding the advanced settings, progressive disclosure helps novice users avoid mistakes and saves them the time they would have spent contemplating features that they don't need.</p>

<p>For <strong>advanced users</strong>, the smaller initial display also saves them time because they avoid having to scan past a large list of features they rarely use.</p>

<p>Progressive disclosure thus improves 3 of <a class="old" href="https://www.nngroup.com/articles/usability-101-introduction-to-usability/" title="Alertbox: Usability 101 - Definition and Introduction to Usability"> usability's 5 components</a>: learnability, efficiency of use, and error rate.</p>

<p>You might assume that by initially focusing users' attention on a few core features, they might build a limiting mental model of the system and thus be unable to understand all of their options. <a class="new" href="https://www.nngroup.com/articles/training-wheels-user-interface/" title="Alertbox sidebar: Training Wheels User Interface"> Research says that these are groundless worries</a>: people understand a system <em> better </em> when you help them prioritize features and spend more time on the most important ones.</p>

<h2 id="toc-usability-criteria-for-progressive-disclosure-3">Usability Criteria for Progressive Disclosure</h2>

<p>Simple as the concept may seem, there are <strong>two things you must get right</strong> when designing for progressive disclosure:</p>

<ul>

<li>You must get the right <strong>split between initial and secondary features</strong>. You have to disclose everything that users frequently need up front, so that they have to progress to the secondary display only on rare occasions. Conversely, the primary list can't contain too many options or you'll fail to sufficiently focus users' attention on truly important issues. Finally, the initial display can't contain confusing features or you'll slow down user performance.</li>

<li>It must be <strong>obvious how users progress</strong> from the primary to the secondary disclosure levels:

<ul>

<li>First, make the <strong>mechanics</strong> of this operation simple. For a website, follow the guidelines for <a class="old" href="https://www.nngroup.com/articles/guidelines-for-visualizing-links/" title="Alertbox: Guidelines for Visualizing Links"> visualizing links</a>. For an application, place the advanced features button in a clearly visible spot.</li>

<li>Second, label the button or link in a way that sets clear <strong>expectations</strong> for what users will find when they progress to the next level. (In other words, the progression should have strong <a class="old" href="https://www.nngroup.com/articles/information-foraging/" title="Alertbox: Information Foraging - Why Google Makes People Leave Your Site Faster"> information scent</a>.)</li>

</ul>

</li>

</ul>

<p>Regarding the first point, how do you <strong>determine which features the initial disclosure level should contain?</strong> Task analysis and field studies can give you insights into what people need, even if you're working on a new design. If you're improving an existing system, frequency-of-use statistics can help you prioritize the features. For a website, <a href="https://www.nngroup.com/courses/analytics-and-user-experience/" title="Nielsen Norman Group training course: Analytics and User Experience">basic analytics</a> tell you how often people look at various pages. However, you must supplement such analytics with <a href="https://www.nngroup.com/reports/topic/user-testing/" title="How to do User Testing, Nielsen Norman Group reports">observational usability testing</a> to discern whether a page gets many hits because users <em> want </em> it or because they simply enter the page by <em> mistake</em>. For an application, you can get even more detailed usage data by instrumenting the code to record how often people use various features.</p>

<p>In theory, there's no reason why you can't have <strong>multiple levels of progressive disclosure</strong>. Even though the secondary level is for experienced users, there are still limits to how complex it should be; some options might be so specialized or rare that you should relegate them to a tertiary level. In practice, designs that go beyond 2 disclosure levels typically have low usability because users often get lost when moving between the levels.</p>

<p>If you have so many features that you need 3 or more levels, consider <a href="https://www.nngroup.com/articles/simplicity-vs-choice/" title="Alertbox: Simplicity Wins over Abundance of Choice">simplifying your design</a>. If you can't scale back the complexity, at least chunk your advanced features into groups that make sense, so that users need check only one place and can ignore any areas that they don't need. Use traditional techniques like <a class="old" href="https://www.nngroup.com/articles/card-sorting-how-many-users-to-test/" title="Alertbox: Card Sorting - How Many Users to Test With"> card sorting</a> to get the grouping right, and invest extra time in <a href="https://www.nngroup.com/articles/usability-101-introduction-to-usability/" title="Alertbox: Usability Testing 101">user testing</a> to ensure that your design supports real task performance, including both common tasks and advanced tasks.</p>

<p>It's also possible to have <strong>multiple secondary displays</strong>, each of which is revealed by a different control on the initial display. The obvious upside to this is that you can accommodate more features without introducing a tertiary level. The obvious downside is added complexity on the initial level, since users must consider multiple buttons for advanced options.</p>

<p>Because progressive disclosure's goal is to expedite use of the initial display, it's rarely a good idea to offer multiple ways to progress to secondary options. If you must do this, however, at least ensure that you clearly label all choices.</p>

<h2 id="toc-staged-disclosure-one-step-at-a-time-4">Staged Disclosure: One Step at a Time</h2>

<p>Staged disclosure is a variant in which users step through a linear sequence of options, with a subset displayed at each step. <strong><a href="https://www.nngroup.com/articles/wizards/">Wizards</a> </strong> are the classic example of staged disclosure. The differences between progressive disclosure and staged disclosure are:</p>

<table align="center" cellspacing="0" style="border-collapse:collapse; border-style:solid; border-width:1px; padding:1ex">

<colgroup>

</colgroup>

<tbody>

<tr>

<th style="border-style: solid; border-width: 1px; padding: 0.3ex; text-align: left"> </th>

<th style="border-style: solid; border-width: 1px; padding: 0.3ex; text-align: left">Progressive Disclosure</th>

<th style="border-style: solid; border-width: 1px; padding: 0.3ex; text-align: left">Staged Disclosure</th>

</tr>

<tr>

<td style="border-style:solid; border-width:1px; padding:0.3ex; text-align:left">Initial display</td>

<td style="border-style:solid; border-width:1px; padding:0.3ex; text-align:left"><strong>Core</strong> features</td>

<td style="border-style:solid; border-width:1px; padding:0.3ex; text-align:left">Features that users access <strong>first </strong> in the task sequence</td>

</tr>

<tr>

<td style="border-style:solid; border-width:1px; padding:0.3ex; text-align:left">Subsequent display(s)</td>

<td style="border-style:solid; border-width:1px; padding:0.3ex; text-align:left"><strong>Secondary</strong> features</td>

<td style="border-style:solid; border-width:1px; padding:0.3ex; text-align:left">Features that users access <strong>later </strong> in the task, even if these features are equally important (or more important)</td>

</tr>

<tr>

<td style="border-style:solid; border-width:1px; padding:0.3ex; text-align:left">Do users access subsequent displays?</td>

<td style="border-style:solid; border-width:1px; padding:0.3ex; text-align:left"><strong>Usually not</strong> — most users get what they need on the initial display</td>

<td style="border-style:solid; border-width:1px; padding:0.3ex; text-align:left"><strong>Yes</strong> — unless users stop the task before completing the sequence</td>

</tr>

<tr>

<td style="border-style:solid; border-width:1px; padding:0.3ex; text-align:left">Navigation between displays</td>

<td style="border-style:solid; border-width:1px; padding:0.3ex; text-align:left"><strong>Hierarchical</strong>: users start at the initial display and, if necessary, move to the secondary display and then (often) return to the initial display</td>

<td style="border-style:solid; border-width:1px; padding:0.3ex; text-align:left"><strong>Linear</strong>: users progress through the task one step at a time</td>

</tr>

<tr>

<td style="border-style:solid; border-width:1px; padding:0.3ex; text-align:left">Main usability benefit</td>

<td style="border-style:solid; border-width:1px; padding:0.3ex; text-align:left"><strong>Learnability</strong>: novice users are focused on the most useful features and confusingly advanced features are hidden</td>

<td style="border-style:solid; border-width:1px; padding:0.3ex; text-align:left"><strong>Simplicity</strong>: each step is simple and its purpose is clear because features that belong to other steps are hidden</td>

</tr>

</tbody>

</table>

<p>Staged disclosure is <strong>useful</strong> when you can divide a task into distinct steps that have little interaction. It is <strong>problematic </strong> when the steps are interdependent and users must alternate between them.</p>

<p>When researching the usability of <a class="old" href="https://www.nngroup.com/articles/ephemeral-web-based-applications/" title="Alertbox: Flash and Web-Based Applications"> 46 web-based applications</a>, we tested a hotel reservation system that squeezed all the reservation stages onto a single screen. Comparing this design with most hotel sites — which distribute the reservation stages over multiple pages — shows the benefits and drawbacks of staged disclosure:</p>

<ul>

<li>The single-screen design worked well when users were trying to decide which hotel room to get because it displayed, on a single screen, the availability and prices for different hotel room categories across various date options considered by the user. Most hotel sites show room categories, prices, dates, and availability across multiple pages, making it more difficult to experiment with various what-if scenarios. People use all of these features together, with frequent back-and-forth modifications, so they should be on 1 screen.</li>

<li>The single-screen design also caused usability problems because it included a segment for users to enter their address and credit card information. Hotels need such information to complete a booking, but it's not needed during the exploratory phase when users are experimenting with various reservations. Staged disclosure would defer the payment details to a secondary screen. Doing so would leave more space on the first screen for room information and the exploratory interface, thus protecting users from various errors that result when too many options are displayed at the same time.</li>

</ul>

<p>As this example shows, staged disclosure requires a thorough task analysis to understand which options are used together and which are better thought of as separate stages. The more features you can defer, the simpler your design, but if you divide the task into too many steps, users get bogged down by excess navigation.</p>

<p>The single-screen hotel reservation design would have been better as a 2-screen design — something overlooked by many naïve analyses that consider 1 screen vs. 5 screens to be the only choices. Testing the 1-screen design with real users (which the hotels don't seem to have done) quickly shows that the compromise of a 2-screen solution would be better.</p>

<h2 id="toc-managing-complexity-5">Managing Complexity</h2>

<p>Progressive disclosure and staged disclosure are both strategies to manage the <a class="old" href="https://www.nngroup.com/articles/feature-richness-and-user-engagement/" title="Alertbox: Feature Richness and User Engagement"> profusion of features</a> and options in modern user interfaces. They are both more than 30 years old and have proven themselves useful in countless applications, and even some websites. Try them — but stay aware of their weaknesses.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=progressive-disclosure&amp;pt=article">

<h4 class="title heading-small">Application Design for Web and Desktop</h4>

<p id="application-design-for-web-and-desktop" class="description body-small">

Components, design patterns, workflows, and ways of interacting with complex data

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Application Design,Interaction Design,accordions,forms,interfaces</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Application Design</span>

<a class="ga-article-related-topic" href="/topic/applications/">Application Design</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/interaction-design/">Interaction Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>