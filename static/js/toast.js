// static/js/toast.js
(function () {
  const toast = document.getElementById('toast');
  if (!toast) return;

  const titleEl = document.getElementById('toast-title');
  const msgEl = document.getElementById('toast-message');
  const iconEl = document.getElementById('toast-icon');
  const progressEl = document.getElementById('toast-progress');
  const closeBtn = document.getElementById('toast-close');

  let hideTimer = null;
  let progressTimer = null;

  const TYPE_STYLES = {
    success: { icon: '✅', border: 'border-green-500', bar: 'bg-green-500' },
    error:   { icon: '❌', border: 'border-red-500',   bar: 'bg-red-500'   },
    info:    { icon: 'ℹ️', border: 'border-blue-500',  bar: 'bg-blue-500'  },
    warning: { icon: '⚠️', border: 'border-yellow-500',bar: 'bg-yellow-500'},
  };

  function clearTimers() {
    if (hideTimer) clearTimeout(hideTimer);
    if (progressTimer) clearInterval(progressTimer);
    hideTimer = null; progressTimer = null;
  }

  function resetClasses() {
    toast.classList.remove('opacity-100','translate-y-0');
    toast.classList.add('opacity-0','translate-y-10','pointer-events-none');

    // remove old border color classes
    toast.classList.remove('border-green-500','border-red-500','border-blue-500','border-yellow-500');
    // reset progress bar width & color
    progressEl.style.width = '0%';
    progressEl.classList.remove('bg-green-500','bg-red-500','bg-blue-500','bg-yellow-500');
  }

  function applyType(type) {
    const sty = TYPE_STYLES[type] || TYPE_STYLES.info;
    iconEl.textContent = sty.icon;
    toast.classList.add(sty.border);
    progressEl.classList.add(sty.bar);
  }

  function showToast(title, message, type = 'info', duration = 3000) {
    clearTimers();
    resetClasses();
    applyType(type);

    titleEl.textContent = title || '';
    msgEl.textContent = message || '';

    // show
    toast.classList.remove('opacity-0','translate-y-10','pointer-events-none');
    toast.classList.add('opacity-100','translate-y-0');

    // progress animation
    let elapsed = 0;
    const step = 25; // ms
    progressTimer = setInterval(() => {
      elapsed += step;
      const pct = Math.min(100, (elapsed / duration) * 100);
      progressEl.style.width = pct + '%';
      if (elapsed >= duration) {
        clearInterval(progressTimer);
        progressTimer = null;
      }
    }, step);

    // auto hide
    hideTimer = setTimeout(hideToast, duration);
  }

  function hideToast() {
    clearTimers();
    toast.classList.remove('opacity-100','translate-y-0');
    toast.classList.add('opacity-0','translate-y-10','pointer-events-none');
  }

  // close button
  if (closeBtn) closeBtn.addEventListener('click', hideToast);

  // allow firing via custom event:
  // document.dispatchEvent(new CustomEvent('show-toast', { detail: { title, message, type, duration } }));
  document.addEventListener('show-toast', (e) => {
    const { title, message, type, duration } = e.detail || {};
    showToast(title, message, type, duration);
  });

  // expose globally for direct calls
  window.showToast = showToast;
})();
