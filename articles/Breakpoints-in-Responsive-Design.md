# Breakpoints in Responsive Design

**Author:** Kelley GordonKelley GordonApril 5, 20242024-04-05

**Topics:** Web Usability

**Source:** https://www.nngroup.com/articles/breakpoints-in-responsive-design/

---

April 5, 20242024-04-05

Share

Both grids and layouts are essential components ofresponsive web design. In responsive design, the design adapts and reacts to device characteristics and screen sizes.

Gridsprovide an organized way to efficiently create layouts in web and mobile designs. A grid is made up of columns, gutters, and margins that provide a structure for the layout of elements on a page.

A layoutrefers to how the different content and UI elements that make up a page are positioned on a screen. Layouts allow designers to utilize the space available on a screen or device to make the design and content most meaningful for users.

Grids are the structure that layouts are designed on. In addition to grids, breakpoints are fundamental in creating responsive designs.

Breakpoints are the building blocks of responsive design. They allow designers to adjust the layout to fit the needs of various screen sizes and devices.

Abreakpointdefines a screen size where the design should adjust to a different layout.

Technically, a breakpoint is a specific screen size. When a window size hits that specific value, (for example, when because the user resized their browser window), the layout will change.

In practice, however, designers tend to use the word “breakpoint” to refer to the screen-size range (minimum and maximum width) for which a specific layout will be shown, because that is what they have to specify in media queries.  For example, a desktop breakpoint might range from 1200px to 1400px — meaning that the desktop layout will be shown on any screen with the width in that range.

The more breakpoints you have, the more your design will be able to adapt to granular screen-size variations properly and gracefully. However, having many layouts corresponding to a plethora of screen sizes may not work in practical situations, where design resources are limited. In practice, designers usually accommodate only 2–3 breakpoints.

Typically, designers will consider designing for 4 basic breakpoints.  We use T-shirt sizing (small, medium, large) as there is no specific standard for each size. As mentioned previously, each breakpoint usually contains a minimum and maximum width that is customizable to fit the design’s layout needs. (A starting point for determining the exact values for these breakpoints would be to analyze the range of devices that your audience uses when accessing your site and then establish the breakpoints so you optimally accommodate the more common display sizes.)

The following layout changes commonly occur when shifting between breakpoint sizes:

Warby Parker is an eyewear brand. Its responsive website used a column grid to create an attractive visual experience.

At the medium screen size, 3 consistently sized columns made up the grid structure, and elements were aligned to and within these columns. On mobile (small screen size), Warby Parker’s 3-column grid reflowed into a one-column grid structure.

On IBM’s website, the left navigation was visible by default in the layout corresponding to the large screen sizes, but at medium screen sizes, it was collapsed under a hamburger icon in the top bar.

Our third example is from Airbnb, a travel-booking site. At the large screen size, both a list of properties and a map with their locations were displayed on the screen. At the small size (corresponding to tablet devices), the list became the default display and the map was hidden behind a button.

Breakpoints are fundamental to responsive design and to creating usable layouts and experiences.

If you don’t already have breakpoints determined, take some time to set them up. Think about the common ranges discussed above and refine them as needed.Decide on a sensible naming convention(like T-shirt sizing) that can adapt if you need to change your breakpoints. For example, if you discover that most of your mobile users now use larger smartphones, you may need to adjust your breakpoints for mobile to accommodate these larger display sizes.

Involve your development team in defining your breakpoints, because that team will set up the website's breakpoints.

If you’re working with an existing website,the breakpoints will most likely be established. In this case, take time to understand the different breakpoints so you can design layouts appropriately.

Once you have your breakpoints defined,think through how the design (including content) will flow and rearrange at these different sizes. Ask yourself:

For example, at the extra-small size (mobile), space is limited. Collapsing a left navigation under a hamburger icon will allow the user to focus on important content.

Or, if at large screen sizes, your main call to action was in the rightmost column, will this still be accessible on mobile, if your columns are stacked? Creating an exception from regular column stacking to make the call to action more discoverable (for example by making some preceding content collapsible under accordions) may be needed. These kinds of questions will help you decide how the layout will change from breakpoint to breakpoint. Once you created and tested your design, communicate to developers how the design will change based on the established breakpoints.

Strategically combine content, visuals, and interactive components to design successful web pages

Interaction

Use psychology to predict and explain how your customers think and act

Interaction