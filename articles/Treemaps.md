# Treemaps: Data Visualization of Complex Hierarchies - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">7</span>

<div class="article-header">

<h1 class="article-h1">Treemaps: Data Visualization of Complex Hierarchies</h1>

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

September 29, 2019

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2019-09-29</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Treemaps: Data Visualization of Complex Hierarchies&amp;body=https://www.nngroup.com/articles/treemaps/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/treemaps/&amp;title=Treemaps: Data Visualization of Complex Hierarchies&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/treemaps/&amp;text=Treemaps: Data Visualization of Complex Hierarchies&amp;via=nngroup" data-share-type="Twitter">

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

</span>A treemap is a complex, area-based data visualization for hierarchical data that can be hard to interpret precisely. In many cases, simpler visualizations such as bar charts are preferable.

</div>

<div class="article-body">

<p>Treemaps are a data-visualization technique for large, hierarchical data sets. They capture two types of information in the data: (1) the value of individual data points; (2) the structure of the hierarchy.</p>

<blockquote>

<p><strong>Definition</strong>: Treemaps are visualizations for hierarchical data. They are made of a series of nested rectangles of sizes proportional to the corresponding data value. A large rectangle represents a branch of a data tree, and it is subdivided into smaller rectangles that represent the size of each node within that branch.</p>

</blockquote>

<figure class="caption"><img alt="A hierarchy showing four levels of the S&amp;P 500" height="1616" loading="lazy" src="https://media.nngroup.com/media/editor/2019/09/16/overall-hierarchy-tree-v2.png" width="3431"/>

<figcaption><em>A hierarchical tree diagram, showing the structure of the S&amp;P 500.  This structure is the basis of the treemap shown below.</em></figcaption>

</figure>

<figure class="caption"><img alt="Four views of the same S&amp;P 500 treemap, with four levels of the hierarchy of the data set highlighted" height="1993" loading="lazy" src="https://media.nngroup.com/media/editor/2019/09/16/levels-of-hte-hierarchy.png" width="3177"/>

<figcaption><em>FinViz Map of the Market uses a treemap corresponding to the tree structure of the S&amp;P 500 dataset depicted above. The items colored in yellow and marked (A), (B), (C), (D) correspond to the items labeled with those letters in the tree diagram above. (A) represents the entire S&amp;P 500 and is the same as the root of the tree. The rectangle (B) is the </em>Technology<em> sector. Within the </em>Technology<em> sector, a smaller rectangle is </em>Communications Equipment<em> (C). Finally, within the </em>Communications<em> </em>Equipment<em> rectangle, all the smaller rectangles represent individual companies within that sector, such as </em>Cisco<em> </em>Systems<em> (D), </em>Qualcomm<em>, and so on. The color of each rectangle shows if the value of that stock is moving up or down – very bright red indicates a big shift downward, and very bright green indicates a big shift upwards.</em></figcaption>

</figure>

<figure class="caption"><img alt="Two zoomed in images of a treemap, with the relative sizes of items shown, to compare their quantitative size" height="1048" loading="lazy" src="https://media.nngroup.com/media/editor/2019/09/16/size-of-tier-3s-and-4s.png" width="2628"/>

<figcaption><em>The size of each rectangle represents the market capitalization (value) of that stock, industry, or sector. At the lowest level of the hierarchy (individual companies), Google (E) has a larger market cap than Facebook (F), and so their relative rectangles are sized appropriately. One level up in the hierarchy (</em>Industry<em>), the entire </em>Internet Information Providers<em> (G) category is larger than </em>Application Software<em> (H), and their rectangles are appropriately sized to show that differences as well.</em></figcaption>

</figure>

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

<a class="ga-article-toc-item" href="#toc-key-uses-of-treemaps-1">Key Uses of Treemaps</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-treemaps-downsides-2">Treemaps’ Downsides</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-alternatives-to-treemaps-3">Alternatives to Treemaps</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-summary-4">Summary</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-references-5">References</a>

</li>

</ul>

</div>

</div><h2 id="toc-key-uses-of-treemaps-1">Key Uses of Treemaps</h2>

<p>Treemaps are commonly found on data <a href="https://www.nngroup.com/articles/dashboards-preattentive/">dashboards</a>. Designers often choose them to add visual variety on a dense dashboard. However, treemaps are a complex visualization and present many obstacles to quick comprehension (which is the main requirement for any information displayed on a dashboard).</p>

<p>Treemaps are often used for sales data, as they capture relative sizes of data categories, allowing for quick perception of the items that are large contributors to each category. Color can identify items that are underperforming (or overperforming) compared to their siblings from the same category. This is why FinViz’s Map of the Market is an enduring example of treemaps: it allows users to identify companies that are doing better than their industry peers, even though their overall stock value may be quite small.</p>

<p>Treemaps work well when your hierarchical data has 2 main dimensions that you want to visualize:</p>

<ol>

<li> A <strong>positive quantitative value</strong>, which will be expressed as the area of the rectangle (Because area cannot be negative, you cannot use treemaps for visualizing variables like gain/loss, which can have both positive and negative values.)</li>

<li value="2">A <strong>categorical or second quantitative value</strong>, which will be expressed as the color of the individual rectangles. If color is used to express a quantitative value, it’s strongly encouraged to use only one color (if all the numbers are positive) or two colors (one for negative and one for positive), and vary the intensity of the color to express precise value. As humans don’t perceive colors to have an inherent order, we strongly recommend that you do not use multiple colors to represent a range of numbers.</li>

</ol>

<figure class="caption"><img alt="An overly colorful treemap" height="1602" loading="lazy" src="https://media.nngroup.com/media/editor/2019/09/16/overly-colorful-treemap.png" width="2576"/>

<figcaption><em>An <a href="http://ncva.itn.liu.se/education-geovisual-analytics/treemap?l=en">example</a> of poor use of color in a treemap: several different colors are used to show the percentage of the population that is over 65 in various regions of Europe; each color indicates a different percentage range (with blue marking the low ranges, yellow the middle, and red the high). Unfortunately, there is no universal <a href="http://www.nngroup.com/articles/natural-mappings/">natural mapping</a> that says that blue is less than yellow or than red. Instead, it would have been better if the intensity of single color was used to indicate percentage.</em></figcaption>

</figure>

<p style="margin-left:.5in;">If color represents a categorical variable, it is okay to use different colors for different possible values, as there’s no need for users to interpret a specific color as being “higher” or “lower” than another. However, as with any use of color in a data visualization, restraint in the number of colors is strongly advised!</p>

<p style="margin-left:.5in;">Regardless of how you use color in a treemap, make the following <a href="https://www.nngroup.com/videos/inclusive-design-welcome-mat/">accessibility </a>accommodations for color-blind users:</p>

<ul>

<li>Avoid using both red and green in the same treemap (especially for values that need to be differentiated quickly).</li>

<li>Use color palettes that are safe for color-blind people.</li>

<li>Test your design with a tool that allows you to simulate a color-blind user’s experience</li>

<li>Use a secondary signal (such as text within the rectangle or appearing on hover) for the data aspect captured through color</li>

</ul>

<figure class="caption"><img alt="A version of the S&amp;P 500 treemap as shown in a color blindness simulator" height="1060" loading="lazy" src="https://media.nngroup.com/media/editor/2019/09/16/color-blind.png" width="3261"/>

<figcaption><em> (Left) FinViz’s map of the market uses red and green to encode the change in the stock value (green is up and red is down). (Right) The same visualization is shown as perceived by someone with deuteranopia: the red and green colors are hard to distinguish. In this design, some (but not all) rectangles do contain the recommended alternative cue: for example, the AMZN rectangle in the upper middle is annotated with “+1.28%”, which informs users that this stock is up even if they can’t tell that it’s green. (The second image is from a <a href="http://www.color-blindness.com/coblis-color-blindness-simulator/">color-blindness simulator</a>).</em></figcaption>

</figure>

<p>Here are a few more guidelines for creating usable treemaps:</p>

<ul>

<li><strong>Visually distinct borders</strong> around higher-level categories help users identify the top-level groupings.</li>

<li><a href="https://www.nngroup.com/articles/text-over-images/"><strong>High-contrast text</strong></a> ensures that people can read the labels inside the treemap rectangles.</li>

<li><strong>A visually distinctive selected state, </strong>reached when users hover (or tap) a rectangle, helps users confirm that they are looking at the right data point.</li>

<li><strong>Additional detail about a selected rectangle</strong> (appearing in an overlay), such as the name, value of the variables allows users to drill into the data.</li>

</ul>

<p> </p>

<figure class="caption"><img alt="A hover state with a clear border and popup window with additional details" height="328" loading="lazy" src="https://media.nngroup.com/media/editor/2019/09/16/hover-state.png" width="548"/>

<figcaption><em>A good example of using a visually distinct border around a selected section of the FinViz treemap, along with additional details about the sector in a popup window.</em></figcaption>

</figure>

<h2 id="toc-treemaps-downsides-2">Treemaps’ Downsides</h2>

<h3>Comparisons Are Difficult</h3>

<p>Human brains are able to process certain visual information <a href="https://www.nngroup.com/articles/dashboards-preattentive/">preattentively</a>: attributes such as length can be grasped quickly and accurately, and values for such attributes can be compared with almost no cognitive effort. Unfortunately, area is not one of these preattentive attributes. Treemaps rely on area (and possibly color) to encode the value of a variable, and therefore, although treemaps can convey overall relationships in a large data set, <strong>they are not suited for tasks involving precise comparisons</strong>.</p>

<figure class="caption"><img alt="A dashboard that includes a treemap." border="0" height="564" loading="lazy" src="https://media.nngroup.com/media/editor/2019/09/16/dashboard.png" width="974"/>

<figcaption><em>This <a href="http://powerbi.microsoft.com/en-us/partner-showcase/adatis-fmcgcpgproduction/">dashboard</a> includes a treemap that shows the production levels for various products produced in four factories. Color is used to designate the different factories and size is used to show the production outputs. While this visualization compresses a lot of data into a small space, the information it conveys efficiently is very high-level — for example, it’s easy to identify the top performers in each category. However, it is difficult and time-consuming to determine the top five overall performers. A bar chart would communicate this information more accurately and more quickly than the treemap.</em></figcaption>

</figure>

<figure class="caption"><img alt="A dashboard treemap zoomed in to show the very similar area of two regions.  This is an example of how treemaps are poor tools for precise comparisons, due to the visual similarity." height="1200" loading="lazy" src="https://media.nngroup.com/media/editor/2019/09/16/aorbtreemapsize.png" width="2558"/>

<figcaption><em>Zoomed-in view of the dashboard image above: Which is larger, (A) or (B)? Since this visualization uses area to communicate the size of the variable, it does not easily allow for specific comparisons between items. Making this comparison requires hovering over a section, waiting for a tooltip with that value to appear, and then keeping that information in one’s <a href="http://www.nngroup.com/articles/short-term-memory-and-web-usability/">short-term memory</a> while repeating the same process on the other section.</em></figcaption>

</figure>

<h3>Inefficient for Data that Is Not Hierarchical</h3>

<p><strong>Treemaps should not be used if your data is not hierarchical: </strong>in those situations, they are functionally equivalent with a pie chart — simply showing a parts-to-whole relationship. (Pie charts are not great visualizations either — like treemaps, they are based on area and angle, attributes that are not preattentive. They should be used only to communicate that one or two items are much larger than the rest, and not for comparing relative sizes of the pie slices.)</p>

<h3>Visually Overwhelming</h3>

<p>Treemaps are often used to visualize very large data sets, with hundreds or thousands of items. This quantity of information can visually overwhelm users — the treemap becomes a sea of tiny rectangles, many too small to bear a text label. Furthermore, in complex treemaps, the overall hierarchy can easily become undiscernible. The solution is a <strong>cushion treemap</strong>, which uses texture to make each rectangle look “raised” in the center like a cushion and tapering off to the edges. This visual effect takes advantage of humans’ tendency to interpret this type of shading as a raised surface, making it faster to identify the different rectangles.</p>

<figure class="caption"><img alt='A "cushion" treemap, used to help users see rectangles more easily.' height="702" loading="lazy" src="https://media.nngroup.com/media/editor/2019/09/16/cushiontreemap.png" width="974"/>

<figcaption><em>In a cushion treemap each rectangle has a slight gradient from the edges to the center. This effect helps to visually identify small items as well as larger categories comprised of several rectangles.</em></figcaption>

</figure>

<h3>Not for Balanced Trees</h3>

<p>Treemaps are also poor choices for data sets with items close in size (i.e., <strong>balanced trees</strong>). In these cases, the main purpose of a treemap (quickly identifying the largest items in a given category) becomes very difficult. Finally, the standard algorithm used to create a treemap attempts to make the rectangles as square as possible, in order to make size comparisons slightly easier and less error-prone. However, in interactive visualizations where change is shown over time, an artifact of this algorithm is that the rectangles may move around as their size changes. As a result, keeping track of a particular item over time becomes very difficult.</p>

<h2 id="toc-alternatives-to-treemaps-3">Alternatives to Treemaps</h2>

<p>In many cases, treemaps can be replaced with bar charts (for data that have one quantitative and one categorical variable) or scatter plots (for data with two quantitative variables) that represent the variables of interest.</p>

<p>This process, however, requires an understanding of your users’ <a href="https://www.nngroup.com/articles/field-studies/">top tasks</a>; for executives attempting to identify the products that have both a high sales volume and a large profit margin in order to advertise them most aggressively, a 2D scatterplot would be better than a treemap. But if the user cares primarily about the overall sales, a sorted bar chart is a better choice than a treemap. (Sorting is often underappreciated, but is one of the simplest ways of making it easy to identify those items with the biggest and smallest values.)</p>

<figure class="caption"><img alt="Scatterplot showing three variables." height="775" loading="lazy" src="https://media.nngroup.com/media/editor/2019/09/16/scatterplot.png" width="793"/>

<figcaption><em>A scatterplot is often a better choice than a treemap for visualizing data with 2 quantitative variables, as the human visual system can quickly and accurately detect 2D position. This <a href="http://www.ryansleeper.com/wp-content/uploads/2018/06/Tableau-Scatter-Plot-with-Fixed-Tick-Marks.png">scatterplot</a> also adds a third, categorical variable, expressed in color.</em></figcaption>

</figure>

<h2 id="toc-summary-4">Summary</h2>

<p>While treemaps can be useful for visualizing certain types of complex, hierarchical data sets, they often hard to interpret. If using a treemap, visually separate the different high-level categories, avoid using multiple colors to express numeric values, and design with color-blind users in mind. Last and foremost, understand what your users need to do with your data and consider whether other visualizations (such as a bar chart or a scatter plot) could replace or augment the treemap.</p>

<h2 id="toc-references-5">References</h2>

<p>Ben Shneiderman: <em>“Tree visualization with tree-maps: 2-d space-filling approach,”</em> ACM Transactions on Graphics, 11,1, 92-99. (1992)</p>

<p> </p>

<p>Jarke J. van Wijk and Huub van de Wetering: <em>“Cushion Treemaps: Visualization of Hierarchical Information,” </em>IEEE Symposium on Information Visualization (INFOVIS’99), San Francisco, (October 25-26, 1999)</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=treemaps&amp;pt=article">

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

<a class="tile ga-article-related-course" data-course-title="Designing Complex Apps for Specialized Domains" href="/courses/complex-apps-specialized-domains/?lm=treemaps&amp;pt=article">

<h4 class="title heading-small">Designing Complex Apps for Specialized Domains</h4>

<p id="designing-complex-apps-for-specialized-domains" class="description body-small">

Create and evaluate applications for advanced decision making, complicated workflows, and complex domains

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

<a class="tile ga-article-related-course" data-course-title="Measuring UX and ROI" href="/courses/measuring-ux/?lm=treemaps&amp;pt=article">

<h4 class="title heading-small">Measuring UX and ROI</h4>

<p id="measuring-ux-and-roi" class="description body-small">

Use metrics from quantitative research to demonstrate value

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

</ul>

</div>

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Application Design,data,ui elements,Accessibility,Analytics &amp; Metrics,complexity,Interaction Design</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Application Design</span>

<a class="ga-article-related-topic" href="/topic/applications/">Application Design</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/accessibility/">Accessibility</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/analytics-and-metrics/">Analytics &amp; Metrics</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/interaction-design/">Interaction Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>