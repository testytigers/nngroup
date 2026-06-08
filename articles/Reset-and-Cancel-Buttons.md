# Reset and Cancel Buttons - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">5</span>

<div class="article-header">

<h1 class="article-h1">Reset and Cancel Buttons</h1>

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

April 15, 2000

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2000-04-15</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Reset and Cancel Buttons&amp;body=https://www.nngroup.com/articles/reset-and-cancel-buttons/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/reset-and-cancel-buttons/&amp;title=Reset and Cancel Buttons&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/reset-and-cancel-buttons/&amp;text=Reset and Cancel Buttons&amp;via=nngroup" data-share-type="Twitter">

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

</span>Most Web forms would have improved usability if the Reset button was removed. Cancel buttons are also often of little value on the Web.

</div>

<div class="article-body">

<p>It is one of the most <a class="old" href="http://www.nngroup.com/articles/ten-usability-heuristics/" title="Ten basic principles for Heuristic Evaluation of user interfaces - by Jakob Nielsen"> basic heuristics for interaction design</a> to <strong> support user control and freedom </strong> by allowing users an "emergency exit" out of any situation they may have entered. <strong> Undo </strong> was truly one of the greatest advances in usability.</p>

<p>The basic rule says to support undo; it doesn't say <em>how</em>. More specific rules are needed for different types of user interfaces:</p>

<ul>

<li>In <strong> window-based GUI applications</strong>, it is standard to have a <em> Cancel </em> button that closes any dialog box and discards any changes the user may have made within that dialog box. A great way to support exploratory learning. Compare with older systems where you were trapped if you ever activated the wrong command.</li>

<li>In <strong>editing systems</strong> it is usual to have an <em> Undo </em> command that makes the document revert to the state before the user's most recent changes. Sometimes, multi-level undo and redo is supported: this can be very useful but confusing.</li>

</ul>

<p>The <em> Reset </em> and <em> Cancel </em> buttons are the Web's attempt at mirroring these features, but <strong> users usually prefer to use the <em> Back </em> button instead </strong> when they want to escape from an undesired state.</p>

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

<a class="ga-article-toc-item" href="#toc-reset-dont-use-1">Reset: Don't Use</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-cancel-use-sparingly-2">Cancel: Use Sparingly</a>

</li>

</ul>

</div>

</div><h2 id="toc-reset-dont-use-1"><em>Reset</em>: Don't Use</h2>

<p>The Web would be a happier place if virtually all <em> Reset </em> buttons were removed. This button almost never helps users, but often hurts them.</p>

<p><em>Reset </em> clears away the user's input on a Web form, but why would people want to do that? The Web is characterized by frequent movement between pages and users rarely encounter the same form twice. Thus, a Web form is almost always cleared when the user sees it. Even when a user revisits a form in a single session, it is usually faster to edit the old data than to erase it and start over.</p>

<p>The <em> Reset </em> button <strong> hurts users </strong> in three ways:</p>

<ul>

<li>The worst problem about <em> Reset </em> is that users <strong> click the button by mistake </strong> when they wanted to click <em> Submit</em>. Bang — all your work is gone!</li>

<li>Having two buttons at the bottom of a form clutters up the interface and makes it harder for users to clearly see their next step. Some small amount of wasted time is spent scanning the useless button and deciding which of the two buttons is the correct one.</li>

<li>Even when users do want to eliminate some of the data they have entered into a form, it may slow them down to have a dedicated button for doing so, since the extra button means that users have a choice:

<ul>

<li>edit the erroneous fields and replace the old text with the new text</li>

<li>click <em> Reset </em> and type the new text into nice clean fields</li>

</ul>

The <strong> extra choice requires extra thinking</strong>, and the time saved by using an optimal interaction technique is often smaller than the time wasted on having to think instead of just moving ahead with a single interaction technique that is always used. It takes at least one second and often two seconds to decide between two possible interaction techniques which is why it is usually better not to offer users a choice. (A second may not seem like much, but it translates into about $100 million in lost productivity per year world-wide.)</li>

</ul>

<h3>Make All Form Entries Undoable</h3>

<p>To eliminate the <em> Reset </em> button, it becomes necessary to offer users another escape route for erroneous form entries. In the case of text fields or check boxes, the user can always erase the entry and revert to the original state.</p>

<p>Unfortunately, some Web forms use radio buttons and pull-down menus in a non-standard manner and do not offer a neutral choice. A classic design mistake on the Web is to have radio buttons that initially do not have a selection. Often, there is no way for the user to select a "nothing" option, once he or she has selected one of the choices. <strong> Always include an explicit radio button for the default choice </strong> and always include a selectable menu entry in pull-down menus for the default choice. Otherwise you do trap users. (See also all <a class="old" href="/articles/checkboxes-vs-radio-buttons/" title="Alertbox Sept. 2004: Checkboxes vs. Radio Buttons">13 guidelines for checkboxes and radio buttons</a>.)</p>

<h3>Exception: Use <em> Reset </em> for Repeated Form-Filling and for Revert-to-Default</h3>

<p><em>Reset </em> can be useful for forms that satisfy <em> both </em> of the following criteria:</p>

<ul>

<li>the form is filled-in repeatedly by the same user</li>

<li>the data to be entered differs significantly from one use of the form to the next</li>

</ul>

<p>Even if a user were to use a form frequently, the reset button would still not be necessary if the data was mostly the same from one use to the next. In these cases, it would be easier for the user to <strong> edit the old data </strong> than to erase it and start from scratch.</p>

<p>A <em>Reset </em>button can also be useful in complex dialogs where the user is asked to specify parameters that have good default valules. If the user has wandered far from the defaults during exploration of the parameter space, <em>Reset </em>can offer a quick way home to safe grounds. (Note that here, <em>Reset </em>doesn't really clear things, as much as it replaces changed values with safer or more normal values.)</p>

<h2 id="toc-cancel-use-sparingly-2"><em>Cancel</em>: Use Sparingly</h2>

<p>The Web is not an application environment, and it usually doesn't have dialog boxes. Instead, the Web is a navigation environment where users move between pages of information. Since hypertext navigation is the dominant user behavior, users have learned to rely on the <em> Back </em> button for getting out of unpleasant situations. Whenever users arrive at pages they don't want, they slam their mouse directly onto the <em> Back </em> button.</p>

<p>Because <em> Back </em> is such a strong behavior on the Web, it is usually not necessary to offer explicit <em> Cancel </em> buttons. If the user asks for something but doesn't want it, then you can be sure that it's <em> Back </em> button time.</p>

<p>Offer a <em> Cancel </em> button when users may fear that they have committed to something they want to avoid. Having an explicit way to <em> Cancel </em> provides an extra feeling of safety that is not afforded by simply leaving.</p>

<p><em>Cancel </em> is mainly useful for multi-step dialogs where the user has progressed past one or more pages with actions. At this time, pressing the <em> Back </em> button will not undo these actions and it would be better if the user would click <em> Cancel</em>.</p>

<p>Of course, one cannot rely on having the user click <em> Cancel </em> , even if it is offered, so the back-end logic must be able to handle abandoned multi-step dialogs where the user decided to leave through the use of the <em> Back </em> button. This added complexity is one of the reasons I don't recommend trying to implement advanced applications inside a Web browser. It is better to use another form of Internet-enabled applications.</p>

<h3><em>Remove </em> Button in Shopping Carts</h3>

<p>It is necessary to have a special button in shopping carts for removing a product. Users cannot be assumed to understand that they can cancel a purchase by buying zero copies (even though this technique should be supported as well since it does not interfere with users unless they decide to use it on their own initiative).</p>

<p>(See my report on <a class="old" href="http://www.nngroup.com/reports/ecommerce-ux-shopping-carts-checkout-registration/" title="Nielsen Norman Group report: 32 Design Guidelines for Shopping Carts, Checkout, and Registration"> shopping cart usability</a> for additional guidelines on forms design.)</p>

<h3>Clarification: When Cancel Is Necessary</h3>

<p>Lisa Padol asks:</p>

<blockquote>When you talk about cancel and reset buttons, you do not mean the stop (as in "stop the page from loading") and reset/refresh buttons, correct?

<p>I presume it's not only acceptable, but also required to have a cancel button for things like downloading files?</p>

</blockquote>

<p>She is correct in both assumptions. The browser's <em> Stop </em> button is a great example of a technique to increase the user's control of the dialogue. Same for a way to interrupt file transfers or any other actions that take more than a few seconds. Designers must include such features in any applets or other design elements that can take time.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=reset-and-cancel-buttons&amp;pt=article">

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

<li>

<a class="tile ga-article-related-course" data-course-title="The Human Mind and Usability" href="/courses/human-mind/?lm=reset-and-cancel-buttons&amp;pt=article">

<h4 class="title heading-small">The Human Mind and Usability</h4>

<p id="the-human-mind-and-usability" class="description body-small">

Use psychology to predict and explain how your customers think and act

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

<a class="tile ga-article-related-course" data-course-title="Web Page UX Design" href="/courses/web-page-design/?lm=reset-and-cancel-buttons&amp;pt=article">

<h4 class="title heading-small">Web Page UX Design</h4>

<p id="web-page-ux-design" class="description body-small">

Strategically combine content, visuals, and interactive components to design successful web pages

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">forms,Application Design,Web Usability</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Application Design</span>

<a class="ga-article-related-topic" href="/topic/applications/">Application Design</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/web-usability/">Web Usability</a>

</li>

</ul>

</div>

</div>

</div>

</div>