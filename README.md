# Gravity Profile — Blurred Photo Background

A sleek, modern, and interactive personal profile landing page (Linktree alternative). It features a glassmorphism design, interactive 3D card tilt effects, and a beautiful dynamic blurred background that adapts to your profile picture.

## ✨ Features

- **Glassmorphism UI**: Beautiful frosted-glass effects using modern CSS backdrop filters.
- **Dynamic Blurred Background**: The background automatically uses your profile picture and applies a smooth blur, color wash, and moving light band to bring it to life.
- **Interactive 3D Hover Effects**: The card smoothly tilts and follows your mouse or touch movements using Vanilla JavaScript.
- **Subtle Parallax**: The background and stage shift slightly as you move your cursor, creating a deep sense of gravity.
- **Fully Responsive**: Adapts perfectly to mobile phones, tablets, and desktop screens.
- **Accessibility Friendly**: Includes support for `prefers-reduced-motion` to disable animations for users who prefer static interfaces, along with proper `aria-labels`.
- **Zero Dependencies**: Built with pure HTML, CSS, and Vanilla JavaScript (uses FontAwesome for icons).

## 🚀 How to Use

1. Download or clone this repository.
2. Ensure you have the `index.html` file on your computer.
3. Simply double-click the `index.html` file to open it in your favorite web browser! No server or build tools required.

## 🎨 Customization

You can easily customize this profile card to make it your own by editing the `index.html` file.

### 1. Change the Profile Picture & Background
The background and the avatar share the same image. 
- Find the `:root` variables in the `<style>` tag and update the `--bg-image` URL:
  ```css
  :root {
    --bg-image: url("YOUR_IMAGE_URL_HERE");
  }here

<img src="YOUR_IMAGE_URL_HERE" alt="Profile picture">

<div class="name">Your Name</div>
<a class="btn whatsapp" href="YOUR_WHATSAPP_LINK">...</a>
<a class="btn instagram" href="YOUR_INSTAGRAM_LINK">...</a>
<a class="btn facebook" href="YOUR_FACEBOOK_LINK">...</a>
<span>+1 234 567 8900</span>
