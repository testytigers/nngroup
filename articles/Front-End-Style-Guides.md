# Front-End Style-Guides: Definition, Requirements, Component Checklist - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">5</span>

<div class="article-header">

<h1 class="article-h1">Front-End Style-Guides: Definition, Requirements, Component Checklist</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Page Laubheimer</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/2022-portrait-page-3.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list">

Page Laubheimer

</span>

<p class="publication-date">

March 27, 2016

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2016-03-27</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Front-End Style-Guides: Definition, Requirements, Component Checklist&amp;body=https://www.nngroup.com/articles/front-end-style-guides/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/front-end-style-guides/&amp;title=Front-End Style-Guides: Definition, Requirements, Component Checklist&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/front-end-style-guides/&amp;text=Front-End Style-Guides: Definition, Requirements, Component Checklist&amp;via=nngroup" data-share-type="Twitter">

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

</span>Front-end style-guides help efficient design and testing, and enforce UI consistency. We present 8 style-guide requirements and 25 common components.

</div>

<div class="article-body">

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

<a class="ga-article-toc-item" href="#toc-what-is-a-front-end-style-guide-1">What Is a Front-End Style Guide?</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-the-ux-benefits-of-a-front-end-style-guide-2">The UX Benefits of a Front-End Style Guide</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-front-end-style-guides-are-not-editorial-or-branding-style-guides-3">Front-End Style Guides Are not Editorial or Branding Style Guides</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-front-end-style-guides-include-responsive-design-patterns-4">Front-End Style Guides Include Responsive Design Patterns</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-checklist-of-8-main-requirements-for-a-front-end-style-guide-5">Checklist of 8 Main Requirements for a Front-End Style Guide</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-25-common-ui-components-included-in-front-end-style-guides-6">25 Common UI Components Included in Front-End Style Guides</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-7">Conclusion</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-references-8">References</a>

</li>

</ul>

</div>

</div><h2 id="toc-what-is-a-front-end-style-guide-1">What Is a Front-End Style Guide?</h2>

<p>Front-end style guides have become an increasingly commonplace deliverable in UX practice. As described by Jeff Gothelf and Josh Seiden in their book <em>Lean UX, </em>they originated in <a href="https://www.nngroup.com/courses/lean-ux-and-agile/">Agile or Lean environments</a>.</p>

<blockquote>

<p style="margin-left:22.5pt">Definition: <strong>Front-end style guides are a modular collection of all the elements in your product’s user interface</strong>, together with code snippets for developers to copy and paste as needed to implement those elements<strong>. </strong>They include common UI components like buttons, form-input elements, navigation menus, modal overlays, and icons.</p>

</blockquote>

<p>A front-end style guide is both a <strong>deliverable</strong> created by the UX team (in concert with the engineering team, typically) and a <strong>tool</strong> used by the entire team for maintaining consistent, nimble product design in a modular format.</p>

<p>Front-end style guides are distinct from design pattern libraries, which are a long-standing tool used by UX practitioners to define broad design ideas, rather than specific implementation details. Unfortunately, <a href="http://ux.mailchimp.com/patterns/about">some</a> <a href="http://alistapart.com/blog/post/getting-started-with-pattern-libraries">proponents</a> of front-end style guides refer to them as <em>pattern libraries</em>, which has caused some confusion in the UX community.</p>

<figure class="caption"><img alt="Salesforce Lightning Design System Screenshot" height="946" loading="lazy" src="https://media.nngroup.com/media/editor/2020/02/29/screen-shot-2016-03-14.png" width="1320"/>

<figcaption><em><a href="http://www.lightningdesignsystem.com/">Salesforce’s Lightning Design System</a> shows a UI element, </em>Button Group Base<em>, along with an example of how to implement it, guidelines for how it should function, and when an alternative variant (such as </em>Button Group Disabled<em>) should be used. The example is a live element that is interactive and exhibits the same behaviors as in the final product.</em></figcaption>

</figure>

<h2 id="toc-the-ux-benefits-of-a-front-end-style-guide-2">The UX Benefits of a Front-End Style Guide</h2>

<p>The purpose of a style guide is to collect all product-interface elements in a modular library. It benefits the UX team in two ways: (1) prototyping ideas and implementing new designs becomes more efficient, and (2) a consistent visual design can be easily enforced throughout the product. Designers and developers are just as lazy as everybody else. (That’s “lazy” in a positive sense, as in preserving effort and company resources.) Thus, if it’s less work to do the right thing and create a consistent user interface, they’re more likely to do it than to invent a new, inconsistent design or implementation.</p>

<p>When a mature front-end style guide exists, the UX team spends less time creating high-fidelity design mockups for every new idea. Instead, the main design-specification deliverable can be a quick sketch that unambiguously references which components get applied where in the design. Such a library of existing modules also allows for fast high-fidelity prototyping: the UX team can quickly assemble a realistic interactive prototype that could be used in usability tests or shared with stakeholders.</p>

<h2 id="toc-front-end-style-guides-are-not-editorial-or-branding-style-guides-3">Front-End Style Guides Are not Editorial or Branding Style Guides</h2>

<p>You may already be familiar with two other types of style guides:</p>

<ol>

<li>Editorial style guides specify writing style, grammar, punctuation, and other content-editing rules. Many websites and most publications do have such style guides and content teams are supposed to follow them.</li>

<li>Branding style guides usually specify brand-related rules such as acceptable logo usage, color palette, and typography.</li>

</ol>

<p>Unlike editorial style guides, front-end style guides do not normally include writing-related guidelines. However, they often do have a high overlap with the branding style guides — in addition to rules and descriptions of the UI components, they include brand-related elements and guidelines.</p>

<figure class="caption"><img alt="Adobe Corporate Branding Guidelines Screenshot" height="1000" loading="lazy" src="https://media.nngroup.com/media/editor/2020/02/29/screen-shot-2016-03-09adobe.png" width="1400"/>

<figcaption><em><a href="http://brandcenterdl.adobe.com/Corpmktg/Brandmktg/Campaign_Assets/guidelines/corporate/corporate_brand_guidelines.pdf">Adobe’s “Corporate Brand Guidelines”</a> is a branding style guide and <strong>not</strong> a front-end style guide. Front-end style guides often contain many of the elements found a branding guidelines document.</em></figcaption>

</figure>

<p>The most important feature that separates front-end style guides from other types of style guides is that front-end style guides are rarely static, but are living collections of UI- elements’ descriptions and corresponding code snippets.</p>

<p>Most often, front-end style guides take the form of a web page or other interactive digital asset, rather than a PDF. You can typically interact with all the components in a front-end style guide, and many development teams choose to implement them so that any change made to components in a style guide will automatically update the product’s design as well. This isn’t a requirement for an effective style guide, but it can help to enforce its rigorous use.</p>

<h2 id="toc-front-end-style-guides-include-responsive-design-patterns-4">Front-End Style Guides Include Responsive Design Patterns</h2>

<p>In <a href="https://www.nngroup.com/articles/responsive-web-design-definition/">responsive designs</a>, the front-end style guide should not only define the interface components, but also describe how their styling and usage will differ across different screen sizes. Here are some pieces of information that are useful:</p>

<ul>

<li>Layout grids indicating how various components should be used in various screen-size contexts</li>

<li>Spacing around common elements when used on different screen sizes</li>

<li>Guidelines for where in the interface specific components should be placed<br/>

(These guidelines can help enforce consistency: for example, in a mobile app, the title bar and navigational elements will typically be present in most screens at the top, so defining that in the style guide can help to avoid one-off screen designs.)</li>

</ul>

<figure class="caption"><img alt="Google Material Design Screenshot" height="1552" loading="lazy" src="https://media.nngroup.com/media/editor/2020/02/29/screen-shot-2016-03-09.png" width="2618"/>

<figcaption><em><a href="https://www.google.com/design/spec/material-design/introduction.html">Google’s Material Design</a> style guide includes representations of how to use the responsive grid system, and where various parts of the interface should be consistently placed.</em></figcaption>

</figure>

<h2 id="toc-checklist-of-8-main-requirements-for-a-front-end-style-guide-5">Checklist of 8 Main Requirements for a Front-End Style Guide</h2>

<p>When creating a style guide, make sure to include the following 8 key features:</p>

<ol>

<li value="1">Table of contents<strong> </strong>that splits components into easily-findable categories</li>

<li value="2">Responsive layout or grid systems used to place common UI elements</li>

<li value="3">Color palette of the product (in appropriate format, e.g. HEX for the Web, UIColor for an iOS app)</li>

<li value="4">Typeface styles (e.g. <em>H1 Title</em>, <em>Body text</em>, <em>Photo caption text</em>), which should include typeface name and foundry, sizes, weights, leading/line height, tracking/kerning, and the appropriate contexts of use for that text style</li>

</ol>

<p>Then, for each of the specific UI elements in your product include the following information:</p>

<ol>

<li value="5">Description of the appropriate context of use: When does it make sense to use one particular component versus a similar one?</li>

<li value="6">Code snippets<strong>,</strong> often hidden in an <a href="https://www.nngroup.com/articles/accordions-complex-content/">accordion</a> feature</li>

<li value="7">Specs for implementation, including positioning and spacing information</li>

<li value="8">Dos and don’ts for that element.</li>

</ol>

<h2 id="toc-25-common-ui-components-included-in-front-end-style-guides-6">25 Common UI Components Included in Front-End Style Guides</h2>

<p>Here’s a starter list of UI elements that typically get included in a style guide. While this not an exhaustive list of all UI elements that <em>can</em> be used in a front-end style guide, it covers many of the common components.</p>

<ol>

<li value="1">Buttons</li>

<li value="2">Button groups</li>

<li value="3">Breadcrumbs</li>

<li value="4">Cards</li>

<li value="5">Tables</li>

<li value="6">Dialogs</li>

<li value="7">Grid lists of content, media, or photos</li>

<li value="8">Vertical lists</li>

<li value="9">Navigational menus (and subnavigation)</li>

<li value="10">Date and time pickers</li>

<li value="11">Progress and loading indicators</li>

<li value="12">Checkboxes</li>

<li value="13">Radio buttons</li>

<li value="14">Drop-down menus</li>

<li value="15">Sliders</li>

<li value="16">On-off switches</li>

<li value="17">Numeric-input steppers/incrementers</li>

</ol>

<ol>

<li value="18">Form fields (include variations with maximum character-count indicators, and indicators for when the field is required)</li>

<li value="19">Tabs</li>

<li value="20">Toolbars</li>

<li value="21">Tooltips</li>

<li value="22">Alert modals</li>

<li value="23">Icons</li>

<li value="24">Animations</li>

<li value="25">Tokens, also known as chips (e.g. email-address field)</li>

</ol>

<p> </p>

<figure class="caption" style="float:left"><img alt="Kayak Numeric Input Stepper" height="103" loading="lazy" src="https://media.nngroup.com/media/editor/2020/02/29/photo-mar-10-11.png" width="320"/>

<figcaption><em>Kayak’s iOS app features numeric-input steppers for the number of rooms and guests. If you feature this input component in your product, it should be included in the style guide.</em></figcaption>

</figure>

<figure class="caption" style="float:left"><img alt="Token from Material Design" height="160" loading="lazy" src="https://media.nngroup.com/media/editor/2020/02/29/screen-shot-2016-03-10.png" width="320"/>

<figcaption>An example of a token (or chip) from <a href="http://www.google.com/design/spec/components/chips.html">Google’s Material Design</a>. Tokens are often used in email-address recipient fields, to show each recipient separately, and allow you to delete a recipient with one click. They are also used in advanced-search fields and metadata tags to distinguish between terms that include a space.</figcaption>

</figure>

<p>Start with this list and pick from it only the components that are present in your product (don’t add new elements to your product or designs simply to satisfy this list). If you have additional unique elements, include them in your style guide.</p>

<h2 id="toc-conclusion-7">Conclusion</h2>

<p>Front-end style guides are becoming one of the most useful UX deliverables. They are especially important in Agile environments, where enabling more efficient design workflows is critical to keeping the fast pace of development. When developed rigorously, style guides promote consistent design practices and enforce developer adherence to specifications. A good front-end style guide should include responsive-design patterns and grids, code snippets for implementation, and strong guidelines for using each component.</p>

<p>Learn more about best practices for determining the appropriate component granularity, common pitfalls when creating (and using) style guides, and workflow options for creating a front-end style guide in our full-day <a href="https://www.nngroup.com/courses/ux-deliverables/">UX Deliverables Seminar</a>.</p>

<h2 id="toc-references-8">References</h2>

<p>Jeff Gothelf and Josh Seiden (2013): <a href="http://www.amazon.com/dp/1449311652?tag=useitcomusablein"><em>Lean UX: Applying Lean Principles to Improve User Experience</em></a>, O’Reilly Media.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Lean UX and Agile" href="/courses/lean-ux-and-agile/?lm=front-end-style-guides&amp;pt=article">

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

<a class="tile ga-article-related-course" data-course-title="Discovery: Building the Right Thing" href="/courses/discovery/?lm=front-end-style-guides&amp;pt=article">

<h4 class="title heading-small">Discovery: Building the Right Thing</h4>

<p id="discovery-building-the-right-thing" class="description body-small">

Conduct successful discovery phases to ensure you build the best solution

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

<a class="tile ga-article-related-course" data-course-title="Effective Ideation Techniques for UX Design" href="/courses/ideation/?lm=front-end-style-guides&amp;pt=article">

<h4 class="title heading-small">Effective Ideation Techniques for UX Design</h4>

<p id="effective-ideation-techniques-for-ux-design" class="description body-small">

Creative solutions for any UX design challenge

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Agile,Design Process,Visual Design</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Agile</span>

<a class="ga-article-related-topic" href="/topic/agile/">Agile</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/ux-design-process/">Design Process</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/visual-design/">Visual Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>