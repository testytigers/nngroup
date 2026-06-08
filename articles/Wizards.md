# Wizards: Definition and Design Recommendations - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">9</span>

<div class="article-header">

<h1 class="article-h1">Wizards: Definition and Design Recommendations</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Raluca Budiu</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/2023-04-portraits-raluca.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/raluca-budiu/">

Raluca Budiu</a></span>

<p class="publication-date">

June 25, 2017

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2017-06-25</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Wizards: Definition and Design Recommendations&amp;body=https://www.nngroup.com/articles/wizards/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/wizards/&amp;title=Wizards: Definition and Design Recommendations&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/wizards/&amp;text=Wizards: Definition and Design Recommendations&amp;via=nngroup" data-share-type="Twitter">

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

</span>A common application-design pattern for inputting information, wizards work well for processes that are performed only occasionally.

</div>

<div class="article-body">

<p>When it comes to inputting data, the two most common patterns used on the web and in applications are forms and wizards. The electronic form is a direct descendant of the paper form: a page with empty fields that the user needs to fill in. The wizard is a minapplication that takes the user through a sequence of forms.</p>

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

<a class="ga-article-toc-item" href="#toc-what-is-a-wizard-1">What Is a Wizard?</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-dynamic-form-or-wizard-2">Dynamic Form or Wizard?</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-wizards-show-less-information-on-the-page-3">Wizards Show Less Information on the Page</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-shortest-path-for-each-user-4">Shortest Path for Each User</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-disadvantages-of-wizards-5">Disadvantages of Wizards</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-recommendations-for-designing-usable-wizards-6">Recommendations for Designing Usable Wizards</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-7">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-what-is-a-wizard-1">What Is a Wizard?</h2>

<p style="margin-left:.5in">Definition: A <strong>wizard</strong> is a step-by-step process that allows users to input information in a prescribed order and in which subsequent steps may depend on information entered in previous ones.</p>

<p>Wizards usually involve multiple pages and are often (but not obligatorily) displayed in <a href="https://www.nngroup.com/articles/modal-nonmodal-dialog/">modal windows</a>. One wizard page typically corresponds to a single step in a multistep process.</p>

<p>As the user enters information, the system computes the appropriate path for that user and routes her accordingly. Wizards thus often have some branching logic behind the scenes, but the perceived user experience is that of a linear flow: one screen after another, and all the user has to do is to click “next.” (Or “back,” or “cancel,” but mainly the user keeps moving forward.)</p>

<p>A classic dilemma in user interface design is whether to allocate control to the user or to the computer. Usually, people feel better when they are in control, but having too much freedom might get the user into trouble and will often cause them to waste time. Wizards allow the computer to control the flow of the dialogue, but this limitation of users’ freedom can be liberating in cases where people don’t care about their choices or don’t know enough to make a decision.</p>

<figure class="caption"><img alt="" height="379" loading="lazy" src="https://media.nngroup.com/media/editor/2017/04/18/turbotax-combined.png" width="700"/>

<figcaption><em>Turbotax: The form (left) is a close replica of the paper tax form, but can be filled in digitally, while the wizard (right) takes users step by step through the process of filling taxes.</em></figcaption>

</figure>

<h2 id="toc-dynamic-form-or-wizard-2">Dynamic Form or Wizard?</h2>

<p>With the prevalence of AJAX technologies, the distinction between form and wizard has become fuzzier. For example, the Fidelity page below asks users whether they are current Fidelity customers, and, depending on their answer, shows <em>on the same page </em>either login fields or name and email information. Is this a form or a wizard? According to our definition, it’s a wizard.</p>

<figure class="caption"><img alt="" height="852" loading="lazy" src="https://media.nngroup.com/media/editor/2017/04/18/fidelity.png" width="400"/>

<figcaption><em>Fidelity.com: The page for opening a Roth IRA account (top) dynamically adds different fields to the form, depending on whether the user is an existing Fidelity customer (middle) or not (bottom). This branching makes the page closer to a wizard than to a form.</em></figcaption>

</figure>

<p>The Microsoft page below also changes the information displayed on the screen as the user enters information — but, in this example, the fields stay the same, while inline error messages or explanations appear as the user progresses. Technically, this page is a form and not a wizard — the steps of the process are not modified by the actions taken by the user, although the form does give dynamic feedback to users as they fill in the different form fields.</p>

<figure class="caption"><img alt="" height="864" loading="lazy" src="https://media.nngroup.com/media/editor/2017/04/18/live.png" width="428"/>

<figcaption><em>Live.com: Create-an-account form dynamically displays inline error messages and field explanations.</em></figcaption>

</figure>

<h2 id="toc-wizards-show-less-information-on-the-page-3">Wizards Show Less Information on the Page</h2>

<p>Because wizards split a complex process into multiple steps, often wizard pages are simpler — they contain fewer fields and overall less information. Page simplicity has several important benefits:</p>

<ul>

<li>Users end up being less overwhelmed by the process. A long form is often daunting and users may overestimate the amount of work involved in filling it.</li>

<li>Less cognitive effort is spent in completing the process. Much of the information in a form may end up being irrelevant, yet people will have to spend attentional resources to scan it and eventually filter it out. With a wizard, the fields displayed depend on users’ previous input and have better chances of actually being important and not just a distraction.</li>

<li>Users make fewer mistakes. With an overly complex form, users may ignore certain parts and be more likely to cause form-submission errors. Or, they may miss something that is relevant for them.</li>

<li>More screen real estate is available for each step. When a complex process is split into simpler steps and each step gets a separate page, there is simply more space for each of the controls in a step. Targets can be bigger and less crowded, information may fit on a single screen (so no scrolling will be necessary), and explanations may be displayed next to the fields.</li>

</ul>

<h2 id="toc-shortest-path-for-each-user-4">Shortest Path for Each User</h2>

<p>For some people the path through the process may be quick and simple, while for others it may be intricate and tedious. If the process is forked depending on users’ inputs and the forking is transparent to the users, then they don’t need to bother with the path that does not apply to them. Thus, in a well-designed wizard, people will only see the steps and the information relevant for their situation.</p>

<p>For example, users who don’t own a credit card need not see the credit-card fields in a checkout form and could focus instead only on the relevant-to-them PayPal fields.</p>

<h2 id="toc-disadvantages-of-wizards-5">Disadvantages of Wizards</h2>

<p>As helpful as wizards are, they are not appropriate for all situations. Here are some common problems associated with wizards:</p>

<p>Compare, for example, the process of typing data into a spreadsheet with multiple columns with that of entering the data field by field in a wizard. The repeated switching between the mouse and the keyboard and the extra attention demanded by a changing display can quickly become tiresome compared with just tabbing through the different columns of the spreadsheet.</p>

<figure class="caption"><img alt="" border="0" height="411" loading="lazy" src="https://media.nngroup.com/media/editor/2017/04/18/latex.png" width="650"/>

<figcaption><em>Microsoft Word: Using a wizard such as Microsoft Word’s Source Manager(top) to enter each reference in a long bibliography list can be a lot more tedious than simply typing it in a table, spreadsheet, or even in text-based typesetting software such as Latex (bottom).</em></figcaption>

</figure>

<figure class="caption"><img alt="" border="0" height="257" loading="lazy" src="https://media.nngroup.com/media/editor/2017/04/18/mint.png" width="600"/>

<figcaption><em>Mint.com: This wizard for determining the best credit card for a user blocked access to the credit score, available in a different area of the application. Luckily our study participant could remember her score without quitting the wizard. (A better design would have skipped this step entirely and would have used the credit-score info already available to the app.)</em></figcaption>

</figure>

<ul>

<li><strong>Wizards can require a higher <a href="https://www.nngroup.com/articles/interaction-cost-definition/">interaction cost</a> (more clicks) than other input patterns</strong>. Especially if wizards need to be invoked repeatedly, the tedium of clicking through each of the steps can overwhelm the advantage of splitting the process into small sections.</li>

<li><strong>Wizards might not allow users to easily transfer or compare information from different steps.</strong> When users see one step at a time, it can be hard to move information across steps or refer to information entered or presented during a previous step. (And, sometimes seeing more steps at a time can give users some additional context to better understand the information requested in each step.)</li>

<li><strong>Wizards are not gracefully interruptible</strong>. If users quit the process midway, they might not only lose their work, but may need to click again through the preceding steps. Even when the wizard supports the saving of the state and resuming of the process at a later date, it can be difficult for users to remember what they were doing and recover their context and the mental model of the process.

<p>(That being said, forms are not gracefully interruptible either — most of the time, the information entered will be lost if the user stops midway, and even in the event when that information is saved, users will still need to recover context.)</p>

</li>

<li>Wizards <strong>may block access to other parts of the app</strong> that are necessary for completing the process. When the wizard is presented in a modal window, it can obstruct information in the background that may be relevant for the current process. Most often, it also prevents users from interacting with other parts of the site.</li>

<li>Wizards <strong>limit the users’ control and creativity</strong>. While it would be appropriate to supply a wizard for amateur photographers to improve the color balance of a photo, it would be too limiting for a professional graphic designer to use a wizard to improve an image.</li>

</ul>

<h2 id="toc-recommendations-for-designing-usable-wizards-6">Recommendations for Designing Usable Wizards</h2>

<ol>

<li><strong>Use wizards for novice users or infrequent processes (e.g., configuration or setup).</strong>

<p>Wizards can help users with little knowledge about a domain by simplifying the processes and by guiding the users. However, as we saw before, wizards can quickly become annoying and overly controlling if they have to be used over and over again or if users have a lot of knowledge of the domain and their <a href="https://www.nngroup.com/articles/mental-models/">mental model</a> of the process is different than the mental model implemented by the app designer.</p>

<p>Basically, use wizards for situations where the users are likely to be unfamiliar with the process — either because they don’t have a lot of domain expertise or because they go through that process only rarely. If you expect that some of your users will perform it repeatedly, consider offering them another faster alternative for inputting their data.</p>

</li>

<li><strong>Communicate a clear mental model of the process </strong>by displaying a list or a diagram of the steps involved and highlighting the current step.

<p>Because the process is presented one step at a time, there is danger that users will miss the context, get confused, or not realize how long the progression will be. It best to set the right expectations and explain to the use what the process looks like and how many steps are involved.</p>

<p>Especially with complicated processes, a clear labeling of each of the steps as well as a clear indicator of the current step can help keep users oriented.</p>

<figure class="caption"><img alt="" border="0" height="429" loading="lazy" src="https://media.nngroup.com/media/editor/2017/04/18/veeam.png" width="600"/>

<figcaption><em>Veeam: In this backup-and-replication software, the steps for creating a new backup job are presented in a list on the side of the wizard window. The next steps are grayed out, and the current step is highlighted. The steps have short, descriptive labels.</em></figcaption>

</figure>

</li>

<li><strong>Enforce a clear sequential order of the steps</strong>. Do not allow users to pick step before completing the steps preceding it.

<p>Although logically it may make no difference if users start with the last step in the process, having a clear ordering minimizes decision making (and sometimes the <a href="https://www.nngroup.com/articles/minimize-cognitive-load/">memory load</a> as well, if the completed steps are not clearly marked and users must remember which steps they’ve already visited) and thus simplifies the interaction.</p>

<p>(If there are substantial benefits to users from being able to complete steps in an arbitrary sequence, then this is an indication that this functionality is not suited to be provided as a wizard.)</p>

<figure class="caption"><img alt="" border="0" height="481" loading="lazy" src="https://media.nngroup.com/media/editor/2017/04/18/miniusa.PNG" width="700"/>

<figcaption><em>Miniusa.com: The steps in this car-configuration process are shown as tabs at the top of the screen. Users can select any of the tabs at any time and the design does not show which steps have been already completed, thus placing an extra memory load and decision-making burden on users.</em></figcaption>

</figure>

</li>

<li><strong>Include buttons for navigating to the next and previous steps and label the steps descriptively</strong>. The general guidelines for button names stand for wizard buttons as well: Generic labels such as <em>Next </em>and <em>Previous </em>have weak information scent and don’t tell users anything about these steps. It’s better to indicate in the label what the user will actually have to do next.

<p>In the Mini example above, the button for the next step is clearly marked with the name of that step. However, there is no explicit button for going back to the previous step. (Users can still do it by selecting the tabs at the top of the page.)</p>

</li>

<li><strong>Allow users to exit the wizard midway and save state. Allow them to resume the process at a later time.</strong>

<p>Interruptions happen, and users should be able to save their work and later continue the process from where they left. They will still incur the cognitive cost of recovering context and remembering their goals, but at least they will not have to reenter the same information.</p>

<p>In the examples above, neither Veeam nor Mint allow users to save their work. One can perhaps argue that the Mint wizard is so simple and short that saving state will only complicate the interface unnecessarily. However, in Veeam’s case, the process is fairly complex and central to the app, so being able to finalize the setup for a new job at a later time is important.</p>

<p>Mini’s wizard includes a <em>Review &amp; Save </em>button that allows users to stop their work at any time and save it in a file that can be retrieved at a later time. Unfortunately, the placement of that button at the top of the page is far from users’ current focus of attention and makes it easy to ignore.</p>

</li>

<li><strong>Wizard steps should be self-sufficient</strong> and not require information available elsewhere in the app (or in a previous step). Make sure that users can easily access all the info that they need as they use the wizard. The Mint example above violates this guideline by requiring users to get their credit scores from elsewhere.

<figure class="caption"><img alt="" border="0" height="437" loading="lazy" src="https://media.nngroup.com/media/editor/2017/04/18/expnsify.PNG" width="650"/>

<figcaption><em>Expensify.com: When the user attempted to add a receipt to an expense, the wizard obscured the expense details. The user had to remember which expense she was entering and for which vendor in order to be able to identify the receipt for that expense.</em></figcaption>

</figure>

</li>

<li><strong>Help and explanations should appear in a window next to the wizard and should not cover the wizard.</strong> Any descriptions of the terms or the fields in the wizard should be viewable next to the wizard and should not cover the fields in the wizard. In this way, users will be able to apply the information in the explanation window to the wizard context.

<figure class="caption"><img alt="" border="0" height="487" loading="lazy" src="https://media.nngroup.com/media/editor/2017/04/18/min-lght.PNG" width="650"/>

<figcaption><em>Miniusa.com: Each of the options that can be added (see previous screenshot) is clickable and opens a <a href="https://www.nngroup.com/articles/overuse-of-overlays/">lightbox</a> with extra information. Unfortunately, the lightbox also covers the content in the background, making it difficult to see the option in context.</em></figcaption>

</figure>

</li>

<li><strong>Consider reusing the user’s selections from previous use as the defaults for the next use of the wizard.</strong> For many tasks, users will benefit if the system remembers their selections and input values from one use of a wizard to the next. The very first time a user employs a wizard, the designer should have chosen appropriate default values, and there are some applications where those standard values should be the default every time.</li>

</ol>

<h2 id="toc-conclusion-7">Conclusion</h2>

<p>Wizards are a powerful design pattern that can be used to simplify complex processes performed infrequently or by novice users. By showing less information at a time, they allow users to focus better on the content pertinent to each step and decrease the chance of errors. When they include branching based on user input, wizards ensure that people will see only the steps applicable to their situation. Some of wizards’ disadvantages can be mitigated by thoughtful design ensuring that the process steps are clearly communicated to the user and they are independent and self-sufficient.</p>

<p>Learn more about wizards in our course <a href="https://www.nngroup.com/courses/application-ux/">Application Design for Web and Desktop</a>.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=wizards&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Design Patterns,Application Design,help and user assistance,Human Computer Interaction,workflow</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Design Patterns</span>

<a class="ga-article-related-topic" href="/topic/design-patterns/">Design Patterns</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/applications/">Application Design</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/human-computer-interaction/">Human Computer Interaction</a>

</li>

</ul>

</div>

</div>

</div>

</div>