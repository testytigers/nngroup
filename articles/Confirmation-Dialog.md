# Confirmation Dialogs Can Prevent User Errors (If Not Overused) - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">6</span>

<div class="article-header">

<h1 class="article-h1">Confirmation Dialogs Can Prevent User Errors — If Not Overused</h1>

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

February 18, 2018

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2018-02-18</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Confirmation Dialogs Can Prevent User Errors — If Not Overused&amp;body=https://www.nngroup.com/articles/confirmation-dialog/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/confirmation-dialog/&amp;title=Confirmation Dialogs Can Prevent User Errors — If Not Overused&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/confirmation-dialog/&amp;text=Confirmation Dialogs Can Prevent User Errors — If Not Overused&amp;via=nngroup" data-share-type="Twitter">

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

</span>8 UX guidelines to avoid many serious user errors reduce the risk that people automatically agree to a warning without realizing the consequences.

</div>

<div class="article-body">

<p>Errors are a big deal for UX. They represent one of the <a href="https://www.nngroup.com/articles/usability-101-introduction-to-usability/">5 key quality components of usability</a>: error frequency and severity are negatively related to the usability of a system. And error prevention is one of the <a href="https://www.nngroup.com/articles/ten-usability-heuristics/">10 heuristics for user interface design</a>.</p>

<p>Even though we talk about “user error,” the <a href="https://www.nngroup.com/articles/error-prevention/">true culprit is the designer</a>, for having made it too easy for users to get into trouble. We cannot assume that people will always use our design in the intended manner.</p>

<p>There are many ways to <a href="https://www.nngroup.com/articles/user-mistakes/">prevent (or at least reduce) user errors</a>. Here, we’ll focus on one of the simplest — the confirmation dialog.</p>

<blockquote><strong>Confirmation dialog:</strong> Asks users whether they are sure that they want to proceed with a command that they have just issued to a system.</blockquote>

<p>In graphical user interfaces, a confirmation dialog usually takes the form of a <a href="https://www.nngroup.com/articles/modal-nonmodal-dialog/">modal dialog box</a> that pops up and must be attended to before the system will execute the user’s command. (Other interaction styles may use different formats for confirmation dialogs. For example, a <a href="https://www.nngroup.com/articles/voice-interaction-ux/">voice UI</a> might use a spoken question that the user can reply to with a “yes” or a “no.”) Whatever the format, confirmation dialogs constitute an interruption initiated by the system; they slow down the user’s task flow. If this delay prevents an error, then it’s time well spent, but, if not, they are disruptive and thus annoying.</p>

<p>Windows 10 offers a good example of a confirmation dialog when the user attempts to empty a recycle bin that contains a single file:</p>

<figure class="caption"><img alt="Windows 10 delete-file (one file)" height="343" loading="lazy" src="https://media.nngroup.com/media/editor/2018/01/23/windows-10-delete-file-confirm.png" width="705"/>

<figcaption><em>Windows 10: The confirmation dialog to delete a single file is an example of good (though not perfect) design.</em></figcaption>

</figure>

<p>However, when the recycle bin contains multiple files, Windows 10 uses a less usable confirmation dialog:</p>

<figure class="caption"><img alt="Windows 10: delete files (2 files)" height="193" loading="lazy" src="https://media.nngroup.com/media/editor/2018/01/23/windows-10-delete-multiple-confirm.png" width="703"/>

<figcaption><em>Windows 10: The confirmation dialog to delete multiple files displays questionable design.</em></figcaption>

</figure>

<p>First of all, why does Windows use two different icons to represent the same issue (permanent file deletion)? The X and the exclamation mark are both <a href="https://www.nngroup.com/articles/icon-usability/">reasonable icons</a> for this type of warning, but pick one, for the sake of <a href="https://www.nngroup.com/articles/do-interface-standards-stifle-design-creativity/">consistency</a> (another top-10 UI heuristic). However, this is a minor issue, since I’m sure users don’t base their response to these dialogs on an analysis of the icons.</p>

<p>The problem with the multiple-file confirmation plagues many confirmation dialogs: <strong>lack of specificity. </strong>Saying <em>these 2 items</em> doesn’t tell users which files will be deleted. In contrast, the single-file confirmation shows the name of the file, as well as some supplementary info that’ll help the user determine whether the right file will be deleted. (For even better usability, display a thumbnail of the file instead of a generic icon.) Admittedly, it’s hard to provide much detail when many files are being deleted, and stating the number of files is one small amount of specificity.</p>

<p>Let’s go back to basics: why have confirmation dialogs in the first place? To <strong>allow users a second chance</strong> to check their work before proceeding with a dangerous action. However, it’s not a second chance at all if users automate their response to the conformation and simply click <em>Yes</em> without thinking further.</p>

<p>A confirmation dialog must restate the user’s request and explain what the computer is about to do, with specific information that allows users to understand the effects of their action. Without identifying details it’s useless to ask users to confirm a request, as shown by the video-delete confirmation from YouTube:</p>

<figure class="caption"><img alt="YouTube confirmation dialog" height="405" loading="lazy" src="https://media.nngroup.com/media/editor/2018/01/23/youtube-permanently-delete.png" width="871"/>

<figcaption><em>YouTube: The confirmation dialog to delete a video lacks specificity. It’s admittedly helpful that the dialog ups the ante by saying </em>“You can’t undo this,”<em> though it would be much better if the system provided resilience by keeping a backup copy of the deleted video around for a little time, so that the user could in fact undo a deletion.</em></figcaption>

</figure>

<p>When users are asked <em>Are you sure you want to do this?</em> without further details, the only sensible reaction is “of course I want to do the thing I just told you to do,” and hit <em>Yes</em> without further thinking. Such automated behavior provides no protection at all, and only serves to <a href="https://www.nngroup.com/articles/does-user-annoyance-matter/">annoy users</a> — and make them pay less attention to future warnings.</p>

<h2>Guidelines for Confirmation Dialog Design</h2>

<ol>

<li>Use a confirmation dialog before committing to <strong>actions with serious consequences</strong> — such as destroying users’ work or costing large amounts of money. In particular, consider a confirmation dialog before actions that cannot be undone. (Though as mentioned, do try your best to offer undo — a key component of another usability heuristic, user control and freedom — in order to reduce anxiety and allow users to recover from major problems.)</li>

<li>Do not use confirmation dialogs for <strong>routine actions</strong>. Like in Aesop’s fable, if you cry wolf too many times, people will stop paying attention to the question, and the confirmation dialog will lose its power to prevent errors.</li>

<li>Be <strong>specific</strong> and inform users about the consequence of their action. Do not ask <em>Are you sure you want to do this? </em>Instead, explain what <em>this</em> is, in <a href="https://www.nngroup.com/articles/user-centric-language/">user-centric terms</a> that are <a href="https://www.nngroup.com/articles/legibility-readability-comprehension/">easy to understand</a> and make it likely that the user would recognize a mistake.</li>

<li>Instead of <em>Yes/No</em> answers, provide <strong>response options that summarize</strong> what will happen for each possible response. For example, in the case of file deletion, use buttons labeled <em>Delete file</em> and <em>Keep file</em>.</li>

<li>Consider using <a href="https://www.nngroup.com/articles/progressive-disclosure/">progressive disclosure</a> to allow users to <strong>find out more</strong> about the consequences of their command before they commit, while still keeping the text in the confirmation dialog brief enough to be easily <a href="https://www.nngroup.com/articles/how-users-read-on-the-web/">scannable</a>.

<figure class="caption"><img alt="Microsoft Word confirmation dialog with progressive disclosure" height="236" loading="lazy" src="https://media.nngroup.com/media/editor/2018/01/23/msword-confirmation-progressive-disclosure.png" width="931"/>

<figcaption><em>Microsoft Word: This confirmation dialog is too verbose, but the </em>Tell Me More <em>button is a good example of using progressive disclosure to keep secondary content out of most people’s eyes.</em></figcaption>

</figure>

</li>

<li>Avoid giving confirmation dialogs a <strong>default</strong> <em>Yes</em> answer. Usually it’s good to have the most common options as the <a href="https://www.nngroup.com/articles/the-power-of-defaults/">default</a> in a dialog box: doing so saves users time and also educates newbies as to the most likely answer. However, the entire purpose of confirmations is to make sure that users double-check their action and don’t proceed unless they’re really sure that they want to perform the dangerous action. You could potentially make <em>No</em> into the default, but it’s probably best not to have a default answer at all.</li>

<li>For particularly dangerous operations, require a <strong>nonstandard action</strong> from the user to confirm. Rather than simply clicking an <em>OK</em> button (or, better, a button with a word or two to describe the action) — which risks becoming an automated behavior — have people do something they would normally not do. For example, type a word into a box, as MailChimp requires before deleting a mailing list. (Don Norman goes so far as to suggest <a href="https://www.fastcodesign.com/90157153/don-norman-what-went-wrong-in-hawaii-human-error-nope-bad-design">requiring a different user to confirm</a> the most dangerous actions.) Such nonstandard response options have to be reserved for the most dangerous and rare actions, because, if they’re used too frequently, they become a new standard and risk turning into yet another automated behavior that loses its power to make the user think through the consequences before committing.

<figure class="caption"><img alt="MailChimp confirmation dialog box" height="707" loading="lazy" src="https://media.nngroup.com/media/editor/2018/01/23/mailchimp-type-delete-confirm.png" width="1060"/>

<figcaption><em>MailChimp: Confirmation dialog to delete a mailing list follows several of our confirmation-dialog guidelines: (1) specificity through the name of the list and (probably more important) the number of subscribers; (2) extra protection against automated behavior by forcing the user to explicitly type in the word </em>DELETE<em>; moreover, the type-in field doesn’t appear until after the user has scrolled. Such a heavy-handed confirmation dialog should be reserved for the most serious cases. (An even better design would provide the user with the opportunity to undo this destructive action.)</em></figcaption>

</figure>

</li>

<li>Consider a <a href="https://www.nngroup.com/articles/customization/">customization option</a> that allows the user to <strong>bypass future routine confirmations</strong>. (See the <em>Do not ask me again about converting documents </em>checkbox from Microsoft Word under guideline #5.) It’s true that guideline #2 says not to use routine confirmations; however, for educational purposes, occasionally you may want to provide confirmations anyway when introducing new features with undesired side effects, even though these effects are not serious. Such confirmations ought to be temporary, and you should offer users a way to avoid them.</li>

</ol>

<p>There is admittedly a tension between guidelines #1 and #2: you want to warn against serious consequences, but you don’t want to warn so often that the warning is overlooked and the answer becomes an automated behavior. The solution is to conduct a task analysis to determine the severity of different outcomes and the frequency of possible user actions. For example, a banking site might be <a href="https://www.nngroup.com/articles/personalization/">personalized</a> to only require confirmation for online payments that are at least twice the amount of each user’s normal range of payments: if I usually pay bills that are around $100–$500, then my first request to pay somebody $1,100 could well be an error, and the desired payment might only be $110. Even if I did want to pay $1,100, I might welcome the chance to doublecheck a payment that would be big — and thus scary — for me. On the other hand, somebody who pays $10,000 bills several times per day would be annoyed to be interrupted for a $1,100 payment. (“Twice the usual amount” is just an example, and not necessarily the optimal threshold — determining that requires user research.)</p>

<p><a href="https://msdn.microsoft.com/en-us/library/windows/desktop/dn742470.aspx">Microsoft provides an even larger set of design guidelines</a> for confirmation dialogs, including how to handle bulk confirms for a sequence of actions. Ultimately, though, I think the most important usability considerations in confirmation dialogs is to <strong>not overuse</strong> them and to be sufficiently <strong>specific</strong> that users know what they’re agreeing to. I say again: if you warn people too much, they stop paying attention. If I said this a few more times, you would stop reading.</p>

<p>Finally, for improved total user experience, beyond the design of the dialog box itself, do go to great lengths to provide <strong>undo</strong>, because some user errors will remain despite the even the best of confirmation dialogs. All you can do is to reduce the number of user errors, but that’s an extremely worthy goal that will increase customer satisfaction, possibly save lives, and definitely increase the business value of your design.</p>

<p> </p>

<p> </p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=confirmation-dialog&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">errors,Application Design</span>

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