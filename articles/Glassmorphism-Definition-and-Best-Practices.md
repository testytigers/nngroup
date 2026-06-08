# Glassmorphism: Definition and Best Practices

**Author:** Megan BrownMegan BrownJune 7, 20242024-06-07

**Topics:** Visual Design, Interaction Design

**Source:** https://www.nngroup.com/articles/glassmorphism/

---

June 7, 20242024-06-07

Share

Glassmorphism is avisual-design trendgaining popularity since 2020 and is prominent in Apple and Microsoft's design systems. Glassmorphic elements look like frosted glass. Thoughtful use of glassmorphism can help designers effectively establish visual hierarchy and depth. However, without a solid grasp of visual-design principles or if overused, glassmorphism can pose significant accessibility and usability challenges.

Glassmorphismis a visual-design style that utilizes different levels of translucency to create depth and contrast between foreground and background elements, mimicking frosted glass.

Typically, glassmorphic UI elements stand out when placed in front of gradients or complex backgrounds to accentuate depth.

While “glassmorphism” is a commonly used term,design systemstend to label this style under the broader category of “material” since these elements replicate the look of physical material in a digital space. For instance,Microsoft’s Fluent Design Systemdefines a material called “Acrylic,” which embodies the characteristics of glassmorphism.

These design systems aim to create depth against complex backgrounds in order to emphasize or contain specific parts of an interface. In virtual- or mixed-reality spaces, glassmorphic elements help maintain a 3D experience by providing texture to objects that might otherwise seem two-dimensional on a standard screen. For example, the Apple Vision Pro uses glassmorphicSwiftUI materialsin translucent UI overlays to effectively blur the virtual-reality environments behind them while keeping them perceptible.

Two main characteristics create glassmorphism’s translucency: opacity and background blur. To achieve a glassmorphic effect, designers can vary the opacity and background blur of components to affect how much background information is visible and distinguishable. Designers can also opt to use strokes and gradients for more depth and contrast if the glassmorphic elements will be placed on both complex and simple backgrounds.

To achieve a glassmorphic look, you need to be able to see through the element you are designing. You can achieve this by adjusting the opacity of your component’s fill (the color, pattern, or gradient inside of an object).

Opacitydefines how much you can see through an element. The more opaque an element is, the less you can see the contents behind it. The less opaque, the more you can see. For example, the glass windows in your home probably have 0% opacity, meaning you can see everything outside clearly.

Background blurdistorts objects behind the main component, giving background elements a fuzzy, out-of-focus appearance. Examples of background blur in the physical world are a walk-in shower with a frosted glass door or a conference room with privacy glass. You can still see objects on the other side, but they are blurred to a point where you might be unable to identify them.

Background blur provides this same effect for low-opacity digital elements. For instance, a white rectangle with 30% opacity and a 25-pixel blur will distort background elements but still have somewhat distinguishable edges. However, by adjusting the blur to 100 pixels, those same background elements become more out-of-focus and blend together.

In addition to opacity and background blur,strokes (borders) and gradientscan emphasize depth of glassmorphic elements, especially when these elements are placed on simple or one-color backgrounds.

A gradient takes two or more colors, color shades, or color opacities and blends them together seamlessly. Gradients can be applied to both fills and strokes of an element. You can add a low-opacity or gradient stroke around a component to create an illusion of thickness. Gradients can also be applied to the fill of the component to mimic the reflection of light on actual glass.

When incorporating glass-like materials in your UI, it is essential to understand the accessibility constraints of translucent components. One of the most significant issues with glassmorphism stems from text readability problems, with text either being too light or too dark or backgrounds being too busy. Follow these three best practices when incorporating glass-like materials into your design system

Ensure that text and graphical elements meet contrast requirements.Since glassmorphic components are translucent, textual elements can fall over multiple colors, which can affect readability. For instance, if you are designing a card component over a busy background, your text might only have enough contrast over certain areas and be challenging to read. If you are designing in Figma, I recommend checking out the pluginContrastby Willowtree, which lets you quickly check the contrast ratios of text and other design elements.

More background blur is better, especially with intricate backgrounds(e.g., video, photography, animations). Many UI designs on Behance or Dribble try too hard to keep background elements distinguishable. However, overwhelming backgrounds can make it hard for users to focus on meaningful content and affect text readability.

In instances where components can appear in various contexts, like an overlay on a website or contextual menu on a desktop application, the background blur mustaccount for the many possible backgrounds on which the item may appear.For example, the contextual menu below uses Microsoft’s acrylic material that appears over a complex image.

On the other hand, if you have control of what appears behind a translucent component, opt for simple or single-color backgrounds.

If feasible,give users the option to control contrast or transparency settings.For example, Apple’s accessibility features allow users to reduce transparency or increase contrast, minimizing or removing the blur of glassmorphic components altogether. These options enable the interface to be adaptable for low-vision users.

If your budget or time constraints do not allow this type ofcustomization, then make sure that any glassmorphic elements in your interface areWCAG-compliant.

Overall, glassmorphism is best when utilized sparingly to create an illusion of depth. Consider using already established design systems, like Apple’s SwfitUI, to avoid any potential issues with creating glassmorphic materials from scratch. Otherwise, be mindful of how translucent components are affected by background elements while maintaining visual hierarchy and accessibility requirements.

Create user interfaces using essential principles, techniques, and methods of visual design

Interaction

Essential UX design principles for small-screen websites and apps

Interaction

Create and evaluate applications for advanced decision making, complicated workflows, and complex domains

Interaction