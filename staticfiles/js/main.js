// Register GSAP plugins
gsap.registerPlugin(ScrollTrigger);

// Custom Cursor Implementation
const cursorDot = document.querySelector('.cursor-dot');
const cursorOutline = document.querySelector('.cursor-outline');
const hoverElements = document.querySelectorAll('.hover-text, a, button');

if (cursorDot && cursorOutline && window.matchMedia("(min-width: 768px)").matches) {
    window.addEventListener('mousemove', (e) => {
        const posX = e.clientX;
        const posY = e.clientY;
        
        cursorDot.style.left = `${posX}px`;
        cursorDot.style.top = `${posY}px`;
        
        // Add subtle delay to the outline for a smooth effect
        cursorOutline.animate({
            left: `${posX}px`,
            top: `${posY}px`
        }, { duration: 500, fill: "forwards" });
    });

    hoverElements.forEach((el) => {
        el.addEventListener('mouseenter', () => {
            cursorOutline.classList.add('cursor-hover');
        });
        el.addEventListener('mouseleave', () => {
            cursorOutline.classList.remove('cursor-hover');
        });
    });
}

// Initial Loading Animations
const heroTL = gsap.timeline();

heroTL.to('.js-hero-text', {
    y: 0,
    opacity: 1,
    duration: 1.2,
    ease: "power4.out",
    delay: 0.2
}).to('.js-hero-fade', {
    opacity: 1,
    duration: 1,
    stagger: 0.2,
    ease: "power3.out"
}, "-=0.8");

// Scroll Reveal Animations
const fadeUpElements = document.querySelectorAll('.js-fade-up');

fadeUpElements.forEach((el) => {
    gsap.fromTo(el, 
        { y: 50, opacity: 0 },
        { 
            y: 0, 
            opacity: 1, 
            duration: 1, 
            ease: "power3.out",
            scrollTrigger: {
                trigger: el,
                start: "top 85%",
                toggleActions: "play none none reverse"
            }
        }
    );
});

// Mobile Menu Toggle
const mobileBtn = document.querySelector('.js-mobile-menu-btn');
const mobileMenu = document.querySelector('.js-mobile-menu');
const mobileLinks = document.querySelectorAll('.js-mobile-link');
let isMenuOpen = false;

if (mobileBtn && mobileMenu) {
    mobileBtn.addEventListener('click', () => {
        isMenuOpen = !isMenuOpen;
        if (isMenuOpen) {
            mobileMenu.classList.remove('hidden');
            mobileMenu.classList.add('flex');
            document.body.style.overflow = 'hidden';
            gsap.to(mobileMenu, { opacity: 1, duration: 0.3 });
        } else {
            closeMenu();
        }
    });
    
    mobileLinks.forEach(link => {
        link.addEventListener('click', closeMenu);
    });
}

function closeMenu() {
    isMenuOpen = false;
    document.body.style.overflow = '';
    gsap.to(mobileMenu, { 
        opacity: 0, 
        duration: 0.3, 
        onComplete: () => {
            mobileMenu.classList.remove('flex');
            mobileMenu.classList.add('hidden');
        }
    });
}

// Navbar styling on scroll
const nav = document.querySelector('.js-nav');
if (nav) {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            nav.classList.add('border-accent', 'shadow-sm');
        } else {
            nav.classList.remove('border-accent', 'shadow-sm');
        }
    });
}
