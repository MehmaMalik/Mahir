---
name: Karigar Design System
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#3f4941'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#6f7a70'
  outline-variant: '#becabe'
  surface-tint: '#006d3d'
  primary: '#006438'
  on-primary: '#ffffff'
  primary-container: '#1a7f4b'
  on-primary-container: '#d0ffda'
  inverse-primary: '#7cda9d'
  secondary: '#1960a3'
  on-secondary: '#ffffff'
  secondary-container: '#7db6ff'
  on-secondary-container: '#00477f'
  tertiary: '#854600'
  on-tertiary: '#ffffff'
  tertiary-container: '#a95b00'
  on-tertiary-container: '#fff1e9'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#98f6b7'
  primary-fixed-dim: '#7cda9d'
  on-primary-fixed: '#00210f'
  on-primary-fixed-variant: '#00522c'
  secondary-fixed: '#d3e4ff'
  secondary-fixed-dim: '#a2c9ff'
  on-secondary-fixed: '#001c38'
  on-secondary-fixed-variant: '#004881'
  tertiary-fixed: '#ffdcc3'
  tertiary-fixed-dim: '#ffb77d'
  on-tertiary-fixed: '#2f1500'
  on-tertiary-fixed-variant: '#6e3900'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  headline-lg:
    fontFamily: DM Sans
    fontSize: 28px
    fontWeight: '500'
    lineHeight: 36px
  headline-md:
    fontFamily: DM Sans
    fontSize: 22px
    fontWeight: '500'
    lineHeight: 28px
  headline-sm:
    fontFamily: DM Sans
    fontSize: 18px
    fontWeight: '500'
    lineHeight: 24px
  body-lg:
    fontFamily: DM Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: DM Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-lg:
    fontFamily: DM Sans
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.1px
  label-sm:
    fontFamily: DM Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.5px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  margin-main: 1rem
  gutter: 0.75rem
  stack-sm: 0.5rem
  stack-md: 1rem
  stack-lg: 1.5rem
---

## Brand & Style

The design system is engineered for the "Karigar Pakistan" mobile platform, a marketplace connecting skilled tradespeople (Ustads) with households. The brand personality is grounded, reliable, and respectful, emphasizing the dignity of manual labor. 

The visual style is strictly **Flat Design**. It avoids all forms of skeuomorphism, shadows, and gradients in favor of high-contrast clarity and structural honesty. This approach ensures maximum legibility and performance on a wide range of mobile devices. The emotional response should be one of "bharosa" (trust) and efficiency, bridging the gap between professional service standards and the local cultural context of Pakistan.

The system incorporates a bilingual content strategy, seamlessly mixing English and Roman Urdu to ensure accessibility for both high-literacy users and vocational workers.

## Colors

This design system utilizes a high-visibility palette rooted in a deep "Karigar Green." 

- **Primary (#1a7f4b):** Used for primary actions, branding, and "Police Verified" status. It represents growth and safety.
- **Secondary (#2b6cb0):** A professional blue reserved for "Master Ustad" designations and secondary informative elements.
- **Tertiary (#d97706):** An amber tone used exclusively for "Safety Scores" and cautionary feedback.
- **Emergency (#dc2626):** A high-alert red dedicated to the Panic/Emergency button.
- **Backgrounds:** The interface uses a pure white (#ffffff) base. Interactive cards and containers must use the neutral off-white (#f8f9fa) to create distinction without using shadows.

## Typography

The design system exclusively uses **DM Sans** to maintain a modern, clean, and highly legible appearance. 

- **Headings:** Set at 500 weight. Headlines should be concise, often utilizing Roman Urdu for immediate recognition (e.g., "Kaam Mukammal").
- **Body:** Set at 400 weight. Used for service descriptions, worker bios, and instructions.
- **Naming Convention:** All service providers must be prefixed with the title **"Ustad"** in all UI instances (e.g., "Ustad Ahmed", "Ustad Khalid"). This is a mandatory typographic rule to instill respect within the ecosystem.

## Layout & Spacing

The layout follows a **Fluid Grid** model optimized for mobile-first interaction. 

- **Safe Zones:** A standard 16px (1rem) side margin is maintained across all screens.
- **Vertical Rhythm:** Elements are stacked using an 8px base grid. 
- **Full-Width Philosophy:** To ensure ease of use for workers in the field, primary interactive elements like buttons and input fields should span the full width of the content area (minus margins).
- **Card Spacing:** Internal padding for cards is set to 12px to match the corner radius, creating visual harmony.

## Elevation & Depth

This design system explicitly rejects the use of shadows or Z-axis elevation markers. Depth is communicated through **Tonal Layering**:

- **Level 0 (Base):** Pure white (#ffffff) background.
- **Level 1 (Content):** Cards and sections use the Neutral background (#f8f9fa).
- **Level 2 (Interaction):** Borders are used instead of shadows to define focus states. 1px solid borders in a slightly darker neutral (#e9ecef) can be used if a card needs extra definition against the white background.

Backdrop blurs or glassmorphism are not permitted, ensuring the UI remains performant on low-spec mobile hardware.

## Shapes

The shape language is friendly but structured. 

- **Standard Radius:** All containers, cards, and buttons must use a **12px** corner radius.
- **Badges:** Small "pill" shapes are used for badges, requiring a fully rounded (32px+) radius to distinguish them from actionable buttons.
- **Icons:** Use thick-stroke, rounded icons to complement the DM Sans typeface.

## Components

### Buttons
- **Primary:** Full-width, #1a7f4b background, white text, 12px radius. 
- **Emergency (Panic):** Red background (#dc2626), white text, bold 500 weight. This should be easily accessible in the active job view.

### Badges (Pills)
Badges consist of a 12px icon followed by label text.
- **Police Verified:** Green background (10% opacity of primary), green text, "Shield" icon.
- **Master Ustad:** Blue background (10% opacity of secondary), blue text, "Award" icon.
- **Safety Score:** Amber background (10% opacity of tertiary), amber text, "Heart" icon.

### Cards
Cards use the #f8f9fa background with 12px padding. They must never have shadows. For Ustad profiles, the card must prominently display the "Ustad" prefix before the name.

### Input Fields
Large tap targets (min 48px height) with 12px rounded corners. Use a 1px border (#dee2e6) and #ffffff background for inputs to make them pop against the #f8f9fa card background.

### Lists
Lists should be separated by simple 1px hairlines (#e9ecef) or grouped within #f8f9fa cards with 8px vertical spacing between cards.
