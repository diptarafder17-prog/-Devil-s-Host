# Devil Control Stack 😈

An automated web dashboard and REST API management layer built to control shared hosting environments over local UNIX sockets.

## 🚀 Architecture Components

*   **Frontend UI (`devil-web`):** A modern, high-performance web dashboard built with SvelteKit.
*   **Backend API (`devil-api`):** A lightweight, fast REST layer built using FastAPI that interacts natively with `/var/run/devil2.sock`.

---

## 🛠️ Quick Start & Installation

### 1. Prerequisites
Ensure you have the following software suites installed on your production box:
* Node.js (v20+)
* Python 3.11+
* Nginx (for web routing)

### 2. Backend Environment (`devil-api/.env`)
```env
DEVIL_API_KEY="your_secure_hex_token"
CORS_ORIGINS="[https://yourdomain.com](https://yourdomain.com)"
LOG_LEVEL="INFO"

🌌 Gravity Profile — Blurred Photo Background

A sleek, modern, and interactive personal profile landing page inspired by Linktree. Built with pure HTML, CSS, and Vanilla JavaScript, Gravity Profile features stunning glassmorphism effects, interactive 3D animations, and a dynamic blurred background generated from your profile picture.

---

✨ Features

🪟 Glassmorphism UI

Beautiful frosted-glass card design using modern CSS backdrop filters and transparency effects.

🌄 Dynamic Blurred Background

Your profile image automatically becomes the page background with:

- Smooth blur effect
- Color wash overlay
- Animated light band
- Soft glowing atmosphere

🎯 Interactive 3D Hover Effects

The profile card reacts to mouse and touch movements with realistic tilt animations.

🌍 Subtle Parallax Motion

Background layers move slightly with cursor movement, creating a sense of depth and gravity.

📱 Fully Responsive

Optimized for:

- Mobile Phones
- Tablets
- Laptops
- Desktop Screens

♿ Accessibility Friendly

Includes:

- "prefers-reduced-motion" support
- Keyboard accessibility
- Proper "aria-label" attributes

⚡ Zero Dependencies

No frameworks required.

Built using:

- HTML5
- CSS3
- Vanilla JavaScript
- Font Awesome Icons

---

🚀 Installation

Method 1: Download

1. Download the repository.
2. Extract the files.
3. Open "index.html" in any modern browser.

Method 2: Git Clone

git clone https://github.com/yourusername/gravity-profile.git
cd gravity-profile

Then simply open:

index.html

No server setup required.

---

📂 Project Structure

gravity-profile/
│
├── index.html
├── README.md

---

🎨 Customization

Change Profile Picture

Locate the CSS root variables:

:root {
  --bg-image: url("https://youtu.be/3Dz09I42NkQ?si=8Lyi47e6sJqSJhRP");
}

Replace with your own image URL:

:root {
  --bg-image: url("https://example.com/profile.jpg");
