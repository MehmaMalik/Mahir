// drawer.js – Self‑contained side menu drawer
// Injects HTML, CSS and provides openDrawer() / closeDrawer() helpers.

(function() {
  const DRAWER_ID = 'side-drawer';
  const BACKDROP_ID = 'drawer-backdrop';

  // Create drawer container
  const drawer = document.createElement('div');
  drawer.id = DRAWER_ID;
  drawer.style.cssText = `
    position: fixed;
    top: 0;
    left: -300px;
    width: 260px;
    height: 100vh;
    background: #fff;
    box-shadow: 2px 0 8px rgba(0,0,0,0.15);
    z-index: 1000;
    transition: transform 0.3s ease-out;
    display: flex;
    flex-direction: column;
    padding: 16px;
    font-family: 'DM Sans', sans-serif;
  `;

  // Close button
  const closeBtn = document.createElement('button');
  closeBtn.innerHTML = '&times;';
  closeBtn.style.cssText = `
    align-self: flex-end;
    font-size: 24px;
    background: none;
    border: none;
    cursor: pointer;
  `;
  closeBtn.addEventListener('click', closeDrawer);
  drawer.appendChild(closeBtn);

  // Drawer content – simple placeholder navigation
  const nav = document.createElement('nav');
  nav.innerHTML = `
    <ul style="list-style:none;padding:0;margin:0;">
      <li><a href="/" style="text-decoration:none;color:#1a7f4b;display:block;padding:8px 0;">Home</a></li>
      <li><a href="/bookings" style="text-decoration:none;color:#1a7f4b;display:block;padding:8px 0;">Bookings</a></li>
      <li><a href="/messages" style="text-decoration:none;color:#1a7f4b;display:block;padding:8px 0;">Messages</a></li>
      <li><a href="/profile" style="text-decoration:none;color:#1a7f4b;display:block;padding:8px 0;">Profile</a></li>
    </ul>
  `;
  drawer.appendChild(nav);

  // Backdrop
  const backdrop = document.createElement('div');
  backdrop.id = BACKDROP_ID;
  backdrop.style.cssText = `
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: rgba(0,0,0,0.4);
    z-index: 999;
    opacity: 0;
    transition: opacity 0.3s ease-out;
    pointer-events: none;
  `;
  backdrop.addEventListener('click', closeDrawer);

  // Append to body
  document.addEventListener('DOMContentLoaded', function() {
    document.body.appendChild(drawer);
    document.body.appendChild(backdrop);
  });

  // Helper functions
  window.openDrawer = function() {
    drawer.style.transform = 'translateX(300px)'; // slide in
    backdrop.style.opacity = '1';
    backdrop.style.pointerEvents = 'auto';
  };

  window.closeDrawer = function() {
    drawer.style.transform = 'translateX(0)'; // hide
    backdrop.style.opacity = '0';
    backdrop.style.pointerEvents = 'none';
  };

  // Swipe to close (touch events)
  let startX = null;
  drawer.addEventListener('touchstart', function(e) {
    startX = e.touches[0].clientX;
  });
  drawer.addEventListener('touchmove', function(e) {
    if (startX === null) return;
    const diff = e.touches[0].clientX - startX;
    if (diff < -30) closeDrawer();
  });
  drawer.addEventListener('touchend', function() { startX = null; });
})();
