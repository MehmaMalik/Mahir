document.addEventListener("DOMContentLoaded", () => {
    // 1. Create and inject Style tag for animations
    const drawerStyle = document.createElement('style');
    drawerStyle.innerHTML = `
        #side-drawer {
            transition: visibility 0.3s;
        }
        #drawer-overlay {
            transition: opacity 0.3s ease-in-out;
        }
        #drawer-content {
            transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }
    `;
    document.head.appendChild(drawerStyle);

    // 2. Create and inject Drawer HTML Structure
    const drawerHtml = `
        <div id="side-drawer" class="fixed inset-0 z-[1000] invisible">
            <!-- Semi-transparent overlay backdrop -->
            <div id="drawer-overlay" class="absolute inset-0 bg-black/50 opacity-0"></div>
            
            <!-- Left-side Drawer Panel -->
            <div id="drawer-content" class="absolute top-0 left-0 bottom-0 w-80 max-w-[85vw] bg-white shadow-2xl flex flex-col transform -translate-x-full">
                
                <!-- Drawer Header -->
                <div class="p-6 bg-gradient-to-r from-[#1a7f4b] to-[#0d5e35] text-white relative">
                    <button id="close-drawer" class="absolute top-4 right-4 text-white/80 hover:text-white min-h-[48px] min-w-[48px] flex items-center justify-center active:opacity-60 transition-opacity">
                        <span class="material-symbols-outlined text-2xl">close</span>
                    </button>
                    <div class="flex items-center gap-4 mt-2">
                        <div class="w-16 h-16 rounded-full bg-white/20 border-2 border-white/40 overflow-hidden flex-shrink-0">
                            <img class="w-full h-full object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCxywGlGEA5vGewdmPlX1Dfth-iZkK-Jh-bZb-hRznYCyLpZZb0Zc2LoFQvlBEbN_NQpQmCk1AhoSeTk6-UvU8JLwwvEdEbCFQeTImg6E7PM3LO2q7Y7xxPtmM6-F6rhqwpBV_yCAxvvvR-2rJS0kEANrdsX9rxS3p06n1hcswiNBby7H0RAcm_f3MmT0zBKBSH4hlcdja5LFNsIc7y0yZR9CXRtZsw0LC_O-Yjkl2YtlIOwnDqEPg7CblVVPZADm6Q1uWKQW0ZB1U" alt="User Profile Image">
                        </div>
                        <div>
                            <h3 class="font-bold text-base leading-tight">Bilal Ahmed</h3>
                            <p class="text-[11px] text-white/80 mt-0.5">bilal.ahmed@example.com</p>
                        </div>
                    </div>
                </div>
                
                <!-- Navigation Menu Items -->
                <nav class="flex-1 py-4 overflow-y-auto">
                    <ul class="space-y-1">
                        <li>
                            <a href="/bookings" class="flex items-center gap-4 px-6 py-3 text-gray-700 hover:bg-gray-50 active:bg-green-50/50 transition-colors font-semibold text-sm">
                                <span class="material-symbols-outlined text-gray-400">handyman</span>
                                <span>My Bookings</span>
                            </a>
                        </li>
                        <li>
                            <a href="#" onclick="alert('Saved Addresses is coming soon!'); return false;" class="flex items-center gap-4 px-6 py-3 text-gray-700 hover:bg-gray-50 active:bg-green-50/50 transition-colors font-semibold text-sm">
                                <span class="material-symbols-outlined text-gray-400">home_pin</span>
                                <span>Saved Addresses</span>
                            </a>
                        </li>
                        <li>
                            <a href="#" onclick="alert('Add New Address functionality is coming soon!'); return false;" class="flex items-center gap-4 px-6 py-3 text-gray-700 hover:bg-gray-50 active:bg-green-50/50 transition-colors font-semibold text-sm">
                                <span class="material-symbols-outlined text-gray-400">add_location_alt</span>
                                <span>Add New Address</span>
                            </a>
                        </li>
                        <li>
                            <a href="/profile" class="flex items-center gap-4 px-6 py-3 text-gray-700 hover:bg-gray-50 active:bg-green-50/50 transition-colors font-semibold text-sm">
                                <span class="material-symbols-outlined text-gray-400">security_update_good</span>
                                <span>Safe Mode Settings</span>
                            </a>
                        </li>
                        <li>
                            <a href="#" onclick="alert('Notifications functionality is coming soon!'); return false;" class="flex items-center gap-4 px-6 py-3 text-gray-700 hover:bg-gray-50 active:bg-green-50/50 transition-colors font-semibold text-sm">
                                <span class="material-symbols-outlined text-gray-400">notifications</span>
                                <span>Notifications</span>
                            </a>
                        </li>
                        <li>
                            <a href="#" onclick="alert('Help and Support is coming soon!'); return false;" class="flex items-center gap-4 px-6 py-3 text-gray-700 hover:bg-gray-50 active:bg-green-50/50 transition-colors font-semibold text-sm">
                                <span class="material-symbols-outlined text-gray-400">help</span>
                                <span>Help and Support</span>
                            </a>
                        </li>
                        <li class="border-t border-gray-100 my-2 pt-2">
                            <a href="/" class="flex items-center gap-4 px-6 py-3 text-red-600 hover:bg-red-50/50 active:bg-red-100 transition-colors font-semibold text-sm">
                                <span class="material-symbols-outlined">logout</span>
                                <span>Logout</span>
                            </a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
    `;

    const container = document.createElement('div');
    container.innerHTML = drawerHtml;
    document.body.appendChild(container.firstElementChild);

    // 3. Elements mapping and drawer API
    const sideDrawer = document.getElementById('side-drawer');
    const drawerOverlay = document.getElementById('drawer-overlay');
    const drawerContent = document.getElementById('drawer-content');
    const closeBtn = document.getElementById('close-drawer');

    // Global Drawer Controllers
    window.openDrawer = function() {
        sideDrawer.classList.remove('invisible');
        setTimeout(() => {
            drawerOverlay.classList.replace('opacity-0', 'opacity-100');
            drawerContent.classList.replace('-translate-x-full', 'translate-x-0');
        }, 10);
    };

    window.closeDrawer = function() {
        drawerOverlay.classList.replace('opacity-100', 'opacity-0');
        drawerContent.classList.replace('translate-x-0', '-translate-x-full');
        setTimeout(() => {
            sideDrawer.classList.add('invisible');
        }, 300);
    };

    // Close actions
    drawerOverlay.addEventListener('click', window.closeDrawer);
    closeBtn.addEventListener('click', window.closeDrawer);

    // 4. Touch swipe gesture to close (left-swipe detection)
    let touchStartX = 0;
    let touchEndX = 0;

    drawerContent.addEventListener('touchstart', e => {
        touchStartX = e.changedTouches[0].screenX;
    }, {passive: true});

    drawerContent.addEventListener('touchend', e => {
        touchEndX = e.changedTouches[0].screenX;
        // If swiped left by more than 50px, close drawer
        if (touchStartX - touchEndX > 50) {
            window.closeDrawer();
        }
    }, {passive: true});
});
