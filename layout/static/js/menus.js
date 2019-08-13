// Use focus-within polyfill so no having to maintain where the current focus is within tree
// Let the DOM do it!
// https://github.com/matteobad/focus-within-polyfill

document.addEventListener('DOMContentLoaded', () => {
  const menus = document.querySelectorAll('.dropdown-menu-list');

  menus.forEach((menu, i) => {
    menu.id = `menu${i}`;

    // Make iterable thruout tree so not just first level works
    Array.from(menu.children).forEach((menuItem, ii) => {
      menuItem.setAttribute('data-menuindex', ii);

      const getMenuItemByI = (j) => menu.querySelector(`[data-menuindex="${j}"]`);

      console.log(menuItem)



      menuItem.addEventListener('keydown', e => {
//      debugger;
        const stop= () =>
        {
          e.stopPropagation();
          e.preventDefault();
        }
        switch (e.key) {
          case 'ArrowDown':{
            stop();
            const el = getMenuItemByI(ii + 1) || document.querySelector(`#menu${menu.id + 1}`);
            console.log(el);
            el.focus();
            break;
          }
          case 'ArrowUp': {
            stop();
            // If overflows, select menu below submenu
            const el = getMenuItemByI(ii - 1) || document.querySelector(`#menu${menu.id - 1}`);
            console.log(el);
            el.focus();
            break;
          }
          case 'Enter':
          case ' ':
            stop();
            // Fall thru intentionally - make sure that right arrow isn't just clicking
            if (!menuItem.dataset.haschildren) menuItem.click();
          case 'ArrowRight':
            stop();
            if (!menuItem.dataset.haschildren) break;
            menuItem.querySelector('.menu-children').focus();
            break;
          case 'ArrowLeft': // Thing
            stop();
            getMenuItemByI(ii).focus();
            break;
          default:
            break;
        }
      })
    })
  })
});
