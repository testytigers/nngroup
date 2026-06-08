# Forms vs. Applications - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">6</span>

<div class="article-header">

<h1 class="article-h1">Forms vs. Applications</h1>

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

September 18, 2005

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2005-09-18</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Forms vs. Applications&amp;body=https://www.nngroup.com/articles/forms-vs-applications/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/forms-vs-applications/&amp;title=Forms vs. Applications&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/forms-vs-applications/&amp;text=Forms vs. Applications&amp;via=nngroup" data-share-type="Twitter">

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

</span>Once an online form goes beyond two screenfulls, it&#x27;s often a sign that the underlying functionality is better supported by an application, which offers a more interactive user experience.

</div>

<div class="article-body">

<p>Forms are rarely the best metaphor for complex interactions with computers. Most big companies, however, have a legacy of paper forms. As a result, their intranets are littered with online forms that attempt to meet needs that are often better served by real applications with a real dialogue flow and more of a full-fledged GUI.</p>

<p>We recently got a call from someone who wanted a usability review of a single intranet form. I usually don't like giving feedback on a single page because the project overhead becomes too large and usability insights tend to be too narrow because you lack the context of, say, a full website or a targeted intranet area. In this case, the request came from within a highly respected company that's been a good client of ours, so we owed them extra service and agreed to take on their form. Good we did, because this single form turned out to be a goldmine of usability issues: our final report contained 27 redesign recommendations.</p>

<p>The form contained 57 interaction elements (e.g., groups of <a class="old" href="/articles/checkboxes-vs-radio-buttons" title="Alertbox: Checkboxes vs. Radio Buttons"> radio buttons</a>, text entry fields, and menus) plus a variety of help links. In total, the form was 3350 pixels tall -- that is, it would scroll across about five screenfulls on a standard monitor (1024x768).</p>

<p>Do you have forms like this on your website or intranet? If so, reconceptualize them as applications. The forms metaphor works best for something simple, like entering shipping and billing addresses on an e-commerce site. Even this data is really an element in a bigger workflow consisting of the shopping cart and checkout process that stretches across multiple steps and has <a class="old" href="http://www.nngroup.com/reports/ecommerce/checkout.html" title="Nielsen Norman Group report: Design Guidelines for Shopping Carts, Checkout, and Registration in E-commerce User Experience"> thirty-two documented usability guidelines</a>.</p>

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

<a class="ga-article-toc-item" href="#toc-when-to-use-a-form-1">When to Use a Form</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-application-benefits-2">Application Benefits</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-application-downsides-3">Application Downsides</a>

</li>

</ul>

</div>

</div><h2 id="toc-when-to-use-a-form-1">When to Use a Form</h2>

<p>Forms work when there's not much to <em> do </em> beyond plain data entry. Just stack up the text boxes and have the user type away mindlessly. A few decision points might be acceptable, such as the traditional question as to whether shipping and billing addresses are the same or different. Even here, a small amount of interactivity improves usability. You might, for example, gray out the billing address area unless the user unchecks the box for "billing address is the same as the shipping address."</p>

<p>Interactions that are more complicated suffer when you present them as straight forms. The following criteria can help you decide whether to present a form or a more interactive design:</p>

<ul>

<li><strong>Complexity of requested information. </strong> If the data request is a no-brainer that people can supply without further ado, use a form. If users need to think and/or refer to supporting materials, use an application (and provide features for accessing the supporting materials).</li>

<li><strong>Number of steps. </strong> If the steps are few, use a form. If they are many, structure them into a natural workflow split across multiple steps.</li>

<li><strong>Conditional areas. </strong> If all questions and options are always the same, use a form. If the users' subsequent entries depend on their actions in previous steps, use an application and present only the options relevant for each step.</li>

<li><strong>Linearity. </strong> Conditional areas are one example of non-linearity, but there are others. If users clearly proceed in a linear sequence and never need to revisit or revise previous steps, use a form. If steps don't depend on each other, use a form. If users need to jump between steps or complete steps in an unpredictable sequence, use an application.</li>

</ul>

<p>Note that the <strong> sheer length of a form </strong> is not a sufficient reason to break it up. Yes, it's best to stick to one or two screenfulls: If a form takes up many screens, you should seriously consider <a class="old" href="/articles/keep-online-surveys-short" title="Alertbox: Keep Online Surveys Short"> eliminating some of the questions and options</a>. Otherwise, you're likely to overwhelm users and reduce your conversion rate. But, if all elements are truly needed, you can certainly place them on one long page -- just ensure that each element is easy and that all users have to do is keep scrolling (and sighing) as they complete each step in the long march to the blessed submit button.</p>

<h2 id="toc-application-benefits-2">Application Benefits</h2>

<p>In the long run, I believe we'll see more stand-alone Internet applications with optimized UIs for handling certain types of tasks and data. The Napster subscription manager, the iTunes music store, and Google Earth are current examples of this trend. Once Windows Vista becomes commonly used, most Internet functionality will likely offer its features to give downloaded code the same look-and-feel as native code (XAML/Avalon). This, of course, will take years. (The usual recommendation is to <a class="old" href="/articles/the-increasing-conservatism-of-web-users" title="Alertbox: The Increasing Conservatism of Web Users"> wait at least two years</a> after a technology's release before using it on your website.)</p>

<p>For now, though, what I call "applications" don't necessarily have to be something downloaded as a stand-alone binary or implemented in the current generation of pre-Vista Internet programming languages like Flash or JavaScript. The type of user tasks I'm referring to here mainly need ephemeral applications that can be implemented as a set of Web pages where all or most of the programming lives on the server.</p>

<p>Even when applications are simply sets of pages embedded within larger websites or intranets, they differ from forms in that they have <strong> programmable logic and workflow</strong>. Compared to forms, applications have the following potential advantages:</p>

<ul>

<li><strong>Focus. </strong> By breaking up the workflow into multiple steps, users can focus on one topic at a time. They're thus potentially less distracted and overwhelmed by other screen elements competing for their attention. For this to be a benefit, you obviously have to modularize the application in ways that make sense to users and minimize the need to refer to information contained in other areas.</li>

<li style="margin-top: 1ex"><strong>In-context help. </strong> Because you have fewer items on the screen, you can afford to clearly explain each one. You can supplement buttons and menus with text and examples that illustrate their proper use. Having this information on the main screen is preferable because users dislike going off to separate help screens. When you can't avoid a help screen, applications let you at least make it more helpful by relating the help text to the current step of the user's workflow.</li>

<li style="margin-top: 1ex"><strong>Avoiding scrunched screen elements. </strong> A second advantage of having fewer items on each screen is that your layout is less burdened by space constraints. For example, you can <a class="old" href="/articles/drop-down-menus-use-sparingly" title="Alertbox: Drop-Down Menus - Use Sparingly"> avoid drop-down menus</a> and tiny scrolling list boxes. Instead, present lists of selectable items in a more expansive menu where all items are visible simultaneously. This makes selection faster and less error-prone.</li>

<li style="margin-top: 1ex"><strong>Eliminating irrelevant steps. </strong> Users never need to see questions and options that don't apply to them. If, for example, your business logic requires you to know whether customers are married, don't show single customers questions relating to the spouses they don't have. Forms get both longer and more complicated when users have to read instructions like <em> "If you answered "yes" to Question 25, then complete Question 26. Otherwise skip to Question 27." </em></li>

<li style="margin-top: 1ex"><strong>Flexible workflow. </strong> With applications, you can let users work on different parts of the problem in a sequence that makes sense to them. You can also let them refer to supporting data sources in this process. If an accounts payable application needs a vendor number to process a payment, for example, you can fire up a search interface so users can locate vendors by name and automatically transfer the numbers and any additional information from one application to the other. (Generally, if you're observing users during <a class="old" href="/articles/field-studies-done-right-fast-and-observational" title="Alertbox: Field Studies Done Right - Fast and Observational"> field studies</a> and see them write down information from one screen on a note pad, only to retype it on another screen, you've identified an opportunity to improve productivity and reduce errors by automating the data transfer.)</li>

<li style="margin-top: 1ex"><strong>Providing feedback. </strong> Take advantage of programmability and restate users' actions and choices to confirm how the computer will interpret them. For example, if users must enter a vendor number, give them feedback by stating the vendor's name. This will drastically reduce errors from mistyped vendor numbers.</li>

<li style="margin-top: 1ex"><strong>Customizability. </strong> If an application will be used repeatedly, you can let users add shortcuts for common actions. For example, an expense reporting application might require users to enter driving distances to get reimbursement for personal automobile use. If an employee often travels the same routes (say, to the airport or an important customer site), the application could provide one-click access to frequently used distances and list them by name (say, "office to JFK").</li>

<li style="margin-top: 1ex"><strong>Interaction elements beyond boxes and buttons. </strong> Applications let you employ all the GUI innovations, from using slides to asking users to mark areas of interest on an image.</li>

</ul>

<h2 id="toc-application-downsides-3">Application Downsides</h2>

<p>Applications have two serious drawbacks. First, they involve programming and technology, with the associated cost and risk of <strong> bugs.</strong> Only develop code if you can afford to debug it to a very high quality level, or you'll hurt users more than you help them.</p>

<p>Second, applications require users to <strong> understand new commands </strong> in an environment where not everything is visible at once. If done poorly, these two issues can drastically reduce usability compared to a one-page form in which the actions are simple (scrolling) and nothing is hidden (though scrolling may be required to expose below-the-fold elements). In our <a class="old" href="/articles/ephemeral-web-based-applications" title="Alertbox: Flash and Web-Based Applications"> testing of 46 Web-based applications</a>, one of the most serious problems was users' lack of up-front understanding of each application's task structure and basic goals.</p>

<p>A resulting guideline is to <strong> start with a brief overview of the application</strong>, its workflow, and the expected outcome. This, of course, adds overhead and is thus an additional downside of ephemeral applications on websites and intranets. On balance, though, many user tasks are sufficiently complex that usability is enhanced when you abandon the old forms metaphor and give users the support of an interactive UI.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=forms-vs-applications&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Application Design,forms</span>

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