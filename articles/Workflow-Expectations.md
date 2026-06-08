# Workflow Expectations: Presenting Steps at the Right Time - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">4</span>

<div class="article-header">

<h1 class="article-h1">Workflow Expectations: Presenting Steps at the Right Time</h1>

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

April 25, 2011

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2011-04-25</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Workflow Expectations: Presenting Steps at the Right Time&amp;body=https://www.nngroup.com/articles/workflow-expectations/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/workflow-expectations/&amp;title=Workflow Expectations: Presenting Steps at the Right Time&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/workflow-expectations/&amp;text=Workflow Expectations: Presenting Steps at the Right Time&amp;via=nngroup" data-share-type="Twitter">

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

</span>Actions at one step of an application impact subsequent steps. When users don&#x27;t understand this relationship, usability suffers.

</div>

<div class="article-body">

<p>When we designed our full-day <a href="http://www.nngroup.com/courses/application-ux/" title="Application Design for Web and Desktop: Principles of application design, with an analysis of GUI screen components, workflows and varying types of users - full-day UX course by Nielsen Norman Group">course on application design</a>, we partitioned the topic into 2 parts: screen components and<span class="new"> workflow</span>.</p>

<p>The first topic is easy to understand: it covers everything from individual controls, such as <a class="old" href="/articles/checkboxes-vs-radio-buttons/" title="Alertbox: Checkboxes vs. Radio Buttons"> radio buttons and checkboxes</a>, to more complex composites of widgets, such as <a class="old" href="/articles/forms-vs-applications/" title="Alertbox: Forms vs. Applications"> forms design</a>, to the <a class="old" href="/articles/closeness-of-actions-and-objects-gui/" title="Alertbox: Closeness of Actions and Objects in GUI Design"> layout of these controls</a>. All very <strong> tangible</strong>.</p>

<p>Workflow is much more <strong> abstract</strong>, but actually more important for the application's ultimate success. We're no longer talking about visible stuff on the screen, but rather about user movements among various features. Workflow theory ranges from simple concepts, such as <a class="old" href="/articles/progressive-disclosure/" title="Alertbox: Progressive Disclosure"> progressive disclosure</a>, to thorny ideas, such as inductive vs. deductive interfaces.</p>

<p>To illustrate the importance of workflow design, I'll offer several concrete examples from recent user testing in varied domains. As the examples illustrate, effective workflow design builds on a simple principle: <strong> Have things happen when users expect them </strong> — either because of their <strong> existing expectations </strong> or because you've clearly communicated what to expect. (The former is obviously better; <strong> instructions automatically degrade the user experience </strong> by diverting users' attention from their main task.)</p>

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

<a class="ga-article-toc-item" href="#toc-premature-requests-asking-users-before-theyre-ready-1">Premature Requests: Asking Users Before They're Ready</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-questions-that-only-make-sense-later-2">Questions That Only Make Sense Later</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-better-workflow-more-use-3">Better Workflow = More Use</a>

</li>

</ul>

</div>

</div><h2 id="toc-premature-requests-asking-users-before-theyre-ready-1">Premature Requests: Asking Users Before They're Ready</h2>

<p>Lately, I've been sitting through many usability tests of iPad apps. After installing a new app, the first thing users typically see is a message in a dialog box: <em> [This App] would like to send you push notifications</em>. This message followed by two buttons: <em> Don't Allow </em> and <em> OK</em>.</p>

<p>Uniformly, users press <em> Don't Allow</em>.</p>

<p><strong>People get enough junk </strong> already. After years of Web usage, people are extraordinarily weary of companies spamming them with "selected offers."</p>

<p>In addition to engendering dramatically stronger customer loyalty by reminding them to use the iPad app, push notifications often provide helpful information that users might appreciate. So why would they refuse good stuff that could enhance the value of having a tablet?</p>

<p>Because the <strong> opt-in prompt appeared at the wrong stage </strong> of the workflow: it was grossly <strong> premature</strong>.</p>

<p>The prompt appears when users open the newly installed app — which is, by definition, <em> before </em> they've actually experienced the application and understood its value. At this early stage, users have a very <strong> low level of commitment </strong> to the app. <a href="http://www.nngroup.com/articles/reciprocity-principle/" title="The Reciprocity Principle: Give Before You Take in Web Design, article">You can't ask them for much, because they don't think much of you yet</a>.</p>

<p>Our <a class="old" href="/articles/mobile-apps-initial-use/" title="Alertbox: iPhone Apps Need Low Starting Hurdles"> user research with mobile apps</a> has shown that they're often <strong> intermittent-use applications</strong>. People download many more apps than they actually use with any frequency. And users know this; they're not going to let an app impose an eternal burden on them when an <em> a priori </em> assessment shows that it'll likely be one of the many apps that they don't really use.</p>

<p>(Yes, it's possible to turn off push notifications later, but most users either don't know how to change system settings or don't want to bother.)</p>

<p>So, a much more fruitful approach is to <strong> first build up some credibility </strong> capital with users by offering a useful service. Once users have grown to really like you and know they'd actually benefit from updates, you can ask them to opt-in for push notifications.</p>

<p>Another example along these same lines: For many years, it's been a key <a class="new" href="http://www.nngroup.com/reports/ecommerce-ux-shopping-carts-checkout-registration/" title="Nielsen Norman Group report: E-commerce User Experience - design guidelines for Shopping Carts, Checkout, and Registration"> guideline for e-commerce checkout</a> to let customers make purchases as "guests" rather than requiring them to become registered users of the site. When making an initial purchase, people aren't yet sufficiently committed to a company to accept the hassle of registering. (Later, after a few purchases, they'll probably register if appropriately prompted to do so.)</p>

<p>Final example: in our <a class="new" href="http://www.nngroup.com/topic/b2b-websites/" title="Nielsen Norman Group report: Business-to-Business Usability"> testing of B2B sites</a>, business professionals usually rebel when a site attempts to collect lead information too early in the sales process — before the (prospective) customer has decided to admit the vendor to the shortlist. Premature request = no leads at all, as users proceed to more welcoming sites.</p>

<h2 id="toc-questions-that-only-make-sense-later-2">Questions That Only Make Sense Later</h2>

<p>In <a class="new" href="http://www.nngroup.com/courses/social-features/" title="Nielsen Norman Group full day seminar: Designing Usable Social Features"> testing social media features</a>, we frequently see sites asking new users for personal information without explaining how it will be used. For example, people are asked to create a screen name when they register. Some users don't realize that this name will be shown next to all of their future postings. Even worse, many sites make it impossible to edit screen names at a later date, when the user's approach to the site has changed.</p>

<p>Knowing that the name would be widely displayed and not just used as a login credential would prevent people from being stuck with unfortunate names like SuperStud on a professional site.</p>

<p>There's a fairly easy fix here: simply explain to users how each piece of information will be used. You might, for example, show them a sample of how their profile and postings will look, and let users edit their entries before committing to register. (Of course, any such instructional text should be concise and thoroughly tested, as we know users allocate minimal attention to instructions.)</p>

<p>Many Web-based applications are <a class="old" href="/articles/ephemeral-web-based-applications/" title="Alertbox: Ephemeral Web-Based Applications"> ephemeral applications</a>, meaning that users view them as low-commitment <strong> transient encounters</strong>: a quick in/quick out of something they've never seen before and might never see again.</p>

<p>In this environment, we frequently observe usability problems caused by users' weak <a class="old" href="/articles/mental-models/" title="Alertbox: Mental Models"> mental models</a> of the application workflow. People don't know what's coming later, and they often don't even understand the application's purpose. It's thus hard for them to correctly answer early questions and they have little motivation to slog through set-up features.</p>

<p>One obvious answer to these problems is to reduce the set-up burden and enhance the usability of the early-use phase. Think of a gently sloping on-ramp rather than a wall that users have to climb.</p>

<p>Even the best designs can't create perfect usability where everybody understands everything without any effort whatsoever. The goal is to set the stage for users to understand the workflow, without slowing them down. Clearly, this is one of the toughest challenges in online communications.</p>

<h2 id="toc-better-workflow-more-use-3">Better Workflow = More Use</h2>

<p>As the examples here illustrate, the user experience is strongly impacted not just by what's on the screen at any given time, but also by how the current screen relates to future states. It's also impacted by how the current screen relates to past screens; here, the general guideline is to reduce the need for users to rely on their <a class="old" href="/articles/short-term-memory-and-web-usability/" title="Alertbox: Short-Term Memory and Web Usability"> fallible memories</a>.</p>

<p>Thus, one reason to care about workflow is simply that usability is enhanced when you consider the totality of the user experience and not just stand-alone screens.</p>

<p>But there's also a more business-oriented argument for improving workflow usability: users can often overcome isolated usability problems, but a broken workflow is much harder for them to fix. Among the typical consequences of bad workflow design are</p>

<ul>

<li><strong>undiscovered errors </strong> that occur when users don't relate what happened on screen A with a (much-later) screen B;</li>

<li><strong>abandonment</strong>, where users simply give up on something they don't understand; and</li>

<li><strong>frustration</strong>, which arises when an awkward process takes much more time than it should. (Individual design elements can also delay users, but a poor workflow takes considerably longer to complete.)</li>

</ul>

<p>The bottom-line outcome of all three? People stop using your application. Conversely, if the process flows smoothly and users feel in control through all the steps, they're much more likely to come back.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=workflow-expectations&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">workflow,Application Design</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Application Design</span>

<a class="ga-article-related-topic" href="/topic/applications/">Application Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>