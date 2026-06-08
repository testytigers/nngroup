# Checkboxes vs. Radio Buttons - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">6</span>

<div class="article-header">

<h1 class="article-h1">Checkboxes vs. Radio Buttons</h1>

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

September 26, 2004

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2004-09-26</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Checkboxes vs. Radio Buttons&amp;body=https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/checkboxes-vs-radio-buttons/&amp;title=Checkboxes vs. Radio Buttons&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/checkboxes-vs-radio-buttons/&amp;text=Checkboxes vs. Radio Buttons&amp;via=nngroup" data-share-type="Twitter">

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

</span>User interface guidelines for when to use a checkbox control and when to use a radio button control. Twelve usability issues for checkboxes and radio buttons.

</div>

<div class="article-body">

<p>I recently encountered the following box on a major website's registration page. It contains at least two design mistakes. See if you can find them before reading further.</p>

<table align="center" cellpadding="0" cellspacing="0" style="border-style: solid; border-width: 1px; border-color: black; padding: 1ex" width="60%">

<tbody>

<tr>

<td>

<form>

<table cellpadding="0" cellspacing="0" style="padding: 0">

<tbody>

<tr>

<td colspan="5" valign="top">Stay informed! Get updates about featured products, solutions, services and educational opportunities. Let Foobar Corp. and selected organizations provide you with information about other offerings.</td>

</tr>

<tr>

<td colspan="5" valign="top"> </td>

</tr>

<tr>

<td colspan="5" valign="top">May we send you updates using e-mail?</td>

</tr>

<tr valign="baseline">

<td><input name="permission" type="checkbox" value="Y"/></td>

<td colspan="4">Yes, please use e-mail to send me information about other offerings.</td>

</tr>

<tr>

<td valign="top"> </td>

<td colspan="4" valign="top"> </td>

</tr>

<tr>

<td colspan="5" valign="top">If you prefer, we will not contact you using the data you provided in this instance.</td>

</tr>

<tr valign="baseline">

<td><input name="discardinfo" type="checkbox" value="YES"/></td>

<td colspan="4">Please do not use the contact details provided here to send me information about other offerings.</td>

</tr>

</tbody>

</table>

</form>

</td>

</tr>

</tbody>

</table>

<p>Mistake #1 is the primary focus of this article: The erroneous use of checkboxes where radio buttons should be. Because the two choices above are mutually exclusive, the page should present users with radio buttons, which restrict them to selecting exactly one option.</p>

<p>Mistake #2 is to present two questions in the first place, and then to put them in a big, verbose box. A single, shorter question would be far better here: "Yes, send me information about other featured products, solutions, services, and educational opportunities."</p>

<p>Ironically, with a single question, using a checkbox would have been correct because the user would be answering yes or no. The recommendation from <a class="old" href="https://www.nngroup.com/reports/ecommerce-user-experience/" title="Nielsen Norman Group report: Design guidelines for ecommerce user experience"> user testing of ecommerce sites</a> is to <strong>leave the checkbox blank by default</strong>, so users must actively click it to opt in for further messages.</p>

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

<a class="ga-article-toc-item" href="#toc-when-to-use-which-widgets-1">When to Use Which Widgets</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-additional-guidelines-2">Additional Guidelines</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-why-these-guidelines-matter-3">Why These Guidelines Matter</a>

</li>

</ul>

</div>

</div><h2 id="toc-when-to-use-which-widgets-1">When to Use Which Widgets</h2>

<p>Ever since the first edition of <cite> Inside Macintosh </cite> in 1984, the rule has been the same for when to use checkboxes versus radio buttons. All subsequent GUI standards and the official W3C Web standards have included the same definition of these two controls:</p>

<ol>

<li style="margin-top: 1ex"><strong>Radio buttons </strong> are used when there is a list of two or more options that are <strong> mutually exclusive </strong> and the user must select exactly one choice. In other words, clicking a non-selected radio button will deselect whatever other button was previously selected in the list.</li>

<li style="margin-top: 1ex"><strong>Checkboxes </strong> are used when there are lists of options and the user may <strong> select any number </strong> of choices, including zero, one, or several. In other words, each checkbox is independent of all other checkboxes in the list, so checking one box doesn't uncheck the others.</li>

<li style="margin-top: 1ex"><strong>A stand-alone checkbox </strong> is used for a single option that the user can turn on or off.</li>

</ol>

<p>Sounds simple enough, right?</p>

<p>Yet I frequently encounter web pages that use radio buttons and checkboxes wrong. Even after twenty years, it's worth stating these guidelines once again.</p>

<h2 id="toc-additional-guidelines-2">Additional Guidelines</h2>

<ol start="4">

<li><strong>Use standard visual representations. </strong> A checkbox should be a small square that has a checkmark or an X when selected. A radio button should be a small circle that has a solid circle inside it when selected.</li>

<li style="margin-top: 1ex"><strong>Visually present groups of choices as groups,</strong> and clearly separate them from other groups on the same page. The boxed example above violates this guideline because the layout makes the two checkboxes appear to be addressing separate topics when theyre actually alternative options for a single topic.

<ul style="margin-top: 0.5ex">

<li><strong>Use subheads to break up a long list of checkboxes</strong> into logical groups. This makes the choices faster to scan and easier to understand. The risk is that users might view each subgroup as a separate set of options, but this is not necessarily fatal for checkboxes — each box is an independent choice anyway. A list of radio buttons, however, must always appear unified, so you cannot use subheads to break it up.</li>

</ul>

</li>

<li style="margin-top: 1ex"><strong>Lay out your lists vertically</strong>, with one choice per line. If you must use a horizontal layout with multiple options per line, make sure to space the buttons and labels so that it's abundantly clear which choice goes with which label. In the following list, for example, it's difficult to see the correct radio button to click for option four.

<div style="text-align: center">

<form><input accesskey="1" checked="checked" id="one" name="sample" type="radio"/> <label for="one"> One </label> <input accesskey="2" id="two" name="sample" type="radio"/> <label for="two"> Two </label> <input accesskey="3" id="three" name="sample" type="radio"/> <label for="three"> Three </label> <input accesskey="4" id="four" name="sample" type="radio"/> <label for="four"> Four </label> <input accesskey="5" id="five" name="sample" type="radio"/> <label for="five"> Five </label> <input accesskey="6" id="six" name="sample" type="radio"/> <label for="six"> Six </label> <input accesskey="7" id="seven" name="sample" type="radio"/> <label for="seven"> Seven </label></form>

</div>

</li>

<li style="margin-top: 1ex"><strong>Use positive and active wording </strong> for checkbox labels, so that it's clear what will happen if the user turns on the checkbox. In other words, avoid negations such as "Don't send me more email," which would mean that the user would have to check the box in order for something <em> not </em> to happen.

<ul>

<li style="margin-top: 0.5ex">Write checkbox labels so that users know both what will happen if they check a particular box, and what will happen if they leave it unchecked.</li>

<li style="margin-top: 0.5ex">If you can't do this, it might be better to use two radio buttons — one for having the feature on, and one for having it off — and write clear labels for each of the two cases.</li>

</ul>

</li>

<li style="margin-top: 1ex"><strong>If possible, use radio buttons rather than drop-down menus</strong>. Radio buttons have <a href="https://www.nngroup.com/articles/minimize-cognitive-load/" title="Minimize Cognitive Load to Maximize Usability">lower cognitive load</a> because they make all options permanently visible so that users can easily compare them. Radio buttons are also easier to operate for users who have difficulty making precise mouse movements. (Limited space might sometimes force you to violate this guideline, but do try to keep choices visible whenever possible.)</li>

<li style="margin-top: 1ex"><strong>Always offer a default selection for radio button lists</strong>. By definition, <a href="https://www.nngroup.com/articles/radio-buttons-default-selection/">radio buttons always have exactly one option selected</a>, and you therefore shouldn't display them without a default selection. (Checkboxes, in contrast, often default to having none of the options selected.)

<ul>

<li style="margin-top: 0.5ex">If users might need to refrain from making a selection, you should provide a radio button for this choice, such as one labeled "None." Offering users an explicit, neutral option to click is better than requiring the implicit act of not selecting from the list, especially because doing the latter violates the rule of always having exactly one option chosen.</li>

</ul>

</li>

<li style="margin-top: 1ex"><strong>Because radio buttons require exactly one choice, make sure that the options are both comprehensive and clearly distinct</strong>. In <a class="old" href="https://www.nngroup.com/reports/senior-citizens-on-the-web/" title="Nielsen Norman Group report: Senior Citizens (Ages 65 and older) on the Web"> tests with older users</a>, for example, people couldn't complete a form that required them to select their job because it didn't offer "retired" as an option. If it's impossible to be comprehensive, offer a button labeled "Other," supplemented by a type-in field.</li>

<li style="margin-top: 1ex"><strong>Let users select an option by clicking on either the button/box itself or its label</strong>:<strong> </strong> a bigger target is faster to click according to <a class="old" href="http://www.asktog.com/columns/022DesignedToGiveFitts.html" title="AskTog: A Quiz Designed to Give You Fitts"> Fitts's Law</a>. In HTML forms, you can easily achieve this by <a class="out" href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label" title="Use of the &lt;LABEL&gt; element in HTML"> coding each label with &lt;label&gt; elements</a>, as I've done for the example with horizontal radio buttons above (to select that option, click on the word "Four"). In testing <a class="old" href="https://www.nngroup.com/articles/ephemeral-web-based-applications/" title="Alertbox: Ephemeral Web-Based Applications">web-based applications in Flash</a>, we found that user errors are further reduced by generous click zones that extend a few pixels beyond the visibly clickable area. (This effect can be hard to achieve in HTML, though some CSS hacks might do the trick.)</li>

<li style="margin-top: 1ex"><strong>Use checkboxes and radio buttons only to change settings, not as action buttons </strong> that make something happen. Also, the changed settings should not take effect until the user clicks the command button (labeled "OK" for example, or "Proceed to XXX" where "XXX" is the next step in a process).

<ul>

<li style="margin-top: 0.5ex">If the user clicks the <em> Back </em> button, any changes made to checkboxes or radio buttons on the page should be discarded and the original settings reinstated. The same guideline obviously holds if the user clicks a <em> Cancel </em> button (though navigational web pages <a class="old" href="https://www.nngroup.com/articles/reset-and-cancel-buttons/" title="Alertbox: Reset and Cancel Buttons"> don't need a cancel option</a> because the <em> Back </em> button serves the same purpose).</li>

<li style="margin-top: 0.5ex">If the user first clicks <em> Back </em> and then <em> Forward</em>, then it's most appropriate to interpret this sequence as an Undo-Redo pair, meaning that the appearance of the controls should show the user's changes as if the user had never clicked <em> Back</em>. These changes should still not take effect on the backend until the user clicks "OK" or an equivalent command.</li>

</ul>

</li>

</ol>

<h2 id="toc-why-these-guidelines-matter-3">Why These Guidelines Matter</h2>

<p>Am I just being picky when I insist on the correct use of checkboxes and radio buttons? No. There are <a href="https://www.nngroup.com/articles/do-interface-standards-stifle-design-creativity/">good usability reasons to follow GUI standards and use the controls correctly.</a></p>

<p>Most important, <strong><a class="old" href="https://www.nngroup.com/articles/the-need-for-web-design-standards/" title="Alertbox: The Need for Web Design Standards"> following design standards</a> enhances users' ability to predict what a control will do</strong> and how they'll operate it. When they see a list of checkboxes, users know that they can select multiple options. When they see a list of radio buttons, they know that they can only select one. (Of course, not every user knows this, but many do, especially since this has been a design standard since 1984.)</p>

<p>Because many people know how to operate standard GUI widgets, employing these design elements correctly <a class="old" href="https://www.nngroup.com/articles/ideologies-of-web-design/" title="Alertbox: Mastery, Mystery, and Misery: The Ideologies of Web Design"> enhances users' sense of mastery</a> over technology. Conversely, <strong>violating the standards makes the user interface feel brittle </strong>— as if anything can happen without warning. Say, for example, that you assume you can click on a radio button without any immediate impact, and can thus consider your choices after making a selection but before hitting "OK." In such a case, it's jarring when a website violates this standard and unexpectedly moves you to the next page once you enter a selection. Worse, it makes you fear what may happen as you work with forms elsewhere on the site.</p>

<p><strong>The biggest usability problems for checkboxes and radio buttons come from labels that are vague, misleading, or describe options that are impossible for average users to understand</strong>. Contextual help can alleviate the latter problem, but it's still best to user test any important set of interaction controls. Luckily, checkboxes and radio buttons are easy to test using <a class="old" href="https://www.nngroup.com/reports/paper-prototyping-training-video/" title="Nielsen Norman Group: Paper Prototyping – A How-To Training Video"> paper prototyping</a>, so you don't need to implement anything to see if users understand the labels and can use the widgets correctly.</p>

<p>No professional interaction designer would make the mistake of using checkboxes when radio buttons are called for. The distinction between these two controls is one of the first things taught in any interaction design class. So here's a final reason to use the right widget: if you don't, you'll be taken for an amateur.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=checkboxes-vs-radio-buttons&amp;pt=article">

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

<a class="tile ga-article-related-course" data-course-title="The Human Mind and Usability" href="/courses/human-mind/?lm=checkboxes-vs-radio-buttons&amp;pt=article">

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

<a class="tile ga-article-related-course" data-course-title="Web Page UX Design" href="/courses/web-page-design/?lm=checkboxes-vs-radio-buttons&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Application Design,Web Usability,graphical user interfaces,forms,controls,Interaction Design,standards &amp; conventions</span>

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

<li>

<a class="ga-article-related-topic" href="/topic/interaction-design/">Interaction Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>