// Small progressive-enhancement layer for accessibility and browser quality.
// The site remains usable if this file fails to load.
(function () {
  function enhance() {
    const app = document.getElementById('app');
    const main = document.querySelector('main');
    if (main && !main.id) main.id = 'main-content';

    if (!document.querySelector('.elyra-skip-link')) {
      const skip = document.createElement('a');
      skip.className = 'elyra-skip-link';
      skip.href = '#main-content';
      skip.textContent = 'Skip to main content';
      skip.style.cssText = 'position:fixed;left:12px;top:-60px;z-index:9999;background:#4A235A;color:#fff;padding:10px 14px;border-radius:10px;font:700 13px Manrope,sans-serif;text-decoration:none;transition:top .2s';
      skip.addEventListener('focus', () => { skip.style.top = '12px'; });
      skip.addEventListener('blur', () => { skip.style.top = '-60px'; });
      document.body.insertBefore(skip, app || document.body.firstChild);
    }

    document.querySelectorAll('.nav a.active,.dropdown-menu a.active').forEach((link) => {
      link.setAttribute('aria-current', 'page');
    });

    const menu = document.getElementById('menuBtn');
    const mobile = document.getElementById('mobileNav');
    if (menu && mobile) {
      menu.setAttribute('aria-controls', 'mobileNav');
      menu.setAttribute('aria-expanded', mobile.classList.contains('open') ? 'true' : 'false');
      if (!menu.dataset.elyraA11yBound) {
        menu.dataset.elyraA11yBound = '1';
        menu.addEventListener('click', () => {
          requestAnimationFrame(() => menu.setAttribute('aria-expanded', mobile.classList.contains('open') ? 'true' : 'false'));
        });
      }
      mobile.querySelectorAll('a').forEach((link) => {
        if (!link.dataset.elyraA11yBound) {
          link.dataset.elyraA11yBound = '1';
          link.addEventListener('click', () => menu.setAttribute('aria-expanded', 'false'));
        }
      });
    }

    document.querySelectorAll('a[target="_blank"]').forEach((link) => {
      const rel = new Set((link.getAttribute('rel') || '').split(/\s+/).filter(Boolean));
      rel.add('noopener');
      rel.add('noreferrer');
      link.setAttribute('rel', Array.from(rel).join(' '));
    });

    document.querySelectorAll('img').forEach((img) => {
      if (!img.hasAttribute('decoding')) img.setAttribute('decoding', 'async');
      if (!img.hasAttribute('alt')) img.setAttribute('alt', '');
    });

    document.querySelectorAll('input[name="name"]').forEach((el) => el.setAttribute('autocomplete', 'name'));
    document.querySelectorAll('input[name="email"]').forEach((el) => el.setAttribute('autocomplete', 'email'));
    document.querySelectorAll('input[name="phone"]').forEach((el) => el.setAttribute('autocomplete', 'tel'));
  }

  window.addEventListener('DOMContentLoaded', enhance);
  window.addEventListener('hashchange', () => setTimeout(enhance, 0));

  const app = document.getElementById('app');
  if (app && 'MutationObserver' in window) {
    new MutationObserver(() => enhance()).observe(app, { childList: true });
  }
})();
