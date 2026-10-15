// =============================================================
// Documents Page — Sticky Category Jump Navigation
// Author: Kate (JavaScript & Data Specialist)
// Auto-generates from .doc-category headings, scrollspy,
// smooth-scroll, accessible, respects prefers-reduced-motion
// =============================================================

(function () {
  'use strict';

  var categories = document.querySelectorAll('.doc-category');
  if (!categories.length) return;

  // --- Build the nav element ---
  var nav = document.createElement('nav');
  nav.className = 'doc-jump-nav';
  nav.setAttribute('role', 'navigation');
  nav.setAttribute('aria-label', 'Document categories');

  var list = document.createElement('ul');
  list.className = 'doc-jump-nav-list';
  list.setAttribute('role', 'list');

  // Ensure each category heading has an id for anchor linking
  categories.forEach(function (heading, i) {
    if (!heading.id) {
      heading.id = 'doc-cat-' + i;
    }

    var li = document.createElement('li');
    li.setAttribute('role', 'listitem');

    var link = document.createElement('a');
    link.href = '#' + heading.id;
    link.className = 'doc-jump-pill';
    // Use only the category name, excluding count badges
    var countBadge = heading.querySelector('.doc-count');
    link.textContent = countBadge
      ? heading.textContent.replace(countBadge.textContent, '').trim()
      : heading.textContent;

    // Click handler: smooth-scroll unless reduced motion preferred
    link.addEventListener('click', function (e) {
      e.preventDefault();
      var target = document.getElementById(heading.id);
      if (!target) return;

      var prefersReducedMotion = window.matchMedia(
        '(prefers-reduced-motion: reduce)'
      ).matches;

      // Offset for the sticky nav height + a little breathing room
      var navHeight = nav.offsetHeight || 56;
      var targetTop =
        target.getBoundingClientRect().top + window.pageYOffset - navHeight - 12;

      if (prefersReducedMotion) {
        window.scrollTo(0, targetTop);
      } else {
        window.scrollTo({ top: targetTop, behavior: 'smooth' });
      }

      // Update URL hash without jumping
      history.replaceState(null, '', '#' + heading.id);

      // Move focus to the heading for screen readers
      target.setAttribute('tabindex', '-1');
      target.focus({ preventScroll: true });
    });

    li.appendChild(link);
    list.appendChild(li);
  });

  nav.appendChild(list);

  // --- Insert nav before the first category heading ---
  var contentArea = categories[0].parentNode;
  contentArea.insertBefore(nav, categories[0]);

  // --- Scrollspy: highlight the active category pill ---
  var pills = nav.querySelectorAll('.doc-jump-pill');
  var activeIndex = -1;

  function updateScrollspy() {
    var navBottom = nav.getBoundingClientRect().bottom + 16;
    var currentIndex = -1;

    for (var i = categories.length - 1; i >= 0; i--) {
      var rect = categories[i].getBoundingClientRect();
      if (rect.top <= navBottom) {
        currentIndex = i;
        break;
      }
    }

    if (currentIndex !== activeIndex) {
      if (activeIndex >= 0 && activeIndex < pills.length) {
        pills[activeIndex].classList.remove('doc-jump-pill--active');
        pills[activeIndex].removeAttribute('aria-current');
      }
      if (currentIndex >= 0 && currentIndex < pills.length) {
        pills[currentIndex].classList.add('doc-jump-pill--active');
        pills[currentIndex].setAttribute('aria-current', 'true');

        // Auto-scroll the nav list to keep the active pill visible
        var activePill = pills[currentIndex];
        var listEl = activePill.closest('.doc-jump-nav-list');
        if (listEl) {
          var pillLeft = activePill.offsetLeft;
          var pillWidth = activePill.offsetWidth;
          var listWidth = listEl.offsetWidth;
          var scrollLeft = listEl.scrollLeft;

          // Scroll if pill is out of view on either side
          if (pillLeft < scrollLeft + 40) {
            listEl.scrollTo({
              left: Math.max(0, pillLeft - 40),
              behavior: 'smooth',
            });
          } else if (pillLeft + pillWidth > scrollLeft + listWidth - 40) {
            listEl.scrollTo({
              left: pillLeft + pillWidth - listWidth + 40,
              behavior: 'smooth',
            });
          }
        }
      }
      activeIndex = currentIndex;
    }
  }

  // Throttle scroll handler for performance
  var ticking = false;
  window.addEventListener(
    'scroll',
    function () {
      if (!ticking) {
        window.requestAnimationFrame(function () {
          updateScrollspy();
          ticking = false;
        });
        ticking = true;
      }
    },
    { passive: true }
  );

  // Initial check
  updateScrollspy();
})();
