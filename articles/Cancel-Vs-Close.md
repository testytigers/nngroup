# Cancel vs Close: Design to Distinguish the Difference - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">6</span>

<div class="article-header">

<h1 class="article-h1">Cancel vs Close: Design to Distinguish the Difference</h1>

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

September 1, 2019

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2019-09-01</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Cancel vs Close: Design to Distinguish the Difference&amp;body=https://www.nngroup.com/articles/cancel-vs-close/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/cancel-vs-close/&amp;title=Cancel vs Close: Design to Distinguish the Difference&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/cancel-vs-close/&amp;text=Cancel vs Close: Design to Distinguish the Difference&amp;via=nngroup" data-share-type="Twitter">

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

</span>Distinguishing between these two actions is critical to avoiding losing users’ work. Save changes before closing a view, use text labels rather than an X icon, and provide a confirmation dialog before destructive actions.

</div>

<div class="article-body">

<p>Long ago, the symbol <em>X </em>meant “this is where the treasure is buried.” In today’s digital interfaces, <em>X </em>no longer marks the spot, but rather functions as a way for users to cancel a process or to dismiss an interim screen. How can one tell for sure whether the <em>X </em>means <em>cancel</em> or <em>close</em>? Sometimes, unfortunately, you can’t.</p>

<p>The main issue lies with the common <a href="https://www.nngroup.com/videos/icon-text-labels/">lack of a text label</a> for the <em>X</em> icon. When an icon represents multiple meanings in similar contexts across different interfaces, <a href="https://www.nngroup.com/articles/icon-usability/">icon usability</a> suffers because users cannot rely on any single interpretation.</p>

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

<a class="ga-article-toc-item" href="#toc-avoid-losing-users-work-1">Avoid Losing Users’ Work</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-1-ask-for-confirmation-2">1. Ask for Confirmation</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-2-use-explicit-labels-3">2. Use Explicit Labels</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-3-favor-close-save-4">3. Favor Close &amp; Save</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-5">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-avoid-losing-users-work-1">Avoid Losing Users’ Work</h2>

<p>When users intend to dismiss a modal or view by clicking the <em>X</em> button, but the system instead completely cancels the process and clears all their work, it is disheartening at best, and maddening at worst. Yes, the <em>X</em> icon is commonly recognized by users to mean either to <em>cancel</em> or to <em>close</em>, but <strong>distinguishing between the two possibilities is critical for the success of the interaction</strong>.</p>

<p>In some cases, the distinction between cancel and close doesn’t matter. When a popup takes over the majority of your screen, hitting the <em>X</em> button (as quickly as humanly possible) serves to both close that <a href="https://www.nngroup.com/articles/modal-nonmodal-dialog/">modal</a> and perhaps cancel any process it might have triggered. However, if a screen contains a running timer, is playing audio, holds several selected filter options, or contains some other type of unsaved work, it becomes much more important to correctly interpret what that <em>X</em> icon represents — you may intend to leave that timer or audio running, apply those selected filters, or save your in-progress work, while wanting to close that view to continue some other related activity.</p>

<p>For example, the Sephora checkout process used a modal window to present free samples that users could add to their cart. In the following example, an item had just been selected by clicking the <em>Add</em> button below it; that action caused the <em>Add</em> button to be replaced by a <em>Remove</em> link, which made it look as if the sample had already been added to the cart. However, when the user closed the modal by clicking the <em>X</em> icon rather than <em>Done</em> link, she discovered that the item was not in the cart and that she needed to add it again.</p>

<figure class="caption"><img alt="Sephora website: Screenshot of Choose a trial product modal window" loading="lazy" src="https://media.nngroup.com/media/editor/2019/08/28/sephora-actionsnotsubmitted_xascancel.jpg"/>

<figcaption><em>Sephora: Even though it looked as if the sample had already been added to the cart because it could now be removed, closing the modal (by clicking the </em>X<em> in the top right corner) canceled the process of choosing a trial item. To add the item to their carts, users had to first click </em>Add<em> and then apply that action by clicking the </em>Done<em> link.</em></figcaption>

</figure>

<p><strong>To avoid losing users’ work, systems need to determine the user’s intent — cancel or close — and provide clear options.</strong></p>

<p>This goal can be accomplished by one or more of the following:</p>

<ol>

<li>Asking the user to confirm their intention</li>

<li>Using explicit text labels rather than ambiguous icons</li>

<li>Presenting two distinct buttons: <em>X</em> for closing the view (with the side effect of saving intermediate work) and <em>Cancel</em> for abandoning the process</li>

</ol>

<h2 id="toc-1-ask-for-confirmation-2">1. Ask for Confirmation</h2>

<p>If a user pressed the <em>X</em> icon on a modal or intermediate view where she had already performed an action, the UI could confirm her intention by directly asking whether to apply that action before closing the view. <strong>This solution is ideal for destructive <em>cancel</em> actions</strong> that would lose the user’s work. Here, the old adage that it’s better to beg forgiveness than ask for permission is absolutely not true — always ask for <a href="https://www.nngroup.com/articles/confirmation-dialog/">confirmation before committing destructive actions</a>.</p>

<p>For example, filter views are often accidentally closed, and that action causes users to lose their work. This problem is particularly rampant on mobile interfaces, as filter screens often consume the majority — if not all — of the available screen space, making it difficult or impossible to tell whether selections have already been applied.</p>

<p>To <a href="https://www.nngroup.com/articles/user-mistakes/">guard against potential mistakes</a>, ask users who close a filter view whether they intend to apply the filters and close the view or clear their selections. For instance, the Lowes mobile app showed a confirmation dialog when the user attempted to close the filter screen before applying her selections.</p>

<figure class="caption"><img alt="Lowes mobile app: 2 screenshots of filter screen and confirmation dialog" loading="lazy" src="https://media.nngroup.com/media/editor/2019/08/28/lowes_mobileapp-filter-confirmationdialog.png"/>

<figcaption><em>Lowes mobile app: Tapping either the </em>X<em> button or the </em>Back<em> arrow could reset any selections and take the user back to the previous result set. Right: After tapping </em>X<em>, a confirmation dialog appeared to check whether the user meant to apply or cancel the filter refinements before returning to the results list.</em></figcaption>

</figure>

<p>Similarly, the language-learning app Duolingo showed a confirmation dialog when users attempted to close an in-progress lesson — lessons could not be left partially completed and had to be either finished or cancelled. At least, the app communicated this constraint to users and gave them the option to return to the lesson to maintain progress.</p>

<figure class="caption"><img alt="Duolingo mobile app: Confirmation dialog before leaving lesson" loading="lazy" src="https://media.nngroup.com/media/editor/2019/08/28/duolingo-confirmationdialog.png"/>

<figcaption><em>Duolingo: Clicking the </em>X <em>button would end the current lesson and forfeit any progress. To guard against mistakes, the app included a confirmation dialog.</em></figcaption>

</figure>

<p>While confirmation dialogs are effective in disambiguating the meaning of the <em>X </em>icon, they add extra steps; moreover, users don’t know what the <em>X</em> does before they press it and, therefore, they may worry about the consequence of their action.</p>

<h2 id="toc-2-use-explicit-labels-3">2. Use Explicit Labels</h2>

<p>Rather than relying on confirmation dialogs to catch users before they unwittingly lose all their selections, you can <strong>eliminate the ambiguous <em>X</em> icon in favor of explicit text-labeled buttons</strong>. Text can reduce ambiguity and clearly communicate what action would occur: <em>cancel</em> versus <em>close</em>.</p>

<p>The filter screen of Yelp’s mobile app offered buttons labeled <em>Cancel</em> and <em>Reset</em> at the top of the screen and a single large <em>Apply</em> button at the bottom. Similarly, the filter view in the Etsy mobile app provided separate buttons labeled <em>Clear</em> and <em>Done</em>. (Note: Etsy used <em>Done</em> rather than <em>Apply</em> because the filters were applied as soon as they had been selected, <a href="https://www.nngroup.com/articles/toggle-switch-guidelines/">as is recommended for toggle switches</a>.)</p>

<figure class="caption"><img alt="Screenshots of Yelp mobile app and Etsy mobile app filter screens" loading="lazy" src="https://media.nngroup.com/media/editor/2019/08/28/yelp_etsy-nox-cleartextlabels.png"/>

<figcaption><em>(Left) Yelp mobile app: Text labels for </em>Cancel<em>, </em>Reset<em>, and </em>Apply<em> were direct and clear, making it less likely that users would inadvertently close the view and lose their filter selections. (Right) Etsy mobile app: The text label </em>Clear<em> gave a clear way (pardon the pun) for users to cancel their selections. The </em>Done<em> link returned to the product-listings page, with the selections already applied.</em></figcaption>

</figure>

<h2 id="toc-3-favor-close-save-4">3. Favor Close &amp; Save</h2>

<p>If the <em>X</em> icon must be used rather than text (to save space or because you’re following your organization’s <a href="https://www.nngroup.com/articles/front-end-style-guides/">style guide</a>), err on the side of caution and <strong>save any intermediate work</strong> that has been done. In addition, provide a separate <em>Cancel</em> button, to give users an <a href="https://www.nngroup.com/videos/usability-heuristic-user-control-freedom/">emergency exit out of the process</a> and to disambiguate between the two possible meanings of the <em>X </em>(closing and cancelling).</p>

<p>For example, Gmail automatically saved a draft of a message composed in its <a href="https://www.nngroup.com/articles/modal-nonmodal-dialog/">nonmodal window</a>. This practice allowed users to collapse or close the window when desired, while still saving their progress. Hovering over the <em>X</em> icon in the top right corner of the message window displayed a tooltip confirming that the draft was going to be saved and closed. Cancelling was also still available (using the <em>Delete</em> trash can icon at the bottom of the message window — far from the <em>Save &amp; close</em> option at the top to help prevent mistakes).</p>

<figure class="caption"><img alt="Gmail site: Screenshot showing tooltip for X icon within compose nonmodal window" loading="lazy" src="https://media.nngroup.com/media/editor/2019/08/28/gmail-composemessage-saveandclosetooltip.jpg"/>

<figcaption><em>Gmail: Hover revealed that the </em>X<em> icon was for dismissing the window and not for deleting the draft, allowing users to </em>Save &amp; close<em> the message window without losing work in progress.</em></figcaption>

</figure>

<p>Saving by default can also be a <strong>good solution for long processes or processes that tend to be run in the background,</strong> such as timers. For instance, the Glow Baby mobile app allowed users to browse other areas of the app while a feeding or sleeping timer ran in the background. Because these timers can run for a long period of time (hopefully, a very long time for the sleeping timer!), this functionality let the user accomplish other tasks in the app, like recording a past diaper change or browsing through articles and forums. Tapping the <em>X</em> icon in the timer view simply dismissed the window without canceling the running timer.</p>

<figure class="caption"><img alt="Glow Baby mobile app: 3 screenshots of nursing timer either getting auto saved or presenting a confirmation dialog" loading="lazy" src="https://media.nngroup.com/media/editor/2019/08/28/glowbabyapp-xasdismissbutsave.png"/>

<figcaption><em>Glow Baby: (Left) Tapping the </em>X<em> icon in a running-timer view dismissed the view without canceling the timer, and thus, allowed the user to continue using the app to log other types of events, participate in the community discussions, read articles, and so on. (Middle) The status for the running timer was displayed in a banner at the top of the screen. (Right) Hitting the </em>X<em> while the timer was paused brought up the </em>Discard<em> or </em>Cancel<em> buttons to detect the user’s intention.</em></figcaption>

</figure>

<p>Note that saving intermediate work or maintaining an ongoing process before closing is proactive, but sometimes can be contrary to the user’s intention: If users intend to cancel their selections by clicking the <em>X</em> button, auto applying those selections could be confusing and frustrating. This is why it’s critical to also include a separate <em>Cancel</em> button, to give users an out rather than forcing them to only save and close the view.</p>

<h2 id="toc-conclusion-5">Conclusion</h2>

<p>While the <em>X</em> icon is ambiguous and can often cause usability problems, it’s unlikely that it will disappear from all interfaces any time soon. Designers should be aware of the multiple meanings of the <em>X</em> icon and disambiguate between <em>close</em> and <em>cancel</em>, as well as provide safeguards such as confirmation dialogs or autosaving to avoid losing any users’ work.</p>

<p><strong>Remember, when in doubt, <em>save</em>, then out.</strong></p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Web Page UX Design" href="/courses/web-page-design/?lm=cancel-vs-close&amp;pt=article">

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

<li>

<a class="tile ga-article-related-course" data-course-title="The Human Mind and Usability" href="/courses/human-mind/?lm=cancel-vs-close&amp;pt=article">

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

<a class="tile ga-article-related-course" data-course-title="Visual Design Fundamentals" href="/courses/visual-design/?lm=cancel-vs-close&amp;pt=article">

<h4 class="title heading-small">Visual Design Fundamentals</h4>

<p id="visual-design-fundamentals" class="description body-small">

Create user interfaces using essential principles, techniques, and methods of visual design

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">popups,information scent,ui elements,Web Usability,Design Patterns,back button,icons</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Web Usability</span>

<a class="ga-article-related-topic" href="/topic/web-usability/">Web Usability</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/design-patterns/">Design Patterns</a>

</li>

</ul>

</div>

</div>

</div>

</div>