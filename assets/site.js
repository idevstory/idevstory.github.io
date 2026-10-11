(() => {
  const progress = document.querySelector('.reading-progress');
  if (!progress) return;
  let pending = false;
  const update = () => {
    const range = document.documentElement.scrollHeight - window.innerHeight;
    progress.style.width = `${range > 0 ? Math.min(100, window.scrollY / range * 100) : 0}%`;
    pending = false;
  };
  window.addEventListener('scroll', () => {
    if (!pending) { pending = true; requestAnimationFrame(update); }
  }, { passive: true });
  window.addEventListener('resize', update);
  update();
  if ('IntersectionObserver' in window) {
    const links = [...document.querySelectorAll('.toc a')];
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          links.forEach(link => link.classList.toggle('active', link.hash === `#${entry.target.id}`));
        }
      }
    }, { rootMargin: '-5% 0px -65% 0px' });
    document.querySelectorAll('.prose h2').forEach(heading => observer.observe(heading));
  }
})();
