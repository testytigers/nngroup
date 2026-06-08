# Dashboards: Making Charts and Graphs Easier to Understand - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">9</span>

<div class="article-header">

<h1 class="article-h1">Dashboards: Making Charts and Graphs Easier to Understand</h1>

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

June 18, 2017

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2017-06-18</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Dashboards: Making Charts and Graphs Easier to Understand&amp;body=https://www.nngroup.com/articles/dashboards-preattentive/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/dashboards-preattentive/&amp;title=Dashboards: Making Charts and Graphs Easier to Understand&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/dashboards-preattentive/&amp;text=Dashboards: Making Charts and Graphs Easier to Understand&amp;via=nngroup" data-share-type="Twitter">

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

</span>Visualizations should leverage human cognition and use length and 2D position to communicate quantitative information quickly.

</div>

<div class="article-body">

<p>Data dashboards are a common tool used in web apps, intranets, and other business intelligence contexts to show regularly updated information that users must frequently monitor.</p>

<p style="margin-left: 40px;">Definition: <strong>Dashboards</strong> are collections of data visualizations, presented in a single-page view that imparts at-a-glance information on which users can act quickly.</p>

<p>The term “dashboard” is a metaphor for a car dashboard, which provides essential information that the driver can absorb quickly, without having to think. Thus, dashboards are not intended as expansive views of complex data: Their goal is not to facilitate exploration; instead, they provide information that can be consumed fast, with a minimum of interaction or cognitive processing. Users can glance at the dashboard and immediately see answers to questions like, “Am I speeding?” and “Am I about to run out of gas?” (in the case of an actual car dashboard), or “Are sales up?” and “Is this week’s email newsletter driving as much traffic as recent newsletters?” (in the case of a data dashboard).</p>

<p>Dashboards are distinct from <a href="https://www.nngroup.com/articles/intranet-portals-personalization/">portals</a>, which provide a combination of resources, information, tools, or access to <a href="https://www.nngroup.com/courses/application-ux/">web-based applications</a>, and are a single-point gateway for a variety of tasks. Dashboards are focused on a single task: communicating critical information.</p>

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

<a class="ga-article-toc-item" href="#toc-operational-dashboards-vs-analytical-dashboards-1">Operational Dashboards vs. Analytical Dashboards</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-preattentive-processing-and-quantitative-representation-2">Preattentive Processing and Quantitative Representation</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-linear-vs-area-based-graphs-3">Linear vs. Area-Based Graphs</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-use-color-shape-and-grouping-to-show-categories-4">Use Color, Shape, and Grouping to Show Categories</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-5">Conclusion</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-references-6">References</a>

</li>

</ul>

</div>

</div><h2 id="toc-operational-dashboards-vs-analytical-dashboards-1">Operational Dashboards vs. Analytical Dashboards</h2>

<p>Data dashboards generally exist in two forms:</p>

<ul>

<li><strong>Operational dashboards </strong>aim to impart critical information quickly to users as they are engaged in time-sensitive tasks.</li>

<li><strong>Analytical dashboards </strong>provide the user with at-a-glance information used for analysis and decision making, but don’t have the same level of time sensitivity as operational dashboards.</li>

</ul>

<figure class="caption"><img alt="ArcGIS operational dashboard" border="0" height="396" loading="lazy" src="https://media.nngroup.com/media/editor/2017/06/06/arcgis.png" width="700"/>

<figcaption><em>An <a href="http://doc.arcgis.com/en/operations-dashboard/web/user/monitor-and-respond-to-events.htm">operational dashboard in ArcGIS</a> shows emergency-management services in an urban environment. This information empowers emergency-response dispatchers to see the status of incidents and response teams. The use of a bar chart to indicate the types of incidents helps dispatchers quickly keep track of which types of emergency services (police, fire, ambulance) are needed.</em></figcaption>

</figure>

<p>Operational dashboards exist to provide information quickly to users that are making immediate decisions and carrying out time-sensitive tasks, such as monitoring server availability, patient vitals during surgery, customer-service calls, or flight traffic. Operational dashboards typically present data that is continuously updating and changing. While not all operational dashboards are used in high-consequence environments like hospitals and emergency management, they all do need to present data quickly to users to help identify unacceptable deviations in parameters or, visualize available resources.</p>

<p>Unlike operational dashboards, which are intended to support time-sensitive decision making and immediate action, analytical dashboards help users identify the need for further thought, investigation, research, or analysis. A sales dashboard (which is usually an instance of analytical dashboard) that is updated once a day won’t show information that requires an immediate emergency intervention from a sales manager, but it can keep the manager aware of fluctuating sales data that will later demand a thoughtful analysis.</p>

<p>Like operational dashboards, analytical dashboards also require an at-a-glance, single-screen view of the data that they monitor, and must quickly communicate important information to a user.</p>

<h2 id="toc-preattentive-processing-and-quantitative-representation-2">Preattentive Processing and Quantitative Representation</h2>

<p>In order to make it easiest for users to quickly understand the relationships between data, it’s useful to leverage the properties of human visual perception. There are a variety of visual attributes that people perceive very quickly, without fully engaging their attention, in a process known as <a href="https://www.nngroup.com/articles/visual-indicators-differentiators/"><strong>preattentive</strong></a><strong> processing</strong>. For example, in a display containing many lines of the same size, the one line that is longer will “pop out,” without the user having to engage in a visual search to locate it. Beside length, other preattentive features include area, angle, 2D position, and color.</p>

<figure class="caption"><img alt="../Articles/Data%20Dashboards/Preattentive.png" border="0" height="327" loading="lazy" src="https://media.nngroup.com/media/editor/2017/06/06/preattentive_lines.png" width="320"/>

<figcaption><em>Even without fully devoting one’s attention to the diagram, it is easy to quickly tell which line is the longest, due to efficient and accurate preattentive processing of length.</em></figcaption>

</figure>

<p>Although all preattentive features stand out easily, not all of them are equal. With some, people simply perceive a difference without being able to exactly pinpoint the size of the difference: for example, although we can effortlessly notice a large rectangle in a display containing many small rectangles, we are not good at judging how much bigger the large rectangle is, compared with the others.</p>

<p>In contrast, we are quite adept at estimating how lengths compare, and we can also accurately estimate position in a 2D space. (See the classical 1985 paper referenced at the end of the article for more detail on this finding.) This fact makes these two preattentive attributes ideal for quantitative representation; charts and graphs taking advantage of these features will generally be easy to understand.</p>

<figure class="caption"><img alt="Dashboard with a line chart on the left and a bar chart on the right" border="0" height="230" loading="lazy" src="https://media.nngroup.com/media/editor/2017/06/06/thedesignwork.png" width="720"/>

<figcaption><em>This dashboard example (<a href="http://www.thedesignwork.com/free-admin-panel-template-psd-download/">from TheDesignWork</a>) shows a line graph on the left and a bar chart on the right. Line charts leverage the fact that people process 2D position preattentively. In the example chart, it is very easy to see that there is a dip in the data that occurs on Wednesday. The bar chart on the right expresses a single quantitative variable using length, another preattentive feature that allows people to quickly and accurately notice any data points that stand out and understand the quantitative relationships between the data. Thus, it is easy to see right away that the bar for c is longer than all the others, and you can even tell that it’s almost twice as long as the second longest bar (for b).</em></figcaption>

</figure>

<p>Another powerful preattentive attribute is color: a red dot will easily stand out in a conglomerate of blue dots. However, unlike length, people do not perceive different colors as being in a particular order, so color should not be used to communicate information about quantitative values or magnitude. (Additionally, up to 4.5% of the general population suffers from some form of color blindness; also notable is the fact that many more men suffer from colorblindness than women — around 8% vs. 0.5%; though exact numbers vary by ethnicity.)</p>

<h2 id="toc-linear-vs-area-based-graphs-3">Linear vs. Area-Based Graphs</h2>

<p>As we mentioned above, 2D position and length are the two preattentive attributes that can be naturally mapped onto quantity and support quick data comparisons and inferences. Thus, visualizations based on them will generally be effective and easy to understand.</p>

<p>Bar charts are a reliable means of representing quantitative data: we pre-attentively process the length of each bar efficiently, allowing for easy comparison of values (especially if they are ordered in an ascending or descending pattern). Graphs that use 2D position like scatter plots or line graphs capitalize on the preattentive 2D attribute.</p>

<figure class="caption"><img alt="Scatterplot of 2-axis data" border="0" height="421" loading="lazy" src="https://media.nngroup.com/media/editor/2017/06/06/scatterplot.png" width="720"/>

<figcaption><em>Scatterplots are an effective visualization for showing relationships between the two variables plotted on the x and y axes. In this graph, because 2D position is a preattentive variable, you can notice right away which data points are highest and lowest along each axis, and can also notice potential correlations or other relationships between the data easily.</em></figcaption>

</figure>

<h3>Circular and Area-Based Graphs Are Difficult to Interpret Quickly or Accurately</h3>

<p>Circular graphs like pie charts, gauges, and radar charts do not convey well quantitative relationships between data, as they rely on area and angle to communicate quantitative information. Although area and angle are preattentive features, it’s harder for people to say how much bigger one area is than another.</p>

<p> </p>

<figure class="caption"><img alt="Microsoft dashboard with donut charts and treemaps" border="0" height="422" loading="lazy" src="https://media.nngroup.com/media/editor/2017/06/06/mspowerbi.png" width="720"/>

<figcaption><em>This <a href="https://appsource.microsoft.com/en-us/product/power-bi/c5a3f852-2f00-41cf-b342-b04496e488a1?tab=Overview">Microsoft Power BI </a>dashboard uses (1) donut charts and (2) tree maps to display data. Donut charts are similar to pie charts — they use area and angle to encode quantitative information — but are made even less effective by the whitespace in the middle, which makes each slice area smaller and thus complicates even more the already difficult task of determining a quantitative value for each option in the chart. The tree map also uses area for representing the relative sales amounts of the different cities — each rectangle’s area denotes its value — but unfortunately, area is a variable that people don’t interpret quickly or with accuracy, and thus a tree map (in this context) is not an effective way to represent quantitative data for rapid understanding.</em></figcaption>

</figure>

<p>Because charts based on area are not terribly efficient as a means of comparing quantities, visualizations like pie charts and tree maps are generally not recommended for <em>quickly</em> communicating complex quantitative relationships among items in a data set. Pie charts (and their even less helpful cousin, donut charts) are notoriously poor at most information-communication tasks (other than simply showing overwhelming disparities in percentage shares, such as a single source of revenue that represents the vast majority of a company’s profits), and should be avoided most of the time.</p>

<p>Tree maps (which show a hierarchical data set as a series of nested rectangles of different sizes, where the size of each rectangle corresponds to a numeric value) can be useful at representing a complex data space in a compact overview, when there is opportunity for users to leisurely explore the data set and seek out additional detail. However, treemaps are not appropriate for simple, actionable dashboards.</p>

<p>Angle, too, communicates quantitative information poorly — gauges that mimic the analog gauges found in car dashboards simultaneously consume a lot of precious space on a dashboard and are also harder to interpret than linear graphs.</p>

<figure class="caption"><img alt="Klipfolio dashboard with car-style gauges and alternative bullet charts" border="0" height="252" loading="lazy" src="https://media.nngroup.com/media/editor/2017/06/06/klipfolio.png" width="720"/>

<figcaption><em>This <a href="https://www.klipfolio.com/gallery/dashboards/google-adwords-account-overview">Klipfolio dashboard</a> uses a radial gauge (1) to show the value of a particular metric within a range. However, circular visualizations require a lot of space to communicate little information, and rely on angle (which is relatively poor at communicating information in a pre-attentive fashion) as the main means of communicating the key data. Just below, this same dashboard uses the significantly better linear bullet charts (2) to communicate similar information (quantitative data along a range, with a target value identified). All of these charts fail to show the overall range of the scale, however.</em></figcaption>

</figure>

<h3>3D Graphics</h3>

<p>Plotting a 2-variable chart in 3D is often done to (arguably) improve aesthetics, but will make the chart much more difficult to interpret quickly and accurately, as it distorts the shapes and alignment of the visual features showing data. While area-based graphs (such as pie charts and tree maps) are most susceptible to the distorting effects of 3D visualizations (as placing them in a 3D projection skews the quantitative meaning of the area), 3D bar charts are also more difficult to properly interpret than their 2D counterparts, as they can make it much harder to see which value the top of a bar represents, and how it aligns with the gridlines.</p>

<figure class="caption"><img alt="" height="211" loading="lazy" src="https://media.nngroup.com/media/editor/2017/06/07/bar-charts-2d-and-3d-side-by-side.png" width="720"/>

<figcaption><em>Using a 3D representation of a chart distorts and skews the shapes that represent the data, thus making it harder to decipher the quantitative values (and relative relationships between specific data). In a 3D visualization, it becomes much tougher to determine which bar is shortest, even though length is a very efficient preattentive variable when presented in 2D. For example, determining the specific relationship between the 3rd and 4th quarters in the 3D chart above is much more difficult than in the 2D version of the same data.</em></figcaption>

</figure>

<p> </p>

<figure class="caption"><img alt="3D pie chart " border="0" height="304" loading="lazy" src="https://media.nngroup.com/media/editor/2017/06/06/3d-pie.png" width="540"/>

<figcaption><em>In a 3D representation of a pie chart, area is distorted. In order to create a 3D perspective, the bottom of the chart is tilted “closer” to the viewer (and thus larger than it would be in a 2D representation), and the top of the chart is tilted “away” from the viewer (and thus smaller) to show perspective. Each square centimeter that is “futher away” from the viewer (1)  therefore represents more of the area (and thus percentage data) than an equivalent square centimeter in the “front” of the 3D space (2).<br/>

In a pie chart (which uses area to show percentage), the visualization is therefore skewed and potentially misrepresenting the data. Considering that area-based visualizations are already poor at conveying quantitative relationships, this 3D representation makes the user’s job much more difficult.</em></figcaption>

</figure>

<h2 id="toc-use-color-shape-and-grouping-to-show-categories-4">Use Color, Shape, and Grouping to Show Categories</h2>

<p>While color and shape are preattentive cues that do not easily communicate quantitative relationships, they can be used to convey categorical information — that is, which items in a visualization belong together. (According to the <a href="https://www.nngroup.com/articles/closeness-of-actions-and-objects-gui/">Gestalt psychology principle</a> of similarity, items that have similar shape or color are usually perceived as related.) Moreover, spatial proximity can also indicate semantic grouping.</p>

<p>Due to the prevalence of people with impaired color vision, color properties such as hue or saturation are helpful as a secondary grouping cue, rather than as the main way of showing groups or categories. Shape or clear visual grouping are more reliable signals for relatedness, and using color properties can help reinforce those relationships. Color can add visual weight to relationships, but, in most cases, should only be used to reinforce information that is already communicated in a different way (such as using proximity or similar shapes), since <a href="https://www.nngroup.com/articles/visual-indicators-differentiators/">the combination of color and shape together make for a more noticeable signal than either alone</a>.</p>

<figure class="caption"><img alt="Dundas call center dashboard " border="0" height="224" loading="lazy" src="https://media.nngroup.com/media/editor/2017/06/06/dundas.png" width="720"/>

<figcaption><em>This <a href="http://www.dundas.com/learning/samples">Dundas call-center dashboard</a> uses shape and borders to indicate different categories of data (shape distinguishes calls from web chat, and borders separate out different call-center agents. While color intensity is used in the </em>Interaction Length <em>section of the dashboard to indicate overlapping events, this attribute conveys information of secondary importance.</em></figcaption>

</figure>

<h2 id="toc-conclusion-5">Conclusion</h2>

<p>Data dashboards are intended to quickly communicate important information without requiring large amounts of time or cognitive resources to interpret. As a result, encoding the most important information in linear charts and graphs enables users to perceive the critical relationships between data before they even fully pay attention to the visualization.</p>

<p>Learn more about data dashboards in our full-day <a href="https://www.nngroup.com/courses/application-ux/">Application Design for Web and Desktop</a> seminar, and more about human cognition and its impacts on UX in our <a href="https://www.nngroup.com/courses/human-mind/">Human Mind and Usability</a> seminar.</p>

<h2 id="toc-references-6">References</h2>

<p>William S. Cleveland and Robert McGill: “Graphical Perception and Graphical Methods for Analyzing Scientific Data,” <em>Science</em>, Vol. 229, No. 4716 (Aug. 30, 1985)</p>

<p><em>Perceptual Edge</em>, “Tapping the Power of Visual Perception,” September 4, 2004 (<a href="https://perceptualedge.com/articles/ie/visual_perception.pdf">link</a>)</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Persuasive and Emotional Design" href="/courses/persuasive-emotional-design/?lm=dashboards-preattentive&amp;pt=article">

<h4 class="title heading-small">Persuasive and Emotional Design</h4>

<p id="persuasive-and-emotional-design" class="description body-small">

Create delightful experiences that touch, convince, or excite your audience

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

<a class="tile ga-article-related-course" data-course-title="The Human Mind and Usability" href="/courses/human-mind/?lm=dashboards-preattentive&amp;pt=article">

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

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=dashboards-preattentive&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">data,Psychology and UX,Application Design,complexity,Visual Design</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Psychology and UX</span>

<a class="ga-article-related-topic" href="/topic/psychology-and-ux/">Psychology and UX</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/applications/">Application Design</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/visual-design/">Visual Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>