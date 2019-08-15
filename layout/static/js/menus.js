// Use focus-within polyfill so no having to maintain where the current focus is within tree
// Let the DOM do it!
// https://github.com/matteobad/focus-within-polyfill

function getParentUlEl(menuItemEl) {
  if (menuItemEl.parentElement.classList.contains('root-menu-list')) {
    return menuItemEl.parentElement // This is the root menu
  } else {
    return menuItemEl.parentElement.parentElement // This is a submenuItem
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const menuGroups = Array.from(document.querySelectorAll('.dropdown-menu-list'));

  menuGroups.forEach(menuGroupUlEl => {
    const menuLiItems = Array.from(menuGroupUlEl.children);

    menuLiItems.forEach((menuLiElement, menuIndex) => {
      const parentUlEl = menuGroupUlEl;
      const parentLiEl = parentUlEl.parentElement.tagName === 'LI' && parentUlEl.parentElement; // If false, is root
      const parentIndex = parentLiEl && parentLiEl.dataset.menuindex; // If false, is root
      const grandParentUlEl = parentLiEl && parentLiEl.parentElement; // If false, is root

      menuLiElement.setAttribute('data-menuindex', menuIndex);

      const getMenuItemByI = (j, el) => el.querySelector(`:scope > [data-menuindex="${j}"]`);

      menuLiElement.addEventListener('keydown',e => {
        const stop = () =>
        {
          e.stopPropagation();
          e.preventDefault();
        };

        switch (e.key) {
          case 'ArrowDown':{
            // Get the item below the current one
            // If nothing is there, go ahead and get the parent one after the current parent
            stop();
            let el = getMenuItemByI(menuIndex + 1, parentUlEl);
            // If overflowing to the parent item below
            if (!el && grandParentUlEl) el = getMenuItemByI(parentIndex + 1, grandParentUlEl);
            // T'was root, still null. Break
            if (!el) break;
            el.focus();
            break;
          }
          case 'ArrowUp': {
            // stop();
            e.stopPropagation();
            e.preventDefault();
            // If overflows, select menu below submenu
            let el = getMenuItemByI(menuIndex - 1, parentUlEl);
            if (!el && grandParentUlEl) el = getMenuItemByI(parentIndex - 1, grandParentUlEl);
            if (!el) break;
            el.focus();
            break;
          }
          case 'Enter':
          case ' ':
            stop();
            // Fall thru intentionally - make sure that right arrow isn't just clicking
            if (!menuLiElement.dataset.haschildren) menuItem.click();
          case 'ArrowRight':
            stop();
            if (!menuLiElement.dataset.haschildren) break;
            const el = menuLiElement.querySelector(':scope > ul > li:first-child');
            if (!el) break;
            el.focus();
            break;
          case 'ArrowLeft': // Thing
            // If root, don't do anything
            if (!grandParentUlEl) break;
            stop();
            getMenuItemByI(parentIndex, grandParentUlEl).focus();
            break;
          default:
            break;
        }
      })
    })
  })
});
